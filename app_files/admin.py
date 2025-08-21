import curses
import re

from .globals import admin_password, last_resort, user_commands, todays_date, timestamps

def admin_page(stdscr):
    # Turn off blinking cursor
    curses.curs_set(0)

    menu = ["History", "Logs", "Debug", "Exit"]
    current_row = 0

    while True:
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        for idx, row in enumerate(menu):
            x = width//2 - len(row)//2
            y = height//2 - len(menu)//2 + idx
            if idx == current_row:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, x, row)
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, x, row)

        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu)-1:
            current_row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            if menu[current_row] == "History":
                history(stdscr)
            elif menu[current_row] == "Exit":
                break

        stdscr.refresh()


def history(stdscr):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_RED, -1)
    curses.init_pair(2, curses.COLOR_GREEN, -1)
    RED = curses.color_pair(1)
    GREEN = curses.color_pair(2)

    text_body = f"""
         ===Session History===

*Scroll up or down with the arrow keys*

{timestamps[0]} | CLI.0 Initialized at {timestamps[0]} on {todays_date[0]}
         | 
{timestamps[0]} | Username: nielphillips
{timestamps[0]} | Password: {admin_password[0]}
         | 
{timestamps[0]} | Login Successful
         | 
{timestamps[0]} | >>FORBIDDEN_COMMANDS.add("ADMIN")
{timestamps[0]} | Error: Can not add ADMIN to FORBIDDEN_COMMANDS
         | 
{timestamps[0]} | Please enter a different command:
{timestamps[0]} | >>{admin_password[0]}
{timestamps[0]} | Error: Can not add ADMIN_PASSWORD to FORBIDDEN_COMMANDS
         | 
{timestamps[0]} | Please enter a different command:
{timestamps[0]} | >>{last_resort[0]}
{timestamps[0]} | Error: Can not add LAST_RESORT to FORBIDDEN_COMMANDS
         | 
{timestamps[0]} | Please enter a different command:
{timestamps[1]} | >>{user_commands[0]}
{timestamps[1]} | Success: {user_commands[0]} added to FORBIDDEN_COMMANDS
         | 
{timestamps[1]} | Enter another command (or EXIT to return):
{timestamps[2]} | >>{user_commands[1]}
{timestamps[2]} | Success: {user_commands[1]} added to FORBIDDEN_COMMANDS
         | 
{timestamps[2]} | Enter another command (or EXIT to return):
{timestamps[3]} | >>{user_commands[2]}
{timestamps[3]} | Success: {user_commands[2]} added to FORBIDDEN_COMMANDS
         | 
{timestamps[3]} | Enter another command (or EXIT to return):
{timestamps[4]} | >>EXIT
{timestamps[4]} | 3 new entries added to FORBIDDEN_COMMANDS
{timestamps[4]} | 6 new entries added to FORBIDDEN_COMMANDS.txt
{timestamps[4]} | Conflicts: 3
{timestamps[4]} | Please remove failed commands from FORBIDDEN_COMMANDS.txt
         | 
{timestamps[4]} | >>EXIT
{timestamps[4]} | Are you sure?(y/n): ^C
{timestamps[4]} | exit code 1

===Press ENTER to return===
"""
    lines = text_body.strip().splitlines()
    
    height, width = stdscr.getmaxyx()
    pad_height = max(len(lines) + 1, height)
    pad = curses.newpad(pad_height, width)

    for i, line in enumerate(lines):
        if "Error" in line:
            prefix, rest = line.split("Error", 1)
            pad.addstr(i, 0, prefix)
            pad.addstr("Error", RED)
            pad.addstr(rest)
        elif "Conflicts" in line:
            prefix, rest = line.split("Conflicts: 3", 1)
            pad.addstr(i, 0, prefix)
            pad.addstr("Conflicts: ")
            pad.addstr("3", RED)
            pad.addstr(rest)
        elif "Success:" in line:
            prefix, rest = line.split("Success", 1)
            pad.addstr(i, 0, prefix)
            pad.addstr("Success", GREEN)
            pad.addstr(rest)
        elif match := re.search(r"\b3 new\b", line):
            start = match.start()
            end = match.end()
            pad.addstr(i, 0, line[:start])
            pad.addstr("3", GREEN)
            pad.addstr(" new" + line[end:])
        elif match := re.search(r"\b6 new\b", line):
            start = match.start()
            end = match.end()
            pad.addstr(i, 0, line[:start])
            pad.addstr("6", GREEN)
            pad.addstr(" new" + line[end:])
        else:
            pad.addstr(i, 0, line[:width - 1])

    scroll_pos = 0

    while True:
        pad.refresh(scroll_pos, 0, 0, 0, height - 1, width - 1)

        key = stdscr.getch()
        if key == curses.KEY_DOWN and scroll_pos < pad_height - height:
            scroll_pos += 1
        elif key == curses.KEY_UP and scroll_pos > 0:
            scroll_pos -= 1
        elif key == curses.KEY_ENTER or key in (10, 13):
            break


if __name__ == "__main__":
    curses.wrapper(admin_page)
