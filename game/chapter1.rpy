label chapter_1:
    # Ren arrives in town and begins to help with renovations
    # Akari comes to him with a proposal to help Kano, their
    # long time friend. Ren eventually accepts her offer.
    call chapter_1_scene_1
    call chapter_1_scene_2
    call chapter_1_scene_3
    call chapter_1_scene_4
    call chapter_1_scene_5

    return

label chapter_1_scene_1:
    # Ren wakes up in the car and speaks with his dad.

    "Chapter 1, Scene 1"

    show black with long_dissolve

    d "Hey."
    d "Wake up, sleepy head, we're almost there."

    "You stir as he reaches over and shakes you gently."

    "Open your eyes?"

    menu:
        "Yes.":
            pass
        "Not yet.":
            "You decide to bask in the moment for a little while longer."

    scene bg_carride with long_dissolve

    "When you open your eyes, you find yourself in your family's Station-Wagon. It's a familiar car that brings back a lot of memories for you. The interior smells subtly of pine resin, a common scent where you're headed."
    "Earlier in the day, your dad picked you up from the airport. You are [r], a college student traveling home for the summer to your quaint hometown that seemingly inhabits the middle of nowhere."
    "Apparently, you fell asleep in the car, which you didn't anticipate. However, you suppose that you needed the rest and shrug it off."

    r "How much longer?"

    d "I'd say 5 minutes or so."

    r "Ok..."

    d "So are you ready to help out with renovations?"

    r "Of course."

    "Your grandmother recently passed and left behind an old inn that she cherished for many years. It was her pride and joy. It seemed as if her very soul still lived within that inn. However, after all the years of wear and tear, the inn was worse for wear."
    "And so, your family has decided to renovate the inn in order to keep her memory alive and to continue on their family business. Since you'll be home for the summer, you've been recruited to help as well."

    r "How've you and [m] been?"

    d "Well, you know. We've been well, we just missed having you around."

    r "Yeah..."

    r "[a] and [k]?"

    d "We've seen [a] around here and there but [k] still seems to be shut away all the time. Poor kid..."

    show black with long_dissolve
    return

label chapter_1_scene_2:
    # Ren and dad arrive in town (at the inn), speak with family
    # Ren runs into Akari helping out to renovate the inn, speaks
    # with her

    # TODO Inn asset

    "Chapter 1, Scene 2"

    r "I can't even remember how long it's been..."
    
    "When you arrive in town, memories come flooding back to you, good and bad."

    scene room_inn with long_dissolve

    "When you enter the inn, you immediately spot your mom."

    show mom with short_dissolve

    m "Hey honey! I missed you so much!"

    r "Hey, [m]! I missed you too. How've you been?"

    m "Your father and I have been hanging in there. You know it's been hard since grandma passed away, but we're managing. How about you, sweetie?"

    r "I've been well! Just same old same old, you know?"

    m "I hear you there!"

    hide mom with short_dissolve

    "You notice someone in the corner."

    r "[a]! What are you doing here?"

    show akari with short_dissolve

    a "Hey [r]! It's been so long! Your family asked me to help out with the renovations, and I thought that I should be here when you came!"

    r "I'm so happy to see you! How have you been?"

    a "I've been good! School's been taking up most of my time, but I'm really glad I decided to come help out for the summer. I made so many memories here..."

    r "We all did."

    a "Yeah..."

    r "Well, we should talk more sometime soon!"

    a "Sounds good! Does tonight work?"
    
    r "Sure thing. Usual spot?"

    a "Sure."

    scene black with long_dissolve
    return

label chapter_1_scene_3:
    # Ren and Akari meet up in the forest where they used to hang out
    # as children, they have a sweet moment before the topic turns
    # to the incident that occured when they were children and the
    # conversation turns sour.

    # TODO Forest asset

    "Chapter 1, Scene 3"
    
    scene bg_forest with long_dissolve

    "As you walk towards the abandoned bench in the clearing in the forest, you spot a lone figure situated upon it. It's [a]."

    show akari with short_dissolve

    a "Oh hey, you finally came."

    r "Yeah... sorry about the wait."

    a "No worries."

    scene black with long_dissolve
    return

label chapter_1_scene_4:
    "Chapter 1, Scene 4"

    scene black with long_dissolve
    return

label chapter_1_scene_5:
    # Ren and Akari talk about Kano
    # Ren decides to help Akari

    "Chapter 1, Scene 5"
    scene room_background with long_dissolve

    show akari with short_dissolve

    r "I don't know, [a]."

    a "What's not to know?"
    
    r "I came back for my family... I just don't know if I can do this."
    r "I haven't talked to [k] in years... I don't know what he's going through. I doubt I'll even be able to get through to him."

    a "But it's worth trying."
    a "He's still your friend, you know."

    r "Yeah. I know."
    r "It's just that ever since... you know... he just hasn't been the same."

    a "I know. Which is why we're trying to help him."
    a "He {i}needs{/i} our help, [r]."

    r "Alright... I guess you're right. But I just don't know if I can do this."
    r "Right now I need to focus on helping out my family. That's what I came here for."

    a "I know, [r], but [k] also needs our help, and now that you're here, maybe he'll listen to you."
    a "I've tried to help him on my own for years and I can never seem to get through to him, but you two had something special, and I'm willing to bet that you can get through to him where I can't."

    r "Maybe..."
    r "..."
    r "Alright. I'll help you, but I need to focus on my family first, got it?"

    a "Got it. Now let's go get something to eat, I'm starving."

    scene black with long_dissolve
    return