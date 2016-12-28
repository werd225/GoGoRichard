# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image bg street = "sch street.png"

image bg living = "living room.png"

image bg school = "sch ground.png"

image bg pro = "prologue.png"

image bg pend = "pend.png"

image bg act1 = "act1.png"

image bg 1end = "1end.png"

image bg act2 = "act2.png"

image bg 2end = "2end.png"

image bg vue = "cinema.png"

image bg bog = "toilet.png"

image yng akeem = "true young akeem.png"

image teen akeem = "young akeem.png"

image yng dan = "young dan.png"

image teen dan = "teen dan.png"

define r = Character("Richard")

define f = Character ("Father")

define m = Character ("Mother")

define ir = Character ("Inner Richard")

define a = Character ("Akeem")

define d = Character ("Daniel")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    scene bg pro


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    

    # These display lines of dialogue.

    "Greetings! This is the story of a gallant young chap called Richard and the trials and tribulations he faces."
    
    "Go!Go! Richard - Prologue: The hollowed shell of an oreo"
    
    scene bg room

    r "Ok Richard you can do this, first day of high school it'll be just like any other bog standard day."

    r "Hmmmm. I wonder if father remembered to put the dough in the bread maker, I do quite enjoy those poppy seed bagels for my sandwich!"
    
    r "{i}I should probably wash up, don't want to stir up a stink on my first day.{/i}"
    
    r "{i}I finish washing up and preparing for school.{/i}" 
    
    r "{i}I head downstairs and enjoy a delightful breakfast with my family as we watch the morning news.{/i}"
    
    scene bg living
    
    r "Well Father, Mother, I best be off wouldn't want to be late on my first day."
    
    f "Quite right Richard my boy, Wouldn't want you to fluff your first day."
    
    m "Goodbye Richy! Enjoy your day and remember to make plenty of friends."
    
    r "{i}I step out and meet with Charlotte from across the street and we make our way to Hellthorne Park.{/i}"
    
    scene bg street
    
    r "How was your summer Charlotte?"
    
    r "{i}And so we engaged in tales of our summer vacations. I told Charlotte about the delightful carbonara I had that one night in the cabin in the alps.{/i}"
    
    r "{i}I couldn't have known at the time, but this chance encounter wouldn't be the last with this odd fellow.{/i}"
    
    "{b}CRASH{/b}"
    
    show yng akeem
    
    r "Oh I'm quiet sorry I didn't see you there chap you ok?"
    
    r "{i}He's just standing there shifting between eye contact and looking behind me{/i}"
    
    r "...Hello?"
    
    a "I'm fine. Sorry"
    
    r "My name is Richard, yours?"
    
    a "..."
    
    r "{i}He looks baffled{/i}"
    
    a "Ask not the sparrow how an eagle soars"
    
    hide yng akeem
    
    r "{i}And just as suddenly as he appeared he was gone.{/i}"
    
    r "Well that was most certainly not a bog standard occurrence."
    
    "You go to the assembly hall and sit through an introductory speech, delivered by the headmaster, with a skewed sense of enthusiasm and duty."
    
    "After completing your morning classes and getting to know some classmates you head to the office to collect your locker key."
    
    scene bg school
    
    r "Alright, it says here my locker is D20."
    
    a "D20 did you say?"
    
    r "{i}A monotonous voice that fills me with grief emanates from beside me. I recognise that voice.{/i}"
    
    show yng akeem
    
    a "I got D19, I guess that makes us locker buds."
    
    r "Oh hey, it's you! The guy from earlier!"
    
    a "My name is Akeem."
    
    r "My name is-"

    a "Richard? Right? I remember you told me earlier and then I heard it again in class while Mr Sery took the register."
    
    r "{i}He's still just shifting between eye contact and looking behind me. He sounds so bored, is something wrong with him?{/i}"

    r "Uh yes, quite right old chap-"
    
    hide yng akeem

    r "Where did he go?"
    
    r "{i}If only I knew the significance of this encounter and how it would change the course of my bog standard life.{/i}"
    
    scene bg pend
    
    "End of prologue!"
    
    $ renpy.movie_cutscene ("AABA.mp4")
    
    #Start of act 1
    
    scene bg act1
    
    "Act 1 - This is the Droid you're looking for!"
    
    scene bg room
    
    "Months had passed at Hellthorne park and Richard was finally settling in, even making a few friends in the process."
    
    scene bg living
    
    "The odd fellow from before, who he only knew as Akeem, was a part of his form but they didn’t have many interactions after that."
    
    scene bg street
    
    "Whenever he did see him he would always have his face buried in a book, reading, a trait of his that can easily be overlooked."
    
    scene bg school
    
    "Reuben" "Alright mates you want to play a bit of blocky 123 like we did back in new zeaaaallaaaand?"
    
    r "Blocky 123?"
    
    show yng dan
    
    d "Well technically here in london we call it forty forty, but yeah sure I’m up for some forty forty! Richard?"
    
    r "Ah of course forty forty, I’m down for a few games sure!"
    
    "Reuben" "Goooooody mates. Dayniel you start!!!"
    
    "And so our average sized hero Richard formed bonds, that would last indefinitely, with a fellow he wasn’t sure was human or robot."
    
    "All he knew was that he would always claim to be right."
    
    hide yng dan
    
    scene bg 1end
    
    "Act 1: Completed"
    
    #Start of act 2
    
    scene bg act2
    
    "Act 2 - Filling the oreo"
    
    scene bg school
    
    "It's been a year since I've joined Hellthorne park and things have been going well. I've made quite a few friends and to quote Reuben 'We enjoy a bit of blocky 123' every break."
    
    "However this lunch time would be different."
    
    show yng akeem at right
    
    a "Hey are you guys playing 40/40?"
    
    r "Yeah!"
    
    r "{i}Wait that's him again! The voice that fills you with dread while also not giving away any emotion.{/i}"
    
    r "Do you want to join?"
    
    a "Yeah sure."
    
    r "{i}He still sounds so bored, maybe its fatigue, however for a brief moment I think I saw a smile.{/i}"
    
    r "This is Daniel, Reuben and Charlotte!"
    
    hide yng akeem
    
    show yng dan
    
    d "Hi, nice to meet you! You can call me Dan"
    
    "sid" "Danier..."
    
    hide yng dan
    
    "Reuben" "Gooodyy another boy to play with!!!"
    
    menu:
        "(Give Reuben a look and ignore it for now)":
            jump choice1_yes
            
        "You might want to rephrase that Reuben":
            jump choice1_no
            
    label choice1_yes:
        
        scene bg bog
        
        "Reuben" "Why don't I show you how we play in new zealand?" 
        
        "Reuben" "Richard?"
        
        "Reuben grabs me by the arm and drags me off to the toilet." 
        
        r "{i}He's staring intensely into my eyes and so I reciprocate.{/i}"
        
        r "I'm just noticing now Reuben but your eyes are a pale blue. Like a clear summer sky."
        
        "Reuben" "It's always a clear sky in new zeaaalllland"
        
        r "{i}We link our hands and slowly our faces are drawn to eachother.{/i}"  
        
        r "{i}We start with a small peck but each time we go in our lips stay locked together for longer until we're fully engrossed in exchaning saliva.{/i}"
        
        "We spend around ten minutes in there, the heat of our passion was enough to make the sun envy us."
        
        "I could tell neither of us wanted this moment to end, but it was outside the realm of man to freeze a single moment in time."
        
        r "We should go back Reuben. Our love is like a candle burning in the wind. Too bright and too hot for this world."
        
        "Reuben" "Lets promise to do more goody goody down the road, Richard!!!"
        
        "And so we returned and continued from the exact point we had left off at."
        
        "That single memory lost to the merciless flow of time, evergoing and indifferent to the struggles and feelings of man."
        
        jump choice1_done
        
    label choice1_no:
        
        scene bg bog
        
        "Reuben storms towards me and grabs me by the arm, dragging me away as the others look on in slight confusion and indifference." 
        
        "We end up in the C block toilet which is rarely visited by anyone and he places me inside a cubicle."
        
        r "Unhand me at once you savage"
        
        "Reuben" "Why don't I show you just how savage a kiwi can be mate."
        
        r "{i}What kind of situation is this. How did I end up here.{/i}"
        
        "I look on in horror as my body refuses to obey me and move at my command, as Reuben undresses himself before me." 
        
        "The boy I once viewed as nothing more but a tiny kiwi, chirping in the presence of lions an animal suited to my british heritage, was now violating me."
        
        "He was relentless with his exploration of my body, groping anything he could fit his hand around."
        
        r "Please, stop! Unhand me at once."
        
        "Reuben" "Now let's make our way back and have fun with the others mate. Perhaps a game of Blocky 123?"
        
        r "{i}And that's all that was said on the matter. As if he were taunting me, my very existence.{/i}"
        
        jump choice1_done
        
    label choice1_done:
        
    scene bg school    
    
    show yng akeem
    
    a "Hello, My name is Akeem."
    
    r "{i}He's looking over each one of us. It's unsettling, almost as if we were frogs caught in the glare of a snake.{/i}"
    
    r "{i}His line of sight returns back to the ground and he starts talking.{/i}"
    
    a "She has grey eyes."
    
    "Charlotte" "Shut up."
    
    "And so with that the strange negro, I had met on my first day here at Hellthorne, had become a regular part of my bog standard life."
    
    "How this would play out was yet to be seen, but for now we'd all much rather enjoy our time as care-free adolescents."
    
    hide yng akeem
    
    scene bg room
    
    show teen dan at right
    
    "It had been a couple years since I met Akeem and Daniel." 
    
    "As the days went by we spent more time together outside of school."
    
    "It wouldn't be strange for us to walk back to my house together and play yu-gi-oh or watch trending youtube videos on my iPod."
    
    hide teen dan
    
    scene bg vue
    
    show teen akeem
    
    "We would even arrange for outings to the cinema inside our little group." 
    
    "Or even arrange sleepovers spent playing party games late into the night."
    
    hide teen akeem
    
    scene bg 2end
    
    "Act 2: Completed"
    
    #start of act 3
    
    "Act 3: Start"
    
    
    
    
    

    
    
    
    

    # This ends the game.

    return
