# Skibidi
def r():
    global role
    role = input('What role - ')

    
def introScene():
    
    print("Hello subject 0042. You have awoken from your tube. Do you decide to break out or not? Type your answer.")

    ans = input("Break out or not? yes / no - ")

    print("\n")

    if ans == 'yes':
        print("Okay, you decided to use your fist to break out and a alarm rings. The scientist call security but you kill them just in time and hiding them. You pretend to be one and run off living your new life.")

    else:
        print("You decided to stay in not realizing 10 scientists walked in to your room, put in pipe and you started fading away into the light never to be seen")
        return ("Mortis, You lose") # Die1

    print("\n")
    print("20 years went by, you became a smart person and haven't been caught and you have been called to a expedition to space to extract something from the moon base of N.A.S.A and you can choose your class before you go.")
    print("\n")
    print("Choose one and i'll tell the perks. Scientist/Alchemist, Engineer and The leader. The scientist/alchemist has alot of viable options but u wont have much to defend yourself and you can make potions. Engineer has the ability to defend itself well but you wont have high intelligence and wont have much options like the others. The leader has the most choices ranging 5-7 but if you die everyone would follow you and die. So what do you decide")
    
    print(" Will you choose Leader, scientist or engineer leader / scientist / engineer - (You must type the same word for a answer like engineer with no caps)")

    r()

  # choosing class and the start

    global congrats_class
    congrats_class = ("Great, that will be your class. You have arrived at the moon with your team with your leader, scientist, you alot of people and the leader's best friend. Get ready you will head out soon and if you are able to retrive it, you will be paid a wealthy amount and become general of the astronauts. Good luck team A")

  # Engineer
    if role == 'engineer':
        introEngineer()

  # Scientist
    elif role == 'scientist':
        introScientist()

  # Leader
    elif role == 'Leader':
        

########---------########---------########


  # Robot sequence and entering the base
      print("\n")

      print("You have arrived at the moon. Your mission is to extract the cataclysm of lunar which is a special moon rock fallen from the stars from a distance galaxy but it's filled with lots of traps and a laser section which i will disable soon give me time. Get ready you will head out soon and if you are able to retrive it, you will be paid a wealthy amount and become general of the astronauts.")





def hallway0():
  # Leader option


          # Maze sequence
      print("\n")

    
              # Taking for the team sequence 
 
########################################
def introScientist():

    print(congrats_class)

    print("You see 2 robots blocking the entrance. what do you do?")
    ans = input("Brew a potion / Splash an invisibility potion / Throw a molotov - (You have to type the exact same sentence of what answer you're doing)")

    if ans == 'Brew a potion':
      print("With your special alchemy skills, you started brewing it but the scent of your potion caught the robots sight. They ran and started shooting you down.")

    elif ans == 'Splash an invisibility potion':
        print("You decide to splash down a potion to everyone and you start sneaking in. The robots sense something but then it wears off as you haven't mastered the ability to do it. The robots get a call and reply that they found you.")

    elif ans == 'Throw a molotov':
      print("You grab a molotov from your secret stash and you throw it out to the robots. The robots start brutally burning and you and the others rush in to the base.")
    


    print("You enter the base and u have to choose where to go to find the cactaclysm. Where do you go?")
    ans = input("Left / Right / Hallway - ")

    if ans == 'Left':
      print("You walk left quietly and you find a locker hoping for supplies, Suddenly a dead body falls and your scientist uses his special watch to see its death and you find it he died of suffucation in the room your standing in. You decided to walk back out. You start to walk backwards and accidently go into the right door and you made a ruckus. You decide to get back up but you see 10 guards all point guns and you fall into jail.")
      return ("Mortis, You lose")

    elif ans == 'Hallway':
      print("You decide to walk through the hallway but you hear footsteps as 4 guards notice you and start shooting and you died of blood loss.")
      return ("Mortis, You lose")

    elif ans == 'Right':
      print("You go right into the door and you notice a lever and without a thought, one of your teammates pulls it and you fall seeing your friend and another person get left behind at the hallway. Gun shots could be heard, and you decide the leader's best friend is dead forever.")

      print("You all went right but you end up in a dead end where do you go?")
    ans = input("Left / Right Again - ")


    if ans == 'Right Again':
       print("The system mocks your stupidity of choosing right and traps you into a endless motion with your other teammates being oppressed to control the endless loop.")

    if ans == 'Left':
       print("You all reach each other and find a dark hallway but you realize the cataclysm of lunar is not here so you fell into a trap. You look through the ditance and see a giant smile lurking at the end of the hallway and starts running at you. No one can stop it unless it's you, your engineer or your alchemist. Who do you sacrafice?")
    ans = input("You / Engineer / alchemist - ")

    if ans == 'You':
      print("You stand up for everyone and start making a potion and putting chemicals that will disentigrate everything. You splash it on the entity but it seems to not work. He gets smacked to the near wall and starts jumping rumbling the floor and smashes him to litres of blood and darts his eye at T̷h̷̡̎ë̵̪́̎̌̀ o̸t̵̒̃̉̔̓̈́h̶ë̵r̸̼̘̔ŝ̶́.")


    elif ans == 'engineer':
      print("You stand up to protect your crewmates by building a titanium wall thinking it would stop the monster but he breaks through with ease, picks you up and brutally bites your head off and starts to kill the rest.")


    else:
      ans == 'Leader'
      print("The leader stands up but the monster starts rushing. everyone else all go to the side but everyone else dies. You rushes and attackes the monster and shines the light to see it but before that the monster disintagrates to dust.")


print("\n")

print("You all find a trapdoor and climb out but you see your best friend standing. He shouts and says that a teammate died of suffocation. You walk out to find him but see a hallway full of blood and dead bodies. You realize something is wrong as you saw your best friend die. you rethink but you come to the solution that your best friend killed them all.")


print("\n")
print("You tell the leader and the leader's best friend hears you. Oh so you found out, i really am the bad guy after all. Try to stop me if you can but you can't escape as i disrupted the ship. He says rushsing off. You divise a plan with your leader giving you two both daggers to defend and repair the ship. You all start the plan and start to fix the ship while your leader gets his best friend.")

print("\n")

print("You are sent by the engineer to grab items to help him out but you see 2 soldiers talking and practicing their aim. What do you do")
ans = input("Hide behind some boxes / Rush in / Throw a molotove - ")

          # fight enemy sequence scientist

if ans == 'Hide behind some boxes':
            print("You hide behind boxes hearing it but you realize their heading for the engineer but it's too late. You try to stop them but the engineer has died. They turn around and start shooting you rapidly.")
            print("Mortis, You lose")

elif ans == 'Rush in':
            print("You start rushing in and they are about to take aim. You dodge it but then one of them get a lucky shot and hit your knee. You are wounded and about to die but you try to hit them but they shoot you finishing you off.")
            print("Mortis, You lose")

else:
            print("You get a molotov from your secret stash and throw it. They start brutally burning to death and you run make gaining the items and materials")

            print("\n")

  # ending

print("You took out the enemies and your leader rushes back. He tells you that he had killed his best friend by himself and feels gulity and says he was the villian of this mission but i have to move on. He says he found the cactaclysm of lunar and you rush there to grab it. you extract it and go to fix the ship and fly back to earth, telling about the incident and becoming heroes.")

print("\n")
          # time skip/ epilogu
print("13 years go by and you and the scientist become teachers in space school. You are just relaxing at home when you and the scientist get teleported to the skies. A cloaked figure tells you two that he can grant anything but you will grow 30 years in age. Would you do it?")

ans = input("Yes / No - ")

if ans == 'Yes':
          print("You both accept but you don't get money but instead fall into a endless cycle of rewatching the entire incident that happened 13 years ago. The cloaked man reveals to be Lucifer-King of the underworld and he says to never trust him ever if you can see him again.")
          print("Mortis, You lose")

else:
          print("You say no and he teleports you back to your place but then your tv starts brodcasting live of the incident 13 years ago stating that you, the scientist and the leader were the main villians.")

print("The End?")

print("\n")
print("Thank you for playing: Search for the cactaclysm of lunar. It was fun making some stuff and other parts were a struggle but thank you - Creator")
print("ggs you won there may be a part 2 but we'll see. Thats the question...")



def introEngineer():
    print(congrats_class)

    print("You see 2 robots blocking the entrance. what do you do?")

    ans = input("Sneak around them / Pretend to be a robot / Hack the robots / Build a wall - (You have to type the exact same sentence of what answer you're doing)")

    if ans == 'Sneak around them':
          print("You have asked to go around and they accept. You all go around the base sneaking past the robots to the back entrance but didn't realize that there was no back entrance. You tried to go back but get caught and get killed to death.")
          return("Mortis, you lose")

    elif ans == 'Hack the robots':
          print("With your coding skills you gained you try to disrupt the robots circut to get in. You start to hack but you didn't know they had a kill code so they use it to disrupt your laptop and it explodes infront of you and your team.")
          return ("Mortis you lose")

    elif ans == 'Build a wall':
          print("You decide to make a wall and strapping some explosives. You whistle to the robots and they get distracted while you exploded it infront of them killing them and allowing you to get in.")

    elif ans == 'Pretend to be a robot':
          print("You find some left over robot junk and dress up like them. You walk through and they let you in.")



    print("You enter the base and u have to choose where to go to find the cactaclysm. Where do you go?")
    ans = input("Left / Right / Hallway - ")

    if ans == 'Left':
      print("You walk left quietly and you find a locker hoping for supplies, Suddenly a dead body falls and your scientist uses his special watch to see its death and you find it he died of suffucation in the room your standing in. You decided to walk back out. You start to walk backwards and accidently go into the right door and you made a ruckus. You decide to get back up but you see 10 guards all point guns and you fall into jail.")
      return ("Mortis, You lose")

    elif ans == 'Hallway':
      print("You decide to walk through the hallway but you hear footsteps as 4 guards notice you and start shooting and you died of blood loss.")
      return ("Mortis, You lose")

    elif ans == 'Right':
      print("You go right into the door and you notice a lever and without a thought, one of your teammates pulls it and you fall seeing your friend and another person get left behind at the hallway. Gun shots could be heard, and you decide the leader's best friend is dead forever.")

      print("You all went right but you end up in a dead end where do you go?")
    ans = input("Left / Right Again - ")


    if ans == 'Right Again':
       print("The system mocks your stupidity of choosing right and traps you into a endless motion with your other teammates being oppressed to control the endless loop.")

    if ans == 'Left':
       print("You all reach each other and find a dark hallway but you realize the cataclysm of lunar is not here so you fell into a trap. You look through the ditance and see a giant smile lurking at the end of the hallway and starts running at you. No one can stop it unless it's you, your engineer or your alchemist. Who do you sacrafice?")
    ans = input("You / Engineer / alchemist - ")

    if ans == 'alchemist':
      print("The alchemist stands up for everyone and starts making a potion and putting chemicals that will disentigrate everything. You splash it on the entity but it seems to not work. He gets smacked to the near wall and starts jumping rumbling the floor and smashes him to litres of blood and darts his eye at Ÿ̴œů.")


    elif ans == 'you':
      print("You stand up to protect your crewmates by building a titanium wall thinking it would stop the monster but he breaks through with ease, picks you up and brutally bites your head off and starts to kill the rest.")


    else:
      ans == 'Leader'
      print("The leader stands up but the monster starts rushing. everyone else all go to the side but everyone else dies. You rushes and attackes the monster and shines the light to see it but before that the monster disintagrates to dust.")


print("\n")

  # Finding out about the leaders best friend being the villan and having to fix the rocket ship scientist 
print("You all find a trapdoor and climb out but you see your best friend standing. He shouts and says that a teammate died of suffocation. You walk out to find him but see a hallway full of blood and dead bodies. You realize something is wrong as you saw your best friend die. you rethink but you come to the solution that your best friend killed them all.")




print("\n")
print("You tell the leader and the leader's best friend hears you. Oh so you found out, i really am the bad guy after all. Try to stop me if you can but you can't escape as i disrupted the ship. He says rushsing off. You divise a plan with your leader giving you two both daggers to defend and repair the ship. You all start the plan and start to fix the ship while your leader gets his best friend.")

print("\n")
print("You start fixing it and 15 minutes go by and you are nearly done. you ask your scientist to get materials while you get some of your own. Another 10 minutes went by and you see your scientist back with blood. He says he fought 2 guys but still gained the materials. You hear footsteps so you two hide and see the enemies. What do you do to attack them")
ans = input("Sneak around them / Rush in / Throw your dagger at them - ")

      # fight enemy sequence
if ans == 'Sneak around them':
          print("You try to sneak around but they easily hear your footsteps and they start shooting. Bullets start grazing you and you die of bloodloss. Before you die you see your leader rushing out and getting shot multiple times before collapsing to the ground.")
          print("Mortis, You lose")

elif ans == 'Throw your dagger at them':
          print("You decidde to throw your dagger but you realize it was a stupid idea as it missed and you have no more weapons. You try to throw hands at them but they easlily shoot you down killing you.")
          print("Mortis, You lose")

else:
          print("You 2 rush from different sides and 2 focus on you while 1 focus on the scientist. the scientist stabs 1 in the neck chopping his head off whil he sneaks behind and and stabs on in the back. The guy shoots the scientist's dagger out of his hands but you attack both and they fall to the ground.")
  # ending
          print("\n")
          print("You took out the enemies and your leader rushes back. He tells you that he had killed his best friend by himself and feels gulity and says he was the villian of this mission but i have to move on. He says he found the cactaclysm of lunar and you rush there to grab it. you extract it and go to fix the ship and fly back to earth, telling about the incident and becoming heroes.")

          print("\n")
      # time skip/ epidlogu
          print("13 years go by and you and the scientist become teachers in space school. You are just relaxing at home when you and the scientist get teleported to the skies. A cloaked figure tells you two that he can grant anything but you will grow 30 years in age. Would you do it?")

          ans = input("Yes / No - ")

          if ans == 'Yes':
              print("You both accept but you don't get money but instead fall into a endless cycle of rewatching the entire incident that happened 13 years ago. The cloaked man reveals to be Lucifer-King of the underworld and he says to never trust him ever if you can see him again.")
              print("Mortis, You lose")

          else:
              print("You say no and he teleports you back to your place but then your tv starts brodcasting live of the incident 13 years ago stating that you, the scientist and the leader were the main villians.")

              print("The End?")

              print("\n")
              print("Thank you for playing: Search for the cactaclysm of lunar. It was fun making some stuff and other parts were a struggle but thank you. ggs! Yes, i'm a molotov glazer and if u chose scientist for the hallway u wouldn't have to choose due to intellegence:/ - Creator")
              print("ggs you won there may be a part 2 but we'll see. Thats the question...")



def introLeader():


      print(congrats_class)

      print("You see 2 robots blocking the entrance. what do you do?")
      ans = input("Sneak around them / Charge / THIS IS AMERICA / sneak inside / Pretend to be a nasa worker / bribe the robot with oil / try to talk smart with economics - (You have to type the exact same sentence of what answer you're doing)")

      if ans == 'Sneak around them':
              print("Your crew follows you as you start going around but 2 men notice you while training their aim and start shooting you down.")


      elif ans == 'Pretend to be a nasa worker':
              print("You cover your spaceX logo with nasa's and you walk in but the robots scan you realising who you are eventually killing you.")


      elif ans == 'Charge':
              print("You decide to not think and become an underdeveloped homo sapian but to your surprise the robots start screaming in fear then they realize they have weapons and shoot you underdeveloped homo sapian brain you underdeveloped homo sapian")

      elif ans == 'try to talk smart with economics':
              print("Your start walking with your suit, tie, cup of tea, walking cane and a distinguished look. You walk up asking about economy, taxes and inflation. The robots eventually malfunction exploding which allowed you into the base.")

      elif ans == 'bribe the robot with oil':
              print("You pull out all your oil giving to the robots and they accept it. They start drinking it with you sneaking pass shooting the robots down with some kill code. allowing you into the base")

      else:
              print("You forgot brains and go americna style with teh THIS IS AMERICA shooting everyone with rockets, bullets, molotovs, knifes, throwing guns and more bullets killing anyone in a 50 meter radius. Which allowed you into the base.")

      print("You enter the base and u have to choose where to go to find the cactaclysm. Where do you go?")
      ans = input("Left / Right / Hallway - ")

      if ans == 'Left':
          print("You walk left quietly and you find a locker hoping for supplies, Suddenly a dead body falls and your scientist uses his special watch to see its death and you find it he died of suffucation in the room your standing in. You decided to walk back out. You start to walk backwards and accidently go into the right door and you made a ruckus. You decide to get back up but you see 10 guards all point guns and you fall into jail.")
          return ("Mortis, You lose")

      elif ans == 'Hallway':
          print("You decide to walk through the hallway but you hear footsteps as 4 guards notice you and start shooting and you died of blood loss.")
          return ("Mortis, You lose")

      elif ans == 'Right':
          print("You go right into the door and you notice a lever and without a thought, one of your teammates pulls it and you fall seeing your friend and another person get left behind at the hallway. Gun shots could be heard, and you decide the leader's best friend is dead forever.")

          print("You all went right but you end up in a dead end where do you go?")
      ans = input("Left / Right Again - ")


      if ans == 'Right Again':
           print("The system mocks your stupidity of choosing right and traps you into a endless motion with your other teammates being oppressed to control the endless loop.")

      if ans == 'Left':
           print("You all reach each other and find a dark hallway but you realize the cataclysm of lunar is not here so you fell into a trap. You look through the ditance and see a giant smile lurking at the end of the hallway and starts running at you. No one can stop it unless it's you, your engineer or your alchemist. Who do you sacrafice?")
      ans = input("You / Engineer / alchemist - ")


                  # Taking for the team sequence 
      if ans == 'alchemist':
              print("The alchemist stands up for everyone and starts making a potion and putting chemicals that will disentigrate everything. You splash it on the entity but it seems to not work. He gets smacked to the near wall and starts jumping rumbling the floor and smashes him to litres of blood and darts his eye at Ÿ̴œů.")


      elif ans == 'engineer':
              print("The engineer stands up and take it by building a titanium wall thinking it would stop the monster but he breaks through with ease, picks you up and brutally bites his head off and starts to kill the rest.")


      else:
              ans == 'You'
              print("You stand up but the monster starts rushing. everyone else all go to the side but everyone else dies. You rushes and attackes the monster and shines the light to see it but before that the monster disintagrates to dust.")


      print("\n")

          # Finding out about the leaders best friend being the villan and having to fix the rocket ship scientist 
      print("You all find a trapdoor and climb out but you see your best friend standing. He shouts and says that a teammate died of suffocation. You walk out to find him but see a hallway full of blood and dead bodies. You realize something is wrong as you saw your best friend die. you rethink but you come to the solution that your best friend killed them all.")

      print("\n")
      print("You tell the remaning crew and your best friend hears you. Oh so you found out, i really am the bad guy after all. Try to stop me if you can but you can't escape as i disrupted the ship. He says rushsing off. You divise a plan with you engineer and alchemist with you giving both two daggers to defend and repair the ship. The engineer and alchemist start the plan and start to fix the ship while you go for your best friend.")

      print("\n")

      print("You are chasing your best friend throughout the nasa base and he starts to throw his dagger at you. What do you do?")
      ans = input("Move left / Move right / Jump / Crouch and slide / Try to catch the knife / let it hit you - ")

          # fight enemy sequence scientist

      if ans == 'Move left':
            print("You go to the left side and he throws at you with a point blank shot making you loose blood. You try to tend to the wound but he catches to you and is about to stab you but you stab him instead. In the end you both die with the mission being unknown from then on")
            return ("Mortis, You lose")

      elif ans == 'Jump':
                    print("He throws his dagger at you and you jumpm above it but you still get stabbed losing blood eventually being unable to walk and being in heaven.")
                    return ("Mortis, You lose")

      elif ans == 'let it hit you':
                    print("You let the knife hit you in the chest and you start bleeding out. Your friend sees your dead body and retrives the cactaclysm of lunar for himslef ")
                    print("you lose.")

      elif ans == 'Try to catch the knife':
                  print("He throws it at you and you life your hand out to catch it and miraculously you caught it. You chuck it back at him with all your stregth hitting him with him agaisnt the wall.")

      elif ans == 'Move right':
              print("You move right and he throws his knife and misses so now you have to chase him. Luckilt you're not battered and you catch up stomping on his leg so he can't walk and he's know pinned agasint the wall. You see his hamd reaching something and he grabbes a knife from his back pocket but you hold it threating him.")



      else:   
              print("You crouch and start sliding down the slippery floor catching up to him. He tries to stab you but you take the knife out of his hands and you break his leg with him lying agaisnt the wall")

              print("\n")

          # ending

              print("You injure your best friend as he tries to play smart with you put you throw the knife at his head with no emotion. You start trailing back to the exit but you find a door full of steam. you decide to open it and theres test tubes filled with alien-like creatures. You start remembering your past and realize you were one of them. You look around and should see a crystal charging the test tubes up. You take a gander at it and scan it with you watch. Scanning... It is a the Cactaclysm of lunar. your watch tells you.")

              print("\n")


              print("You pick it up and the test tubes shut off for some reason. You see that the cactaclysm of lunar powered it and you take it back out. You go pass your best friend's body lying agaisnt the wall. You rush back to the engineer and alchemist realising your guilt. You tell everything and become heroes but you never told what happened to anyone but the agents that sent you")
                  # time skip/ epilogu
              print("13 years go by and you become the head of the science facility and you hear rumours about people getting teleported to the sky. You finsihed your job and when you head back to your familiy you suddenly get teleported. He asks if you want to revive your best friend. Do you accept?")

              ans = input("Yes / No - ")

      if ans == 'yes':
                    print("\n")
                    print("You accept the deal and you get teleported back at your office but it isn't the science one instead its a normal one. You look on the news and see the incident on nasa's base and you see your dead friend's body with nasa winning. You get a voice from above and reveals himslef and lucifer-king of the underworld and he says nothing can change someones fate and you were the cause of it you try to talk back but you get teleported back. You realise you created a time paradox.")


      else:
              print("You say no and he teleports you back to your main office seeing a perfect life. It seems all happy but on all billboards it talks about the abadoned misson that it was actually a massacre and says you, the engineer and the alchemist are badguys causing the stolen cactaclysm.")

              print("The End?")

              print("\n")
              print("Thank you for playing: Search for the cactaclysm of lunar. It was fun making some stuff and other parts were a struggle - Creator")
              print("ggs you won there may be a part 2 but we'll see. Thats the question...")
              print("\n")
