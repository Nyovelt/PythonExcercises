import random, time 

girls = ["Chocola", "Vanilla", "Minaduki"]  #Nekopara

for i in range(3):

    the_name = random.sample(girls, 1)

    #the_name = random.choice(["Chocola", "Vanilla", "Minaduki"])

    the_one = "".join(the_name)
    
    #print(the_one)

    your_love = input("Please input the name from girls list: ")

    if the_one == your_love:
        print("Nyan")
    else:
        print("Restart")

    time.sleep(3)
