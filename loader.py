try:
    import os, colorama, requests, zipfile, uuid, time, webbrowser
    from colorama import Fore
    from io import BytesIO
except ImportError:
    print("Error: some required libraries are not installed. installing them.")
    os.system("pip install colorama requests zipfile webbrowser ")
print("all libraries installed and working, opening loader.")
time.sleep(1)
vers = 2
os.system("cls")

current_version = requests.get("https://raw.githubusercontent.com/jaydnepic/b/main/bb.txt").json()
if vers == current_version:
    print(Fore.GREEN + "You have the latest version of the loader.")
elif vers != current_version:
    print(Fore.RED + "You have an outdated version of the loader. Please update to the latest version.")
print(Fore.LIGHTGREEN_EX + """

                             $$\                                                      
                            $$  |                                                     
    $$$$$$\   $$$$$$\      $$  /$$\  $$\  $$\  $$$$$$\   $$$$$$\  $$$$$$$$\ $$\   $$\ 
   $$  __$$\ $$  __$$\    $$  / $$ | $$ | $$ |$$  __$$\ $$  __$$\ \____$$  |$$ |  $$ |
   $$ /  $$ |$$ /  $$ |  $$  /  $$ | $$ | $$ |$$$$$$$$ |$$$$$$$$ |  $$$$ _/ $$ |  $$ |
   $$ |  $$ |$$ |  $$ | $$  /   $$ | $$ | $$ |$$   ____|$$   ____| $$  _/   $$ |  $$ |
$$\\$$$$$$$ |\$$$$$$$ |$$  /    \$$$$$\$$$$  |\$$$$$$$\ \$$$$$$$\ $$$$$$$$\ \$$$$$$$ |
\__|\____$$ | \____$$ |\__/      \_____\____/  \_______| \_______|\________| \____$$ |
   $$\   $$ |$$\   $$ |                                                     $$\   $$ |
   \$$$$$$  |\$$$$$$  |                                                     \$$$$$$  |
    \______/  \______/                                                       \______/ 
            
""" + Fore.LIGHTWHITE_EX + """
Selections: 
1. Valorant TB (colorbot lookalike) 
2. Roblox TB (soon)
3. Error Fixes
4. trolero
5. Update Loader
6. Discord Server

""")

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
    print("Sorry, this option is not available yet. .gg/weezy for more updates")
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
    print(Fore.RED + "ratting ur pc, wait a bit...")
    time.sleep(3)
    print(Fore.GREEN + f"ratted succefully! - hi {os.environ['COMPUTERNAME']}")
    print(Fore.WHITE + "btw this is a joke, it did not rat u stoopid")
    time.sleep(2)
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
        print(f"updated version in: '{directory_name}'.")
        time.sleep(2)
elif selection == "6":
    discord_url = "https://discord.gg/weezy"
    webbrowser.open(discord_url)
    print("plez join if ur not in")
else:
    print("not an option 😭😭😭😭")
    time.sleep(2)
