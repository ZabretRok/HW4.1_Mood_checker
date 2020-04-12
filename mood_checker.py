user_mood=input("What mood are we in today?").capitalize().lower()

if(user_mood)== "happy":
    print("It is great to see you happy!")
elif(user_mood)== "nervous":
    print("Take a deep breath 3 times.")
elif(user_mood)== "sad":
    print("Don't worry, everything will be alright.")
elif(user_mood)== "excited":
    print("For what reason?")
elif(user_mood)== "relax":
    print("Good to hear.")
else:
    print("I don't recognize this mood")