import time
import random
import os

def main_menu():
    clear_screen()
    print("    _   ______  ____    _    __")
    print("   / | / / __ \/ __ \  | |  / /")
    print("  /  |/ / / / / /_/ /  | | / /")
    print(" / /|  / /_/ / _, _/   | |/ /")
    print("/_/ |_/\____/_/ |_|    |___/")
    print_colored("Yuvi - Crazy Hackers", "cyan")
    print_colored("Contact: WhatsApp +918950027349", "yellow")
    print("1. Launch Attack\n2. Brute Force\n3. Help\n4. Check for Updates\n5. Contact Us")
    choice = input("Enter your choice: ")

    if choice == '1' or choice == '2':
        password = input("Enter the key password: ")
        if password == "Yuvi Hacker":
            victim_username = input("Enter the victim's username: ")
            process = "Launching Attack" if choice == '1' else "Brute Forcing"
            print_colored(f"{process} against {victim_username}", "green" if choice == '1' else "yellow")
            perform_process(process, victim_username)
        else:
            print_colored("Incorrect key password. Access denied.", "red")
    elif choice == '3':
        print("Help menu content here.")
    elif choice == '4':
        print("Checking for updates...")
        time.sleep(2)
        print("No updates available.")
    elif choice == '5':
        print("Contact us at: WhatsApp +918950027349")
    else:
        print_colored("Invalid choice. Please select a valid option.", "red")

def perform_process(process, victim_username):
    keyword_list = []  # Store all found keywords
    total_iterations = 200  # Repeat the process 200 times
    for _ in range(total_iterations):
        progress_bar(process, 100)
        result = "Success" if process == "Launching Attack" else random.choice(["Success", "Failure"])
        if process == "Brute Forcing":
            modified_keyword = modify_keyword(victim_username)
            if result == "Success":
                keyword_list.append(modified_keyword)
                result_text = f"Keyword found: {modified_keyword}"
                print_colored(result_text, "green")
                save_keyword_to_file("brute_force.txt", modified_keyword)
        else:
            print_colored(f"Attack {result}!", "green" if result == "Success" else "red")
        time.sleep(2)  # Pause before next iteration

    if keyword_list:
        save_keywords_to_file("saved_keywords.txt", keyword_list)
        print_colored("Keywords saved to 'saved_keywords.txt'.", "yellow")

def save_keywords_to_file(filename, keywords):
    with open(filename, "w") as file:
        for keyword in keywords:
            file.write(keyword + "\n")

def save_keyword_to_file(filename, keyword):
    with open(filename, "a") as file:
        file.write(keyword + "\n")

def modify_keyword(keyword):
    keyword_variation = "".join(random.choice([c.upper(), c.lower()]) for c in keyword)
    return keyword_variation

def progress_bar(message, total):
    print()
    for i in range(total + 1):
        time.sleep(0.02)
        print(f"\r{message}... {i}% ", end='', flush=True)
    print("\n")

def print_colored(text, color):
    print("\033[{}m{}\033[0m".format(color_codes[color], text))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

color_codes = {
    "red": "31",
    "green": "32",
    "yellow": "33",
    "cyan": "36"
}

if __name__ == "__main__":
    main_menu()
