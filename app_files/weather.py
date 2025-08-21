from . import effects as ef
from .globals import address, city, completion, postal_code, zip_code

def weather_app() -> None:
    global completion
    global city

    ef.clear_screen()

    ef.type_out("Time to check the weather!")
    ef.type_out("Now let's see...", pause=5)
    ef.type_out("First! I need to ask you a few questions!")
    ef.type_out("What city do you live in? ", pause=0, clear=False)

    city.append(ef.cli_input("What city do you live in? "))
    ef.clear_screen()

    ef.type_out("Great!", pause=0.75)
    ef.spinner()
    ef.type_out("What neighborhood do you live in? ", pause=0, clear=False)

    ef.cli_input("What neighborhood do you live in? ")
    ef.clear_screen()

    ef.type_out("Great!", pause=0.75)
    ef.spinner()
    ef.type_out("What is your postal/zip code? ", pause=0, clear=False)

    code = ef.cli_input("What is your postal/zip code? ").strip().replace(" ", "")
    if code.isnumeric():
        zip_code.append(code)
    else:
        postal_code.append(code)
    ef.clear_screen()

    ef.type_out("Great!", pause=0.40)
    ef.spinner(seconds=0.5)
    ef.type_out("What is your full address? ", pause=0, clear=False)

    address.append(ef.cli_input("What is your full address? "))
    ef.clear_screen()

    ef.type_out("Great!", pause=0.75)
    ef.spinner(seconds=10)
    ef.type_out("I don't know :)", pause=2)
    ef.type_out("But it's so nice getting to know you better!")
    ef.type_out("We should do this more often")
    ef.type_out(":)")
    ef.type_out("Let's go see what else I can do!")

    completion.add("1")
    
    return


