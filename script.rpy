
define sk = Character('Santa Claus', color="#2653dc", what_bold = True, what_italic = True)
define a = Character('Astera', color="#52301c", what_bold = True, what_italic = True)
define i = Character('Isol', color="#282529ff", what_bold = True, what_italic = True)
define au = Character('Author', color="#000000ff", what_bold = True, what_italic = True)
define d = Character('Dwarf', color="#c52424ff", what_bold = True, what_italic = True)
define by = Character('Baba Yaga', color="#3ac524ff", what_bold = True, what_italic = True)

label start:
    $ points = 0
    scene bg santa home with fade
    show astera smile at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")    
    "???" "Hi! My name is Astera. I am an elf. \nNice to meet you, friend!"(what_bold = True, what_italic = True)
    show astera smile eyes 
    a "Welcome to the game \"Winter Mystery: Journey to the New Year\"!"
    a "I will be your helper during the game"
    show astera smile without teeth
    a "Our main task is to find all the gifts, take them to Santa Claus \nso that he can bring them to children on time"
    a "Along the way you will be faced with a choice, for correct answers you will receive points, which will eventually become gifts"
    a "So now press the button \"START\" for the beginning"
    hide astera smile without teeth with fade

menu optional_name:
    "START":
        jump loc1

label loc1:
    scene bg forest with fade
    show isol smirk at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")  
    "???" "Ohh, who is this in my forest?"(what_bold = True, what_italic = True)
    show astera shock at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")    
    a "OMG.. This is Isol.."
    i "Yeah, I am Isol and I am a wolf"
    show isol angry
    i "Who did you bring with, Astera?"
    a "*whisper* We need to be careful with him.."
    show astera close eyes
    a "Be calm, Isol. This is my friend. We are helping for Santa to find gifts"
    show isol smirk
    i "Helping is good. I want to help too! I know the short road. Do you want to go with me?"
    show astera shock
    hide astera shock at offscreenleft

menu:
    "No, I want to go with Astera":
        $ points += 1
        hide isol smirk at offscreenright
        au "You get 1 gift point!"
        jump loc2
    "Yes, I want to go with you, Isol":
        jump loc3

label loc2:
    scene bg light forest with fade
    show astera big eyes at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "Phew, we got rid of the Isol, \nnow he won't bother us"
    show astera smile without teeth

menu: 
    a "Shall we continue?"
    "Yes, I will":
        $ points += 1
        hide astera smile without teeth
        au "You get 1 gift point!"
        jump loc4
    "No, it is not for me":
        show astera angry
        a "But we must.. Please, don't leave me"
        jump loc4

label loc4:
    scene bg roads with fade
    show astera big eyes at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "Oh, there are two roads.. Which should we choose?"

menu:
    "Right one":
        jump rr
    "Left one":
        jump lr
