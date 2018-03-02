label flowey_fp_hangout1:

	scene background ruins_toy_knife_room
		
	show flowey backside with Dissolve(.25)
	flowey "..."
	flowey "...!"
	show flowey surprised with Dissolve(.25)
	flowey "You!"
	show flowey suspicious with Dissolve(.25)
	flowey "What do you want?"
		
	menu:
		"Mind if I hang out with you?":
			$world.get_monster('Flowey').update_FP(3)
			show flowey surprised with Dissolve(.25)
			flowey "Hang...out?"
			flowey "Why would...?"
			show flowey annoyed with Dissolve(.25)
			flowey "..."
			show flowey backside with Dissolve(.25)
			flowey "Sure. Knock yourself out."
			flowey "..."
						
			menu:
				"...":
					$world.get_monster('Flowey').update_FP(-2)
					flowey "..."
					flowey "..."
					flowey "...Wow"
					show flowey annoyed with Dissolve(.25)
					flowey "You sure have a lot to say."
					flowey "I know you’re not that talkative, but I didn’t think you’d go all 'silent protagonist' on me."
								
				"It’s a nice view":
					$world.get_monster('Flowey').update_FP(2)
					flowey "..."
					show flowey neutral with Dissolve(.25)
					flowey "...Yeah. It is."
					flowey "I used to come here all the time with..."
					show flowey surprised with Dissolve(.25)
					flowey "..."
					show flowey sideglance with Dissolve(.25)
					flowey "I bet it’s pitiful compared to views on the surface, though."
					flowey "I’ve heard there are cities that stretch for miles and miles, with buildings so tall they touch the clouds."
					show flowey wink with Dissolve(.25)
					flowey "It must suck to know you’ll never be able to see that again."
										
				"Do you come here often?":
					$world.get_monster('Flowey').update_FP(1)
					flowey "Not so much anymore."
					flowey "I used to come here all the time with..."
					flowey "..."
					show flowey angry with Dissolve(.25)
					flowey "Actually, you know what? That’s none of your business."
						
		"What are you looking at?":
			$world.get_monster('Flowey').update_FP(1)
			flowey "Why do you care?"
			flowey "..."
			show flowey suspicious with Dissolve(.25)
			flowey "..."
			flowey "It’s the city. The only view in these bleak ruins not filled with crumbling rocks and spineless Froggits."
						
			menu:
				"What’s so bad about froggits?":
					show flowey annoyed with Dissolve(.25)
					flowey "You’re joking, right?"
					flowey "Have you {i}met{/i} a froggit?"
					show flowey smug with Dissolve(.25)
					flowey "They’re just about the weakest monsters down here. One of those practice dummies could beat them in a fight."
								
				"Have you ever been to the city?":
					$world.get_monster('Flowey').update_FP(1)
					show flowey surprised with Dissolve(.25)
					flowey "Plenty of times."
					flowey "I used to go with my family, but..."
					flowey "...that was a long..."
					show flowey sideglance with Dissolve(.25)
					flowey "...{i}long{/i}...time ago."
					flowey "..."
								
				"The Ruins aren’t all that bleak.":
					$world.get_monster('Flowey').update_FP(-1)
					flowey "They are when you’ve been around them as long as I have."
					show flowey smug with Dissolve(.25)
					flowey "Which is, might I say..."
					show flowey wink with Dissolve(.25)
					flowey "...an awfully long amount of time."
					show flowey normal with Dissolve(.25)
						
		"I need something to satiate my boredom. I guess you’ll do.":
			$world.get_monster('Flowey').update_FP(-4)
			show flowey angry with Dissolve(.25)
			flowey "Just because you’ve got control down here doesn’t make me your {i}plaything{/i}."
			show flowey horror with Dissolve(.25)
			flowey "Unless you want to be torn limb from limb."
						
			menu:
				"No, I’d much rather prefer my limbs intact, thank you.":
					show flowey laughing with Dissolve(.25)
					flowey "Then you’d better think twice before opening that obnoxious mouth of yours."
					show flowey sideglance with Dissolve(.25)
					flowey "If that’s how you talk to everyone here...well..."
					show flowey smug with Dissolve(.25)
					flowey "I won’t be the only one wishing those flowers hadn’t broken your fall..."
								
				"Bring it, flower.":
					$world.get_monster('Flowey').update_FP(-5)
					flowey "You asked for it, {i}H U M A N{/i}."
					flowey "..."
					show flowey sideglance with Dissolve(.25)
					flowey "..."
					show flowey angry with Dissolve(.25)
					flowey "...What? I can't..."
					flowey "..."
					show flowey suspicious with Dissolve(.25)
					flowey "{i}UGH{/i}."
					flowey "Curse this casual gameplay style."
					flowey "Looks like the only way I can cause you pain..."
					flowey "...is through my {i}words{/i}."
					flowey "..."
					show flowey angry with Dissolve(.25)
					flowey "What kind of a lame game is this?"
					flowey "Do you really have nothing better to do with your time? Like bashing your skull against a rock?"
						
		"Nothing, really. I’ll be on my way.":
			show flowey annoyed with Dissolve(.25)
			flowey "Of course you will."
						
	if inventory.get_count(Snail_Pie) > 0:
		show flowey surprised with Dissolve(.25)
		flowey "Wait…"
		show flowey suspicious with Dissolve(.25)
		flowey "What’s that smell?"
		flowey "It’s like…"
		flowey "...bread...and…"
		flowey "...slime?"
			
		menu:
			"It's something tasty~":
				show flowey angry with Dissolve(.25)
				flowey "Well, DUH. What is it?"
								
				menu:
					"*Show him what’s in your bag.":
						$world.get_monster('Flowey').update_FP(1)
						show flowey surprised with Dissolve(.25)
						flowey "Is that... Snail Pie?"
						jump flowey_fp_hangout1_share:

					"I’ll give you three guesses.":
						$world.get_monster('Flowey').update_FP(-2)
						flowey "You might be playing games here, but I’m not."
						jump flowey_fp_hangout1_guesses:

					"I’ll be back later to show you.":
						flowey "Thanks for wasting my time."
								
			"It's Snail Pie! I can't wait to eat it!":
				$world.get_monster('Flowey').update_FP(-2)
				show flowey surprised with Dissolve(.25)
				flowey "Wait...Snail Pie?"
				show flowey angry with Dissolve(.25)
				flowey "You can’t possibly eat the whole thing."
				jump flowey_fp_hangout1_share:
						
			"I have a gift for you.":
				$world.get_monster('Flowey').update_FP(4)
				show flowey surprised with Dissolve(.25)
				flowey "A... gift?"
				show flowey suspicious with Dissolve(.25)
				flowey "Why give me anything?"
								
				menu:
					"Because I think you'll like it.":
						$world.get_monster('Flowey').update_FP(3)		
						show flowey surprised with Dissolve(.25)
						flowey "Really?"
						flowey "Well, what is it? It smells... familiar."
						jump flowey_fp_hangout1_friendship:
										
					"Oooh, you’re curious, aren’t you?":
						$world.get_monster('Flowey').update_FP(-2)
						show flowey angry with Dissolve(.25)
						flowey "So what? Shove a bag in my face and of course I’d be curious, idiot."
										
					"I’m not too fond of it myself, so I figured I’d give it to you.":
						$world.get_monster('Flowey').update_FP(-1)	
						show flowey annoyed with Dissolve(.25)
						flowey "..."
						flowey "Should have guessed."						
						
					flowey "I don’t need any gifts."
					show flowey annoyed with Dissolve(.25)
					flowey "I’m not going to be your friend. I’m not like those other idiots - I don’t become friends with someone just because they give me stuff."
						
					menu:
						"It’s not to be friends. I just thought you might like it.":
							$world.get_monster('Flowey').update_FP(3)
							flowey "Hmph. Alright. What is it?"
										
label flowey_fp_hangout1_friendship:
								
	menu:
		"*Show him what's in your bag.":
			$world.get_monster('Flowey').update_FP(1)
			jump flowey_fp_hangout1_surprise:
										
		"I’ll give you three guesses.":	
				$world.get_monster('Flowey').update_FP(-2)
				show flowey angry with Dissolve(.25)
				flowey "You might be playing games here, but I’m not."
				jump flowey_fp_hangout1_guesses:
								
							"You don’t know that yet":
								$world.get_monster('Flowey').update_FP(-2)
								show flowey horror with Dissolve(.25)
								flowey "Oh, trust me, I do know. I know more than you ever could."
								
							"It’s not polite to decline a gift.":
								$world.get_monster('Flowey').update_FP(-4)
								show flowey angry with Dissolve(.25)
								flowey "It’s also not polite to pester a talking flower."
				
					flowey "Now show me what’s in the bag or get out of my face, idiot."
						
					menu:
							"Okay, jeez. Here it is.":
								jump flowey_fp_hangout1_surprise:
							
							"Fine, I’ll leave":
								$world.get_monster('Flowey').update_FP(-3)
								show flowey sideglare with Dissolve(.25)
								flowey "About time."
										
label flowey_fp_hangout1_guesses:
	flowey "Stop messing around and show me what’s in the bag."
								
	menu:
		"No way. I want your three guesses first.":
			show flowey neutral with Dissolve(.25)
			flowey "Fine then."
			show flowey horror with Dissolve(.25)
			flowey "A bloody knife, a bottle of dust, and a lifeless child."
			show flowey angry with Dissolve(.25)
			flowey "Now just show me already."
												
			menu:
				"Alright, alright, calm down.":
				show flowey surprised with Dissolve(.25)
				flowey "Is that... Snail Pie?"
				jump flowey_fp_hangout1_share:
																
		"I’ll be back later to show you":
		flowey "Thanks for wasting my time."
										
		"*Show him what’s in your bag":
			jump flowey_fp_hangout1_surprise:
										
		"I’ll be back later to show you.":
			flowey "Thanks for wasting my time."
												
label flowey_fp_hangout1_surprise:
	show flowey surprised with Dissolve(.25)
	flowey "Is that... Snail Pie?"
	show flowey backside with Dissolve(.25)
	flowey "What do you expect me to do with this disgusting thing?"
								
	menu:
		"Oh, um, sorry. I’ll get rid of it for you...":
			$world.get_monster('Flowey').update_FP(1)
			show flowey surprised with Dissolve(.25)
			flowey "No!"
			show flowey bashful with Dissolve(.25)
			flowey "I mean, it’s not doing any harm just sitting here."
			show flowey annoyed with Dissolve(.25)
			flowey "Just leave, already. You’re getting annoying."
			flowey "..."
			show flowey backside with Dissolve(.25)
			flowey "But...um..."
			flowey "..."
			flowey "...thanks."
			$inventory.drop(Snail_Pie)
												
		"Wow, ungrateful, aren’t you?":
			$world.get_monster('Flowey').update_FP(-4)
			show flowey annoyed with Dissolve(.25)
			flowey "Well, I never asked for your stupid gift, did I?"
			flowey "Get lost, already."
			show flowey wink with Dissolve(.25)
			flowey "But leave the pie."
			flowey "Not that I actually want it, but this is the least you owe me for wasting my time."
			$inventory.drop(Snail_Pie)
												
label flowey_fp_hangout1_share:
	show flowey sideglare with Dissolve(.25)
	flowey "Not that I {i}really{/i} want any..."
	flowey "...But a flower’s gotta eat somehow."
	show flowey wink with Dissolve(.25)
	flowey "Surely you can spare a piece."
								
	menu:
	"Of course! Here you go.":				
		$world.get_monster('Flowey').update_FP(3)
		show flowey smug with Dissolve(.25)
		flowey "Thanks, pal! Looks like you’re good for something after all."
		flowey "Now buzz off before I throw you over the balcony."
		$inventory.drop(Snail_Pie)
												
	"No way, man, this is all for me.":
	$world.get_monster('Flowey').update_FP(-3)
	show flowey angry with Dissolve(.25)
	flowey "You’ve GOT to be joking."
												
	menu:
		"Nope! See ya, flower. I’m going to go enjoy this.":
			$world.get_monster('Flowey').update_FP(-4)
			flowey "..."
			show flowey horror with Dissolve(.25)
			flowey "You better run, or you won’t be enjoying anything for long."
														
		"*Stare Flowey in the eyes as you shove pie into your mouth.":
			$world.get_monster('Flowey').update_FP(-5)
			show flowey surprised with Dissolve(.25)
			flowey "Wow."
			show flowey angry with Dissolve(.25)
			flowey "RUDE."
			show flowey backside with Dissolve(.25)
			flowey "I’m out of here. Enjoy your stupid pie, idiot."
			$inventory.drop(Snail_Pie)
																
		"Haha yep! Totally joking. Here, have a piece.":
			$world.get_monster('Flowey').update_FP(1)
			show flowey annoyed with Dissolve(.25)
			flowey "That was dumber than all of Sans’ jokes combined."
			flowey "Just gimme the pie and leave, already."
			$inventory.drop(Snail_Pie)