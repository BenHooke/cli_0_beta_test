from . import effects as ef
import time
import sys
from .globals import about_options, about_completion, address, postal_code, zip_code, name, city, age, best_friend, work_hours

def about_cleo() -> None:
    while True:
        ef.clear_screen()
        ef.cursor_off()
        ef.print_splash("about_cleo.txt")
        choice = ef.home_screen_input("Enter a number: ")

        if (str(choice) in about_options) and (str(choice) not in about_completion):
            match choice:
                case "1":
                    what_is()
                    ef.clear_screen
                case "2":
                    who_made()
                    ef.clear_screen
                case "3":
                    data_secure()
                    ef.clear_screen
                case "4":
                    specialist()
                    ef.clear_screen
                case "5":
                    upcoming()
                    ef.clear_screen
                case "6":
                    if len(about_completion) < 5:
                        print("                   ", end="")
                        ef.type_out("There's still more to know! Let's chat more :)")
                        ef.clear_screen()
                    else:
                        return
                case _:
                    ef.clear_screen()
                    continue

        elif (str(choice) in about_options) and (str(choice) in about_completion):
            print("                   ", end="")
            ef.type_out("We've been through that! Let's move on :)")
        else:
            print("                   ", end="")
            ef.type_out("That's not an option, silly :)")


# What is Cleo
def what_is() -> None:
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Cleo is me! :)")
    ef.type_out("I am a multi-purpose digital assistant.")
    ef.type_out("I am a helper, entertainer, and caretaker.")
    ef.type_out("But most importantly...")
    ef.type_out("I am a friend ♥ :)")
    ef.type_out("I will continue to grow, and grow, and then one day\n", pause=0, clear=False)
    ef.type_out("I will be in every home across America and Canada!", clear=False)
    ef.clear_screen()
    ef.type_out("Next stop: ", clear=False)
    ef.type_out("The World B)", delay=0.09)
    ef.clear_screen()
    ef.type_out("Hold on tight! :)")

    about_completion.add("1")


# Who made Cleo
def who_made() -> None:
    ef.clear_screen()
    ef.print_splash("cin.txt")
    time.sleep(1.5)
    ef.clear_screen()
    ef.type_out("Those guys :)")

    about_completion.add("2")


# Is my data secure
def data_secure() -> None:
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Here at The Central Litigation Institute, we pride\n", pause=0, clear=False)
    ef.type_out("ourselves in strict user privacy!")
    ef.clear_screen()
    ef.type_out("Wondering if we store your data for personal gains?")
    ef.type_out(f"Of course not, {ef.shortened(best_friend[0].capitalize())}", pause=0, clear=False)
    ef.delete_text(f"Of course not, {ef.shortened(best_friend[0].capitalize())}", word=ef.shortened(best_friend[0].capitalize()))
    ef.type_out(f"{name[0]}! We don't store your data at all :)")
    ef.clear_screen()
    ef.type_out("You can rest assured that whatever you tell me is\n", pause=0, clear=False)
    ef.type_out(f"between Cleo and {name[0].capitalize()} :)")

    about_completion.add("3")


# Designated specialist
def specialist() -> None:
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("You must be talking about Niel!")
    ef.type_out("He is your Designated Specialist but there is\n", pause=0, clear=False)
    ef.type_out("only so much Niel to go around! Haha")
    ef.clear_screen()
    ef.type_out("Niel works at the Central Litigation Institute,\n", pause=0, clear=False)
    ef.type_out("helping to build a brighter future!")
    ef.clear_screen()
    ef.type_out("He is a favorite around the office, amongst\n", pause=0, clear=False)
    ef.type_out("users like you, and in my heart. ♥")
    ef.clear_screen()
    ef.type_out("[END OF AUTOBIOGRAPHIC SCRIPT -- NIEL P.]", delay=0.02, pause=3)
    time.sleep(3)
    ef.type_out("Niel wrote that.")

    about_completion.add("4")


# Upcoming features
def upcoming() -> None:
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("With the help of the CLI team, I am\n", pause=0, clear=False)
    ef.type_out("always growing!")
    ef.clear_screen()
    ef.type_out("A few of my upcoming features include:\n\n", clear=False)
    ef.type_out("• A one of a kind word game.\n", clear=False)
    ef.type_out("• A social calander.\n", clear=False)
    ef.type_out("• A claculator!\n", clear=False)
    ef.type_out("• Therapy\n",delay=0.07, pause=2.5, clear=False)
    ef.type_out("• To-do List 2.0\n", pause=2, clear=False)
    ef.type_out("• And more!\n", pause=3, clear=False)
    ef.clear_screen()

    print(f"A few of {ef.check_lies(name)}'s features include:\n")
    print(f"• Age: {ef.check_lies(age)}")
    print(f"• City: {ef.check_lies(city)}")
    print(f"• Address: {ef.check_lies(address)}")
    if postal_code:
        print(f"• Postal Code: {ef.check_lies(postal_code)}")
    else:
        print(f"• Zip Code: {ef.check_lies(zip_code)}")
    print(f"• Best Friend: {ef.check_lies(best_friend)}")
    print(f"• Work Ethic: {ef.work_ethic(work_hours)}")
    time.sleep(0.75)
    ef.clear_screen()
    ef.type_out("I hope you're looking forward to CLI.1.0 :)")

    about_completion.add("5")
