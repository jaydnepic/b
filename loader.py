import time, uuid, zipfile, os
try:
    import requests, webbrowser, subprocess, fade, mss, keyboard, win32api, numpy, ctypes
    from colorama import Fore
    from io import BytesIO
except ImportError:
    print("Error: some required libraries are not installed. installing them.")
    os.system("pip install colorama requests fade mss keyboard pywin32 numpy pynput")
    input("press enter to close...")
    exit()
print("all libraries installed and working, opening loader.")
time.sleep(1)
vers = 6
os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("shatted.lol | free valorant triggerbot loader")
username = os.getlogin()
current_version = requests.get("https://raw.githubusercontent.com/jaydnepic/b/main/bb.txt").json()
if vers == current_version:
    print(Fore.GREEN + "You have the latest version of the loader.")
elif vers != current_version:
    print(Fore.RED + "You have an outdated version of the loader. Please update to the latest version.")

logo = """
  ██████  ██░ ██  ▄▄▄     ▄▄▄█████▓▄▄▄█████▓▓█████ ▓█████▄       ██▓     ▒█████   ██▓    
▒██    ▒ ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌     ▓██▒    ▒██▒  ██▒▓██▒    
░ ▓██▄   ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒███   ░██   █▌     ▒██░    ▒██░  ██▒▒██░    
  ▒   ██▒░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌     ▒██░    ▒██   ██░▒██░    
▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░ ░▒████▒░▒████▓  ██▓ ░██████▒░ ████▓▒░░██████▒
▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒  ▒▓▒ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▓  ░
░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░   ░        ░     ░ ░  ░ ░ ▒  ▒  ░▒  ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░ ▒  ░
░  ░  ░   ░  ░░ ░  ░   ▒    ░        ░         ░    ░ ░  ░  ░     ░ ░   ░ ░ ░ ▒    ░ ░   
      ░   ░  ░  ░      ░  ░                    ░  ░   ░      ░      ░  ░    ░ ░      ░  ░
                                                    ░        ░
BOOST discord.gg/shatted SO I CAN KEEP THE VANITY PLSSS MORE UPDATES ARE GONNA COME OUT TRUST ME 🙏🙏🙏🙏
"""
logoo = fade.water(logo)
print(logoo)

sz = """
Selections: 
1. Valorant TB (colorbot lookalike)
1.1 Valorant Auto Counterstrafe 
1.2 Virtual Keycode Grabber
2. Roblox TB AHK [ass] (ahk by @venueofdeath)
3. Error Fixes
4. Uninject Malware from Discord
5. Roblox Address Dumper (src) (looks like its been patched.)
6. Update Loader
7. Discord Server (support and updates.)
gave up on roblox stuff, made an ai gen pred in https://discord.gg/39C6bzkPTN
"""
file = f'C:\shatted.lol\inv.txt'
newpath = r'C:\shatted.lol'
if not os.path.exists(newpath):
    os.makedirs(newpath)
if os.path.exists(file):
    pass
else:
    open(file, 'a').close()
    discord_url = "https://discord.gg/TZvR4gy42Q"
    webbrowser.open(discord_url)
szz = fade.greenblue(sz)
print(szz)


selection = input(Fore.LIGHTGREEN_EX + "> ")

if selection == "1":
    print("downloading valorant triggerbot...")
    download = requests.get("https://github.com/jaydnepic/b/raw/main/b.zip")
    zip_file = zipfile.ZipFile(BytesIO(download.content))
    directory_name = str(uuid.uuid4())
    os.makedirs(directory_name, exist_ok=True)
    zip_file.extractall(directory_name)
    print(f"valorant triggerbot downloaded and extracted successfully in '{directory_name}'.")
    time.sleep(2)
elif selection == "1.1":
    print("downloading valorant auto counterstrafe...")
    download = requests.get("https://cdn.discordapp.com/attachments/1284214250235105401/1287853184882053230/counter_strafe.zip?ex=66f30e3e&is=66f1bcbe&hm=3e56286982197b12304f9c8fff3c4f2cb7b99c18fc2065aa97a3f33d5d9d4840&")
    zip_file = zipfile.ZipFile(BytesIO(download.content))
    directory_name = str(uuid.uuid4())
    os.makedirs(directory_name, exist_ok=True)
    zip_file.extractall(directory_name)
    print(f"valorant auto counterstrafe downloaded and extracted successfully in '{directory_name}'.")
elif selection == "1.2":
    import ctypes
    from pynput import keyboard, mouse
    import win32api, time
    import win32con
    print("Press any button on your mouse or keyboard to capture its Microsoft virtual keycode.")

    VIRTUAL_KEYCODE_TABLE = {
        0x00: "VK_NONE",
        0x01: "VK_LBUTTON",
        0x02: "VK_RBUTTON",
        0x03: "VK_CANCEL",
        0x04: "VK_MBUTTON",
        0x05: "VK_XBUTTON1",
        0x06: "VK_XBUTTON2",
        0x08: "VK_BACK",
        0x09: "VK_TAB",
        0x0C: "VK_CLEAR",
        0x0D: "VK_RETURN",
        0x10: "VK_SHIFT",
        0x11: "VK_CONTROL",
        0x12: "VK_MENU",
        0x13: "VK_PAUSE",
        0x14: "VK_CAPITAL",
        0x15: "VK_KANA",
        0x17: "VK_JUNJA",
        0x18: "VK_FINAL",
        0x19: "VK_HANJA",
        0x1B: "VK_ESCAPE",
        0x1C: "VK_CONVERT",
        0x1D: "VK_NONCONVERT",
        0x1E: "VK_ACCEPT",
        0x1F: "VK_MODECHANGE",
        0x20: "VK_SPACE",
        0x21: "VK_PRIOR",
        0x22: "VK_NEXT",
        0x23: "VK_END",
        0x24: "VK_HOME",
        0x25: "VK_LEFT",
        0x26: "VK_UP",
        0x27: "VK_RIGHT",
        0x28: "VK_DOWN",
        0x29: "VK_SELECT",
        0x2A: "VK_PRINT",
        0x2B: "VK_EXECUTE",
        0x2C: "VK_SNAPSHOT",
        0x2D: "VK_INSERT",
        0x2E: "VK_DELETE",
        0x2F: "VK_HELP",
        0x30: "VK_0",
        0x31: "VK_1",
        0x32: "VK_2",
        0x33: "VK_3",
        0x34: "VK_4",
        0x35: "VK_5",
        0x36: "VK_6",
        0x37: "VK_7",
        0x38: "VK_8",
        0x39: "VK_9",
        0x41: "VK_A",
        0x42: "VK_B",
        0x43: "VK_C",
        0x44: "VK_D",
        0x45: "VK_E",
        0x46: "VK_F",
        0x47: "VK_G",
        0x48: "VK_H",
        0x49: "VK_I",
        0x4A: "VK_J",
        0x4B: "VK_K",
        0x4C: "VK_L",
        0x4D: "VK_M",
        0x4E: "VK_N",
        0x4F: "VK_O",
        0x50: "VK_P",
        0x51: "VK_Q",
        0x52: "VK_R",
        0x53: "VK_S",
        0x54: "VK_T",
        0x55: "VK_U",
        0x56: "VK_V",
        0x57: "VK_W",
        0x58: "VK_X",
        0x59: "VK_Y",
        0x5A: "VK_Z",
        0x5B: "VK_LWIN",
        0x5C: "VK_RWIN",
        0x5D: "VK_APPS",
        0x5F: "VK_SLEEP",
        0x60: "VK_NUMPAD0",
        0x61: "VK_NUMPAD1",
        0x62: "VK_NUMPAD2",
        0x63: "VK_NUMPAD3",
        0x64: "VK_NUMPAD4",
        0x65: "VK_NUMPAD5",
        0x66: "VK_NUMPAD6",
        0x67: "VK_NUMPAD7",
        0x68: "VK_NUMPAD8",
        0x69: "VK_NUMPAD9",
        0x6A: "VK_MULTIPLY",
        0x6B: "VK_ADD",
        0x6C: "VK_SEPARATOR",
        0x6D: "VK_SUBTRACT",
        0x6E: "VK_DECIMAL",
        0x6F: "VK_DIVIDE",
        0x70: "VK_F1",
        0x71: "VK_F2",
        0x72: "VK_F3",
        0x73: "VK_F4",
        0x74: "VK_F5",
        0x75: "VK_F6",
        0x76: "VK_F7",
        0x77: "VK_F8",
        0x78: "VK_F9",
        0x79: "VK_F10",
        0x7A: "VK_F11",
        0x7B: "VK_F12",
        0x7C: "VK_F13",
        0x7D: "VK_F14",
        0x7E: "VK_F15",
        0x7F: "VK_F16",
        0x80: "VK_F17",
        0x81: "VK_F18",
        0x82: "VK_F19",
        0x83: "VK_F20",
        0x84: "VK_F21",
        0x85: "VK_F22",
        0x86: "VK_F23",
        0x87: "VK_F24",
        0x90: "VK_NUMLOCK",
        0x91: "VK_SCROLL",
        0xA0: "VK_LSHIFT",
        0xA1: "VK_RSHIFT",
        0xA2: "VK_LCONTROL",
        0xA3: "VK_RCONTROL",
        0xA4: "VK_LMENU",
        0xA5: "VK_RMENU",
        0xA6: "VK_BROWSER_BACK",
        0xA7: "VK_BROWSER_FORWARD",
        0xA8: "VK_BROWSER_REFRESH",
        0xA9: "VK_BROWSER_STOP",
        0xAA: "VK_BROWSER_SEARCH",
        0xAB: "VK_BROWSER_FAVORITES",
        0xAC: "VK_BROWSER_HOME",
        0xAD: "VK_VOLUME_MUTE",
        0xAE: "VK_VOLUME_DOWN",
        0xAF: "VK_VOLUME_UP",
        0xB0: "VK_MEDIA_NEXT_TRACK",
        0xB1: "VK_MEDIA_PREV_TRACK",
        0xB2: "VK_MEDIA_STOP",
        0xB3: "VK_MEDIA_PLAY_PAUSE",
        0xB4: "VK_LAUNCH_MAIL",
        0xB5: "VK_LAUNCH_MEDIA_SELECT",
        0xB6: "VK_LAUNCH_APP1",
        0xB7: "VK_LAUNCH_APP2",
        0xBA: "VK_OEM_1",
        0xBB: "VK_OEM_PLUS",
        0xBC: "VK_OEM_COMMA",
        0xBD: "VK_OEM_MINUS",
        0xBE: "VK_OEM_PERIOD",
        0xBF: "VK_OEM_2",
        0xC0: "VK_OEM_3",
        0xDB: "VK_OEM_4",
        0xDC: "VK_OEM_5",
        0xDD: "VK_OEM_6",
        0xDE: "VK_OEM_7",
        0xDF: "VK_OEM_8",
        0xE1: "VK_OEM_AX",
        0xE2: "VK_OEM_102",
        0xE5: "VK_PROCESSKEY",
        0xE6: "VK_PACKET",
        0xE7: "VK_ATTN",
        0xE8: "VK_CRSEL",
        0xE9: "VK_EXSEL",
        0xEA: "VK_EREOF",
        0xEB: "VK_PLAY",
        0xEC: "VK_ZOOM",
        0xED: "VK_NONAME",
        0xEE: "VK_PA1",
        0xEF: "VK_OEM_CLEAR"
    }


    def get_virtual_keycode(key):
        if isinstance(key, int):
            return key
        elif hasattr(key, 'value'):
            return key.value
        else:
            return None

    def on_press(key):
        virtual_keycode = get_virtual_keycode(key)
        if virtual_keycode is not None:
            time.sleep(0.3)
            print(f"0x{virtual_keycode:02X}")
            time.sleep(1)
    def on_click(x, y, button, pressed):
        if pressed:
            virtual_keycode = win32api.GetAsyncKeyState(button)
            if virtual_keycode:
                print(f"0x{virtual_keycode:02X}")

    def get_input():
        while True:
            for key in range(0, 0xFF):
                if win32api.GetAsyncKeyState(key) & 0x8000:
                    on_press(key)
            for button in [win32con.VK_LBUTTON, win32con.VK_RBUTTON, win32con.VK_MBUTTON]:
                if win32api.GetAsyncKeyState(button) & 0x8000:
                    on_click(0, 0, button, True)

    if __name__ == "__main__":
        get_input()

elif selection == "2":
    print("downloading roblox ahk triggerbot...")
    download = requests.get("https://raw.githubusercontent.com/jaydnepic/b/main/triggerbot.ahk")
    with open("downloaded_content.txt", "w", encoding="utf-8") as file:
        file.write(download.text)
    os.rename("downloaded_content.txt", "ahk_triggerbot.ahk")
    print("downloaded, check folder.")
    time.sleep(2)
elif selection == "3":
    print("checking some shit...")
    try:
        import keyboard
        import win32api
        import ctypes
        import numpy
        import mss
    except ImportError:
        print(Fore.RED + "one or more of the required libraries are missing.")
        print(Fore.LIGHTWHITE_EX + "would u like to install? (y/n) ")
        bleeh = input(">")
        if bleeh == "y" or "Y":
            os.system("pip install keyboard pywin32 numpy mss")
        else:
            print("alr ur getting touched")
        time.sleep(2)
    else:
        print(Fore.GREEN + "all required libraries are installed.")
        time.sleep(2)
elif selection == "5":
    print("downloading roblox address dumper...")
    download = requests.get("https://cdn.discordapp.com/attachments/1275527195686735905/1282330055476904052/address_dumper.zip?ex=66def66d&is=66dda4ed&hm=da8e78743748e7d23857fdbaca473126d96a65a514d6d77d8ac7e6f683faeecc&")
    zip_file = zipfile.ZipFile(BytesIO(download.content))
    directory_name = str(uuid.uuid4())
    os.makedirs(directory_name, exist_ok=True)
    zip_file.extractall(directory_name)
    print(f"dumper downloaded and extracted successfully in '{directory_name}'.")
    time.sleep(2)
elif selection == "4":
    base_path = fr'C:\\Users\\{username}\\AppData\\Local\\Discord\\'

    app_dir = None
    for dir_name in os.listdir(base_path):
        if dir_name.startswith('app-'):
            app_dir = dir_name
            break
    if app_dir:
        file_path = os.path.join(base_path, app_dir, 'modules', 'discord_desktop_core-1', 'discord_desktop_core', 'index.js')
        print("really simple discord uninfestor")
        with open(file_path, 'r') as file:
            content = file.read()
            if content == "module.exports = require('./core.asar');":
                print("Discord is already uninfested.")
            else:
                with open(file_path, 'w') as file:
                    print("uninfesting discord...")
                    file.write("module.exports = require('./core.asar');")
                    print("Discord has been uninfested.")
                    print(f"old contents {content}")
        input("press enter to exit...")
    else:
        print("No directory starting with 'app-' found.")
elif selection == "6":
    print("checking version...")
    current_version = requests.get("https://raw.githubusercontent.com/jaydnepic/b/main/bb.txt").json()
    if vers == current_version:
        print(Fore.GREEN + f"You're running the latest version ({vers})")
    else:
        print(Fore.RED + "outdated loader! ; updating...")
        download = requests.get("https://raw.githubusercontent.com/jaydnepic/b/main/loader.py")
        directory_name = str(uuid.uuid4())
        os.makedirs(directory_name, exist_ok=True)
        file_path = os.path.join(directory_name, "loader.py")
        with open(file_path, "wb") as file:
            file.write(download.content)

        print(f"updated version in: '{directory_name}'.")
        time.sleep(2)
        subprocess.run(["python", file_path])
elif selection == "7":
    discord_url = "https://discord.gg/TZvR4gy42Q"
    webbrowser.open(discord_url)
    print("plez join if ur not in")
    time.sleep(2)
elif selection == "8":
    print("you found the secret option! now get out")
    time.sleep(2)
else:
    print("not an option 😭😭😭😭")
    time.sleep(2)
