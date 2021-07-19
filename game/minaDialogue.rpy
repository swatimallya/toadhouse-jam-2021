#Mina Section
define mina = Character('Mina', color="#ffffff")
define unknown = Character('????', color="#ffffff")

define talkedAboutFather = False
define talkedAboutMother = False
define talkedAboutBrotherOlder = False
define talkedAboutBrotherYounger = False

define MentionedOlderBrotherName = False

define finishedMintTea = False
define finishedBeer = False

#-----mina art----
#mina neutral
#mina relaxed
#mina sigh
#mina remembering

#-----sfx------
#kettle audio ringing?
#tea pouring

label startMina:
    "Another customers emerges from the shadow.."
    "He seems to be a little confused."
menu:
    "Invite him over":
        show mina neutral
        jump friendlyMina
    "Wait for him to come":
        show mina neutral
        jump realxedMina

label friendlyMina:
    unknown "Hi there, you're parked way out in the middle of no where"
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
    "Molokheya and Rice":
        jump Starter_MRice_Mina
    "Tea with mint":
        jump Start_MTea_Mina
    "Beer":
        jump Start_Beer_Mina

#if (Molokheya and rice) is selected as the first choice! (More info about the mom) and also, Mina won't accept it.
label Starter_MRice_Mina:
    mina "Oh, we're going in for the food already?"
    mina "You know, I'm gonna ask you to push that back a little."
    mina "This dish reminds me a lot of my mother, she used to make the best Molokheya I ever tasted."
    mina "And rice to be frank."
    mina "I sometimes got it from restaurants because I would hang out with friends."
    mina "But none of these ones tasted as good as the one at home."
menu:
    "Offer a different starter":
        mina "Oh, yeah. Time for the starter!"
        jump Starters1_Again_Mina
    "...":
        mina "She always found something she didn't like about the food she made."
        mina "I think I learned to be hard on myself just observing her"
        mina "but whenever I notice myself doing that, I stop."
menu:
    "Offer a different starter":
        jump Starters1_Again_Mina
    "...":
        $ talkedAboutMother = True
        mina "When I was still living with my parents, I remember feeling a lot of extra pressure"
        mina "Most of it was because they were very vocal of their expecations of me or my brothers."
        mina "My mother wasn't \"vocal\" in her own way. She used to have this look that made me feel like a disappointment."
        "mina sighs.."
        mina "Anyway"
        mina "So what do you have for me to start with?"
        jump Starters1_Again_Mina

#After "Molokheya and rice" is rejected
label Starters1_Again_Mina:
    "Remind me again what can I have?"
menu:
    "Tea with mint":
        jump Start1_MTea_Mina
    "Beer":
        jump Start1_Beer_Mina

#if Mint tea was selected as the first choice! (More info about the dad)
label Start_MTea_Mina:
    mina "Oh! We're starting with mint tea!"
    mina "I know a lot of people who grew mint at their home to have it as fresh as possible!"
    #Talks about the dad and their problem together
    mina "You know, "
    extend "my father used to pick fresh mint from a small garden outside of his workplace" #extend is a built in character that is supposed to continue on the last line with the same character as above.
    show mina sigh
    mina "He always had to make sure everything was done right."
    mina "even a cup of tea with some mint"
    mina "It had to be the exact amount of sugar, the exact amount of tea "
    extend "and of course the exact amount of mint."
menu:
    "Prepare the tea":
        jump MTea_Mina
    "...":
        $ talkedAboutFather = True
        "You say nothing and let Mina continue."
        mina "It felt like he wanted to control everything"
        mina "My older brother, Thomas, was always on his side"
        $ MentionedOlderBrotherName = True
        mina "It only seemed to have bothered me though."
        mina "Dad was always proud of him the most, even though he always said to his friends that I'm too much like him"
        mina "It bothered me a lot knowing that he found us similar"
        mina "I was either as controlling as I saw him, or he didn't see himself the way I saw him"
        mina "Well we both liked mint tea the same way that's for sure"
        jump MTea_Mina

#if mint tea was not selected as the first choice!
label Start1_MTea_Mina:
    mina "Mint tea! sounds good!"
    jump MTea_Mina

#This happens either way since Mina won't reject it if chosen first or later.
label MTea_Mina:
    "You bring out a kettle already filled with water and you place it on the stove" #heater??
    mina "Oh!"
    show mina remembering
    "Mina seems to have remembered something!"
    mina "That's how I used to drink it at home!"
    mina "We had the electric kettle but we used to make tea old school on the stove" #oven????
    #remembers the resolution to him and his dad's conflict
    if talkedAboutFather:
        mina "By we I mean me and my dad"
        mina "This was probably the only time of the day when we didn't fight at all"
        mina "Well, maybe we fought a little bit at the begining when I was learning, but after I got the hang of it I made the best tea for us"
    mina "You know, I had Mint tea served at my wedding because I knew it was dad's favorite thing to drink"
    mina "Even then though, dad didn't enjoy the tea that much"
    mina "I remember him saying it wasn't the best he'd had"
    #sfx kettle audio ringing?
    "The kettle is ready, you turn off the stove."
    #sfx tea pouring
    "You pour the water into the cup and stir the tea and add the mint."
    mina "yum! smells great!"
    "You present the cup to Mina"
    "He takes a sip"
    "..."
    mina "Hold on!"
    show mina remembering
    extend "I remember!"
    mina "The night before the wedding! Dad came over to my house and we stayed in the garden outside."
    mina "There was a cool breeze, the stars were beautiful and we were sitting on pop up chairs"
    mina "I had the kettle we used to have when I was younger, it looks like this one you have here."
    if talkedAboutFather:
        mina "At home, we had a spot we preferred on the stove"
    mina "I started a small fire- made sure it was safe, of course"
    mina "And we made tea while we talked about our lives up to that point"
    mina "He said he missed me, I had been living in a different city for a few years by then"
    if talkedAboutFather:
        mina "\"Mina,\" He said, \"I realized I was too hard to deal with too late\""
    mina "He felt like a different person then, and whatever I felt was difficult between us just faded away"
    show mina relaxed
    "Mina takes a deep breath"
    mina "I also said sorry about being mean sometimes too"
    mina "The kettle was whistling too high by then,"
    mina "\"Oh no!\" I said, "
    extend "\"the mint! We don't have mint!\""
    mina "He had mint in his pocket for God knows how long"
    mina "We laughed about it and thought it would probably be expired or gone bad by then but we added it to the tea anyway"
    mina "At the wedding the next day"
    mina "When he told me that the mint tea wasn't the best"
    mina "He said that the best one he had ever had was that night before"
    mina "I am glad we talked about these things"
    "Mina smiles at you"
    mina "I am glad your tea reminded me of that!"
    $ finishedMintTea = True
    jump FoodOptions2_Mina

label Start_Beer_Mina:
    $ talkedAboutBrotherYounger = True
    mina "Oh, beer, I'm down!"
    mina "But can I ask you something because I can't tell"
    mina "I notice the sky is dark but are we closer to midnight or to the next morning?"
menu:
    "Shrug":
        mina "Oh you don't know too?"
        show mina sigh
        mina "hmm"
        jump Start_Beer_Mina_2
    "...":
        mina "You really are keeping the mystery alive, Chef"
        mina "I'll drink either way"
        jump Start_Beer_Mina_2

label Start_Beer_Mina_2:
    show mina relaxed
    "Mina looks at the sky and he seems to have something on his mind"
    mina "My younger brother, David, and I used to drink together more than our older brother"
    mina "He used to do crazy things when we were all living in the same house and he rarely got in trouble"
    mina "I did less crazy things and I always got in trouble"
    mina "I always asked him to be more responsible but he never listened"
    mina "I tried to cover for him some times but I don't think he noticed"
    jump Beer_Mina

label Start1_Beer_Mina:
    mina "Beer it is then!"
    jump Beer_Mina

label Beer_Mina:
    "You grab a really big mug from under the counter"
    mina "wow"
    "You start pouring the beer from the barrel inside the cart"
    mina "So, why won't you have one too while you're at it?"
    "..."
    mina "Alright!"
    "You present the mug to Mina"
    "He grabs it and chugs it all in one go!"
    mina "Heyy!"
    show mina remembering
    mina "I remember something!"
    if talkedAboutBrotherYounger:
        mina "David! "
    else:
        mina "My younger brother! "
    extend "When I was moving to a different city, we stayed up the whole night before in the balcony"
    mina "I think I was quicker to get tipsy"
    mina "I remember we never shouted but our conversation got intense"
    mina "I was out of line but I asked him to be more responsible when I leave"
    mina "He asked me what I meant and I think I said things I didn't think through"
    mina "He told me that out of me and our older brother I was more like dad"
    show mina sigh
    mina "..."
    mina "I didn't like that"
    mina "I think me and him had the same issues with dad, he was too distant and acted like he knew us"
    mina "I realized that I did the same thing with him"
    mina "I immediately apologized!"
    mina "I explained to him the way I saw it in my head and how I felt that I had to take care of him"
    mina "And how I thought I was protecting him from the rest of the family because "
    extend "I saw the \"real\" them"
    if talkedAboutBrotherYounger:
        mina "But I realized David was always doing better than me mentally"
        mina "I had to ask him what his secret was"
    mina "He told me I didn't have to do all these mental gymnastics"
    mina "\"You spent too much time worrying about me\" He said"
    mina "\"Worrying about everyon else but you\""
    mina "\"Whatever you were doing to pretend they weren't also a part of my life\" He said"
    mina "\"It only made you another character I had to find a way around\""
    mina "He said that he noticed all the small things about the rest of the family"
    mina "And he gave them what they wanted"
    mina "He said I needed to feel like I was in control just like dad"
    mina "But sometimes I needed to feel the opposite of that"
    mina "For some reason, David seemed to have developed a very flexible character"
    mina "He didn't lie to anyone about who he was but he knew what we needed and gave it to us"
    mina "I learned a lot on that day"
    mina "I started watching my behaviour and focusing on the people around me and tried not to be a heavy weight on their hearts"
    show mina neutral
    mina "So Chef, what do you have next?"
    jump FoodOptions2_Mina

label FoodOptions2_Mina:
"What would you offer Mina?"
menu:
    "Molokheya and Rice":
        jump FoodOptions2_MolokheyaAndRice
    "Koshary":
        jump FoodOptions2_Koshary

label FoodOptions2_MolokheyaAndRice:
    jump Ending_Mina

label FoodOptions2_Koshary:
    jump Ending_Mina

label Ending_Mina:
    return