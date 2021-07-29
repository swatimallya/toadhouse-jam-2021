#Mina Section
define mina = Character('Mina', color="#ffffff")
define unknown = Character('????', color="#ffffff")

define talkedAboutFather = False
define talkedAboutMother = False
define talkedAboutBrotherYounger = False
define talkedAboutBrotherOlder = False

define MentionedOlderBrotherName = False
define perfectPlaceperfectTime = False

define audio.oceanAmbience = "audio/OceanAmbience.ogg"
define audio.plate = "audio/Plate.ogg"
define audio.plate2 = "audio/Plate2.ogg"
define audio.cooking = "audio/Cooking.ogg"
define audio.cupstir = "audio/CupwithStirring.ogg"
define audio.pouring = "audio/Pouring1.ogg"
define audio.pouring2 = "audio/Pouring2.ogg"
define audio.kettle = "audio/Kettle.ogg"
define audio.startStove = "audio/StartStove.ogg"
define audio.stoveOff = "audio/OffStove.ogg"

#-----mina art----
#mina neutral
#mina relaxed
#mina sigh
#mina remembering

#-----sfx------
#kettle audio ringing?
#tea pouring

init python:
    renpy.music.register_channel("ambience", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("minaDrums", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("minaHappyMelody", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("minaFreeMelody", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("minaHappyHarmony", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)
    renpy.music.register_channel("minaFreeHarmony", mixer="music", loop=True, stop_on_mute=True, tight=False, file_prefix=u'', file_suffix=u'', buffer_queue=True, movie=False, framedrop=True)

label startMina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")

    $ renpy.music.play("audio/MinaTheme_Drums.ogg", channel="minaDrums",loop=True, synchro_start=True, fadein=1.0, fadeout=1.0, tight=None, if_changed=False, relative_volume=1.0)
    $ renpy.music.play("audio/MinaTheme_HappyMelody.ogg", channel="minaHappyMelody",loop=True, synchro_start=True, fadein=1.0, fadeout=1.0, tight=None, if_changed=False, relative_volume=1.0)
    $ renpy.music.play("audio/MinaTheme_FreeMelody.ogg", channel="minaFreeMelody",loop=True, synchro_start=True, fadein=1.0, fadeout=1.0, tight=None, if_changed=False, relative_volume=1.0)
    $ renpy.music.play("audio/MinaTheme_HappyHarmony.ogg", channel="minaHappyHarmony",loop=True, synchro_start=True, fadein=1.0, fadeout=1.0, tight=None, if_changed=False, relative_volume=1.0)
    $ renpy.music.play("audio/MinaTheme_FreeHarmony.ogg", channel="minaFreeHarmony",loop=True, synchro_start=True, fadein=1.0, fadeout=1.0, tight=None, if_changed=False, relative_volume=1.0)

    "Another customer emerges from the shadow..."
    "He seems to be a little confused."
menu:
    "Invite him over.":
        show mina neutral
        jump friendlyMina
    "Wait for him to come.":
        show mina neutral
        jump realxedMina

label friendlyMina:
    $ perfectPlaceperfectTime = True
    unknown "Hi there, you're parked way out in the middle of nowhere."
    unknown "That must be really bad for business, unless this place is really popping any time other than now."
    mina "Oh, I am Mina by the way. I don't know where I am but you seem very friendly."
    mina "I am also very hungry. I think we were meant to find each other here. Perfect time, perfect place."
    jump Stage1Mina

label realxedMina:
    unknown "Oh, hello! Another person, finally!"
    mina "My name is Mina by the way."
    mina "I can't tell how long I've been walking but I can tell you, I am glad I finally found someone."
    mina "Oh! And you serve food also! I can't tell you how much I need to eat right now!"
    jump Stage1Mina

label Stage1Mina:
    mina "So what are you offering?"
    "What should Mina start with?"
menu:
    "Tea with mint.":
        jump Start_MTea_Mina
    "Beer.":
        jump Start_Beer_Mina
    "Molokheya and rice.":
        jump Starter_MRice_Mina

#if (Molokheya and rice) is selected as the first choice! (More info about the mom) and also, Mina won't accept it.
label Starter_MRice_Mina:
    play sound plate volume 1.0
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "Oh, we're going in for the food already?"
    mina "You know, I'm gonna ask you to push that back a little."
    mina "This dish, it reminds me a lot of my mother, she used to make the best Molokheya I ever tasted."
    mina "And rice to be frank."
    mina "I sometimes got it from restaurants because I would hang out with friends."
    mina "But none of these ones tasted as good as the one at home."
menu:
    "Offer a different starter.":
        mina "Oh, yeah. Time for the starter!"
        jump Starters1_Again_Mina
    "...":
        mina "She always found something she didn't like about the food she made."
        mina "I think I learned to be hard on myself just observing her"
        mina "but whenever I notice myself doing that, I stop."
menu:
    "Offer a different starter.":
        jump Starters1_Again_Mina
    "...":
        $ talkedAboutMother = True
        mina "When I was still living with my parents, I remember feeling a lot of extra pressure."
        mina "Most of it was because they were very vocal of their expecations of me or my brothers."
        mina "My mother was \"vocal\" in her own way. She used to have this look that made me feel like a disappointment."
        show mina sigh
        "Mina sighs..."
        mina "Anyway."
        jump Starters1_Again_Mina

#After "Molokheya and rice" is rejected
label Starters1_Again_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    "Remind me again what can I have?"
menu:
    "Tea with mint.":
        jump Start1_MTea_Mina
    "Beer.":
        jump Start1_Beer_Mina

#if Mint tea was selected as the first choice! (More info about the dad)
label Start_MTea_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "Oh! We're starting with mint tea!"
    mina "I know a lot of people who grew mint at their home to have it as fresh as possible!"
    #Talks about the dad and their problem together
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "You know, "
    extend "my father used to pick fresh mint from a small garden outside of his workplace." #extend is a built in character that is supposed to continue on the last line with the same character as above.
    show mina sigh
    mina "He always had to make sure everything was done right."
    mina "Even a cup of tea with some mint"
    mina "It had to be the exact amount of sugar, the exact amount of tea "
    extend "and of course the exact amount of mint."
menu:
    "Prepare the tea.":
        jump MTea_Mina
    "...":
        $ talkedAboutFather = True
        "You say nothing and let Mina continue."
        mina "It felt like he wanted to control everything."
        mina "My older brother, Thomas, was always on his side."
        $ MentionedOlderBrotherName = True
        mina "It only seemed to have bothered me though."
        mina "Dad was always proud of him the most, even though he always said to his friends that I'm too much like him."
        mina "It bothered me a lot knowing that he found us similar."
        mina "I was either as controlling as I saw him, or he didn't see himself the way I saw him."
        mina "Well we both liked mint tea the same way that's for sure."
        jump MTea_Mina

#if mint tea was not selected as the first choice!
label Start1_MTea_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    mina "Mint tea! Sounds good!"
    jump MTea_Mina

#This happens either way since Mina won't reject it if chosen first or later.
label MTea_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    "You bring out a kettle already filled with water and you place it on the stove." #heater??
    play sound startStove volume 1.0
    mina "Oh!"
    show mina remembering
    "Mina seems to have remembered something!"
    mina "That's how I used to drink it at home!"
    mina "We had the electric kettle but we used to make tea old school on the stove." #oven????
    #remembers the resolution to him and his dad's conflict
    if talkedAboutFather:
        mina "By we I mean me and my dad."
        mina "This was probably the only time of the day when we didn't fight at all."
        mina "Well, maybe we fought a little bit at the begining when I was learning, but after I got the hang of it I made the best tea for us."
    mina "You know, I had mint tea served at my wedding because I knew it was dad's favorite thing to drink."
    mina "Even then though, dad didn't enjoy the tea that much."
    mina "I remember him saying it wasn't the best he'd had."
    #sfx kettle audio ringing?
    play sound kettle volume 1.0
    queue sound stoveOff volume 1.0
    "The kettle is ready, you turn off the stove."
    #sfx tea pouring
    play sound pouring volume 1.0
    queue sound cupstir volume 1.0
    "You pour the water into the cup and stir the tea and add the mint."
    mina "Yum! smells great!"
    "You present the cup to Mina."
    "He takes a sip."
    "..."
    mina "Hold on!"
    show mina remembering
    extend " I remember!"
    stop ambience fadeout 1.0
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")

    mina "The night before the wedding! Dad came over to my house and we stayed in the garden outside."
    mina "There was a cool breeze, the stars were beautiful and we were sitting on pop up chairs."
    mina "I had the kettle we used to have when I was younger, it looks like this one you have here."
    if talkedAboutFather:
        mina "At home, we had a spot we preferred on the stove."
    mina "I started a small fire - made sure it was safe, of course."
    mina "And we made tea while we talked about our lives up to that point."
    mina "He said he missed me, I had been living in a different city for a few years by then."
    if talkedAboutFather:
        mina "\"Mina,\" he said, \"I realized I was too hard to deal with too late.\""
    mina "He felt like a different person then, and whatever I felt was difficult between us just faded away."
    show mina relaxed
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    "Mina takes a deep breath."
    mina "I also said sorry about being mean sometimes too."
    mina "The kettle was whistling too high by then."
    mina "\"Oh no!\" I said, "
    extend "\"the mint! We don't have mint!\""
    mina "He had mint in his pocket for God knows how long."
    mina "We laughed about it and thought it would probably be expired or gone bad by then but we added it to the tea anyway."
    mina "At the wedding the next day."
    mina "When he told me that the mint tea wasn't the best."
    mina "He said that the best one he had ever had was that night before."
    mina "I am glad we talked about these things."
    "Mina smiles at you."
    mina "I am glad your tea reminded me of that!"

    play ambience oceanAmbience fadein 1.0 volume 0.2
    jump FoodOptions2_Mina

label Start_Beer_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")

    $ talkedAboutBrotherYounger = True
    mina "Oh, beer, I'm down!"
    mina "But can I ask you something because I can't tell."
    mina "I notice the sky is dark but are we closer to midnight or to the next morning?"
menu:
    "Shrug.":
        mina "Oh you don't know too?"
        show mina sigh
        mina "Hmm"
        jump Start_Beer_Mina_2
    "...":
        mina "You really are keeping the mystery alive, Chef."
        mina "I'll drink either way."
        jump Start_Beer_Mina_2

label Start_Beer_Mina_2:
    show mina relaxed
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    "Mina looks at the sky and he seems to have something on his mind."
    mina "My younger brother, David, and I used to drink together more than our older brother."
    mina "He used to do crazy things when we were all living in the same house and he rarely got in trouble."
    mina "I did less crazy things and I always got in trouble."
    mina "I always asked him to be more responsible but he never listened."
    mina "I tried to cover for him some times but I don't think he noticed."
    jump Beer_Mina

label Start1_Beer_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    mina "Beer it is then!"
    jump Beer_Mina

label Beer_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    "You grab a really big mug from under the counter."
    mina "Wow."
    "You start pouring the beer from the barrel inside the cart."
    mina "So, why won't you have one too while you're at it?"
    "..."
    mina "Alright!"
    "You present the mug to Mina."
    "He grabs it and chugs it all in one go!"
    mina "Heyy!"
    show mina remembering
    mina "I remember something!"
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    if talkedAboutBrotherYounger:
        mina "David! "
    else:
        mina "My younger brother! "
    extend "When I was moving to a different city, we stayed up the whole night before in the balcony."
    mina "I think I was quicker to get tipsy."
    mina "I remember we never shouted but our conversation got intense."
    mina "I was out of line but I asked him to be more responsible when I leave."
    mina "He asked me what I meant and I think I said things I didn't think through."
    mina "He told me that out of me and our older brother I was more like dad."
    show mina sigh
    mina "..."
    mina "I didn't like that."
    mina "I think me and him had the same issues with dad, he was too distant and acted like he knew us."
    mina "I realized that I did the same thing with him."
    mina "I immediately apologized!"
    mina "I explained to him the way I saw it in my head and how I felt that I had to take care of him."
    mina "And how I thought I was protecting him from the rest of the family because "
    extend "I saw the \"real\" them."
    if talkedAboutBrotherYounger:
        $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
        $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
        $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
        $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeMelody")
        $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
        mina "But I realized David was always doing better than me mentally."
        mina "I had to ask him what his secret was."
    mina "He told me I didn't have to do all these mental gymnastics."
    mina "\"You spent too much time worrying about me,\" he said."
    mina "\"Worrying about everyone else but you.\""
    mina "\"Whatever you were doing to pretend they weren't also a part of my life,\" he said."
    mina "\"It only made you another character I had to find a way around.\""
    mina "He said that he noticed all the small things about the rest of the family."
    mina "And he gave them what they wanted."
    mina "He said I needed to feel like I was in control just like dad."
    mina "But sometimes I needed to feel the opposite of that."
    mina "For some reason, David seemed to have developed a very flexible character."
    mina "He didn't lie to anyone about who he was but he knew what we needed and gave it to us."
    mina "I learned a lot on that day."
    mina "I started watching my behaviour and focusing on the people around me and tried not to be a heavy weight on their hearts."
    mina "Thank you for the beer!"
    jump FoodOptions2_Mina

label FoodOptions2_Mina:
    play ambience oceanAmbience fadein 1.0 volume 0.2
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    show mina neutral
    mina "So Chef, what do you have next?"
    "What dish are you gonna offer Mina?"
menu:
    "Molokheya and rice.":
        jump FoodOptions2_MolokheyaAndRice
    "Koshary.":
        jump FoodOptions2_Koshary

label FoodOptions2_MolokheyaAndRice:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    "You start preparing the dish."
    "Preparing the rice, crushing Molokheya leaves and getting the soup ready."
    mina "We had two versions of this dish at home."
    mina "We usually eat vegetarian for two thirds of the year, you seem to be doing that version."
    mina "It reminds me a lot of the time after I quit my first job and went back home for a while."
    if talkedAboutMother:
        show mina sigh
        mina "Mom still had that look that made me feel like I did something wrong."
        mina "I don't even think she knew what I did at my work."
        mina "But she still expressed her \"disappointment\" or whatever."
    #sfx something is finished
    play sound plate2 volume 1.0
    "The dish is done!"
    "Your pour the Molokheya in the rice and present it to Mina."
    show mina neutral
    mina "Aah! smells great!"
    "Mina starts eating the dish."
    show mina remembering
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "I remember something!"
    mina "The first few days after I was back, there was some tension between me and mom."
    if talkedAboutMother:
        mina "She kept asking what was my next opportunity."
        mina "\"So you just left without having a plan?\" she asked."
        mina "\"I couldn't stay any longer, it was very draining,\" I replied."
    show mina sigh
    mina "She said that I let go of good opportunities really quickly."
    mina "\"You have to learn how to take a punch, you're being too soft.\""
    mina "I left the dinner table and went to my room."
    mina "It felt like I was in my teens again."
    mina "Only this time, I was the one that quickly got out again and asked her to talk."
    mina "I had decided this time to sit and listen very carefuly and not let anything get on my nerves."
    mina "I asked my brothers to give us some time and my dad had already headed to bed."
    mina "She began everything by talking about my choices and how she thinks they were wrong."
    mina "I let her finish and I asked her if she ever regretted a choice."
    mina "I told her that I took my choices knowing that they might cost me better things."
    mina "I still do not reget them."
    mina "She opened up about the things she gave up in her life."
    mina "Painting, promotions, even driving."
    mina "She said that she always picked the safest options and it made sense to her."
    mina "But at the same time she felt regret."
    show mina remembering
    mina "I think we ended up agreeing to support each other's crazy decisions more than the safe ones."
    mina "Which made sense then but I think it shouldn't apply to every decision."
    mina "However, I remember now that she went back to painting and she got her driving license after she retired."
    mina "I was very happy for her!"
    mina "Thank you for the meal!"
    jump Ending_Mina

label FoodOptions2_Koshary:
    $ talkedAboutBrotherOlder = True
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "Koshary, a really messy dish! "
    extend "But it's exciting!"
    mina "When I was younger, I used to eat it every Friday after church."
    if MentionedOlderBrotherName:
        mina "Thomas, my older brother, always tagged along."
    else:
        mina "My older brother, always tagged along."
        mina "His name is Thomas, by the way."
    mina "My younger brother, David, didn't like it at all."
    mina "It's too much for the stomach to handle."
    mina "I'm sure you know, chef."
    "You don't know."
    "That doesn't stop you from making the best Koshary dish"
    mina "I can't wait to taste this one"
    mina "Something about Koshary in Egypt, you just never know what you'll get at each place."
    mina "It always tasted a little different at every place that made it."
    mina "Even the same chain of restaurants."
    play sound cooking volume 1.0
    "You prepare the pasta, lentils, rice, chickpeas and salsa."
    "-and of course the fry the onions."
    show mina sigh
    if talkedAboutFather:
        mina "He was of course gentler than dad in many ways."
        mina "But he still tried to make sense of dad's control over us."
    if talkedAboutMother:
        mina "He wasn't telling us he was disappointed."
        mina "But he was always silent when mom did that."
    mina "It felt like he thought he was the guardian of his younger siblings."
    mina "But in reality it felt like he was a lieutenant to the parents."
    play sound plate volume 1.0
    "Koshary is finally done!"
    "You put everything in one dish."
    show mina neutral
    mina "Let's dive in!"
    "Mina grabs the dish and starts eating."
    mina "Heyy!"
    show mina remembering
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaFreeHarmony")
    mina "It was at some time of the year when we were fasting"
    extend "-only eating vegetarian food."
    mina "Thomas visited me at my new home to say hi."
    mina "He asked to take me out for Koshary."
    mina "We went out to one of the good Koshary places."
    mina "\"Mina,\" he said, \"I want to apologize.\""
    mina "I wondered what he meant with that."
    mina "Turns out he felt guilty for all the time of us at home."
    mina "He says he should have been a better brother."
    mina "\"Are you doing this again?\" I asked. "
    extend "\"You're being hard on yourself again.\""
    mina "I told him that me and David already knew that he was as hard on himself as he was on us."
    mina "I said that we were waiting for him to realize it. We thought that since we did he should've already done it."
    mina "\"I think in a way I'm the youngest then,\" he said."
    mina "He wasn't."
    mina "But I agreed cause I wanted him to feel good!"
    mina "To be fair, David told me that about Thomas but I didn't believe it."
    mina "I only believed it when I heard it from him and I'm glad I did."
    mina "Thank you for the meal!"
    jump Ending_Mina

label Ending_Mina:
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")

    show mina neutral
    mina "I think that's it huh?"
    mina "I don't think I figured out where we are still."
    show mina relaxed
    mina "But I'm glad I ran into you."
    mina "I hope I wasn't rambling for too long. For some reason, I just feel like opening up about my life."
    mina "I never got to hear your story."
    mina "Maybe let's take it from now and move backwards, how did you get here?"
    "..."
    show mina neutral
    mina "Wait, why did you get here might be more important."
    mina "This place seems so far from the city, are you sure this is good for business?"
    mina "It's a little odd of me asking this, but what is the city in the back?"
    mina "My head is so foggy, I can't remember how the day even started today."
    show mina sigh
    mina "Hey...I keep getting these flashes of a farm."
    mina "It's weird though, I see people that look like my family but they're much younger."
    mina "..."
    show mina remembering
    $ renpy.music.set_volume(1.0, 0.0, channel="minaDrums")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyMelody")
    $ renpy.music.set_volume(1.0, 0.0, channel="minaHappyHarmony")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeMelody")
    $ renpy.music.set_volume(0.0, 0.0, channel="minaFreeHarmony")
    mina "They're my kids! And my grandkids!"
    mina "You're saying I lived long enough to meet all of them."
    mina "I had a farm and I grew old in it with my loved ones."
    show mina sigh
    mina "I made sure I didn't repeat my same mistakes or the mistakes my family has done."
    show mina neutral
    mina "I made new ones."
    show mina relaxed
    mina "Thank you for showing me my life."
    mina "I went out surrounded by love and understanding."
    mina "Whatever your job is, you're doing great."
    "He smiles and closes his eyes."
    if perfectPlaceperfectTime:
        mina "Perfect place, perfect time."

    hide mina
    with dissolve

    "His form fades away until there is nothing left."

    $ renpy.music.stop(channel="minaDrums", fadeout=1.0)
    $ renpy.music.stop(channel="minaHappyMelody", fadeout=1.0)
    $ renpy.music.stop(channel="minaFreeMelody", fadeout=1.0)
    $ renpy.music.stop(channel="minaHappyHarmony", fadeout=1.0)
    $ renpy.music.stop(channel="minaFreeHarmony", fadeout=1.0)

    return
