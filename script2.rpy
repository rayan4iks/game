label loc3:
    scene bg dark with fade
    show isol smirk at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    i "Welcome to the REAL forest"
    show isol kind
    i "Do you really thought that I will help you?"
    show isol smirk
    i "Naive person.. Good luck freezing here!"
    show isol smirk at Move((0.2, 0.5), (3.0, 0.5), 3.0,
                xanchor="center", yanchor="center")
    scene bg game over
    au "You lost.. You must restart the game."

menu:
    "RESTART":
        jump start

label rr:
    scene bg houses with fade
    show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "Wow, look! \nWe are in the dwarf village"
    show dwarf at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
    d "Welcome, friends!"
    a "Hi, dear! We are helping Santa to find all gifts"
    d "It is very good, but before you will go out, you must solve my riddle"
    show astera shock
    a "*whisper* Be careful!"
    hide astera shock at offscreenleft
    d "So, let`s start! \nMy riddle: Soon joy will come to the house, \nTime of joy and laughter. \nI have gifts in a bag, who am I, tell me?"

menu:
    "Father Frost":
        d "Execellent!"
        d "Have a nice trip! Merry Christmas, friends!"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Thanks, dear! Bye-bye"
        $ points += 1
        hide astera smile without teeth at offscreenleft
        hide dwarf at offscreenright
        au "You get 1 gift point!"
        jump right
    "Snow Maiden":
        d "Wrong!"
        d "It's okay, don't worry. Merry Christmas, friends!"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Thanks, dear! Bye-bye"
        jump right
    "Santa Claus":
        d "Execellent!"
        d "Have a nice trip! Merry Christmas, friends!"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Thanks, dear!"
        hide astera smile without teeth at offscreenleft
        hide dwarf at offscreenright
        $ points += 1
        au "You get 1 gift point!"
        jump right
    "New Year":
        d "Wrong!"
        d "It's okay, don't worry. Merry Christmas, friends!"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Thanks, dear! Bye-bye"
        jump right

label lr:
    scene bg yaga with fade
    show astera shock at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "It seems we have come to Baba Yaga's hut"
    show baba yaga at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
    by "So so so, who has come to see me?"
    show astera close eyes
    a "Hello, Baba Yaga! We help Santa find all the presents"
    by "That's good, but to let you go to Santa, you have to solve my riddle"
    show baba yaga apple
    by "My favorite color is green, so in the next picture you have to count all the things where there is green"
    scene bg game with fade
    hide astera close eyes at offscreenright
    hide baba yaga apple at offscreenleft

menu:
    "28":
        show baba yaga at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
        by "Wrong! Better luck next time.. Goodbye, friends"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Goodbye!"
        jump right
    "29":
        show baba yaga at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
        by "Execellent! I wish you good luck! Bye-bye"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Goodbye!"
        hide astera close eyes at offscreenright
        hide baba yaga apple at offscreenleft
        $ points += 1
        au "You get 1 gift point!"
        jump right
    "30":
        show baba yaga at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
        by "Wrong! Better luck next time.. Goodbye, friends"
        show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
        a "Goodbye!"
        jump right

label right:
    scene bg home with fade
    show astera smile without teeth at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "We are already at the finish line, here is Santa Claus's house. Let's go in"
    jump santa

label santa:
    scene bg tree with fade
    show astera close eyes at Move((0.0, 0.5), (0.2, 0.5), 1.0,
                xanchor="center", yanchor="center")
    a "Hello, darling Santa! We've come a long way to get to you"
    show sk at Move((3.0, 0.5), (0.8, 0.45), 1.0,
                xanchor="center", yanchor="center")
    sk "Hello, my darlings! I've been waiting for you for a long time"
    if points == 3:
        show astera smile without teeth
        a "We have collected the required number of gifts, now you can give them to everyone"
        sk "Thank you, my darlings! You have done a great job, thanks to which now all the children will be happy for the Christmas"
        scene bg presents with fade
        au "Congratulations! You have completed the game! Happy new year!"
    else: 
        show astera big eyes
        a "Actually, we did not collect the required number of gift points.."
        sk "Oh no.. Then you need to go back to the start"

        menu:
            "RESTART":
                jump start