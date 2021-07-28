define death = Character(_("Death"), color="6B8E23")

define likedTheJob = False

#-----death art----
#death neutral
#death smug

#Death has done this many times before. 
#Death knows the chef's past
#It's their job to take souls to the other side and they give as much time as possible to the dead.
#Death is giving the chef something they need to find closure just how the chef was giving the customers

label death_ending:
    "What now?"
    "You check to see if there are any more customers on their way to you"
    "..."
    "There isn't"
    "Uma and Mina both disappeared in front of you"
    "The memories they've regained"
    extend ", they turned out to remember they've died already"
    show death neutral
    with dissolve
    death "Hello! I see you're done already"
menu:
    "Who's next?":
        jump choices1_likeTheJob
    "I've had enough":
        jump choices1_whoIsNext

label choices1_likeTheJob:
    $ likedTheJob = True
    death "I see you like the job already"
    death "Me too"
    death "Which means a lot coming from me, you know"
    show death smug
    death "I've been doing this for eternity"
    jump theDeal

label choices1_whoIsNext:
    $ likedTheJob = False
    death "Oh"
    death "You're not having fun?"
    death "In this part of existence there is all the time in the world"
    death "I like to sit down with every person that comes here and learn about them"
    show death smug
    death "I never run out of entertainment"
menu:
    "Entertainment?":
        jump question1_entertainment

label question1_entertainment:
    death "sure"
    death "You got to see how it can go with Uma and Mina"
    death "I get to do that but imagine more people heh"
    extend "from all over the world"
    death "very entertaining"
    jump theDeal

label theDeal:
    death "Everyone is so unique"
    death "I get to hear their stories and they get to talk about their lives"
    death "Surprisingly, that's usually what they need to find closure"
    death "Enough time to feel and think about their lives and everything that surrounded them."
    death "good or bad"
    show death neutral
    death "However"
    extend ", some people need more than this to move on"
    show death smug
    death "Not everyone gets to find closure by talking"
    death "some find it by"
    extend " listening"
    show death neutral
    death "They come with..." 
    extend " unresolved situations"
    death "let's say for example, someone who is conflicted over what they believe and how they feel"
    death "\"People only want what's best for them\" and yet they themselves go out of their way to help others"
    death "And yet they run into people whom that belief doesn't apply"
    death "and for some reason, they turn their face the other way around"
    death "listening helps"
    death "looking at life through the eyes of other people helps"
    death "Don't take it from me though. I've only been doing this for.. "
    show death smug
    extend "eternity"
    death "Take it from Uma and Mina at least"
    death "Well, here's a question, chef"
    death "You've been doing a great job so far"
    show death neutral
    death "What do you think is stopping you from moving on?"
menu:
    "Does that mean I'm dead too?":
        jump question2_amIDead
    "I don't know":
        jump question2_IDK
    "I could have done more":
        jump question2_DoneMore

label question2_amIDead:
    show death smug
    death "Really?"
    death "I mean, you're here"
    death "so yes, you've also died"
    death "I'm gonna ask again hm?"
    show death neutral
    death "What do you think is stopping you from moving on?"
menu:
    "I don't know":
        jump question2_IDK
    "I could have done more":
        jump question2_DoneMore

label question2_IDK:
    death "well, then our customers today gave you something to think about"
    death "I even handpicked those two for you"
    death "maybe people aren't all bad after all"
    show death smug
    death "I mean, I know they aren't"
    jump question2_subquestion

label question2_subquestion:
menu:
    "I didn't get my moment":
        jump question2_DoneMore
    "Nod":
        jump death_conclusion

label question2_DoneMore:
    show death neutral
    death "Looking back at the past wouldn't change it"
    death "I've met a lot of people who haven't gotten moments of confrontation or clarity when they were alive"
    death "There is no best solution for that because everyone is different"
    death "But here's one thing someone told me about many years ago"
    death "They imagine themselves standing where they're at and they start zooming out"
    death "as they go further back, more things enter their view"
    death "other people that have very different lives but just as complex"
    death "animals and nature that have to deal with human's actions"
    death "They see the sea and the waves and the mountains and the clouds"
    death "and they finally get to space"
    death "All of this is just on one big blue dot"
    death "But even then, as they go further the dot begins to become smaller"
    death "The universe is big"
    show death smug
    death "That's not even counting my realm"
    show death neutral
    death "They told me that this thought made them thing that whatever they're going through, the world is still turning"
    death "and somehow that made them feel like that applies to everything"
    death "nature doesn't seem to stress over it, it keeps going"
    death "the animals, the sun, the moon and the earth are just doing what they're good at"
    death "maybe existing and experiencing whatever happened is also part of the bigger picture"
    death "Of people being people"
    death "Well, that's only one person's way of looking at it"
    death "It might not be your way and that is completely fine"
    death "That's why I'm here"
    jump death_conclusion

label death_conclusion:
    death "Now then, chef"
    death "It's your choice"
    death "Do you need more time here or are you ready to move on?"
menu:
    "I need more time":
        jump end1_Stay
    "I am ready":
        jump end2_MoveOn

label end1_Stay:
    show death neutral
    "Death takes a look at the cart and the dirty dishes"
    if likedTheJob:
        death "Let me clean that up for you"
        extend ". but don't get used to it!"
    else:
        show death smug
        death "yikes"
        death "You should clean that up"
        "You clean up the cart"
    show death smug
    death "This is just a welcoming gift"
    show death neutral
    death "As I said, we have all the time in the world"
    death "hear as many stories as you need"
    death "meet as many people as you want"
    death "cook as many dishes as you like"
    show death smug
    death "you'll be doing a fraction of my job"
    show death neutral
    death "when you feel ready, just let me know"
    show death smug
    death "or I will know when you disappear from my realm"
    show death neutral
    death "See you around, chef"
    
label end2_MoveOn:
    show death neutral
    death "I'm glad you feel this way"
    death "I can see it in your eyes, you know"
    death "People do care about each other, and about other living beings and other things"
    death "People can be open and talk things out"
    death "People can do all of those things and still do a lot of mistakes"
    death "People are people and that might not be so bad"
    show death smug
    death "At the very least"
    extend " entertaining"
    "You smile at Death"
    "They smile back at you"
    "Your form starts fading away"
    "The world around you is changing"
    "Onward you go"