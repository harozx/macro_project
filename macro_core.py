import time
import os
import json 
import threading # Cần import threading
from pynput import keyboard

class MacroPlayer:
    """
    NÂNG CẤP: Hỗ trợ nhiều bộ phím (key layout).
    """
    KEY_LAYOUTS = {
        "old": {
            "name": "Bộ cũ (yuiophjkl;nm,./)",
            "json_map": {
                "1Key0": "y", "1Key1": "u", "1Key2": "i", "1Key3": "o", "1Key4": "p",
                "1Key5": "h", "1Key6": "j", "1Key7": "k", "1Key8": "l", "1Key9": ";",
                "1Key10": "n", "1Key11": "m", "1Key12": ",", "1Key13": ".", "1Key14": "/"
            }
        },
        "new": {
            "name": "Bộ mới (asdfghjqwertyui)",
            "json_map": {
                "1Key0": "a", "1Key1": "s", "1Key2": "d", "1Key3": "f", "1Key4": "g",
                "1Key5": "h", "1Key6": "j", "1Key7": "q", "1Key8": "w", "1Key9": "e",
                "1Key10": "r", "1Key11": "t", "1Key12": "y", "1Key13": "u", "1Key14": "i"
            }
        }
    }

    def __init__(self):
        self.controller = keyboard.Controller()
        self.current_layout = "old"
        self.json_key_map = self.KEY_LAYOUTS["old"]["json_map"]

    def set_key_layout(self, layout_name):
        """Đổi bộ phím. layout_name: 'old' hoặc 'new'"""
        if layout_name in self.KEY_LAYOUTS:
            self.current_layout = layout_name
            self.json_key_map = self.KEY_LAYOUTS[layout_name]["json_map"]
            print(f"Da chuyen sang: {self.KEY_LAYOUTS[layout_name]['name']}")
        else:
            print(f"Loi: Khong tim thay bo phim '{layout_name}'.")

    def get_layout_name(self):
        """Trả về tên bộ phím hiện tại."""
        return self.KEY_LAYOUTS[self.current_layout]["name"]

    def _string_to_key(self, key_str):
        """(Không thay đổi)"""
        return key_str

    def _press_keys_sync(self, keys_str):
        """
        (Không thay đổi)
        """
        if keys_str == "SILENT":
            pass 
        else:
            try:
                keys_to_press_str = list(keys_str) 
                key_objects = [self._string_to_key(k) for k in keys_to_press_str]
                
                for key in key_objects:
                    self.controller.press(key)
                time.sleep(0.05) # Giữ phím (nhanh, không cần interrupt)
                for key in key_objects:
                    self.controller.release(key)
            except Exception as e:
                print(f"LOI KHI NHAN PHIM '{keys_str}': {e}")

    # --- HÀM MỚI QUAN TRỌNG ---
    def _interruptible_sleep(self, duration_sec, stop_event, pause_event):
        """
        Hàm "ngủ" mới. Sẽ ngủ trong các đoạn 0.01s
        và liên tục kiểm tra xem 'stop_event' (phím Esc) đã được nhấn chưa.
        Trả về True nếu ngủ thành công, False nếu bị ngắt.
        Nếu 'pause_event' được bật, sẽ tự động chờ cho đến khi tắt.
        """
        if duration_sec < 0.01:
            # Ngay cả khoảng nghỉ nhỏ cũng kiểm tra pause trước
            while pause_event and pause_event.is_set():
                if stop_event.is_set(): return False
                time.sleep(0.05)
            time.sleep(duration_sec)
            return True
            
        end_time = time.time() + duration_sec
        while time.time() < end_time:
            # Kiểm tra Stop
            if stop_event.is_set():
                return False
            
            # Kiểm tra Pause (chờ vô hạn đến khi Resume hoặc Stop)
            while pause_event and pause_event.is_set():
                if stop_event.is_set():
                    return False
                time.sleep(0.05)
                # Đẩy end_time lên để bù cho khoảng thời gian bị pause
                end_time += 0.05
            
            # Ngủ 10ms (0.01s)
            time.sleep(0.01)
            
        return True



    # --- CHỨC NĂNG MỚI (ĐÃ SỬA) ---
    def play_json_sheet(self, song_data, stop_event, pause_event=None):
        """
        NÂNG CẤP: Dùng _interruptible_sleep thay vì time.sleep
        """
        print("Phat nhac theo MOC THOI GIAN (JSON).")
        print("Bat dau sau 3 giay... (Nhan 'Esc' de DUNG)")
        
        # Thay time.sleep(3)
        if not self._interruptible_sleep(3, stop_event, pause_event):
            print("DA HUY (truoc khi bat dau).")
            return

        try:
            if isinstance(song_data, list) and len(song_data) > 0:
                song_notes = song_data[0]['songNotes']
            else:
                song_notes = song_data['songNotes']
        except (KeyError, TypeError):
            print("Loi: File JSON co cau truc khong dung (khong tim thay 'songNotes').")
            return

        song_notes.sort(key=lambda note: note['time'])
        grouped_notes = {}
        for note in song_notes:
            timestamp = note['time']
            key_code = note['key']
            translated_key = self.json_key_map.get(key_code)
            if translated_key:
                if timestamp not in grouped_notes:
                    grouped_notes[timestamp] = []
                grouped_notes[timestamp].append(translated_key)

        last_time_ms = 0
        
        for timestamp_ms in sorted(grouped_notes.keys()):
            delay_ms = timestamp_ms - last_time_ms
            delay_sec = delay_ms / 1000.0
            
            if delay_sec > 0:
                # Thay time.sleep(delay_sec)
                if not self._interruptible_sleep(delay_sec, stop_event, pause_event):
                    break # Bị ngắt
            
            keys_to_play_list = grouped_notes[timestamp_ms]
            chord_string = "".join(keys_to_play_list)
            self._press_keys_sync(chord_string)
            last_time_ms = timestamp_ms

            # Kiểm tra sau khi nhấn (để dừng ngay)
            if stop_event.is_set():
                break

        if stop_event.is_set():
            print("Da DUNG bai hat (Kieu JSON).")
        else:
            print("Da phat xong 'Sheet Nhac' (Kieu JSON).")