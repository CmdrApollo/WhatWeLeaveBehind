label chapter_1:
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

    "When you arrive in town, memories come flooding back to you, good and bad."

    show black with long_dissolve
    return

label chapter_1_scene_3:
    "Chapter 1, Scene 3"

    show black with long_dissolve
    return

label chapter_1_scene_4:
    "Chapter 1, Scene 4"

    show black with long_dissolve
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