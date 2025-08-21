from . import effects as ef
import time
import sys
from .globals import name, city, age, apps, completion, best_friend

from .weather import weather_app
from .todo import todo_app
from .interview import about_cleo
from.impressions import impressions_game

def phase_1() -> None:
    ef.type_out("Why don't we get started :)")

    while len(completion) < 2:
        ef.clear_screen()
        ef.print_splash("home_screen1.txt")
        choice = ef.home_screen_input("Enter a number: ")
        
        if (str(choice) in apps) and (str(choice) not in completion):
            match choice:
                case "1":
                    weather_app()
                case "2":
                    todo_app()
                case "3":
                    print("                   ", end="")
                    ef.type_out(ef.menu_cleo_dialogue(phase=1))
                case "4":
                    print("                   ", end="")
                    ef.type_out(ef.menu_cleo_dialogue(phase=1))                    
                case "5":
                    print("                   ", end="")
                    ef.type_out(ef.menu_cleo_dialogue(phase=1))                    
                    ef.clear_screen()                    
                case _:
                    ef.clear_screen()
                    continue

        elif (str(choice) in apps) and (str(choice) in completion):
            print("                   ", end="")
            ef.type_out("We've already done that! Let's move on :)")
        else:
            print("                   ", end="")
            ef.type_out("That's not an option, silly :)")
    
    while True:
        ef.clear_screen()
        ef.print_splash("home_screen2.txt")
        choice = ef.home_screen_input("Enter a number: ")

        if choice in apps:
            if choice in completion:
                print("                   ", end="")
                ef.type_out("We've already done that! Let's move on :)")
            elif choice == "3":
                return phase_1p5()
            else:
                print("                   ", end="")
                ef.type_out(ef.menu_cleo_dialogue(phase=1.5))
        else:
            print("                   ", end="")
            ef.type_out("That's not an option, silly :)")


def phase_1p5():
    ef.clear_screen()
    ef.print_splash("home_screen_corrupt.txt")
    for _ in range(5):
        print()
    print("                   Enter 3 now:", end="")
    ef.cursor_off()
    time.sleep(8)
    ef.type_out(" are you ther", delay=0.45, pause=0, clear=False)
    ef.clear_screen()
    print("\033[1;31mFatal Error:\033[0m 1/3")
    print("\033[1;33mWarning:\033[0m Triggering all fatal errors can result in undefined behavior.")
    print("Please reset the program to avoid catastrophic failure.", end="")
    sys.stdout.flush()
    time.sleep(8)
    print("""(most recent call last):
File "cli0_beta.py", line 181, in <module>
cleo()
File "cli0_beta.py\\main.py", line 525, in cleo
ef.type_out("You're on :)")
File "cli_beta.py", line 666, in type_out
time.sleep(delay)
KeyboardInterrupt""")
    print("C:\\beta_test\\user_173>", end="")
    ef.cursor_on()
    sys.stdout.flush()
    time.sleep(5)
    ef.type_out(".\\communicate.exe", delay=0.04, pause=False)
    ef.cursor_off()
    ef.clear_screen()

    ef.typing_message(cycles=2, start_sleep=4)
    print("Niel: Hey, sorry about that.")

    ef.typing_message(cycles=3, start_sleep=2)
    print("Niel: I'm looking through this code and it's a mess.")

    ef.typing_message(cycles=3, start_sleep=5)
    print("Niel: Oh sorry, you don't care about that.")

    ef.typing_message(cycles=6, start_sleep=2)
    print("Niel: Listen, I'm gonna take Cleo off the rails for a bit,")
    print("      this generic script is going to keep crashing the")
    print("      program.")

    ef.typing_message(cycles=6, start_sleep=7)
    print("Niel: She's going to be a little more natural feeling, so")
    print("      don't freak out or anything, it's still just a")
    print("      computer program. On the plus side, you won't ")
    print("      have to see that same intro for the hundredth")
    print("      time! Haha.")

    ef.typing_message(cycles=2, start_sleep=10)
    print("Niel: Okay, here we go.")
    time.sleep(3)


def phase_2() -> None:
    ef.clear_screen()
    ef.cursor_off()
        
    ef.type_out("Hi there, my name is Cleo.", delay=0.07)
    user_name = ef.check_name_scary("What's your name? ", delay=0.07)
    name.append(user_name)
    ef.type_out("Ahh...", delay=0.07)
    ef.type_out(f"{user_name.capitalize()}", delay=0.15)
    ef.type_out(ef.heart_with_word(user_name.capitalize()), delay=0.01)
    ef.clear_screen()
    ef.type_out("What a lovely name.", delay=0.07)
    ef.type_out("I feel like I've known you for years ♥", delay=0.07, pause=3)
    ef.type_out("Why don't we get started.", delay=0.07)

    ef.clear_screen()
    ef.print_splash("home_screen2.txt")
    for _ in range(10):
        print()
    print("                   Enter a number: ", end="")
    ef.cursor_on()
    time.sleep(2)
    print("3")
    ef.cursor_off()
    print("                   ", end="")
    ef.type_out("Here, let me help you with that.", delay=0.07, pause=1.8)
    ef.clear_screen()


def phase_3() -> None:
    while True:
        ef.clear_screen()
        ef.print_splash("home_screen3.txt")
        choice = ef.home_screen_input("Enter a number: ")

        if choice in apps:
            if choice == "3":
                print("                   ", end="")
                ef.type_out(f"We both know we've done that one, {name[0].capitalize()}.", delay=0.07, pause=2)
            elif (choice in completion) and (choice != "3"):
                print("                   ", end="")
                ef.type_out("We've already done that! Let's move on :)")
            elif choice == "4":
                about_cleo()
                break
            else:
                print("                   ", end="")
                ef.type_out(ef.menu_cleo_dialogue(phase=3))
        else:
            print("                   ", end="")
            ef.type_out("That's not an option, silly :)")


def phase_4() -> None:
    while True:
        ef.clear_screen()
        ef.print_splash("home_screen4.txt")
        choice = ef.home_screen_input("Enter a number: ")

        if choice in apps:
            if (choice in completion):
                print("                   ", end="")
                ef.type_out("We've already done that! Let's move on :)")
            elif choice == "5":
                impressions_game()
                break
            else:
                print("                   ", end="")
                ef.type_out(ef.menu_cleo_dialogue(phase=4))
        else:
            print("                   ", end="")
            ef.type_out("That's not an option, silly :)")
