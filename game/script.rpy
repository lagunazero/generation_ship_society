
# Characters - Special
define narrator = Character(None, kind=nvl)
define c_cent = Character(None,
                            what_xalign=0.5,
                            what_text_align=0.5,
                            window_background=None,
                            window_yminimum=0,
                            window_xfill=False,
                            window_xalign=0.5,
                            window_yalign=0.5)
define c_temp = Character('*TEMP*', color="#c8ffc8", kind=nvl)

# Characters - Player group
define prot_name = 'Me'
define mira_name = 'Mira'
define kasp_name = 'Kasper'
define zoee_name = 'Zoë'
define faye_name = 'Faye'
define jian_name = 'Jianyu'

define c_prot = DynamicCharacter('prot_name', color="#c8ffc8", kind=nvl)
define c_mira = DynamicCharacter('mira_name', color="#c8ffc8", kind=nvl)
define c_kasp = DynamicCharacter('kasp_name', color="#c8ffc8", kind=nvl)
define c_zoee = DynamicCharacter('zoee_name', color="#c8ffc8", kind=nvl)
define c_faye = DynamicCharacter('faye_name', color="#c8ffc8", kind=nvl)
define c_jian = DynamicCharacter('jian_name', color="#c8ffc8", kind=nvl)

####################### Characters - The Habitat
define vikt_name = 'Viktor'

define c_vikt = DynamicCharacter('vikt_name', color="#c8ffc8", kind=nvl)

#################################################

# Images - Overlays
image overlay black = "#000"
image overlay black_mid = "#000A"

# Images - Backgrounds
image bg black = "#000"
image bg gray = "#AAA"
image bg red = "#E22"
image bg cryopods = "cryopods"
image bg flashback_railway = "landscape__16_by_sylar113-d71lpn3.jpg"
image bg corridor = "cryopods" #TODO: temp

# Images - Special/Events
image bg in_cryo = "in_cryo"

#################################################

# Transitions
define dissolve_fast = Dissolve(0.1)
define dissolve_mid = Dissolve(0.75)
define dissolve_slow = Dissolve(2.0)
define pixellate_fast = Pixellate(0.5, 6)
define pixellate_mid = Pixellate(1.0, 5)
define pixellate_slow = Pixellate(2.0, 5)

#################################################

init python:

    menu = nvl_menu
    config.empty_window = nvl_show_core
    config.window_hide_transition = None
    config.window_show_transition = None
    config.nvl_paged_rollback = True
    
    style.nvl_window.background = "#0007"

# The game starts here.
label start:
    window hide
    nvl show dissolve
    scene bg black
    
    # Causes the text window to stick around during transitions. Use "window hide" in a segment where that's not desirable, then "window show" again.
    window show

    jump plot_intro

    return

label plot_intro:
    $ v_plot_intro_mira_legs = False
    $ v_plot_intro_guess_year = 0
    $ v_plot_intro_remember_mira = False
    $ v_plot_intro_guess_mira = ""

    nvl clear
    $ mira_name = 'Voice'
    
    # TODO: Sfx: Bubbles with heavy reverb. Underwater.
    nvl clear
    scene bg in_cryo with dissolve_slow
    pause 1.5
    c_cent "Hey."
    
    # Full white with heavy blur. Hesitantly (back and forth) fades to a dark chamber full of cryopods.
    nvl clear
    show bg black with dissolve_mid
    pause 1.0
    c_cent "Hey, wake up!"
    pause 0.7
    
    show bg in_cryo with dissolve_mid
    pause 0.2
    nvl clear
    "In the distance, I hear repeated thuds."
    "Or rather, I sense the vibrations of something banging on something."
    "But it's too distant."
    "Too cold."

    show bg black with dissolve_mid
    nvl clear
    pause 0.3
    show bg gray with dissolve_fast
    show bg black with dissolve_fast
    "A light flashes."
    "The banging sound is a lot closer."
    
    # Starts waking up. Mira blurry in front.
    nvl clear
    show bg cryopods with dissolve_slow
    show bg black with dissolve
    show bg cryopods with dissolve
    pause 0.1
    show bg black with dissolve_fast
    show bg cryopods with dissolve_fast
    pause 1.5
    "Hot air is blowing in my face. I'm cold everywhere."
    "It's bright, much too bright."
    "Someone is standing in front of me, but I can't make it out."
    c_mira "Shit, we really can't stay here..."
    "I don't recognize the voice."
    "My eyes hurt."
    
    # Blur again and start to fade.
    nvl clear
    show overlay black_mid with dissolve_mid
    pause 0.2
    c_mira "Fuck, I knew it was too late!"
    c_mira "Are you already dead?"
    c_mira "Guess you're not gonna answer that..."
    "Someone leans towards me and I'm wrapped in an embrace."
    c_mira "Well here goes!"
    
    # Screen jolts as Mira lifts up the player.
    nvl clear
    show bg cryopods with pixellate_mid
    "I'm in someone's arms. Finally, it's warm."
    c_mira "Good thing you haven't eaten shit for months. This should be doable."
    c_mira "I hope."
    show bg black with dissolve_mid
    
    # Mira carries the player and reveals she's the sister.
    nvl clear
    c_mira "Hey, don't go out on me!"
    "I'm shaken and something knocks against my head."
    show bg cryopods with dissolve_mid
    c_mira "Don't you worry. Your big sis is gonna take care of you."
    "Oh. So that's who it is."
    "I suppose I have a sister."
    "My mind is still black. I can't recollect anything."
    "But it's good. Now it's all good."
    "My sister is here."
    $ mira_name = 'Sister'
    show bg black with dissolve_slow
    hide overlay
    
    # Title
    nvl clear
    pause 0.2
    show text "GENERATION SHIP SOCIETY" at truecenter with dissolve
    pause 1.3
    hide text with dissolve
    
    # Mira talks a little. Sees cryopod.
    nvl clear
    show bg cryopods with dissolve
    "I force my eyes open again. I don't know what's going on, but I'm starting to become anxious about it."
    "Why am I here?"
    "Why is my sister here?"
    "Where is {i}here{/i}?"
    c_mira "I hope I'm not holding you too crummily."
    c_mira "It's not as easy as when we were kids, you know."
    "I'm scuffed up a bit, so that my head is leaning over her shoulder. Behind us is some kind of capsule, open, with a bed-like bottom and glass cover. There's flashing text on the cover, but I can't read what it says."
    
    # Mira talks some more. Starts walking.
    nvl clear
    "We're walking slowly across a floor of metal panels. On both our sides are rows of capsules like the one behind us. Some are open, but there's no flashing text on them. Others are still closed, with people in them. I try to see if anyone's breathing, I stretch my head closer to one as we pass it, but I don't see any movement at all."
    c_mira "Hey, hey! Don't move now."
    "My sister stops and re-adjusts me. As she takes a first step again, she suddenly halts and turns to the capsule I tried to peer into."
    c_mira "You didn't...?"
    c_mira "Huh."
    
    # Look into a capsule. Realize nakedness. Chinese name is Lu Xueqin.
    nvl clear
    "She slowly approaches the capsule, facing it so we can both see it well. There's a man inside, probably in his fifties. He looks Chinese, or at least east Asian. He's bare naked, aside from a small, square metal tag hanging around his neck."
    "Hey, am I naked too?!"
    "Squirming a little, I confirm that I'm at least wrapped in a thin blanket. Well, I suppose it doesn't matter too much. It's warm out here and there's only my sister here, not counting the sleepers."
    nvl clear
    "Just like before, the glass cover has one line of flashing green text on it."
    "{color=#2F2}鲁雪芹{/color}"
    "Huh. I look up and down the capsule, but there's nothing else to tell me anything about this man. Only three Chinese characters."
    c_mira "We should get going. This guy's not gonna wake up anytime soon."
    c_mira "But someone else might... And we don't want to wait around for that."
    
    # Starts walking again. Observes surroundings. Listens.
    nvl clear
    "We start walking again, faster this time. My eyes slowly begin to adjust to the hazy, blue light that seems to be emitted from strips along the battens against both ceiling and floor. I look into all the capsules we pass, but no-one is moving. No-one is awake."
    # "There are men and women of all ages. Even children. Most seem to be either European or Asian, but of course it's hard to tell. Mostly Chinese, but a lot of what I think are Indians, Japanese and south-east Asians too."
    "There's a deep rumble coming from somewhere far away, maybe below us. It comes and goes in waves; at times inaudible, then crashing towards us so strongly that it feels like it's just underneath our feet. It sounds like a large dryer, only instead of clothes it's filled with metal and rocks. After a few seconds when I think it's going to show up running head-first towards us, the noise slowly fades again. Less than a minute later, it returns."
    "Was that what I heard before?"
    
    # Mira stops and goes to see her child.
    nvl clear
    c_mira "Wait..."
    "She comes to a halt and quickly puts me down on the floor, looking to the side. The cold metal finds the gaps in my blanket, chilling my bum and legs and sending a tinge through my whole body and I gasp. But my sister doesn't notice. Instead, she walks off and vanishes into the rows of capsules without looking back."
    "I hear only a few steps after I lose sight of her, then the room descends into silence. I try to move my arms for the first time and, though they ache, I manage to grip whatever I'm leaning against and push myself up a little higher."
    "It's marginally more comfortable."
    
    # Starts to regain sense/body control.
    nvl clear
    "I fold and unfold my hands a few times, each time with slightly more ease. The skin is pale and wrinkled, but with a shiny luster. It's like I'm a senior who's just been at spa."
    "Once I'm satisfied enough with my hand movements, I start straightening my legs..."
    show bg red with dissolve_fast
    show bg cryopods with dissolve_fast
    "Ah!"
    "My thighs are riveted, as though the blanket that covers them was really made of nails. An intense pain shoots up through my abdomen and I bend over."
    show bg red with dissolve_fast
    show overlay black_mid with None
    show bg cryopods with dissolve_fast
    "Hahh... Hahh..."
    "Something is grabbing my stomach and twisting it apart."
    "Everything up to my shoulders is shaking."
    "I'm falling to pieces."
    "My vision blurs..."
    "...flickers..."
    show bg black with pixellate_slow
    "...and goes out."
    hide overlay
    
    # Is out cold.
    nvl clear
    "Some..."
    "............time..."
    "...................passes..."
    
    # Starts waking up. Realizes immobility.
    nvl clear
    show bg red with dissolve_fast
    show bg black with dissolve_fast
    "A sharp sting pierces my hip. I snap awake and reflexively push myself away. I have a headache from hell and I want to throw up, but my throat is too dry. Breathing heavily for air, I almost gag instead. Slowly, I move my hands along my body. My arms and torso seem to be mostly fine, but I have no tactility from my thighs down. I force my eyes open."
    show bg cryopods with dissolve
    "I'm lying with my back on the floor and my head still resting upright. Looking down, there's a dent in the floor panel just beside me, with a few sharp points straight at me. Aside from the momentary pain, I don't think it actually injured me."
    "Rather, I have a feeling this immobility isn't new."

    # Mira returns, wakes player. Worried.
    nvl clear
    c_mira "Sorry 'bout that, let's keep---"
    show bg cryopods with pixellate_fast
    "As I'm looking up to see where my sister's coming from, she suddenly throws herself down."
    c_mira "What's going...?! How, how are you feeling?!"
    "She starts patting me all over and setting the overthrown blanket right again. Her eyes wander up and down me rapidly as she rambles."
    c_mira "What, what happened? Are you alright? Did you... I mean, is this alright? Where does it hurt? Does it hurt? It hurts, right? Oh fuck fuck fuck fuck fuck fuck..."
    "I give her a bleak smile and am about to pull myself up when I remember how it felt just now."
    c_mira "Oh fuck... I'm so {i}so{/i} sorry! I never should've left you like that! Shit!"
    "She hugs me closely, absorbing me in a smell of diesel, deep wood, and fat hair. I inhale deeply and..."
    
    # Flashback to childhood railway.
    nvl clear
    show bg black with dissolve_fast
    show bg gray with dissolve
    show bg flashback_railway with dissolve_mid
    "The sun is warm. The grass tickles my bare skin. There's nothing in the soundscape but cicadas and grasshoppers. Even though there's only the one tree nearby, the immensity of the surrounding forest covers the whole clearing in a musky smell. I somehow know this forest is older than the railway, older than any city or man-made thing I've ever seen. It's what grounds me to this place, to this life."
    "I look up and down the tracks from where I'm sitting by the tree. There hasn't passed a train in a while, but I'm here nonetheless."
    "Maybe now."
    
    # Flashback cnt.
    nvl clear
    "From some way behind me, up the road, someone approaches me with familiarly steady steps. I sit up straighter as the pace quickens. When the gravel's crunch is replaced with the soft thuds and wisps of bending grass, I close my eyes."
    show bg black with dissolve
    "Thick arms take a tight hold on me and I'm lifted high, then burrowed into a birdnest of a hair, but I keep my eyes shut and just inhale deeply the reassuring diesel."
    "Maybe I won't see a train today either."
    "But it's good. It's all good."

    nvl clear
    c_cent "Hey."
    c_cent "Hey, snap out of it!"
    
    # Wakes up from flashback. First spoken words.
    nvl clear
    show bg cryopods with pixellate_mid
    c_mira "Hey, you okay?! Shit!"
    "The grass is suddenly metal again. My sister is shaking me, but I think she's shaking just as much. Only her eyes are stable, pointed straight into mine."
    c_mira "Right... Are you... Are you okay? Can you speak?"
    "I open my mouth and cough twice. At first there's only a wheeze as I try to make a sound, but at my second attempt it's already grown strong enough to say at least something."
    menu:
        "I'm fine.":
            jump plot_intro_first_talk_fine
        "I don't think my legs work.":
            jump plot_intro_first_talk_legs
        "There was a railway.":
            jump plot_intro_first_talk_railway

    label plot_intro_first_talk_fine:
    nvl clear
    c_mira "Ah. That's... that's good. That's great."
    "She smiles and moves back a little bit. The wrinkles in her face fade away and she brushes a hand through her short but thick hair."
    jump plot_intro_p2
    
    label plot_intro_first_talk_legs:
    nvl clear
    $ v_plot_intro_mira_legs = True
    c_mira "Oh. Huh. Hmm..."
    "She frowns and squeezes my legs lightly. At least it looks that way, I can't feel a thing in them."
    c_mira "Legs are a no-go, huh? Fuck..."
    "She moves back a little and spits on the floor beside her, then flicks at her nose."
    c_mira "Well, we'll just have to see what happens. No going back now."
    jump plot_intro_p2

    label plot_intro_first_talk_railway:
    nvl clear
    c_mira "Ah, mm. That's, yeah, okay. I'm, I'm just happy you're okay."
    "She smiles and moves back a little bit. The wrinkles in her face fade away and she brushes a hand through her short but thick hair."
    c_mira "I wouldn't worry about that, if I were you. But we'll talk about it later, okay?"
    jump plot_intro_p2
    
    # Starts walking again.
label plot_intro_p2:
    nvl clear
    "She glances up ahead the corridor of capsuled sleepers, but there's nothing else there."
    c_mira "I'm sorry to rush you, but we need to get going. It's dangerous here."
    c_mira "I'll carry you."
    c_mira "Well. Obviously."
    "A bit more carefully than before, she scoops me up and carries me like you would a child. She still smells like a garage, but maybe I shouldn't tell her so. The worst pain has subsided in favour of a numbness. My mind is clearer than ever since waking up, but my body feels like it's a hundred years old. But I don't want to sleep. Not yet. Not for a long time."

    # Pick name
    nvl clear
    c_mira "So this is gonna sound weird, but... I should ask you some basic questions. Real rudimentary stuff."
    "She slows her walking and glances at me sideways. Her eyes grow narrower as she opens her mouth slowly, but says nothing. Shrugging her shoulders slightly, she looks away again and starts moving more briskly."
    c_mira "It's just standard protocol, you know. Gotta know that you're alright. Well, as alright as you can be. As anyone can be in this dump."
    "Her hands take a firmer grip on me as she spits."
    c_mira "I don't think I've slipped up and said it yet, so... Do you remember your name?"
    menu:
        "I think so.":
            jump plot_intro_questions_name_yes
        "No...":
            jump plot_intro_questions_name_no
    
    label plot_intro_questions_name_yes:
        nvl clear
        c_mira "You do? Hah, I'm glad. So let me hear you say it!"
        "She slows down again and looks at me, this time with a smile."
        jump plot_intro_questions_name_pick
        
    label plot_intro_questions_name_no:
        nvl clear
        c_mira "You don't? Huh..."
        "She twists her mouth into an ugly grin and bits hard into her lower lip. After a few seconds, she exhales and her tense face softens."
        c_mira "You want to pick a new one, then?"
        c_mira "I figure, if you can't recall what our parents gave you, maybe you never really liked it anyway."
        jump plot_intro_questions_name_pick
    
    label plot_intro_questions_name_pick:
        $ prot_name = renpy.input(prompt="My name?", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        if not prot_name:
            jump plot_intro_questions_name_pick
        $ prot_name = prot_name.strip().title()
        
        nvl clear
        if prot_name == "Mira":
            if not v_plot_intro_remember_mira:
                $ v_plot_intro_remember_mira = True
                c_mira "What?!"
                "She stops so abruptly that I almost fall forward, but she catches both me and her breath quickly."
                $ mira_name = 'Mira'
                c_mira "Don't joke around, that's my name! Still... I'm very happy you remember."
                c_mira "Come on, can I have a real answer now?"
                nvl clear
            jump plot_intro_questions_name_pick
        
        c_mira "It's [prot_name], huh?"
        "There's a playfulness in her eyes that I haven't noticed before."
        menu:
            "Yes":
                c_mira "I'm happy."
                jump plot_intro_p3
            "No":
                c_mira "No? You're just trying it out?"
                jump plot_intro_questions_name_pick

    # Guess year
label plot_intro_p3:
    nvl clear
    "My sister looks around and her grip gets tighter."
    c_mira "I'd like to pick up the pace, but there's no point in overdoing it now in case something comes up later. So hopefully we can keep chattting."
    c_mira "It's been a while, after all."
    "She gives me a glance and half a smile, but it only lasts a second before her eyes become stern again."
    c_mira "Now then. Do you know what year it is?"
    menu:
        "Maybe...":
            jump plot_intro_questions_year_pick
        "Sorry...":
            c_mira "Hah... No, don't worry about it."
            jump plot_intro_p4
    
    label plot_intro_questions_year_pick:
        python:
            try:
                v_plot_intro_guess_year = int(renpy.input(prompt="The current year?", allow="0123456789",length=5))
            except ValueError:
                v_plot_intro_guess_year = 0
        if not v_plot_intro_guess_year:
            jump plot_intro_questions_year_pick
        
        nvl clear
        if v_plot_intro_guess_year < 2015:
            jump plot_intro_questions_year_earlier
            
        elif v_plot_intro_guess_year > 2200:
            jump plot_intro_questions_year_later

        else:
            jump plot_intro_questions_year_here
    
    label plot_intro_questions_year_earlier:
        c_mira "Hah."
        c_mira "I don't know much, but at least {i}that{/i} would require a time travel. Still, stranger things have happened, right?"
        jump plot_intro_p4

    label plot_intro_questions_year_later:
        c_mira "Wouldn't that be something..."
        "She takes a deep breath and gazes into the ceiling."
        c_mira "Maybe that would even be the best. Everyone long gone. Everything's changed. Maybe even... only us..."
        jump plot_intro_p4
        
    label plot_intro_questions_year_here:
        c_mira "Your guess is as good as any."
        jump plot_intro_p4
    
    # Explain that everyone's been frozen down. Not knowing the year.
label plot_intro_p4:
    c_mira "See, I don't really know what year it is either."
    if v_plot_intro_guess_year:
        c_mira "Maybe it really is [v_plot_intro_guess_year], I dunno."
    c_mira "We've all been frozen down for who knows how long, and nothing here's got any kind of time on it. Can't fucking believe it..."
    "Her lips pinch together and stays so for some time as we walk on."
    
    # Exit the capsule room
    nvl clear
    show bg corridor with dissolve_mid
    "We reach and enter through a doorway, at the other side of which we come into a corridor that stretches on both left and right. My sister's grip on me tightens as she peers up and down the corridor twice. I'm about to ask where we're going when she starts a brisker walk to the right, her head still half-turned in the other direction."
    "There's less light out here and the dimness makes me drowsy again. I close my eyes for just a moment..."
    show bg black with dissolve_mid
    
    # TODO: Continued dream?
    
    # Wake up
    nvl clear
    show bg corridor with dissolve_fast
    c_mira "Be quiet."
    "I open my eyes to see the wall of a corridor that looks the same as before, but I doubt it was only a moment ago. My sister's hand covers my mouth but I resist the instinct to gasp loudly. We're hunched in a small alcove together with some wiring and dust. In the distance - behind us? - there are sounds of hard, fast footsteps. As they grow louder, they also grow in number. Maybe ten, maybe more."
    "I peer up at my sister's face; it's sterner than I've seen it before and there's sweat that I don't think came from the rapid walk. She's staring at the alcove's wall in the direction of the footsteps, as if she could see right through it, inching her gaze closer and closer to the visible part of the corridor. Looking the rest of her down, she's holding a small gun in the hand that's not in my face. Both hands are shaking."
    
    # Runner passes by
    nvl clear
    show bg white with dissolve_fast
    show bg corridor with dissolve_fast
    "A man passes us by in a split second."
    "The speed of the runner and the surprise makes me lose all balance and I almost fall out of my sister's tight grip. But she won't let me move an inch. I glance upwards again. She's still looking back, ignoring the man who just passed us by. There are more footsteps coming; a lot more. Her hands grow shakier, as does her mouth. Only her narrow eyes are in control."
    
    # Raiders pass
    nvl clear
    "Several people pass us in rush. One, two, four, five, seven or eight, nine, twelve?"
    "I'm lifted ever so slightly as my sister's whole body tenses up. Her hand pushes harder onto my mouth and it's difficult to breathe. I try not to."
    "Thirteen?"
    "Fifteen?"
    show bg black with dissolve_mid
    "I shut my eyes, and instantly feel like a fool for using baby-logic, but I know I must stay calm. I must not make a sound or a move, and counting them only makes me whisper it out loud. As soon as I do so, the footsteps immediately grow more faint; replaced more by their echo than anything real. Still, I keep my eyes shut until I feel my sister relax."
    "So I wait."
    
    # Wait for Mira to relax
    nvl clear
    "And I wait."
    nvl clear
    "And wait."
    
    # Start moving again
    nvl clear
    show bg corridor with dissolve_mid
    "Finally she stands up again. The sounds of running are gone, except for in my mind. Wordlessly, we start walking again. I want to ask her, but her hand is still covering my mouth; though gentler now."
        
    # Guess Mira's name
    if v_plot_intro_remember_mira:
        jump plot_intro_p5
    nvl clear
    "It takes several minutes before she casually lets go of my mouth, almost an after-thought, as she gives me a quick glance."
    c_mira "There's one more thing I wanted to ask you before we arrive."
    c_mira "It's not really a fair question, but just indulge me, okay?"
    "She gives me a quick smile, before her eyes dart back to the road ahead. So far she hasn't let her eyes leave the corridor in front of us for longer than a second, ever since those people passed us. I'd thought she would be stopping to listen every now and then, too, but her tempo has been constant, even as she speaks to me."
    c_mira "So the thing is... Do you remember my name?"
    jump plot_intro_remember_mira_pick
    
    label plot_intro_remember_mira_pick:
        nvl clear
        $ v_plot_intro_guess_mira = renpy.input(prompt="My sister's name?", allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
        if not v_plot_intro_guess_mira:
            jump plot_intro_remember_mira_pick
        $ v_plot_intro_guess_mira = v_plot_intro_guess_mira.strip().title()
        if v_plot_intro_guess_mira == prot_name:
            jump plot_intro_remember_mira_pick
        if v_plot_intro_guess_mira == "Mira":
            jump plot_intro_questions_mira_correct
        else:
            jump plot_intro_questions_mira_other

    label plot_intro_questions_mira_correct:
        $ v_plot_intro_remember_mira = True
        c_mira "What?!"
        $ mira_name = 'Mira'
        "She stops so abruptly that I almost fall forward, but she catches both me and her breath quickly."
        c_mira "I mean... I just... I really didn't think you'd remember..."
        "She looks away from me and sniffles twice, then clears her throat."
        c_mira "It's like, you don't remember anything and you hadn't said my name yet and I thought you would if so and I just didn't think you'd, well... I'm, ah..."
        "She exhales loudly. After a few seconds of silence, she faces me again with a strained smile."
        c_mira "I'm just happy. That you remember me... Not everyone does."
        jump plot_intro_p5
    
    label plot_intro_questions_mira_other:
        c_mira "[v_plot_intro_guess_mira]?"
        "She smiles, still looking ahead, and shakes her head slightly."
        c_mira "That's a nice name, but it's not mine."
        c_mira "I'm Mira."
        "Mira? I don't recognize the name... But I don't remember much else either..."
        c_mira "Well, no worries. I didn't expect you to. People usually don't remember much, if anything."
        $ mira_name = 'Mira'
        jump plot_intro_p5
        
    # Start moving forward again.
label plot_intro_p5:
    nvl clear
    
    nvl clear
    c_temp "Arrive at HQ"
    
    nvl clear
    c_temp "Meet Kasper. Who are you? I'm Mira's sister/brother!"
    
    nvl clear
    c_temp "Talk about disability"
    
    nvl clear
    c_temp "Talk about walkie-talkies."
    
    nvl clear
    c_temp "Sleep"
    
    nvl clear
    c_temp "First morning. Talk about assignment mechanic."
    
    nvl clear
    c_temp "What's needed ASAP?"
    
    nvl clear
    c_temp "Assign duties to Mira and Kasper."
    
    
    
    
    
    