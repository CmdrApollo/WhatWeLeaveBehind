# The script of the game goes in this file.

define r = Character("Ren", color="#ffc080")
define a = Character("Akari", color="#80ffc0")
define k = Character("Kano", color="#ff8080")

define t = Character("Mr. Takahashi", color="#c0ff80")
define d = Character("Dad", color="#c080ff")
define m = Character("Mom", color="#ffff80")

define short_dissolve = Dissolve(0.5)
define long_dissolve = Dissolve(1.0)

label start:
    call chapter_1

    return