define unknown_character = Character(_("???"), color="FFFFFF")
define death = Character(_("Death"), color="6B8E23")
define audio.mainTheme = "audio/MainTheme.ogg"

#-----death art----
#death neutral
#death smug

label interlude:
    play music mainTheme fadein 1.0
    "You raise a hand to your chest. The adrenaline rush is starting to wear off, and you\'re starting to process everything that just happened."

    show death neutral
    with dissolve

    unknown_character "So? How do you feel?"

    menu:
        "This is the afterlife?":
            jump this_is_the_afterlife

label this_is_the_afterlife:

    show death smug

    unknown_character "Ah, I see you figured that out!"

    show death neutral
    
    unknown_character "Yes, all of your customers are dead, and I\'ve made it your job to help me send them off."
    
    show death smug

    unknown_character "I must say, you\'re doing great so far!"

    menu:
        "Why me?":
            jump why_me

label why_me:

    show death neutral

    unknown_character "Before I say any more, I suppose I should formally introduce myself."

    unknown_character "You may already know me by many names."

    unknown_character "Yama. Enma. Batara Kala."

    show death smug
    
    unknown_character "Here, you may call me Death."

    death "And as we discussed earlier, this is the afterlife."

    show death neutral
    
    death "Well, this is one of its infinite possible forms."

    death "I can change how the afterlife looks and functions depending on the needs of those I serve at a given time."

    death "As for why I chose you specifically…that\'s for you to figure out."

    death "All I can tell you is that my services are only reserved for the toughest of cases. For those who refuse to move on."

    death "You sure have your work cut out for you! Welcome to my life!"

    show death smug
    
    death "My ‘afterlife\', that is. Heh."

    show death neutral
    
    death "Anyway, joking aside."

    show death smug
    
    death "It looks like you\'ve got more customers lining up! Should\'ve known my new part-timer would be in such high demand!"
    
    show death neutral

    "You look around and see nothing but emptiness. Not a single human figure is visible, even in the distance."

    death "Well, once again, I should let you go."

    death "Let\'s talk again after you\'ve spoken to another customer."

    hide death
    with dissolve

    "Their figure fades away once again, ever mysterious. You sigh and prepare yourself for the next person."

    stop music fadeout 1.0
