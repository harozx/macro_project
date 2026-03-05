# 🎵 MACRO PLAYER

Ứng dụng Macro Player mạnh mẽ hỗ trợ chơi nhạc tự động trong game (Genshin, Roblox, v.v...) với giao diện GUI thân thiện, luôn nổi trên màn hình và hỗ trợ Hotkey tùy chỉnh hoàn toàn.

---

## 🌟 TÍNH NĂNG NỔI BẬT

- **Giao diện trong suốt 🔆:** Có thể điều chỉnh độ mờ từ 20% đến 100%, không che khuất màn hình game.
- **Mini-mode ⊟:** Thu gọn cửa sổ thành 1 thanh công cụ nhỏ gọn ngang màn hình.
- **Gán Hotkey Tùy Chỉnh ⌨️:** Không gò bó với `F1-F8`. Bạn có thể tùy ý gán phím nào cũng được để tránh xung đột với các game (VD tránh F9 của Steam).
- **Phát / Tạm Dừng Thông Minh ⏸️:** Sẵn sàng Tạm Dừng (Pause) ngay lập tức khi bạn cần chat trong game, nhấn lại phím để Tiếp Tục (Resume) phát tiếp từ vị trí đó. Không lo mất trớn!
- **Tự Động Lưu Trữ (Cache) 💾:** Mọi thay đổi về phím tắt, bài hát yêu thích, trong suốt hay bố cục (Old/New) đều được lưu lại và tự khôi phục vào lần kế tiếp. Không cần phải Setup lại từ đầu mỗi lần mở!
- **Trình Cài Đặt 1 Click ⚡:** File cài đặt có khả năng tự động tải và cài đặt Python, cài đặt thư viện cần thiết (`pynput`) nếu máy chưa có.

---

## 🚀 CÁCH CÀI ĐẶT & SỬ DỤNG

### 1. Khởi động (Chỉ cần 1 Cú Click)
Bạn chỉ cần Double-click vào file:
👉 **`start.vbs`**

- **Lần đầu tiên chạy (hoặc sang máy mới):** Nếu máy chưa có Python hoặc thiếu thư viện `pynput`, script sẽ yêu cầu `Quyền Admin`. Bạn cứ nhấn **Yes**, nó sẽ **tự động tải và cài đặt Python 3.12 (64-bit) & thư viện**. Tự động mở app sau khi cài xong.
- **Các lần sau:** Sau khi đã đủ máy móc, script sẽ chạy âm thầm, không hiện màn hình CMD đen gây khó chịu.

### 2. Tab Nhạc 📂
- Là nơi hiển thị thư viện sheet nhạc nằm trong thư mục `sheets/`. 
- **Tìm kiếm:** Gõ tên bài vào ô "🔍" để lọc bài hát.
- **Phát/Dừng:** Bạn có thể bấm để nghe thử ngay lập tức.
- **Thêm vào Album:** Nhấn nút ❤ để đưa bài vào danh sách bài tủ.

### 3. Tab Hotkey ⌨️
- **Gán bài hát:**
  1. Sang **Tab Nhạc**, chọn 1 bài hát.
  2. Quay lại **Tab Hotkey**, nhấn chữ **"Gán"** ở Slot tùy ý.
- **Đổi Phím Mặc Định:** 
  1. Thay vì dùng F1, F2..., bạn có thể click vào nút tên phím (Ví dụ nhấn vào chữ `F1`). Chữ sẽ đỏ lên biến thành `???`.
  2. **Gõ phím mới bạn muốn** trên bàn phím (ví dụ ~, [, v.v).
  3. Xong! (Nếu lỡ tay thì nhấn `ESC` để huỷ).
  
> Chỉ cần gán 1 lần! Lần sau mở app nó vẫn lưu y nguyên.

### 4. Tab Cài Đặt ⚙️
- **Bảng phím (Layout):** Game có nhiều kiểu sheet cũ và mới `QWE...` vs `ZXC...` Bạn có thể chuyển đổi linh hoạt.
- **Trong Suốt (Alpha):** Kéo thanh trượt để phần mềm chìm vào game, không bị che mất tầm nhìn.
- **Tạm Dừng / Tiếp Tục:** Phím mặc định là **`F9`**. Tương tự Slot Hotkey, tính năng Tạm Dừng cũng có thể **Đổi Phím** bằng cách click vào để gõ phím thay thế (để tránh nút record của Steam hay OBS).

---

## 🎮 KHI VÀO GAME (THỰC CHIẾN)

1. Mở `start.vbs`. Gán các bài hát vào Slot 1-8 ở màn hình Hotkey.
2. Thu nhỏ cửa sổ lại bằng dấu **⊟ Mini Mode** (Hoặc nhét vào một góc, kéo thanh Trong suốt lên).
3. Quay lại màn hình Game:
   - Nhấn phím **Hotkey** bạn đã gán ➝ Bài sẽ tự động Play.
   - Bất chợt có người chat hoặc kẹt quái? Nhấn **F9** (Hoặc phím Pause bạn cài) ➝ Nhạc dừng ngay lập tức!!
   - Xong việc? Nhấn **F9** tiếp ➝ Đánh đàn tiếp tục hoàn hảo từ chỗ đứt quãng.
   - Nhấn **F10** ➝ Huỷ & Dừng hẳn bài hát.
   - Gặp lỗi không tắt được nhạc, kẹt phím? Nhấn **ESC**. Dừng khẩn cấp mọi thứ.
