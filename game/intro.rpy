define unknown_character = Character(_("???"), color="FFFFFF")
define audio.oceanAmbience = "audio/OceanAmbience.ogg"
define audio.mainTheme = "audio/MainTheme.ogg"

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)

#-----death art----
#death neutral
#death smug

label intro:
    stop music fadeout 1.0
    play ambience oceanAmbience fadein 1.0 volume 0.2
    play music mainTheme fadein 1.0

    "You open your eyes to an unfamiliar place."

    "The night sky above shimmers like a deep blue curtain of stars, and the sound of ocean waves in the distance is soothing."

    "When you look around, you see food stalls scattered across the coastline."

    "You try to remember how you got here, where you came from, but your mind suddenly draws a blank."

    "You can\'t seem to recall anything about yourself at all."

    show death neutral
    with dissolve

    unknown_character "Ah, I see you\'ve gained consciousness."

    "A mysterious figure stands before you. They wear an enigmatic smile."

    unknown_character "Welcome, welcome! I\'m so glad to be able to speak to you face to face."

    menu:
        "Who are you? ":
            jump _continue
        "What is this place? ":
            jump _continue
        "Why am I here? ":
            jump _continue

label _continue:
    unknown_character "Such a good question! Don\'t worry, you\'ll have your answer in due time."

    unknown_character "For now, all you need to worry about...is this!"

    "They hand you an apron and gesture towards a nearby food stall."

    show death smug

    unknown_character "You could say I\'m in the business of providing services to people."

    show death neutral

    unknown_character "Recently, I decided to try diving into food service specifically."

    unknown_character "I have my hands full managing the logistics, though, so I thought I\'d hire a chef to mind a food stall for me."

    unknown_character "I needed to make sure I got someone I could form a, uh..."

    show death smug

    unknown_character "Mutually beneficial relationship with."

    show death neutral

    unknown_character "And you seemed like the perfect fit!"

    unknown_character "It\'s a simple job, don\'t worry - all you have to do is serve customers food that they like. Easy enough!"

    menu:
        "How will I know what people like? ":
            jump _how
        "Who are the customers? ":
            jump _who

label _how:
    unknown_character "Worry not! I have that taken care of."

    unknown_character "I don\'t want to overcomplicate things, so let\'s just say that you\'ll know when you see them."

    jump help

label _who:

    show death smug

    unknown_character "Another thing you\'ll find out in due time, I\'m afraid."

    show death neutral

    unknown_character "But we won\'t be getting anyone violent or hostile, I can assure you of that. If it helps."

    jump help

label help:
    unknown_character "So what do you say? Will you help me?"

    menu:
        "Uh, sure. ":
            jump _yes
        "You\'re suspicious. No way. ":
            jump _no_way
        "Tell me why I can\'t remember anything first. ":
            jump _tell_me_more

label _yes:

    show death smug

    unknown_character "Great!"

    jump bye

label _no_way:

    show death smug

    unknown_character "Suspicious? {i}Me?{i}"

    unknown_character "Well. I suppose I can see that, seeing as you have no idea where you are or who I am or why you have this job."

    show death neutral

    unknown_character "But just trust me, this is all for a good cause."

    unknown_character "Try serving one person, and then we can see how you feel, hm?"

    jump bye

label _tell_me_more:

    show death smug

    unknown_character "Persistent {i}and{/i} curious."

    unknown_character "If our conversation so far is any indication, you\'ll start to get some answers as you serve some customers."

    unknown_character "Hence the ‘mutually beneficial relationship!\'"

    jump bye

label bye:

    show death neutral

    unknown_character "Well, then, I\'ll just get out of your way."

    unknown_character "But I\'ll be close by, if you need me."

    hide death
    with dissolve

    "The enigmatic smile stays plastered on their face as they disappear into the shadows."

    "You look around, still confused. The area is pretty deserted, so it\'s not likely you\'ll be seeing other people very often."

    "Still, there doesn\'t really seem to be anywhere else you can go."

    "So you slip the apron on and relax your shoulders, mentally preparing yourself to serve your first customer."

    "..."

    "To your surprise, it doesn\'t take long."

    stop music fadeout 1.0
