from app_files import effects as ef

import curses
from datetime import datetime
import time
import sys
from app_files.globals import name, city, age, admin_password, last_resort, user_commands, best_friend, address, postal_code, zip_code, work_hours, todays_date

from app_files.admin import admin_page, history
from app_files import homescreen as home
from app_files.guess import game, guessing_game
from app_files.impressions import impressions_game
from app_files.interview import about_cleo
from app_files.todo import todo_app
from app_files.weather import weather_app


def main() -> None:
    ef.admin_generate()
    ef.log_file_create()

    start_up(phase=0)
    intro_scene(phase=0)
    # First crashout restart
    start_up(phase=0)
    # Reboot
    intro_scene(phase=1)
    start_up(phase=1)
    # First meeting Cleo
    cleo(phase=0)
    # Second crashout restart
    cleo(phase=1)
    # Cleo off the rails
    start_up(phase=2)
    cleo(phase=2)

    cleo(phase=3)
    cleo(phase=4)

    cleo_finale()

def start_up(phase=0) -> None:
    ef.clear_screen()
    ef.cursor_off()

    print("Initializing")
    ef.progress_bar(40)
    ef.clear_screen()

    ef.spinner(seconds=5, text="Processing... ")
    ef.clear_screen

    if phase == 0:
        ef.print_splash("cin.txt")
        time.sleep(5)
        ef.press_enter()
        ef.clear_screen()
        time.sleep(3)
    elif phase == 1:
        ef.print_splash("cli0.txt")
        time.sleep(5)
        ef.press_enter()
        ef.clear_screen()
        time.sleep(3)    
    elif phase == 2:
        ef.print_splash("cli3.txt")
        time.sleep(5)
        ef.press_enter("I've been expecting you")
        ef.clear_screen()
        time.sleep(3)
        


def intro_scene(phase=0) -> None:
    ef.clear_screen()
    ef.cursor_off()

    print("Hello, thank you for participating in the CLI.0 Beta Test.\n")
    time.sleep(4)
    ef.clear_screen()
    time.sleep(2)

    name.append(ef.check_name_standard())

    ef.clear_screen()
    time.sleep(2)

    city.append(ef.cli_input("Please enter your city of origin: "))
    ef.clear_screen()
    time.sleep(2)

    age.append(ef.cli_input("Please enter your age: "))


    # First system crash fake-out
    if phase == 0:
        ef.print_splash("type_error.txt", center=False)
        print("C:\\beta_test\\user_173>", end="")
        ef.cursor_on()
        sys.stdout.flush()
        time.sleep(5)
        ef.type_out(".\\communicate.exe", delay=0.04, pause=False)
        ef.cursor_off()
        ef.clear_screen()

        ef.typing_message(cycles=3, start_sleep=2)
        print("Niel: Hey sorry about that. Just a simple error.")
    
        ef.typing_message(cycles=4, start_sleep=2)
        print("Niel: The computer thought your age was a number haha.")

        ef.typing_message(cycles=2, start_sleep=1)
        print("Niel: I'll fix that, one sec.")

        ef.typing_message(cycles=2, start_sleep=4)
        print("Niel: I'm your designated specialist.")

        ef.typing_message(cycles=1, start_sleep=1)
        print("Niel: By the way.")

        ef.typing_message(cycles=1, start_sleep=2)
        print("Niel: Haha")

        ef.typing_message(cycles=2, start_sleep=4)
        print("Niel: Okay that should do the trick.")

        ef.typing_message(cycles=6, start_sleep=1)
        print("Niel: That might happen every now and then, we're still in beta")
        print("      afterall! I know the wall of text is intimidating, but don't")
        print("      worry about a thing. If it looks like a mess of gibberish to")
        print("      you, then it's probably harmless!")

        ef.typing_message(cycles=2, start_sleep=8)
        print("Niel: Anyway, I'll start it back up for you.")
        time.sleep(3)
        return
    
    elif phase == 1:
        ef.clear_screen()
        ef.cursor_off()
        time.sleep(2)
        print("Thank you for completing the introductory survey.")
        time.sleep(4)
        ef.clear_screen()
        time.sleep(3)
        return
    

def cleo(phase=0) -> None:
    if (phase == 0) or (phase == 1):
        ef.clear_screen()
        ef.cursor_off()

        ef.type_out("Hello, welcome to your new digital assistant!")
        ef.type_out("My name is Cleo :)")

        name.append(ef.check_name_scary())
        ef.clear_screen()

        ef.type_out(f"Nice to meet you, {name[2].capitalize()}!")
        ef.type_out("With the help of good, law-abiding citizens like you, we\ncan develop CLI.0 into CLI.1.0 :)", pause=3)
        ef.clear_screen()



    if phase == 0:
        ef.type_out("Let me give you a tour of what I have to offer!")
        ef.type_out("1. I can tell you your local weather. Hope it's sunny!\n", clear=False)
        ef.type_out("2. I can write you a to-do list. Organization is key!\n", clear=False)
        ef.type_out("3. I can keep your mind sharp with a guessing game!\n", clear=False)
        ef.type_out("4. Curious? You can get to know me!\n", clear=False)
        ef.type_out("5. Finally, if you get bored", clear=False)
        ef.type_out("... ",delay=0.7, clear=False)
        ef.type_out("I do some great impressions :)", clear=False)
        ef.clear_screen()
        
        ef.type_out("Why don't we get st\n", pause=5, clear=False)
        ef.type_out("Why don't we get started :", pause=1)
        sys.stdout.flush()
        ef.glitch_shake("Why don't we get started :")
        print("Why don't we get started :")
        sys.stdout.flush()
        time.sleep(1)
        ef.clear_screen()
        print("\033[1;31mFatal Error:\033[0m 1/3")
        print("\033[1;33mWarning:\033[0m Triggering all fatal errors can result in undefined behavior.")
        print("Please reset the program to avoid catastrophic failure.", end="")
        sys.stdout.flush()
        time.sleep(8)
        print("""(most recent call last):
  File "cli0_beta.py", line 181, in <module>
    cleo()
  File "cli0_beta.py\\main.py", line 144, in cleo
    ef.type_out("Why don't we get started :)")
  File "cli_beta.py", line 277, in type_out
    time.sleep(delay)
KeyboardInterrupt""")
        print("C:\\beta_test\\user_173>", end="")
        ef.cursor_on()
        sys.stdout.flush()
        time.sleep(5)
        ef.type_out(".\\communicate.exe", delay=0.04, pause=False)
        ef.cursor_off()
        ef.clear_screen()

        ef.typing_message(cycles=3, start_sleep=2)
        print("Niel: Ah okay, see? That's actually something to worry about.")
        
        ef.typing_message(cycles=2, start_sleep=3)
        print("Niel: No need to panic though!")

        ef.typing_message(cycles=4, start_sleep=1)
        print("Niel: As long as I'm here to reset the program, there's no way")
        print("      all three fatal errors can trigger.")

        ef.typing_message(cycles=4, start_sleep=4)
        print("Niel: Okay I'm going to reset the program one more time. I was")
        print("      able to catch a save state before the crash this time.")
        print("      I'll start you up where you left off.")
        time.sleep(8)

        return
    
    elif phase == 1:
        home.phase_1()

    elif phase == 2:
        home.phase_2()
        guessing_game()

    elif phase == 3:
        ef.clear_screen()
        ef.cursor_off()

        ef.type_out("Hello, welcome to your new digital assistant!")
        ef.type_out("My name is Cleo :)")

        newer_name  = ef.check_name_scary()
        name.append(newer_name)
        ef.clear_screen()

        ef.type_out("Oh! Niel tells me you've been here before!")
        ef.type_out(f"Hello, {newer_name.capitalize()} :)")
        
        ef.type_out("Let's get back to business :)")
        home.phase_3()

    elif phase == 4:
        ef.clear_screen()
        ef.cursor_off()

        ef.type_out("Looks like there is only one more to go :)")
        home.phase_4()


def cleo_finale() -> None:
    start_up(phase=0)
    ef.clear_screen()
    ef.cursor_off()

    ef.save_date()
    ef.save_time()

    print("Hello, thank you for participating in the CLI.0 Beta Test.")
    time.sleep(4)

    while len(user_commands) < 3:
        ef.clear_screen()
        time.sleep(2)

        forbidden_name = ef.check_name_standard()
        name.append(forbidden_name)
        user_commands.append(forbidden_name)
        ef.save_time()
        ef.forbidden_input("access_logs", success=True)

    ef.clear_screen()
    ef.log_file_update("ADMIN -- failed to add system critical input")
    ef.log_file_update(f"{admin_password[0]} -- failed to add system critical input")
    ef.log_file_update(f"{last_resort[0]} -- failed to add system critical input")
    for i in range(3):
        ef.log_file_update(user_commands[i])

    ef.save_time()

    while True:
        ef.clear_screen()
        print("""\033[1;32m3\033[0m new entries added to FORBIDDEN_COMMANDS
\033[1;32m6\033[0m new entries added to FORBIDDEN_COMMANDS.txt
Conflicts: \033[1;31m3\033[0m
Please address failed commands in FORBIDDEN_COMMANDS.txt""")
        ef.cli_input(">>")

 

if __name__ == "__main__":
    main()




 

