import autoit

def IG_CATS_toggle():
    autoit.control_click("CATS Main Window", "WindowsForms10.BUTTON.app.0.141b42a_r9_ad124")
    
def test_autoit():
    autoit.run("notepad.exe")
    autoit.win_wait_active("[CLASS:Notepad]", 3)
    autoit.control_send("[CLASS:Notepad]", "Edit1", "hello world{!}")
