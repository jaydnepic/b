import time, uuid, zipfile, os
try:
    import requests, webbrowser, subprocess, fade, mss, keyboard, win32api, numpy
    from colorama import Fore
    from io import BytesIO
except ImportError:
    print("Error: some required libraries are not installed. installing them.")
    os.system("pip install colorama requests fade mss keyboard pywin32 numpy")
    input("press enter to close...")
    exit()
print("all libraries installed and working, opening loader.")
time.sleep(1)
vers = 4
os.system("cls")

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

if ur a .gg/weezy member, i recommend you leave sooner than you think. 
stellar external real server: .gg/stellarblx                                                    

"""
logoo = fade.water(logo)
print(logoo)

sz = """
Selections: 
1. Valorant TB (colorbot lookalike) 
2. Roblox TB (ahk by @venueofdeath)
3. Error Fixes
4. Uninject Malware from Discord
5. Update Loader
6. Discord Server (support and updates.)
7. Roblox TB Python (soon)
"""

szz = fade.greenblue(sz)
print(szz)

discord_url = "https://discord.gg/TZvR4gy42Q"
webbrowser.open(discord_url)

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
elif selection == "4":
    username = os.getlogin()
    file_path = fr'C:\\Users\\{username}\\AppData\\Local\\Discord\\app-1.0.9161\\modules\\discord_desktop_core-1\\discord_desktop_core\\index.js'
    print("really simple dis'cord uninfestor")
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

elif selection == "5":
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
elif selection == "6":
    discord_url = "https://discord.gg/TZvR4gy42Q"
    webbrowser.open(discord_url)
    print("plez join if ur not in")
    time.sleep(2)
elif selection == "7":
    print("soon coming, stay tuned!")
    time.sleep(2)
else:
    print("not an option 😭😭😭😭")
    time.sleep(2)
