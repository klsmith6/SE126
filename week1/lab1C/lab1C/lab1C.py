#Karissa Smith
#se126.02
#7/23/2019

#Lab 1C


#FUNCTIONS--------------------------------------------------

#capacity--asks user for max capacity of the rooms and returns that value
def capacity():

    #roomCap will ask user the max capacity for the room they are renting
    roomCap = int(input("Please Enter total room capacity: "))
    return roomCap

#attendees-- asks user for how many people are attending the conference and returns that value
def attendees():
    #pplAttend will represent the number of people attending the event
    pplAttend = int(input("Please Enter Number of People Attending: "))
    return pplAttend

#register--calculates the difference between capacity and attendees
def register(roomCap, pplAttend):
    if (roomCap > pplAttend):
        #morePpl will represent how many more people can attend event 
        morePpl = roomCap - pplAttend
        return morePpl
    elif (roomCap < pplAttend):
         #lessPpl will represent how many people the user is over in order to follow fire safety regulations
        lessPpl = pplAttend - roomCap
        return lessPpl
    
#again-- this will ask user if they want to check any more rooms
def again():
    answer = input("Would you like to check another room?")
    answer = answer.lower()
    while answer != 'y' and answer != 'n':

        print("*****ERROR*****")
        print("Sorry! I do not recognize what you are trying to do. please enter y for yes or n for no")
        answer = input("Would you like to check another room?")
        answer = answer.lower()
    
    return answer

#BASE PROGRAM-----------------------------------------------

print("Welcome to my Event Planner")
print("This program will determine if your party is in code with our fire regulations")


ans = 'y'

while ans == 'y':
    
    #this will represent roomCap from the capacity function
    rmCap = capacity()
    #this will represent pplAttend from the attendees function
    numPpl= attendees()
    #this will represent more or less people from the register function
    difference = register(rmCap, numPpl)

    #these will determine if the conference can be held in the room or not
    if (rmCap > numPpl):
        print("Your event follows our fire regulations! you may hold your event at our establishment")
        print("If you wanted to, you could invite {0} more people to your event!".format(difference))
    elif (rmCap < numPpl):
        print("I'm sorry, you have too many people coming to your event.")
        print("You can still host your event in this room if you have {0} less people attending your event.".format(difference))
    elif(rmCap == numPpl):
        print("Your Party follows fire regulations, but you have reached the max capacity of the room!")
    
    ans = again()

#exited loop
print("Goodbye!")



