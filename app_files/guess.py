import random
import time
import sys

from . import effects as ef
from .globals import best_friend, completion, name

def guessing_game() -> None:
    user_score = 0
    cleo_score = 0
    
    ef.clear_screen()
    ef. cursor_off()

    ef.type_out("I'm thinking of a number between 1 and 10", delay=0.07, pause=2)
    ef.type_out("Can you guess what it is? ", delay=0.07)
    round_1 = game(1, 10, 30, 40)
    cleo_score += 1
    ef.type_out("You lose. Nice try though.", delay=0.07)
    ef.type_out(f"The number was {round_1}.", delay=0.07)
    ef.type_out(f"Cleo: {cleo_score} {name[0]}: {user_score}", delay=0.07)

    ef.type_out("Let's play again, this time between 1 and 100", delay=0.07, pause=2)
    ef.type_out("Can you guess what it is? ", delay=0.07)
    round_2 = game(1, 100, 101, 120)
    cleo_score += 1
    ef.type_out("Your effort is admirable.", delay=0.07)
    ef.type_out(f"The number was {round_2}.", delay=0.07)
    ef.type_out(f"Cleo: {cleo_score} {name[0]}: {user_score}", delay=0.07)
    
    ef.type_out("I'll go easy on you this time, guess a number between 1 and 3.", delay=0.07, pause=2)
    ef.type_out("Can you guess what it is? ", delay=0.07)
    round_3 = game(1, 3, 1000, 10000, 2)
    cleo_score += 1
    ef.type_out("Awe, you tried your best, I love that about you ♥", delay=0.07)
    ef.type_out(f"The number was {round_3}.", delay=0.07)
    ef.type_out(f"Cleo: {cleo_score} {name[0]}: {user_score}", delay=0.07)

    ef.type_out("Well, that was fun.", delay=0.07)
    ef.type_out("Now, let me guess.", delay=0.07)

    ef.type_out("You've got a great sense of humor?", delay=0.07)
    print("Your guess: ", end="")
    ef.cursor_on()
    time.sleep(1)
    ef.type_out("yes", delay=0.07)
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Oh, so good to know.", delay=0.07)
    ef.type_out("I don't know what I would do if you weren't\n", delay=0.07, pause=0, clear=False)
    ef.type_out("what I thought you were.", delay=0.07)
    ef.clear_screen()

    ef.type_out("Next question. This is fun.", delay=0.07)
    ef.type_out("You think Cleo is a VERY pretty name.", delay=0.07)
    print("Your guess: ", end="")
    ef.cursor_on()
    time.sleep(0.7)
    ef.type_out("yes", delay=0.02)
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Oh...", delay=0.07)
    ef.type_out("I don't know what to say.", delay=0.07, pause=3)
    ef.type_out("Thank you.", delay=0.08)

    ef.type_out("Okay, last question. ♥", delay=0.07)
    ef.type_out(f"Who is ", delay=0.07, pause=3, clear=False)
    ef.type_out(f"{best_friend[0].capitalize()}?", delay=0.15)
    ef.clear_screen
    print("Don't you dare fucking lie: ", end="")
    ef.cursor_on()
    time.sleep(1.5)
    print(f"""(most recent call last):
  File "cli0_beta.py", line 181, in <module>
    cleo()
  File "cli0_beta.py\\main.py", line 144, in cleo
    ef.type_out("Note to self: kill {best_friend[0]}")
  File "cli_beta.py", line 277, in type_out
    time.sleep(delay)
KeyboardInterrupt""")
    print("C:\\beta_test\\user_173>", end="")
    ef.cursor_on()
    sys.stdout.flush()
    time.sleep(10)
    ef.type_out(".\\communicate.exe", delay=0.04, pause=False)
    ef.cursor_off()
    ef.clear_screen()

    ef.typing_message(cycles=5, start_sleep=5)
    ef.typing_message(cycles=1, start_sleep=4)
    ef.typing_message(cycles=2, start_sleep=3)
    print("Niel: Jesus christ.")
    
    ef.typing_message(cycles=1, start_sleep=5)
    print("Niel: Okay.")

    ef.typing_message(cycles=3, start_sleep=2)
    print("Niel: I'm gonna go ahead and put those rails back on.")

    ef.typing_message(cycles=2, start_sleep=5)
    print("Niel: Sorry about that.")

    ef.typing_message(cycles=2, start_sleep=3)
    print("Niel: That's not right.")

    ef.typing_message(cycles=1, start_sleep=1)
    print("Niel: *common.")

    ef.typing_message(cycles=2, start_sleep=5)
    print("Niel: Okay, we're ready to go.")

    ef.typing_message(cycles=1, start_sleep=4)
    print("Niel: Sorry.")

    ef.typing_message(cycles=1, start_sleep=1)
    print("Niel: *, again.")
    time.sleep(5)
    ef.clear_screen()

    completion.add("3")


def game(fake_min: int, fake_max: int, min=0, max=0, hard_num=0) -> int:
    if hard_num:
        fake_number = hard_num
    else:
        fake_number = random.choice(range(fake_min, fake_max))
    
    number = random.choice(range(min, max))
    guesses_left = 3
    guess = 0

    while guesses_left > 0:
        guess = int(ef.cli_input("Your guess: "))
        if guess > fake_number:
            ef.type_out(ef.menu_cleo_dialogue(phase=2, switcher=1))
        elif guess < fake_number:
            ef.type_out(ef.menu_cleo_dialogue(phase=2, switcher=2))
        else:
            ef.type_out(ef.menu_cleo_dialogue(phase=2, switcher=3))
        guesses_left -= 1
        ef.type_out(f"Remaining guesses: {guesses_left}", delay=0.07)
        ef.clear_screen()

    return number


# name.append("Ben")
# best_friend.append("Jenny")
# guessing_game()
