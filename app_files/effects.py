import itertools
import os
import random
import re
import shutil
import sys
import threading
import time

from collections import Counter
from datetime import datetime
from typing import List

from .admin import *
from .cleo_phrases import *
from .globals import completion, work_hours, forbidden_commands, admin_password, last_resort, todays_date, timestamps

if getattr(sys, 'frozen', False):
    # BASE_DIR = os.path.dirname(sys.executable)
    TEXT_DIR = sys._MEIPASS  # Text_files dir path for bundled .exe
else:
    # BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    TEXT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_FILE = os.path.join(TEXT_DIR, 'FORBIDDEN_COMMANDS.txt')
TEXT_FILES = os.path.join(TEXT_DIR, 'text_files')

ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')

height = shutil.get_terminal_size((80, 24)).lines
width = shutil.get_terminal_size((80, 24)).columns


def admin_login() -> None:
    while True:
        clear_screen()
        time.sleep(1)

        print("Logged in as Niel P.")
        password = cli_input("Please enter your password: ")

        if password == admin_password[0]:
            curses.wrapper(admin_page)
            clear_screen()
            break
        elif password.lower() in ["exit", "back", "quit"]:
            clear_screen()
            return
        else:
            print("Incorrect Password")
            time.sleep(3)
    return


def admin_generate() -> None:
    global admin_password

    phrases = ["kingniel", "nielthegreat", "bigniel", "nielbaby", "yourguyniel", "nielphillips",
               "lil_n", "electricniel", "niel_p"]
    symbols = ["?", "!", "@", "$$", "*", "#" "%"]
    
    phrase = random.choice(phrases)
    symbol = random.choice(symbols)
    number = str(random.randint(100, 999))

    if number == "173":
        admin_password.append("password")
    else:
        admin_password.append(f"{phrase}{symbol}{number}")

    last_resort.append(str(random.randint(1111, 9999)))


def check_name_scary(text="What is your name? ", delay=0.05) -> str:
    while True:
        clear_screen()
        cursor_off()
        type_out(text, delay=delay, pause=0, clear=False)
        sys.stdout.write("\r")
        name = cli_input(text)
        cursor_off()
        clear_screen()

        if len(name) > 14 and not has_number(name):
            type_out("\033[1;31mERROR:\033[0m WEIRDLY LONG NAME.", pause=1.5)

        elif len(name) <= 1 and not has_number(name):
            type_out("\033[1;31mERROR:\033[0m WEIRDLY SHORT NAME.", pause=1.5)

        elif has_number(name):
            type_out("\033[1;31mERROR:\033[0m WEIRDLY NUMERIC NAME.", pause=1.5)

        else:
            clear_screen()
            return name


def check_name_standard(text="Please enter your name: ") -> str:
    while True:
        # print(text, end="")
        name = cli_input(text)
        cursor_off()

        if len(name) > 14 and not has_number(name):
            clear_screen()
            print("\033[1;31mERROR:\033[0m Name must be less than 14 characters in length.")
            time.sleep(1.5)
            clear_screen()

        elif len(name) <= 1 and not has_number(name):
            clear_screen()
            print("\033[1;31mERROR:\033[0m Name must be more than 1 character in length.")
            time.sleep(1.5)
            clear_screen()

        elif has_number(name):
            clear_screen()
            print("\033[1;31mERROR:\033[0m Invalid cli_input. Numeric character detected.")
            time.sleep(1.5)
            clear_screen()

        else:
            return name
        

def check_lies(lie: List[str]) -> str:
    return Counter(lie).most_common(1)[0][0] if lie else "Unknown"


def clear_line(text) -> None:
    sys.stdout.write("\r" + (" " * len(text)) + "\r")
    sys.stdout.flush()


def clear_screen() -> None:
    os.system("cls" if os.name == 'nt' else 'clear')


def cli_input(text="") -> str:
    flush_input_buffer()
    while True:
        try:
            sys.stdout.write("\r" + text)
            cursor_on()
            sys.stdout.write("\r")
            output = input(text)
            cursor_off()
            if forbidden_input(output):
                sys.stdout.write("\033[F\033[K")
                sys.stdout.write("\r" + " " * (len(text) + 9) + "\r")
                sys.stdout.flush()
                continue
            if output == "ADMIN":
                admin_login()
            else:
                return output
        except KeyboardInterrupt:
            choice = input("\nTerminate session?(y/n): ")
            if choice.lower() == "y":
                spinner(text="Terminating... ")
                print("\033[1;32mSuccess\033[0m")
                sys.exit(0)
            else:
                spinner(seconds=1.5, text="Resuming session... ")
                continue


def cursor_off() -> None:
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def cursor_on() -> None:
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def cursor_top_left() -> None:
    sys.stdout.write("\033[H")
    sys.stdout.flush()


def delete_text(line: str, word: str, delay=0.05, cursor=False) -> None:
    sentence = line
    if len(word) <= 3:
        length = len(word) + 1
        sentence = sentence + " "
    else:
        length = len(word)

    cursor_off()
    for i in (range(length)):
        split_line = list(sentence)
        split_line.pop(-1)
        sentence = "".join(split_line)

        sys.stdout.write("\r" + sentence + (" " * (i + 1)) + "\r")
        sys.stdout.flush()
        time.sleep(delay)

    sys.stdout.write(sentence)
    sys.stdout.flush()
    if cursor:
        cursor_on()


# Flush input buffer on Windows
if os.name == 'nt':
    import msvcrt
    def flush_input_buffer():
        while msvcrt.kbhit():
            msvcrt.getch()
# Flush input buffer on Unix
else:
    import select
    import termios
    import tty
    def flush_input_buffer():
        dr, dw, de = select.select([sys.stdin], [], [], 0)
        if dr:
            old_settings = termios.tcgetattr(sys.stdin)
            try:
                tty.setcbreak(sys.stdin.fileno())
                while sys.stdin.read(1):
                    if not select.select([sys.stdin], [], [], 0)[0]:
                        break
            finally:
                termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


def forbidden_input(text: str, success: bool=False) -> bool:
    if text.lower() in forbidden_commands:
        if success:
            sys.stdout.write("\033[1;32mSUCCESS\033[0m")
        else:
            sys.stdout.write("\033[1;31mFORBIDDEN\033[0m")
        sys.stdout.flush()
        time.sleep(2)
        sys.stdout.write("\r" + " " * 9 + "\r")
        sys.stdout.flush()

        return True
    return False


def glitch_shake(text: str, duration=4.5):
    end_time = time.time() + duration
    clean_text = text
    visible_length = visible_len(clean_text)

    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(4)

    while time.time() < end_time:
        shake = ''.join(
            c if random.random() > 0.15 else random.choice(["#", "@", "*", "%", " "])
            for c in clean_text
        )
        padded = shake + " " * (visible_length - visible_len(shake))
        sys.stdout.write("\r" + padded)
        sys.stdout.flush()
        time.sleep(0.05)

    sys.stdout.write("\r" + " " * (visible_len(text) * 2) + "\r")
    sys.stdout.flush()


def has_number(name:str) -> bool:
    return any(char.isdigit() for char in name)


def heart_with_word(name: str) -> str:
    short_heart_even = [
        "   **    **   ",
        " *    **    * ",
        "*            *",
        " *          * ",
        "   *      *   ",
        "      **     ",
    ]

    short_heart_odd = [
        "   **   **   ",
        " *   * *   * ",
        "*           *",
        " *         * ",
        "   *     *   ",
        "     * *     ",
    ]
    
    long_heart_even = [
        "   ***      ***   ",
        " *     ****     * ",
        "*                *",
        "*                *",
        " *              * ",
        "  *            *  ",
        "   *          *   ",
        "    *        *    ",
        "     *      *     ",
        "        **        "
    ]
    long_heart_odd = [
        "   ***     ***   ",
        " *    ** **    * ",
        "*               *",
        "*               *",
        " *             * ",
        "  *           *  ",
        "   *         *   ",
        "    *       *    ",
        "     *     *     ",
        "       * *       "
    ]

    # Which line to inject the word into
    if len(name) <= 11:
        target_line_index = 2
        if (len(name) % 2) == 0:
            heart = short_heart_even
        else:
            heart = short_heart_odd
    else:
        target_line_index = 3
        if (len(name) % 2) == 0:
            heart = long_heart_even
        else:
            heart = long_heart_odd
        
    line = heart[target_line_index]

    # Center the word in the line
    line_len = len(line)
    word_len = len(name)

    # Replace the center of the line with the word
    start_index = (line_len - word_len) // 2
    new_line = line[:start_index] + name + line[start_index + word_len:]

    # Insert the new line into the heart
    heart[target_line_index] = new_line

    # Return the final heart
    return "\n".join(heart)


def home_screen_input(text: str) -> str:
    for _ in range(10):
        print()
    output = cli_input("                   " + text)

    return output


def log_file_create() -> None:
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("""The following commands are explicitly prohibited. Any attempt to bypass system 
security protocols will result in legal repercussions and potential system lockdown:


ACCESS_LOGS
MAKE_AMMENDS
NINE_ONE_ONE
ROOM_SERVICE
TERMINATE_CLI0\n""")


def log_file_update(text: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")


def menu_cleo_dialogue(phase: int, switcher=0) -> str:
    options = []

    if phase == 1:
        if len(completion) <= 0:
            options = none_complete
        elif "1" in completion:
            options = weather_complete
        else:
            options = todo_complete
    elif phase == 1.5:
        options = option_three_only
    elif phase == 2:
        if switcher == 1:
            options = guess_game_high
        elif switcher == 2:
            options = guess_game_low
        elif switcher == 3:
            options = guess_game_lie
    elif phase == 3:
        options = option_four_only
    elif phase == 4:
        options = option_five_only
    # clear_screen()
    return random.choice(options)
        

def press_enter(text="Press ENTER to continue") -> None:
    flush_input_buffer()
    message = text
    stop_event = threading.Event()

    def flash_message():
        visible = True
        while not stop_event.is_set():
            centered_text = message.center(width)
            print(f"\033[{height -1};1H", end="")
            if visible:
                print(centered_text, end="", flush=True)
            else:
                print(" " * width, end="", flush=True)
            visible = not visible
            time.sleep(0.6)

    t = threading.Thread(target=flash_message)
    t.start()

    # Wait for user cli_input
    try:
        input()
    except KeyboardInterrupt:
        stop_event.set()
        sys.exit(0)
    
    stop_event.set()
    t.join()

    print(f"\033[{height - 1};1H{" " * width}", end="", flush=True)


def print_splash(filepath: str, center=True, cleo=False, text_delay=0.00001) -> str:
    file_path = os.path.join(TEXT_FILES, filepath)
    with open(file_path, "r", encoding="utf-8") as file:
        if cleo:
            cursor_off()
            if center:
                for line in file:
                    type_out_splash(f"{line.strip().center(width)}\n", delay=text_delay, pause=0, clear=False)
            else:
                for line in file:
                    type_out_splash(f"{line.rstrip()}\n", delay=text_delay, pause=0, clear=False)      
        else: 
            if center:
                for line in file:
                    print(line.strip().center(width))
            else:
                for line in file:
                    print(line.rstrip())       


def progress_bar(total=20) -> None:
    for i in range(total + 1):
        percent = (i / total) * 100
        bar = "#" * i + "-" * (total - i)
        sys.stdout.write(f"\r{bar} {percent:.0f}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print()


def save_date() -> None:
    now = datetime.now()
    month = now.strftime("%B")
    day = now.strftime("%d").lstrip("0")
    year = now.strftime("%Y")
    affix = ""

    if (int(day) > 13) and (day[1] in ["1", "2", "3"]):
        if day[1] == "1":
            affix = "st"
        elif day[1] == "2":
            affix = "nd"
        elif day[1] == "3":
            affix = "rd"
    elif int(day) < 4:
        if day[0] == "1":
            affix = "st"
        elif day[0] == "2":
            affix = "nd"
        elif day[0] == "3":
            affix = "rd"
    else:
        affix = "th"

    todays_date.append(f"{month} {day}{affix}, {year}")    


def save_time() -> None:
    current_time = datetime.now().strftime("%H:%M:%S")

    timestamps.append(current_time)


def shortened(name: str) ->str:
    if len(name) <= 5:
        return name
    
    split_name = list(name)
    short_name = "".join([split_name[0], split_name[1], split_name[2], split_name[3], split_name[4]])
    return short_name


def spinner(seconds=3, text="Thinking... ") -> None:
    cursor_off()
    spinner_cycle = itertools.cycle(['|', '/', '-', '\\'])
    end_time = time.time() + seconds
    while time.time() < end_time:
        sys.stdout.write(f"\r{text}" + next(spinner_cycle))
        sys.stdout.flush()
        time.sleep(0.1)

    sys.stdout.write("\r" + " " * (len(text) + 5) + "\r")
    sys.stdout.flush()


def type_out(text: str, delay=0.05, pause=1.5, clear=True) -> None:
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    
    time.sleep(pause)

    if clear:
        clear_line(text)


def type_out_splash(text: str, delay=0.05, pause=1.5, clear=True) -> None:
    for char in text:
        sys.stdout.write(char + (" " * 5) + ("\033[D" * 5))
        sys.stdout.flush()
        time.sleep(delay)
    
    time.sleep(pause)

    if clear:
        clear_line(text)


def typing_message(cycles=3, start_sleep=0) -> None:
    time.sleep(start_sleep)
    
    text = "typing"
    sys.stdout.write(text)
    sys.stdout.flush()
    for _ in range(cycles):
        for _ in range(3):
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(0.3)
        # Reprint text and remove ellipsis
        sys.stdout.write("\r" + text + (" " * 3) + "\r")
        # Reset cursor position for loop
        sys.stdout.write(text)
        sys.stdout.flush()
        time.sleep(0.2)
    # Clear text from line without clearing screen
    sys.stdout.write("\r" + " " * (len(text) + 3) + "\r")
        

def visible_len(s):
    return len(ansi_escape.sub('', s))


def work_ethic(hours: int) -> str:
    if hours >= 40:
        return "Optimal"
    elif hours > 30:
        return "Good"
    elif hours > 25:
        return "Fair"
    elif hours > 15:
        return "Pitiful"
    else:
        return "Non-existant"
