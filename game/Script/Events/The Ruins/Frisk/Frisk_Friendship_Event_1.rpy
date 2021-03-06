

label frisk_friendship_event_1(owner=get_frisk()):
    
    show frisk smallsmile with Dissolve(.25)
    frisk "Yeah, that sounds fun!"
    frisk "It’s always a lot more interesting with friends."
    show frisk smallsmile with Dissolve(.25)
    frisk "I’m... uh..."
    frisk "Sorry, nevermind."


    if player.current_room != "Snail Hunting Room":
        show frisk normal with Dissolve(.25)
        frisk "Let’s just get going, okay?"
        $ renpy.transition(fade)
        $ renpy.show(world.get_room("Snail Hunting Room").bg)
        frisk "Alright, we’re here!"

    frisk "Are you... uhm..."
    frisk "..."
    frisk "Oh, sorry."
    show frisk smallsmile with Dissolve(.25)
    frisk "Are you ready?"
    menu:
        "You seem distracted.":
            show frisk normal with Dissolve(.25)
            frisk "It’s nothing."
            frisk "Come on, let’s focus. Mom will be disappointed if we come back with nothing!"
            show frisk smallsmile with Dissolve(.25)
            frisk "I’m sure you’re ready, so here we go."
        "Let's start!":
            $ get_frisk().update_FP(2)
            frisk "Yeah... We’re both ready, so here we go."
    #call demo_undersnail
    
    #after game, regardless of performance
    show frisk distant with Dissolve(.25)
    frisk "..."
    frisk "..."
    menu:
        "Frisk...?":
            frisk "I..."
            show frisk sad with Dissolve(.25)
            frisk "I don’t feel so good."
            show frisk disgusted with Dissolve(.25)
            frisk "I’ll, uhh..."
            frisk "See you later."
            hide frisk with Dissolve(.25)
        "...":
            frisk "..."
            show frisk disgusted with Dissolve(.25)
            frisk "I can’t..."
            frisk "I’ll, uhh..."
            frisk "See you later."
            hide frisk with Dissolve(.25)
    $ get_frisk().move_to_room("Tunnel Divide")
    $ player.variables['frisk_f1_phase2'] = True
    $ get_frisk().set_special_event('frisk_friendship_event_1_tunnels')
    $ move_to_room("Snail Hunting Room")

label frisk_friendship_event_1_tunnels(owner=get_frisk()):
    #player is free to move around the Ruins. Once they go back to the tunnel divide...
    play music "audio/ruins/frisk.mp3" fadein 5
    show frisk distant with Dissolve(.25)

    "* Frisk is standing in the middle of the room, but they don’t appear to have noticed you."
    frisk "..."
    frisk "Please..."
    frisk "Please stop."
    frisk "Stop!"
    frisk "..."
    show frisk panicking with Dissolve(.25)
    frisk "Stop it! Stop!"
    menu:
        "What happened?":
            show frisk panicking with Dissolve(.25)
            frisk "Y-you..."
            frisk "How did you find me?"
            frisk "You shouldn’t be here!"
            frisk "I-I can’t control..."
            frisk "It never stops!"
        "Are you okay?":
            show frisk panicking with Dissolve(.25)
            frisk "Y-you..."
            frisk "Why are you here?"
            frisk "You need to leave!"
            frisk "I-it’s not safe f-for you!"
        "Have you gone crazy?":
            $ get_frisk().update_FP(-3)
            show frisk panicking with Dissolve(.25)
            frisk "No! I..."
            frisk "I..."
            frisk "I don’t know..."
            frisk "No! I’m not!"
            frisk "I just..."
    frisk "Argh..."
    frisk "I can’t..."
    show frisk panicking hands with Dissolve(.25)
    frisk "I can’t think!"
    frisk "I... I..."
    frisk "Help me!"
    frisk "No, don’t!"
    frisk "I..."
    menu:
        "*Give them space":
            frisk "No, don’t leave!"
            frisk "Please!"
            frisk "Not again!"
            frisk "Help me..."
        "*Reach out to help":
            frisk "No, you shouldn’t!"
            frisk "I just..."
            frisk "Since you’re here, I just..."
            frisk "I need to know you’re there."
        "\"Stop this childish act.\"":
            $ get_frisk().update_FP(-3)
            frisk "No. No nonono no."
            frisk "This isn't even an act."
            frisk "It's-"
            frisk "I can't."
            frisk "Please help me!"
            frisk "Please!"
            
    menu:
        "You're gonna be fine.":
            $ get_frisk().update_FP(1)
            frisk "I can’t..."
            frisk "I want to believe that, but..."
            frisk "It won’t g-go away!"
        "I'm not leaving.":
            $ get_frisk().update_FP(3)
            frisk "Thank y-you..."
            frisk "D-don’t go..."
            frisk "Please don’t!"
        "I'll go get Toriel.":
            $ get_frisk().update_FP(-2)
            frisk "No! Don’t!"
            frisk "She can’t help!"
            frisk "I-I can’t let her see me like this again!"
        "I thought you could handle things by yourself.":
            $ get_frisk().update_FP(-3)
            frisk "I..."
            frisk "..."
    #/// If > 7("Have you gone crazy?") and 9.1("Stop this childish act.") and 12.1("I thought you could handle things by yourself.")<
            frisk "Why do you keep saying these things?"
            frisk "I-I’m not making this up!"
            frisk "There’s this thing that just- It keeps..."
            frisk "Why are you doing this?"
            menu:
                "...":
                    pass
                "I'm just trying to help you help yourself":
                    frisk "Wha- what?"
                    frisk "Don’t you get it?"
                    frisk "It’s..."
                    frisk "No! Please! Just help me! I..."
                    frisk "C-can I really...?"
                    frisk "Ahg!"


    frisk "It n-never stops!"
    frisk "Why won’t it j-just stop!?"
    show frisk disgusted with Dissolve(.25)
    frisk "Why?"
    frisk "Why...?"
    show frisk panicking with Dissolve(.25)
    frisk "Won’t it just l-leave me alone!?"
    show frisk disgusted with Dissolve(.25)
    frisk "But I won’t let it..."
    frisk "I can’t let it..."
    frisk "I can’t..."
    frisk "Never..."
    frisk "No more..."
    frisk "..."
    menu:
        "Are you okay?":
            $ get_frisk().update_FP(2)
            frisk "..."
            frisk "I..."
            show frisk distant with Dissolve(.25)
            frisk "Yeah..."
            frisk "I think so."
            frisk "..."
        "Now tell me what this is all about?":
            frisk "..."
            frisk "It’s..."
            frisk "I don’t-"
            frisk "..."
            
    #/// If >14("Now tell me what this is this all about.?") and 7("Have you gone crazy?") and 9.1("Stop this childish act.") and 12.1("I thought you could handle things by yourself.") <
    frisk "..."
    frisk "It’s..."
    frisk "I’m sorry."
    frisk "I don’t-"
    frisk "Please don’t be mad."
    frisk "..."

            
            
    show frisk distant with Dissolve(.25)
    frisk "I... I’m sorry..."
    frisk "I shouldn’t have asked you to help."
    frisk "You shouldn’t have seen that."
    frisk "..."
    show frisk sad with Dissolve(.25)
    frisk "Please, don’t tell Mom."
    frisk "I’m sorry..."
    hide frisk with Dissolve(.25)
    $ player.variables['frisk_f1_phase3'] = True
    $ get_frisk().move_to_room("Black Tree Room")
    $ get_frisk().set_special_event('frisk_friendship_event_1_blacktree')
    $ move_to_room("Tunnel Divide")

label frisk_friendship_event_1_blacktree(owner=get_frisk()):
    #player is free to move around the Ruins. Once they go back to the black tree room:
    play music "audio/ruins/frisk.mp3" fadein 5
    show frisk surprised with Dissolve(.25)
    frisk "What?"
    frisk "Why are you following me?!"
    show frisk sad with Dissolve(.25)
    frisk "Let’s just forget about this..."
    frisk "It would be best for both of us."
    menu:
        "Are you okay?":
            $ get_frisk().update_FP(1)
            frisk "Look, I’m fine."
            frisk "Thanks for your concern, but..."
            frisk "There’s nothing to say."
            show frisk smallsmile with Dissolve(.25)
            frisk "I’ll see you later, okay?"

        "I think you owe me an explanation.":
            $ get_frisk().update_FP(-2)
            show frisk annoyed with Dissolve(.25)
            frisk "Look, I told you already, it was just..."
            show frisk sad with Dissolve(.25)
            frisk "Do we really have to talk about this now?"
            menu:
                "Yes, we do.":
                    $ get_frisk().update_FP(-2)
                    frisk "..."
                    frisk "I’d really rather not, okay?"
                    menu:
                        "Don't I deserve an explanation?":
                            $ get_frisk().update_FP(-2)
                            frisk "..."
                            show frisk annoyed with Dissolve(.25)
                            frisk "You know what? No."
                            frisk "I’m not going to talk about this. In fact, I’ll just leave."
                            show frisk sad with Dissolve(.25)
                            frisk "...Goodbye."

                        "Alright, fine.":
                            $ get_frisk().update_FP(1)
                            frisk "Thank you."
                            frisk "Look, I’m gonna go now."
                            frisk "I’ll talk to you later."

                "Not if you aren't feeling up to it.":
                    $ get_frisk().update_FP(1)
                    frisk "Thank you."
                    frisk "I mean..."
                    frisk "You already think I’m crazy, don’t you?"
                    menu:
                        "I don't think you're crazy.":
                            $ get_frisk().update_FP(3)
                            show frisk smallsmile with Dissolve(.25)
                            frisk "Thanks."
                            frisk "But I don’t get it..."
                            frisk "I just met you, so why are you being so patient with me?"
                            menu:
                                "Because we're friends.":
                                    $ get_frisk().update_FP(4)
                                    frisk "Friends..."
                                    show frisk smallsmile with Dissolve(.25)
                                    frisk "Yeah... I guess so."
                                    frisk "Well, if we’re really friends, then you’ll let this go. Right?"
                                    show frisk smallsmile with Dissolve(.25)
                                    frisk "..."
                                    frisk "Maybe I’ll tell you about it one day."
                                    frisk "But for now, I should go."
                                    show frisk smallsmile with Dissolve(.25)
                                    frisk "Thanks again."

                                "I'm not sure.":
                                    frisk "Really?"
                                    frisk "Well, whatever it was for, thanks again."
                                    frisk "Maybe I’ll tell you about it someday."
                                    frisk "But, uhm... Not now."
                                    frisk "I should get going."
                                    frisk "See you later."      
 
                                "That's just the way I am.": #if patience >0
                                    $ get_frisk().update_FP(2)
                                    frisk "Huh, yeah, I guess that makes sense."
                                    frisk "Well, thanks again."
                                    frisk "Maybe I’ll tell you about it someday."
                                    frisk "But, uhm... Not now."
                                    frisk "I should get going."
                                    frisk "See you later."
                        "Yeah, a bit.":
                            $ get_frisk().update_FP(-1)
                            show frisk sad with Dissolve(.25)
                            frisk "..."
                            frisk "I think I’ll just go now."
                            frisk "Please don’t bring this up again."
                            frisk "See you later."
                            
            
    hide frisk with Dissolve(.25)
    $ player.variables['Hunted_Snails_With_Frisk'] = True
    $ get_frisk().move_to_room("Frisk's Room")
    $ move_to_room("Black Tree Room")
    return
    