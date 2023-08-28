#!/data/data/com.termux/files/usr/bin/python

import os

PASSWORD_FILE = "password.txt"
PASSWORD = "Crazy Yuvi"
logged_in = False
search_locked = False

def set_initial_password():
    with open(PASSWORD_FILE, "w") as file:
        file.write(PASSWORD)

def load_password():
    with open(PASSWORD_FILE, "r") as file:
        return file.read().strip()

def login():
    global logged_in
    attempts = 3
    while attempts > 0:
        user_input = input("\033[1;33mEnter password to access the script:\033[0m ")
        if user_input == load_password():
            print("\033[1;32mLogin successful!\033[0m")
            logged_in = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"\033[1;31mIncorrect password. {attempts} attempts remaining.\033[0m")
    if not logged_in:
        print("\033[1;31mToo many incorrect attempts. Exiting.\033[0m")
        exit()

def start_tor():
    os.system("tor")

def stop_tor():
    os.system("pkill -f tor")

def restart_network():
    os.system("svc data disable")
    os.system("svc data enable")
    print("\033[1;36mNetwork connection restarted.\033[0m")

def check_ip():
    os.system("torsocks curl -s https://api64.ipify.org?format=json")

def toggle_wifi(state):
    os.system(f"su -c svc wifi {state}")
    print("\033[1;36mWi-Fi", "enabled." if state == "enable" else "disabled.\033[0m")

def toggle_hotspot(state):
    os.system(f"su -c svc wifi {state}")
    print("\033[1;36mHotspot", "enabled." if state == "enable" else "disabled.\033[0m")

def search():
    if search_locked:
        print("\033[1;31mSearch is currently locked.\033[0m")
        return
    query = input("\033[1;33mEnter search query:\033[0m ")
    print(f"\033[1;36mSearching for: {query}\033[0m")

    os.system("torsocks curl -s 'https://www.startpage.com/do/search?q=" + query + "' > search_results.html")

    with open("search_results.html", "r") as file:
        content = file.read()
        lines = content.split("<h3 class=\"search-item__title\">")[1:]
        counter = 1
        print("\033[1;34mSearch Results:\033[0m")
        results = []
        for line in lines:
            title = line.split("</h3>")[0]
            results.append(title)
            print(f"{counter}. {title}")
            counter += 1
        return results

def save_results(results):
    filename = input("\033[1;33mEnter a filename to save the results:\033[0m ")
    with open(filename, "w") as file:
        for result in results:
            file.write(result + "\n")
    print("\033[1;36mSearch results saved to", filename, "\033[0m")

def show_contact():
    print("\033[1;36mDeveloper: Yuvi")
    print("Channel: Hack_heaven by Crazy hacker")
    print("Contact: WhatsApp +918950027349\033[0m")

# Check if the password file exists
if not os.path.exists(PASSWORD_FILE):
    set_initial_password()

# Display menu
while True:
    if not logged_in:
        login()
    print("\033[1;32m  *** TOR Access Menu ***\033[0m")
    print("1. \033[1;34mStart TOR\033[0m")
    print("2. \033[1;34mStop TOR\033[0m")
    print("3. \033[1;34mRestart Network\033[0m")
    print("4. \033[1;34mCheck IP Address\033[0m")
    print("5. \033[1;34mToggle Wi-Fi\033[0m")
    print("6. \033[1;34mToggle Hotspot\033[0m")
    print("7. \033[1;34mSearch using TOR\033[0m")
    print("8. \033[1;34mSave Search Results\033[0m")
    print("9. \033[1;34mLock/Unlock Search\033[0m")
    print("10. \033[1;34mShow Developer Info\033[0m")
    print("11. \033[1;31mExit\033[0m")
    choice = input("\033[1;33mEnter your choice:\033[0m ")

    if choice == "1":
        start_tor()
    elif choice == "2":
        stop_tor()
    elif choice == "3":
        restart_network()
    elif choice == "4":
        check_ip()
    elif choice == "5":
        toggle_wifi("disable" if os.system("svc wifi") == 0 else "enable")
    elif choice == "6":
        toggle_hotspot("disable" if os.system("svc wifi") == 0 else "enable")
    elif choice == "7":
        search()
    elif choice == "8":
        save_results(results)
        print("\033[1;36mSearch results saved.\033[0m")
    elif choice == "9":
        search_locked = not search_locked
        print("\033[1;36mSearch is now", "locked." if search_locked else "unlocked.\033[0m")
    elif choice == "10":
        show_contact()
    elif choice == "11":
        print("\033[1;35mExiting.\033[0m")
        break
    else:
        print("\033[1;31mInvalid option.\033[0m")
