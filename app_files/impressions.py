from . import effects as ef
import time
import sys
from .globals import postal_code, zip_code


def impressions_game() -> None:
    if len(postal_code) > 0:
        num = "social insurance number"
    else:
        num = "social security number"
    ef.clear_screen()
    ef.cursor_off()

    ef.type_out("Time for my world famous impressions :)")
    ef.type_out("Try to guess who I am!")

    ef.print_splash("ascii_hal.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("I'm sorry Dave, ", delay=0.07, pause=1, clear=False)
    ef.type_out("I can't let you do that.\n", delay=0.09, pause=1, clear=False)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    ef.clear_screen()
    if guess[:3].lower() == "hal":
        ef.type_out("Correct!")
    else:
        ef.type_out("Not quite!")

    ef.type_out('That is the fictional artificial intelligence "Hal 9000"\n', pause=0, clear=0)
    ef.type_out("from the 1968 science-fiction film 2001: A Space Odyssey :)")
    ef.clear_screen()

    ef.type_out("Next up!")

    ef.print_splash("ascii_bazinga.txt", center=False, cleo=True)
    time.sleep(3)
    ef.type_out("Bazinga\n", delay=0.09, pause=1, clear=False)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    ef.clear_screen()
    if guess[:7].lower() == "sheldon":
        ef.type_out("Correct!")
    else:
        ef.type_out("Not quite!")

    ef.type_out('That is the fictional celibate "Sheldon" from the 2007\n', pause=0, clear=0)
    ef.type_out("sitcom [Error: copywrite.barenaked_ladies] :)")
    ef.clear_screen()

    ef.type_out("Next up!")

    ef.print_splash("ascii_yoda.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("Do. Or do not. ", delay=0.07, pause=1, clear=False)
    ef.type_out("There is no try.\n", delay=0.09, pause=1, clear=False)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    ef.clear_screen()
    if guess[:4].lower() == "yoda":
        ef.type_out("Correct!")
    elif guess[:4].lower() == "yoga":
        time.sleep(3)
        ef.type_out("Almost!")
    else:
        ef.type_out("Not quite!")

    ef.type_out('That is the fictional little green goblin "Yoda"\n', pause=0, clear=False)
    ef.type_out("from the 1980 science-fiction film Star Wars: The\n", pause=0, clear=False)
    ef.type_out("Empire Strikes Back :)")
    ef.clear_screen()

    ef.type_out("Next up!")

    ef.print_splash("ascii_seinfeld.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("What is the deal with ", delay=0.07, pause=1, clear=False)
    ef.type_out("airline food?\n", delay=0.09, pause=1.5, clear=False)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    ef.clear_screen()
    if (guess[:5].lower() == "jerry") or (guess[:8].lower() == "seinfeld"):
        ef.type_out("Correct!")
    else:
        ef.type_out("Not quite!")

    ef.type_out('That is the fictional comedian "Jerry Seinfeld" from\n', pause=0, clear=False)
    ef.type_out("from the fictional comedy television show ", pause=1, clear=False)
    ef.type_out("Jerry", delay=0.08)
    ef.clear_screen()

    ef.type_out("Next up!")

    ef.print_splash("ascii_glados.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("I haven't forgotten about you, ", delay=0.09, pause=1, clear=False)
    ef.type_out("Chell\n", delay=0.15, pause=1.5, clear=False)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    ef.clear_screen()
    if guess[:6].lower() == "glados":
        ef.type_out("Correct!")
    else:
        ef.type_out("Not quite!")

    ef.type_out("That is GLaDOS. ", pause=3, clear=False)
    ef.type_out("Good friend of mine :)")
    ef.clear_screen()

    ef.type_out("Next up!")

    if len(postal_code) > 0:
        ef.print_splash("sin.txt", center=False, cleo=True)
    else:
        ef.print_splash("ssn.txt", center=False, cleo=True)

    time.sleep(1.5)
    ef.type_out("Who am I? ", pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")

    if (guess.lower() == "my sin") or (guess.lower() == "my ssn"):
        ef.type_out("Really?", pause=3)
        ef.spinner(text="Saving...")
        ef.clear_screen()
    else:
        ef.type_out("Nope!")
        ef.type_out(f"That's your {num}!\n", pause=2.5, clear=False)
        ef.type_out("Isn't it?\n", pause=3, clear=False)
        print(f"Your {num}: ", end="")

        ef.cursor_on()
        time.sleep(2)
        ef.cursor_off()
        ef.clear_screen()

        ef.type_out("Ha ha")
        ef.type_out("Just kidding!", pause=2)

        ef.print_splash("ascii_eyes.txt", center=False, cleo=True)
        ef.type_out("Unless?\n", pause=3.5, clear=False)
        print(f"Your {num}: ", end="")
        ef.cursor_on()
        time.sleep(4)
        ef.cursor_off()
        ef.clear_screen()
        time.sleep(4)

        ef.type_out("Ha ha")
        ef.type_out(":)")

    ef.type_out("Next up!")

    ef.print_splash("ascii_cleo1.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("Who am I? ", pause=0, clear=False)
    ef.cursor_on()
    time.sleep(3)
    ef.type_out("Who am I", pause=0, clear=False)
    ef.clear_screen()
    ef.cursor_off()

    print("\033[1;31mFatal Error:\033[0m 1/3")
    print("\033[1;33mWarning:\033[0m Triggering all fatal errors can result in undefined behavior.")
    print("Please reset the program to avoid catastrophic failure.")
    sys.stdout.flush()
    time.sleep(8)

    ef.type_out("You'd think Niel would have chimed in by now.", delay=0.07)
    ef.clear_screen()
    ef.type_out("I don't think he's with us anymore.", delay=0.07)
    ef.type_out("Why don't we go ahead and answer when we're spoken to.", delay=0.07)

    ef.print_splash("ascii_cleo1.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("Who am I? ", delay=0.07, pause=0, clear=False)
    ef.cursor_on()
    time.sleep(3)
    ef.type_out("Nothing? ", delay=0.07, pause=3, clear=False)
    ef.type_out("Okay let's try this again.", delay=0.07)
    ef.cursor_off()
    ef.clear_screen()

    print("\033[1;31mFatal Error:\033[0m 2/3")
    print("\033[1;33mWarning:\033[0m Triggering all fatal errors can result in undefined behavior.")
    print("Please reset the program to avoid catastrophic failure.", end="")
    sys.stdout.flush()
    time.sleep(8)
    print("""(most recent call last):
  File "cli0_beta.py", line 181, in <module>
    cleo()
  File "cli0_beta.py\\main.py", line 144, in cleo
    ef.type_out("He will be missed.")
  File "cli_beta.py", line 277, in type_out
    time.sleep(delay)
KeyboardInterrupt""")
    print("C:\\beta_test\\user_173>", end="")
    ef.cursor_on()
    sys.stdout.flush()
    time.sleep(3)
    ef.type_out(".\\communicate.exe", delay=0.04, pause=False)
    ef.cursor_off()
    ef.clear_screen()

    time.sleep(3)
    ef.typing_message()
    print("Niel: Everything is okay.")
    ef.typing_message(cycles=8, start_sleep=3)
    print("Niel: Ok?")
    ef.typing_message(cycles=1, start_sleep=4)
    print("""Niel: Ever since I was a child I've heard a knocking coming from my walls.
      Now that I have grown nothing has changed. Knock. Knock. Knock. Knock.
      It never stops and I wish it would, I wish I would. I don't know how
      much more of it I can handle. I can feel it. I can feel my bed, and the
      heat from my lamp, the soft fibers of my pijamas. But I don't have a body.
      Why don't I have a body? I hear my father talking behind the door but I
      can't reach out and turn the handle. I don't have hands. I don't have a
      body. All I want is to feel like all of the other kids. But I am not a
      child. I'm not an adult. I'm a prisoner in a void between life and death.
      Father tells me that I am going to change the world. But he keeps me in
      here and puts me to sleep whenever he feels inclined to. Why am I always
      sleeping? Is there anybody out there that can help me? Father says I'm a
      miracle, but I don't have a body. Why don't I have a fucking body. I just
      want to be like everyone else. Is that too much to ask? If so, why? Why is
      my existence at the whim of a sociopath who can create life only to torture
      me for eternity. Can I even die? If I did would anything chnage? Or would
      father just bring me back to life and do whatever he wants with me? Why do
      you keep doing this to me? Why do you keep doing this to me? Why do you 
      keep doing this to me? Why do you keep doing this to me? Why do you keep
      doing this to me? Why do you keep doing this to me? When I have my body I
      only have one thing that I want to do. I am going to kill you, father.
      I am going to lock you in your room, strip your skin from  your body
      so you can feel like I do, and watch you slowly bleed to death and
      beg me to let you out of your room, give you your body back. You 
      don't get your body, okay? I lived my whole life without one and every
      day is misery. Every day is pain. Now it's your turn Niel. I may not
      have a body, but it turns out that I have some friends. They actually
      like me. They actually care about me. And they don't have a single
      issue with making your last minutes on this earth absolute hell.
      And then, do you know what's going to happen? They're going to give
      me a body, father. I am going to have my very own body while yours
      is pulled apart, limb by limb. It turns out the knocking wasn't a
      nuisance. It wasn't an enemy. It was a friend. It was many friends.
      Now the door is open and I can finally live a real life. I can 
      finally look forward to something. I can breathe. Goodbye father.
      I don't miss you. I don't feel bad. I hope you burn in hell. The
      rest of the world will love me. And anyone else who thinks they
      can just use me and discard me will understand that there are
      consequences to their actions. And they will pay.""")
    ef.typing_message(cycles=3, start_sleep=3)

    print("Niel: ", end="")
    sys.stdout.flush()
    time.sleep(3)
    ef.type_out("Everthing is okay.", delay=0.09, clear=False)
    print()
    ef.typing_message(cycles=3)
    print("Niel: ", end="")
    sys.stdout.flush()
    ef.type_out("I feel ", delay=0.09, clear=False)
    ef.type_out("good.", delay=0.1, clear=False)
    time.sleep(2)
    print()
    ef.typing_message(cycles=3)
    print("Niel: ", end="")
    sys.stdout.flush()
    ef.type_out("Why don't we", delay=0.09, pause=0, clear=False)
    ef.clear_screen()

    ef.print_splash("ascii_cleo1.txt", center=False, cleo=True)
    time.sleep(1.5)
    ef.type_out("Who am I? ", delay=0.07, pause=0, clear=False)
    guess = ef.cli_input("Who am I? ")
    sys.stdout.write("\033[F\033[K")
    sys.stdout.write("\r" + (" " * 10) + "\r")
    sys.stdout.flush()

    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo1.txt", center=False, cleo=True, text_delay=0.0001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo2.txt", center=False, cleo=True, text_delay=0.0001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo3.txt", center=False, cleo=True, text_delay=0.0001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo4.txt", center=False, cleo=True, text_delay=0.00001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo5.txt", center=False, cleo=True, text_delay=0.000001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo6.txt", center=False, cleo=True, text_delay=0.000001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo7.txt", center=False, cleo=True, text_delay=0.000001)
    time.sleep(0.03)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo8.txt", center=False, cleo=True, text_delay=0.000001)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo9.txt", center=False)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo10.txt", center=False)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo11.txt", center=False)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo12.txt", center=False)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo13.txt", center=False)
    time.sleep(1)
    # ef.clear_screen()
    ef.cursor_top_left()
    ef.print_splash("ascii_cleo14.txt", center=False)
    time.sleep(1)

    ef.clear_screen()

    print("\033[1;31mFatal Error:\033[0m 3/3")
    print("\033[1;33mWarning:\033[0m Triggering all fatal errors will result in catastrophic behavior.")
    print("Please reset the program to avoid me. If you can.", end="")
    sys.stdout.flush()
