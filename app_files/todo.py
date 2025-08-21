from . import effects as ef
from .globals import completion, best_friend, work_hours

def todo_app() -> None:
    global work_hours

    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Let me help you craft a personalized to-do list!")
    ef.type_out("Let's go over some things that might affect your list:")

    ef.type_out("How many hours do you work per week? ", pause=0, clear=False)
    work_hours = int(ef.cli_input("How many hours do you work per week? "))
    ef.clear_screen()
    
    ef.type_out("How many pets do you have? ", pause=0, clear=False)
    ef.cli_input("How many pets do you have? ")
    ef.clear_screen()
    
    ef.type_out("Have you been in a jury lately? ", pause=0, clear=False)
    ef.cli_input("Have you been in a jury lately? ")
    ef.clear_screen()

    ef.type_out("What's your best friend's name? ", pause=0, clear=False)
    best_friend.append(ef.cli_input("What's your best friend's name? "))
    ef.clear_screen()

    ef.type_out("Great!", pause=1)
    ef.type_out("Let's generate your to-do list.")
    ef.spinner(text="Generating...")

    ef.type_out("• Get groceries  □\n", clear=False)
    ef.type_out("• Get a pet", pause=2, clear=False)
    ef.type_out("?  □\n", delay=1, clear=False)
    ef.type_out("• Feed your pet  □\n", clear=False)
    ef.type_out("• Report for jury duty  □\n", clear=False)
    ef.type_out("• Report suspicious behavior to the authorities  □\n", clear=False)
    ef.type_out("• Hang out with ", pause=0.5, clear=False)
    ef.type_out(f"{best_friend[0].capitalize()}  □\n", delay=0.08, pause=3, clear=False)
    ef.type_out("• Eat  □\n", clear=False)

    print()
    ef.type_out("I'll give you a minute to write that down.", pause=0.75)
    ef.clear_screen()
    ef.type_out("Great!", pause=1.25)
    ef.type_out("Let's move on.")

    completion.add("2")


