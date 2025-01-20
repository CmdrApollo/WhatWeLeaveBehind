label chapter_2:
    # Akari comes to Ren with a proposition to help Kano
    # Ren eventually agrees to help her out
    call chapter_2_scene_1
    call chapter_2_scene_2

    return

label chapter_2_scene_1:
    "Chapter 2, Scene 1"

    scene black with long_dissolve
    return

label chapter_2_scene_2:
    # Ren and Akari talk about Kano
    # Ren decides to help Akari

    "Chapter 2, Scene 2"
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