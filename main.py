WizardName = 'Bromedius'
print('Welcome, welcome. I am ' + WizardName + '.')
print('What is your name, friend, and fellow traveler?')
print()
Usern = input()
print()
print(Usern + "... what kind of imbecile has a name like that?")
print()
ImbecileType = input()
print() 
print (ImbecileType + '?! ' + ImbecileType + "!! I can't believe you even remember that long extinct culture! *laughs* Ah, you sure have a natural joketeller in you...") 
print("What do you reckon? What do you think your favorite hobby is?")
print()
FavoriteHobby = input()
print()
print("Wow. That is the most obscure hobby in existence.")
if FavoriteHobby == "Trying to shut you up" or "Trying to shut you up." or "Shutting you up" or "Shutting you up."or "Making you shut up" or "Making you shut up." or "Trying to make you shut up." or "Trying to make you shut up":
  print ('Also, sorry to say it, ' + Usern + ', but that sounds kind of hopeless.')
print("But Anyways, I'm just a humble game dealer, and you must figure out your strengths and weaknesses.")
print("You have 15 points. Divide them between Strength, Dexterity, Intelligence, and being an imbecile.")
for tries in range(4999959999999998999997529):
  print("How many points would you like to put into Strength?")
  print() 
  Strength = int(input())
  if Strength == 15:
    print()
    print("Wow. You're strong. Also a braindead imbecile. And horrible at jumping. You have expended all your points, and thus you will not have an opportunity to put points into Dexterity or Intelligence.")
    break
  elif Strength > 15:
    print()
    print("You were so tough that you generated your own gravitaional field,  floated off into space, and suffocated. Retry.")
  elif Strength < 0:
    print()
    print("You were so skinny that you turned into a stick and died. Retry.")
  elif Strength < 15:
    print()
    print("You are so weak. I can't believe you. NERD!")
    print("What Dexterity do you want?")
    print()
    Dexterity = int(input())
    if Dexterity+Strength > 15:
      print()
      print("Your dexterity and strength combined exceed te power of the demi-gods. The Gods are angry, so they kill you. Retry.")
    elif Dexterity == 15:
      print()
      print("Wow. You are quite dexterous. But unfortunately you are as strong as a twig,and less intelligent than an ant. Hence you cannot do your Intelligence Stat.")
      break
    elif Dexterity > 15:
      print()
      print("Your joints move so fast that you manage to jump into space, before you falling to your eventual death due to suffocation. At least you can do 40 backflips per second while you die!")
    elif Dexterity < 0:
      print()
      print("You are so un-dexterous that your joints stop working. As a statue, you wach as all your loved ones die. Retry.")
    elif Dexterity < 15:
      print("You UNDEXTEROUS NERD!")
