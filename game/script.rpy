# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")

#image background:
 #     zoom 0.75
  #    "bg street.png"


# The game starts here.

label start:
    #scene bg street #original was too big
    #scene background
    scene bg street
    call intro from _call_intro
    call uma_story from _call_uma_story
    call interlude from _call_interlude
    call startMina from _call_startMina
    call death_ending from _call_death_ending

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    return
