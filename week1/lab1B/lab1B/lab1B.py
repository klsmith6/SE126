#Karissa Smith
#se126.02
#7/23/2019

#Lab 1B

#BASE PROGRAM------------------------------------------------

print("Welcome to my Event Planner")
print("This program will determine if your party is in code with our fire regulations")

#answer will represent the answer keeping us in the loop
answer = 'y'

while answer == 'y':

    #roomCap will ask user the max capacity for the room they are renting
    roomCap = int(input("Please Enter total room capacity: "))

    #pplAttend will represent the number of people attending the event
    pplAttend = int(input("Please Enter Number of People Attending: "))

    #if room capacity is  > people attending, this statement will print that the event can be held
    if (roomCap > pplAttend):

        print("Your event follows our fire regulations! you may hold your event at our establishment")

        #morePpl will represent how many more people can attend event 
        morePpl = roomCap - pplAttend
    
        print("If you wanted to, you could invite {0} more people to your event!".format(morePpl))

    elif (roomCap < pplAttend):
        print("I'm sorry, you have too many people coming to your event.")
    
        #lessPpl will represent how many people the user is over in order to follow fire safety regulations
        lessPpl = pplAttend - roomCap
    
        print("You can still host your event in this room if you have {0} less people attending your event.".format(lessPpl))

        print("")

    answer = input("Would you like to check another room?")
    answer = answer.lower()
    while answer != 'y' and answer != 'n':

        print("*****ERROR*****")
        print("Sorry! I do not recognize what you are trying to do. please enter y for yes or n for no")
        answer = input("Would you like to check another room?")
        answer = answer.lower()
    

 
    


print("Goodbye!")