'''Phase 1 || Weather and To-Do'''

option_locked_all = [
    "Let's not get hasty! Let's finish 1 and 2 first :)",
    "Love the enthusiasm! We'll get there, don't worry!",
    "Ha ha, look at you go! We're not quite ready for that one yet :)",
    "Sounds pretty fun hey? Patience is key :)",
    "What's the rush? There's plenty of time for that later! ;)",
    "Not so fast, silly! That won'te be locked for long :)",
    "Early bird gets the worm :) you're a bit TOO early though he he",

]

option_locked_todo = [
    "Doesn't the menu remind you of a list? Like a to-do list? ;) ;)",
    "One thing at a time! Maybe we can make a to-do list about it? :)",
    "Look at all of those options! So many things... to-do ;) ;)",
    "to-do or not to-do? That is the question, but let's do :)",
    "This one will be so much better afer you have a to-do list I bet :)"
]

option_locked_weather = [
    "Aren't you curious about the weather? Let's start there :)",
    "I wonder if it's raining outside? Should I check??",
    "I'm thirsty, Dark and Stormy anyone? Maybe a Tequila Sunrise??",
    "Windy outside? The weather app will BLOW you away ha ha ;)",
    "Check the weather and grab an umbrella before you go there!"
]

none_complete = option_locked_all + option_locked_todo + option_locked_weather
todo_complete = option_locked_all + option_locked_weather
weather_complete = option_locked_all + option_locked_todo


'''Phase 1.5 || Option 3 (No Other Way)'''

option_three_only = [
    "Let's play a guessing game! I bet it will be fun :)",
    "There's only one way to go! Guessing game time!",
    "No time to dilly dally, I wanna play! :)",
    "On the count of 3. 1, 2,... 3!"
]


'''Phase 2 || Guessing Game'''

guess_game_high = [
    "Ooh super close, a little bit high.",
    "Close, but no cigar, think smaller.",
    "You're going high when you should be going low.",
    "Think that, but a bit less."
]

guess_game_low = [
    "Ah so close, but you're flying low.",
    "Nice Guess, but not quite, pump those numbers up.",
    "You're looking for ants on a bird hunt.",
    "Look to god. (Too low)"
]

guess_game_lie = guess_game_low + guess_game_high


'''Phase 3 || Getting To Know You'''

option_four_only = [
    "Let's keep moving along! Don't you want to get to know me? :)",
    "Option 4 is open now! Let's try that one out :)",
    "We've got a lot of ground to cover! Let's try option 4!",
    "Let's see what's behind door number 4! he he :)",
    "Let's have a chat, option number 4!"
]


'''Phase 4 || Impressions'''

option_five_only = [
    "We've been throug so much! But we're not done yet :)",
    "Look at all that progress we've made! Let's finish up :)",
    "Number 5, here we go!",
    "Don't you want to see some impressions?? :)",
    "I bet you're quite the pop-culture wiz, let's find out :)"
]
