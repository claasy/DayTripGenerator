#I'm struggling with the user's selection and where to store that as a variable and what to save it as so I can use it again. I thnk I'm getting my variable confused on what one will be random and what one saves their choice. I will be re-submitting once I have that figured out.
destinations=["London", "Godric's Hollow", "Hogsmead", "Chudleigh"]
restaurants=["The Leaky Cauldron", "Florean Fortescue's Ice Cream Parlour", "The Hopping Pot", "Sugarplum's Sweet Shop"]
transportation=["apparition", "floo powder", "The Knight Bus", "portkey"]
entertainment=["attend a Quidditch Game", "compete in the Tri-Wizard Tournament", "learn how to fly on a broom", "practice your spell-casting"]
import random
random_destination=(random.choice(destinations))
random_restaurants=(random.choice(restaurants))
random_transportation=(random.choice(transportation))
random_entertainment=(random.choice(entertainment)) 
def destination_choice ():
    destination=random_destination
    return destination
def restaurant_choice ():
    restaurant=random_restaurants
    return restaurant
def transportation_choice ():
    transportation=random_transportation
    return transportation
def entertainment_choice ():
    entertainment=random_entertainment
    return entertainment    
other_choice = True
destination=random_destination
y_n_answer=input(f'Welcome witches and warlocks, I am The Sorting Hat! I will be sorting you into your very own magical experience! I have selected {random_destination} for you! Do you like this village? Please enter Y or N: ')
while other_choice is True:
    if y_n_answer== "N" or y_n_answer=="n": #Answer=No
        destination_selection=random_destination
        y_n_answer=input(f'Will it be {destination_selection} for you then? Please enter Y or N: ')
    else: #Answer=Yes
        print(destination_selection)
        transportation=random_transportation
        y_n_answer=input(f'Brilliant! You will be traveling via {random_transportation}. Are you dressed appropriately? Please enter Y or N: ')
        while other_choice is True:
            if y_n_answer=="N"or y_n_answer=="n": #Answer=No
                y_n_answer=input(f'Is {random.choice(transportation)} better for you? Please enter Y or N: ')
            else: #Answer=Yes
                entertainment=random_entertainment
                y_n_answer=input(f'I hope you brought your wizarding robes! Would you like to {random_entertainment}? Please enter Y or N: ')      
                while other_choice is True:
                    if y_n_answer == "N" or y_n_answer =="n": #Answer=No
                        y_n_answer=input(f'Is {random.choice(entertainment)} better for you? Please enter Y or N: ')
                    else: #Answer=Yes
                        restaurant=random_restaurants
                        y_n_answer=input(f'Right-O! We now have a reservation for you at {random_restaurants}, Shall we keep these? Please enter Y or N: ')
                        while other_choice is True:
                            if y_n_answer == "N" or y_n_answer =="n": #Answer=No
                                y_n_answer=input(f'Is {random.choice(restaurants)} better suited for you? Please enter Y or N: ')
                            else:
                                y_n_answer=input(f"Jolly good! Prepare for your very own magical excursion! You will arrive in {random_destination} and travel by {random_transportation}, where you will {random_entertainment}. Your evening will conclude at {random_restaurants}. I hope everything is to your liking? Please enter Y or N: ")
                                
                                
                                #Thank you for allowing me to serve you and I hope #you have a bloody good time! Here is what you've selected; for your destination you have chosen: {random_destination}, "
#Destination: {random_destination}
#Transportation: {random_transportation}
#Restaurant: {random_restaurant}
#Entertainment: {random_entertainment}
#input(f"Would you like to finalize this trip? Enter Y or N: "
#""')