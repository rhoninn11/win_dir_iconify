import os
import sys
import win32api
import win32con
import win32gui
from PIL import Image

def convert_to_icon(image_path, output_path):
    img = Image.open(image_path)
    img.save(output_path, format='ICO', sizes=[(256, 256)])

def create_ini(path, icon_path):
    ini_file = os.path.join(path, "desktop.ini")
    if os.path.exists(ini_file):
        return
    
    with open(ini_file, "w") as f:
        f.write("[.ShellClassInfo]\n")
        f.write("IconResource=" + icon_path + ",0\n")

    # set attributes
    os.system(f"attrib +h +s {ini_file}")

    # # refresh folder
    win32gui.SendMessage(win32con.HWND_BROADCAST, win32con.WM_SETTINGCHANGE, 0, 'Update;Folder;%s' % path)

def clear_ini_ico(path):
    ini_file = os.path.join(path, "desktop.ini")
    if os.path.exists(ini_file):
        os.remove(ini_file)

def clear_ico(ico_file ):
    if os.path.exists(ico_file):
        os.remove(ico_file)

def process_directory(path, step):
    icon_path_png = os.path.join(path, "icon.png")
    icon_path_jpg = os.path.join(path, "icon.jpg")
    icon_path_ico = os.path.join(path, "icon.ico")

    if os.path.exists(icon_path_png) or os.path.exists(icon_path_jpg):
        if step == "ini":
            create_ini(path, icon_path_ico)
        if step == "ico":
            if os.path.exists(icon_path_png):
                convert_to_icon(icon_path_png, icon_path_ico)
            elif os.path.exists(icon_path_jpg):
                convert_to_icon(icon_path_jpg, icon_path_ico)
        if step == "ini_c":
            clear_ini_ico(path)
        if step == "ico_c":
            clear_ico(icon_path_ico)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            process_directory(item_path, step)

def help_info():
    print("Arguments: ")
    print("   1.'path' - path to directory")
    print("   2.'step' : ini, ico, ini_c, ico_c")

def main():
    # path readed from first argument of script
    if len(sys.argv) > 2:
        parent_dir = sys.argv[1]
        step = sys.argv[2]
        possible_steps = ["ini", "ico", "ini_c", "ico_c"]
        if step in possible_steps:
            process_directory(parent_dir, step)
            return

    print("!!! bad arguments !!!")
    help_info()

if __name__ == "__main__":
    main()