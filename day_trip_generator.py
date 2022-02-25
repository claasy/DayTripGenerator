destinations=["London", "Godric's Hollow", "Hogsmead", "Chudleigh"]
restaurants=["The Leaky Cauldron", "Florean Fortescue's Ice Cream Parlour", "The Hopping Pot", "Sugarplum's Sweet Shop",]
transportation=['apparition', 'floo powder', 'The Knight Bus', 'portkey']
entertainment=['attend a Quidditch Game', 'compete in the Tri-Wizard Tournament', 'learn how to fly on a broom', 'practice your spell-casting']
import random
random_destination=(random.choice(destinations))
random_restaurants=(random.choice(restaurants))
random_transportation=(random.choice(transportation))
random_entertainment=(random.choice(entertainment))
y_n = True
def destination_choice ():
    destination = random_destination
    return destination
destination=random_destination
choice=input(f'Welcome witches and warlocks, I am The Sorting Hat! Get ready to be sorted into your very own bewitching experience! We have selected {random_destination} for you! Will you be partaking? Please enter Y or N: ')
other_choice = True
while other_choice is True:
    if choice == "Y" or "y":
        other_choice = False
        def restaurant_choice ():
            restaurants = random_restaurants
            return restaurants
        restaurant=random_restaurants
        choice=input(f'Good choice! We have selected {random_restaurants} for your fine dining experience. Do you like this choice? Please enter Y or N: ')
        other_choice = True
        while other_choice is True:
            if choice == "Y" or "y":
                other_choice - False
                def transportation_choice ():
                    transportation = random_transportation
                    return transportation
                transportation=random_transportation
                choice=input(f'Jolly good! For your luxurious mode of transportation we have chosen {random_transportation}, is this acceptable? Please enter Y or N: ')
            
            else:
                other_choice = True
                choice=input(f'For your luxurious mode of transportation we have chosen {random.choice(transportation)}, is this acceptable? Please enter Y or N: ')
    if choice == "N,n":
        other_choice = True
        choice=input(f'We have selected {random.choice(destinations)} for you! Will you be partaking in this option? Please enter Y or N: ')
    else:
        print=input(f'')



def transportation_choice ():
    transportation = random_transportation
    return transportation
transportation=random_transportation
choice=input(f'Jolly good! For your luxurious mode of transportation we have chosen {random_transportation}, is this acceptable? Please enter Y or N: ')
def entertainment_choice ():
    entertainment = random_entertainment
    return entertainment
entertainment=random_entertainment
choice=input(f"I'm super jealous of the amazing time you're going to have! For your entertainment we've selected for you to {random_entertainment}, is this to your liking? Please enter Y or N: ")

#'Have a bloody good time!'






