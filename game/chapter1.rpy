label chapter_1:
    # Ren arrives in town and begins to help with renovations
    # He meets up with long time friend Akari and they begin
    # to rekindle their relationship
    call chapter_1_scene_1
    call chapter_1_scene_2
    call chapter_1_scene_3

    return

label chapter_1_scene_1:
    # Ren wakes up in the car and speaks with his dad.

    "Chapter 1, Scene 1"

    scene black with long_dissolve

    d "Hey."
    d "Wake up, sleepy head, we're almost there."

    "You stir as he reaches over and shakes you gently."

    "Open your eyes?"

    menu:
        "Yes.":
            pass
        "Not yet.":
            "You decide to bask in the moment for a little while longer."

    scene train with long_dissolve

    "When you open your eyes, you find yourself in a fairly empty train car, rattling along the tracks per usual."
    "Earlier in the day, your dad met you at the airport. You are [r], a college student traveling home for the summer to your quaint hometown that seemingly inhabits the middle of nowhere."
    "Apparently, you fell asleep on the ride there, which you didn't anticipate. However, you suppose that you needed the rest and shrug it off."

    r "How much longer?"

    d "I'd say 5 minutes or so."

    r "Ok..."

    d "So are you ready to help out with renovations?"

    r "Of course."

    "Your grandmother recently passed and left behind an old,  that she cherished for many years. It was her pride and joy. It seemed as if her very soul still lived within that inn. However, after all the years of wear and tear, the inn was worse for wear."
    "And so, your family has decided to renovate the inn in order to keep her memory alive and to continue on their family business. Since you'll be home for the summer, you've been recruited to help as well."

    r "How've you and [m] been?"

    d "Well, you know. We've been well, we just missed having you around."

    r "Yeah..."

    r "[a] and [k]?"

    d "We've seen [a] around here and there but [k] still seems to be shut away all the time. Poor kid..."

    scene black with long_dissolve
    return

label chapter_1_scene_2:
    # Ren and dad arrive in town (at the inn), speak with family
    # Ren runs into Akari helping out to renovate the inn, speaks
    # with her

    "Chapter 1, Scene 2"

    scene street with long_dissolve

    r "I can't even remember how long it's been..."
    
    "When you arrive in town, memories come flooding back to you, both good and bad."

    "You make your way to the inn with your dad. It seems that work is starting early for you."
    "{i}At least{/i}, you think, {i}I'll have some time with family where I don't have to worry about everything else.{/i}"

    scene diner with long_dissolve

    "When you enter the inn, you immediately spot your mom."

    
    show mom with short_dissolve:
        subpixel True zoom 0.75
        pos (300, 115)

    m "Hey honey! I missed you so much!"

    r "Hey, [m]! I missed you too. How've you been?"

    m "Your father and I have been hanging in there. You know it's been hard since grandma passed away, but we're managing. How about you, sweetie?"

    r "I've been well! Just same old same old, you know?"

    m "I hear you there!"

    hide mom with short_dissolve

    "You notice someone in the corner."

    r "[a]! What are you doing here?"

    show akari with short_dissolve:
        subpixel True zoom 0.75
        pos (540, 115)

    a "Hey [r]! It's been so long! Your family asked me to help out with the renovations, and I thought that I should be here when you came!"

    r "I'm so happy to see you! How have you been?"

    a "I've been good! School's been taking up most of my time, but I'm really glad I decided to come help out for the summer. I made so many memories here..."

    r "We all did."

    a "Yeah..."

    r "Well..."
    r "I have to go put my stuff away."
    r "I have a lot of stuff to check on first, but would you like to talk more later?"
    
    a "Yeah, I'd love that. Did you want to meet..."
    
    r "At the usual spot?"

    a "That would be perfect. I'll see you later..."
    a "And [r]?"

    r "Yeah?"

    a "I missed you."

    r "I missed you too."

    scene black with long_dissolve
    return

label chapter_1_scene_3:
    # Ren and Akari meet up in the forest where they used to hang out
    # as children, they have a sweet moment before the topic turns
    # to the incident that occured when they were children and the
    # conversation turns sour.

    "Chapter 1, Scene 3"
    
    scene temple with long_dissolve

    "As you walk towards the abandoned temple, you spot a lone figure in the shadows. It's [a]."

    show akari with short_dissolve:
        subpixel True zoom 0.75
        pos (540, 115)

    a "Oh hey, you finally came."

    r "Yeah... sorry about the wait."

    a "No worries."

    "You take a seat on the ground next to her, enjoying the subtle warmth of her body against the crisp autumn air."

    r "So how have you been, really?"

    a "Well... you know..."

    "She gives a weak smile."

    a "Things have been tough... Y'know with [k] how he is and everything. I've been trying so hard to get him back on track but it seems like nothing I do is working."
    
    r "I'm sorry to hear that. You know that I'll always be here for you, right?"

    a "Of course."

    r "How are you handling everything?"

    a "Alright I suppose. Sobriety's been kicking my ass lately though."

    r "At least you're trying"

    "You turn and give her a small hug."

    r "I'm proud of you, [a]. I really am."

    a "Thank you. It's taken a lot for me to get this far and I'm just glad to have made it... no matter what happened before."

    r "Yeah... poor [k]. I can't even imagine how tough that was for him..."

    a "I'd rather not talk about it any more."

    "She turns away sheepishly."

    r "Alright, alright. Sorry about that."

    a "It's fine."

    "It's clear to you that it isn't."

    "After a few more minutes spent cozied up in the piercing silence, you decide that it's time to head out."

    r "Should we get going? It's getting pretty cold out here."

    a "Yeah... Let's head out."

    scene black with long_dissolve
    return