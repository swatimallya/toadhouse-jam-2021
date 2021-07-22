define unknown_character = Character(_("???"), color="FFFFFF")
define uma = Character(_("Uma"), color="FFA500")

#-----uma art----
#uma neutral
#uma happy + unique var content
#uma angry
#uma surprised
#uma sad + unique var pained

label uma_story:
    "A woman hesitantly approaches your stand."

    show uma neutral
    
    unknown_character "...hello..."
    unknown_character "...this is a food stall, right?"
    
    menu:
        "Nod.":
            jump nod
        "Say nothing.":
            jump say_nothing

label nod:

    show uma happy

    unknown_character "Great! I was starting to get hungry."
    
    "She sits down enthusiastically."

    show uma neutral
    
    unknown_character "Do you have a special?"
    
    jump choices1

label say_nothing:

    show uma sad

    unknown_character "I guess it\'s obvious...?"
    
    "She sits down, looking slightly confused."

    show uma neutral
    
    unknown_character "Um...do you have a menu?"
    
    jump choices1

label choices1:
    menu:
        "Offer her a plate of vada pav. ":
            jump _vada_pav
        "Offer her a masala dosa thali. ":
            jump _masala_dosa
        "Offer her a hot cup of chai. ":
            jump _chai

label _vada_pav:
    "You place a steaming hot plate of vada pav in front of her, along with an assortment of chutneys."
    
    show uma surprised

    unknown_character "Oh!"
    
    "She picks it up and takes a bite, and a euphoric expression spreads across her face."
    
    show uma happy

    unknown_character "Wow, that\'s really authentic! Tastes just like my favourite food stand back in Bengaluru."
    
    show uma sad

    unknown_character "..."
    
    unknown_character "...I kind of guessed I\'m not there anymore. This place looks nothing like the city I\'m used to."
    
    show uma neutral

    unknown_character "And honestly, I don\'t really remember much else...aside from my name..."
    
    show uma sad

    unknown_character "..."

    show uma neutral
    
    uma "It\'s Uma."
    
    uma "I don\'t really know why I told you that...it\'s just..."
    
    uma "This place feels...comfortable. This food brings back good memories."

    show uma happy
    
    uma "Actually, this is exactly what I was eating when I met Golu for the first time."
    
    jump choices2

label _masala_dosa:
    "You place a thali with a large masala dosa, bhaji, and several assorted chutneys in front of her."
    
    show uma sad

    unknown_character "..."
    
    "Reluctantly, she takes a bite, her eyes firmly fixed on the surface of the stand. Then, despite her initial disinterest, she takes another bite, seemingly satisfied with the taste."
    
    show uma neutral

    unknown_character "...it\'s good."
    
    unknown_character "Really good, in fact. Tastes just like the restaurant my..."
        
    show uma sad

    unknown_character "...my parents used to take me to when they needed to have \"important conversations\" with me."
    
    show uma angry

    unknown_character "Like \"Uma, why are your grades so bad this year?\"" 
    
    uma "\"Uma, you need to choose a good boy and settle down right now.\""
    
    uma "\"Uma, we want grandchildren. Your younger siblings are married. Why are you such a disappointment?\""
    
    show uma sad

    uma "..."
    
    uma "They never even accepted Golu as part of the family."
    
    jump choices2

label _chai:
    "You place a freshly brewed cup of chai in front of her."
    
    unknown_character "Hm?"

    show uma surprised
    
    "She takes a sip, and her eyes grow wide with surprise."
    
    unknown_character "This...there\'s no way..."
    
    unknown_character "It tastes exactly how the chai stand below my apartment makes it."
    
    unknown_character "The owner always calls me over by name when I walk home..."
    
    unknown_character "\"Uma!\" he says. \"Come get your evening chai!\""
    
    uma "..."
    
    uma "Sometimes he would even give it to me for free."

    show uma happy
    
    uma "Such a kind man. Always looked out for me and Golu."
    
    jump choices2

label choices2:
    menu:
        "Raise a curious eyebrow. ":
            jump _eyebrow
        "Wipe the table disinterestedly. ":
            jump _wipe_table
        "Give her a small smile. ":
            jump _small_smile

label _eyebrow:

    show uma sad

    uma "Ah...right..."

    show uma neutral
    
    uma "Golu is my cat."
    
    jump next

label _wipe_table:

    show uma happy

    uma "...ahaha...I don\'t even remember how long it\'s been since I\'ve been away from Golu, but I miss him so much already."
    
    uma "I know you probably don\'t care, but..."
    
    uma "Golu is my cat."
    
    jump next

label _small_smile:

    show uma happy

    uma "Thank you. For listening to me, I mean."
    
    uma "It feels like it\'s been a long time since I\'ve had someone to talk to who cared, even a little bit."
    
    uma "You\'re probably wondering who Golu is, huh?"
    
    uma "He...he\'s my cat."
    
    jump next

label next:

    show uma neutral

    uma "I found him on the street one evening."
    uma "He was eating scraps from the ground, and he looked so round and overweight...which is why I gave him his name."
   
    show uma sad

    uma "His fur was so dirty and he was covered in scabs...my heart broke when I saw him."

    show uma neutral

    uma "I knew right then that I needed to take him home."
    uma "Since then, it\'s been just me and him against the world."
    uma "I would do anything for him."

    show uma sad

    uma "When he was sick, I..."
    uma "I spent my full paycheck on his treatment and special food."

    show uma neutral

    uma "I only ate Maggi noodles that whole month, but he was worth it."
    uma "..."

    show uma angry

    uma "...most people don\'t understand."
    uma "My parents most of all."
    uma "They wanted me to have a life that I didn\'t want."
    uma "But I\'m my own person! I had a job, I lived and worked on my own."

    show uma sad

    uma "Even when it was hard, even when it was stressful..."
    uma "Golu was there for me when no one else was."
    uma "Even...in the end..."
    
    jump memories

label memories:

    show uma pained

    "A strange expression comes over Uma. You feel your chest grow heavy."
    
    "Memories began to flash through your mind."
    
    "Memories...that you somehow know aren\'t your own."
    
    uma "Urgh...I...in the end...?"
    
    "You see a woman waving goodbye to the owner of a food stall."
    
    "Then, as she turns to walk away, she suddenly collapses to the ground, clutching her chest."
    
    "In the few moments before everything goes black, you hear footsteps rushing towards her from behind, hear the voices of children calling out."

    "Then, the memories stop, and the world fades into view again."
    
    uma "I..."
    
    "She places a hand over her heart."

    show uma sad
    
    uma "I...collapsed..."
    
    uma "I don\'t remember anything else after that until I came here..."
    
    uma "..."

    show uma neutral
    
    uma "...I didn\'t make it, did I?"

    show uma sad
    
    uma "I\'d always had a weak heart, even since I was young."
    
    uma "The pollution and the stress didn\'t help."
    
    uma "I\'d been struggling for a while...struggling to make it on my own..."
    
    uma "..."

    show uma neutral
    
    uma "Tell me the truth."
    
    uma "I\'m dead, and this is the afterlife, isn\'t it?"
    
    jump choices3

label choices3:
    menu:
        "Nod hesitantly.":
            jump nod_hesitantly
        "Shake your head.":
            jump shake_your_head
        "Say nothing. ":
            jump _silent

label nod_hesitantly:
    "You nod hesitantly, partially because you don\'t want to stress her out any further, and partially because..."
    "...because something tells you that she isn\'t wrong."

    show uma sad

    uma "I knew it..."
    uma "I\'m...dead..."
    
    jump realization

label shake_your_head:
    "You shake your head. That\'s not possible...because that would mean..."
    uma "You can try to lie to me...but I know the truth."

    show uma sad

    uma "I think I\'ve known since the moment I got here."
    uma "It was just...a feeling I had that I couldn\'t quite place."
    uma "And now I know what it is."

    show uma angry

    uma "I\'m...really dead..."
    
    jump realization

label _silent:
    "You stay still. What could you even say or do? It\'s not like you know what this place is, either."
    uma "You don\'t have to say anything."
    uma "Somehow I just...know."
    uma "I know that I\'m...dead..."
    
    jump realization

label realization:

    show uma sad

    uma "I don\'t...I don\'t even know what to say...what to think..."
    
    uma "All I can think about is...Golu..."
    
    uma "I left him behind...I\'m all he ever had in this world..."
    
    uma "And he...he was all I had too..."

    show uma angry
    
    uma "What\'s going to happen to him?!"
    
    uma "I need..."
    
    uma "..."

    show uma pained
    
    uma "I need to go back!!"
    
    "Her eyes begin to fill with tears and she starts looking around helplessly. You have no idea how to respond."
    
    "Something prickles at the back of your mind...a memory."
    
    "But this time, it feels more personal."
    
    "All your life, you never thought anyone could care this much about another human being, much less an animal."
    
    "Seeing someone whose only thought in death is to want to go back and continue to live for someone else..."
    
    "...it fills your chest with a strange, unfamiliar warmth."
    
    uma "Golu...why...why did I have to die so soon..."
    
    "You think about what you could do to help."
    
    "You\'ve seen Uma\'s past...her memories..."
    
    "All you can do...is offer her one last meal."
    
    jump choices4

label choices4:
    menu:
        "Offer her a plate of tea biscuits. ":
            jump _tea_biscuits
        "Offer her a bowl of toffees. ":
            jump _toffee
        "Offer her some homemade grapefruit chips. ":
            jump _grapefruit_chips

label _tea_biscuits:
    "You slide a plate of tea biscuits across to her."
    uma "...these..."

    show uma sad

    "Her tears subside and she reaches out and picks up a biscuit, taking a hesitant bite."

    show uma surprised

    uma "These taste like the biscuits the chai stand owner near my apartment used to serve."
    uma "I remember...before I blacked out, I heard his voice."
    uma "He saw me collapse...he knew I had a cat."
    uma "He\'d offered to take care of him in the past, when he knew I was busy."

    show uma sad

    uma "I think...he would take good care of Golu."
    
    jump end

label _toffee:
    "You place a bowl of assorted toffees in front of her, covered in colourful wrappers."
    uma "...these..."

    show uma sad

    "Her tears subside and she reaches out and unwraps a toffee, popping it in her mouth."

    show uma surprised

    uma "This is the brand I used to give to the neighbourhood kids..."
    uma "They were always coming to visit, to see Golu."
    uma "They loved him...almost as much as I did."

    show uma sad

    uma "I think...they would take him in and look after him."
    
    jump end

label _grapefruit_chips:
    "You place a plate of homemade grapefruit chips in front of her."

    show uma surprised

    uma "...these...!"
    "Her tears subside and she reaches out and takes a chip, placing it in her mouth."
    uma "These taste like home!"
    uma "Even after my parents gave up on me...my grandmother would still come visit."
    uma "She understood why I wanted to live the way I did. She loved Golu too."

    show uma sad

    uma "Unlike the rest of my family...she was proud of me."
    uma "I think...she would take care of Golu."
    
    jump end

label end:
    uma "..."

    show uma neutral
    
    uma "...thank you."
    
    uma "My parents thought I was a lost cause."

    show uma sad
    
    uma "And I was so caught up in those feelings...I convinced myself that everyone else in the world thought the same."
    
    show uma neutral

    uma "But I was wrong."

    show uma happy
    
    uma "In the end, there were still people in my life who cared about me."
    
    uma "People who accepted me as I was...people who didn\'t judge my choices."
    
    uma "People who knew and understood that Golu was the center of my world. That I would\'ve done anything for him."
    
    show uma sad

    uma "They all knew how much I\'d want him to be taken care of after I was...gone."
    
    show uma neutral

    uma "You helped me remember that."
    
    uma "I feel like...I can move on now."

    show uma content
    
    "She smiles contentedly and closes her eyes."
    
    uma "I hope I\'ll see you again someday...Golu..."
    
    "Her form fades away until there is nothing left."