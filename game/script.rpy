# The script of the game goes in this file.

define r = Character("Ren", color="#ffc080")
define a = Character("Akari", color="#80ffc0")
define k = Character("Kano", color="#ff8080")

define t = Character("Mr. Takahashi", color="#c0ff80")
define d = Character("Dad", color="#c080ff")
define m = Character("Mom", color="#ffff80")

define short_dissolve = Dissolve(0.5)
define long_dissolve = Dissolve(1.0)

label splashscreen:
    scene black
    with Pause(1)

    show text "Two-Way Studios Presents..." with long_dissolve
    with Pause(2)

    hide text with long_dissolve
    with Pause(1)

    return

label show_title:
    scene black
    with Pause(1)

    show text "[title]" with long_dissolve
    with Pause(2)

    hide text with long_dissolve
    with Pause(1)

    return

label start:
    $ title = "Chapter 1: Familiar Faces"
    call show_title
    call chapter_1
    $ title = "Chapter 2: Down to Business"
    call show_title
    call chapter_2

    return