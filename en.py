import config

# Help
help           =  '''Commands:
┌───┬─────────┬────────────────────────────┬────────────────────────────────────────────────────────────────────────────────────┐
│ № │ Command │ Name                       │ Description                                                                        │
├───┼─────────┼────────────────────────────┼────────────────────────────────────────────────────────────────────────────────────┤
│ 1 │ start   │ Greetings                  │ It just prints out a greeting. In autostart.                                       │
│ 2 │ help    │ Command List               │ Outputs this list.                                                                 │
│ 3 │ dialog  │ Dialogue Mode              │ A tricky function.                                                                 │
│ 4 │ new     │ New feature command        │ Displays honest reasons for the long release of updates.                           │
│ 5 │ news    │ News                       │ Bot news, or rather new features.                                                  │
│ 6 │ echo    │ Echo-mode                  │ It just prints what you write. Carefully! Getting out of there is a bit tricky.    │
│ 7 │ rand    │ Ramdom number              │ Shows a random number in your range.                                               │
│ 8 │ restart │ Restart bot                │ May be useful for changing the language.                                           │
│ 9 │ about   │ About PBot                 │ Shows brief information about the project and the author.                          │
└───┴─────────┴────────────────────────────┴────────────────────────────────────────────────────────────────────────────────────┘'''

# News
news = f'''News - (AAA?):
- Updated the list of commands
- Added restart function
- Added "About PBot" feature
- Questions?'''

# About
about = f'''
░▄▄▄▄░     █████░░████░░░░░░░░░░░██░
▀▀▄██►     █░░░░█░█░░░█░░░███░░░████
▀▀███►     █████░░████░░██░░░██░░██░
░▀███►░█►  █░░░░░░█░░░█░██░░░██░░██░
▒▄████▀▀   █░░░░░░████░░░░███░░░░███

Bot written according to the homework of the Algorithmika school
CAREFULLY! NON-FUNNY JOKES!

{news}

Install:
    git clone https://github.com/TRFish/PBot.git
    cd PBot
    ./pbot.py

{help}
'''

# Start
start          = f'Hi, my name is {config.Name}, a bot for all occasions (well, or for those provided by the code)\nTo display a list of commands, write help'

# Tips
tip_exit       =  'To exit, write "exit"'
tip_text       =  'Enter any text'

# Achivements
ach_mamont     =  'the mammoth is deceived'
ach_received   =  'You have received an achievement:'

# Dialog
dialog_welcome = f'Dialog-mode. Here you can really chat about anything. {tip_exit}'
dialog_rep1    =  'Hahaha\nDid you think I put it in here?'
dialog_rep2    =  'HAHAHAHAHAHAHA'

# New
new_rep1       =  'I made new functions, and this dinosaur broke them'
new_rep2       =  'Honestly\n'
new_rep3       =  "But I'm already making new ones at the speed of a dead snail!"

# Echo-mode
echomode_rep1  =  '(To exit, write "stop"):'
echomode_rep2  =  '(And the magic word):'
echomode_rep3  =  "(I didn't hear you):"
echomode_rep4  =  '(And now all together):'
echomode_exit  =  "All right, all right. Don't shout."

# Rando
rando_rep1     =  'Minimum number:'
rando_rep2     =  'Maximum number:'

# Restart
restart        = 'Switch language'

# Exit
exit           =  'Bye!'
