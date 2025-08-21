# Cleo will gather information to test the user's truthfulness
address = []
age = []
best_friend = []
city = []
name = []
postal_code = []
zip_code = []
work_hours = 0

# Menu control for available/locked/coming-soon apps
apps = ["1", "2", "3", "4", "5"]
completion = set()

# Menu control for available/locked/coming-soon apps
about_options = ["1", "2", "3", "4", "5", "6"]
about_completion = set()

# Commands that match the forbidden_commands.txt file
forbidden_commands = set(["access_logs", "make_ammends", "nine_one_one", "room_service",
                        "terminate_cli0"])

# Generated at the beginning of the game to randomize puzzles
admin_password = []
last_resort =[]

# User commands, date, and time saved for the Cleo Finale
user_commands = []
todays_date = []
timestamps= []
