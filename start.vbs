' Macro Player Launcher
' - Kiem tra Python va pynput
' - Neu chua co: chay setup.bat de cai dat
' - Neu da co: chay gui.py truc tiep (khong hien CMD)

Dim objFSO, objShell, strDir
Set objFSO   = CreateObject("Scripting.FileSystemObject")
Set objShell = CreateObject("Shell.Application")
strDir = objFSO.GetParentFolderName(WScript.ScriptFullName)

' === KIEM TRA PYTHON ===
Dim objExec, bNeedSetup
bNeedSetup = False

On Error Resume Next
Set objExec = CreateObject("WScript.Shell").Exec("python -c ""import pynput""")
objExec.StdOut.ReadAll()
If objExec.ExitCode <> 0 Then bNeedSetup = True
On Error GoTo 0

' === KIEM TRA PYTHON CO TON TAI KHONG ===
If bNeedSetup Then
    Dim answer
    answer = MsgBox("Chua du cai dat (Python hoac pynput)." & Chr(13) & Chr(13) & _
                    "Nhan YES de tu dong cai dat va chay." & Chr(13) & _
                    "Nhan NO de thoat.", _
                    vbYesNo + vbQuestion, "Macro Player - Can Cai Dat")
    If answer = vbYes Then
        ' Chay setup.bat voi quyen Admin va doi ket thuc
        objShell.ShellExecute "cmd.exe", _
            "/c """ & strDir & "\setup.bat""", strDir, "runas", 1
    End If
Else
    ' === MOI THU OK: CHAY GUI KHONG HIEN CMD ===
    objShell.ShellExecute "pythonw.exe", _
        """" & strDir & "\gui.py""", strDir, "runas", 0
End If
