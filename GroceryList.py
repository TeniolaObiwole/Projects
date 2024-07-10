#Create a Grocery to do list.

#print greeting and collect user's name.
print("Hello! ")
userName = input("What's your name?\n").capitalize()
print("Okay {},let's create your grocery list!".format(userName))
groceryList = []

def listItems():
    #Collect the items of a grocery list from a user.
    groceryItem = input('\nEnter grocery item:\n')
    groceryList.append(groceryItem)

def lastItem():
    again = True
    while again:
        listCompleted = str(input('Is this the last item? Y/N?\n'))
        if listCompleted.upper() == 'N':
            listItems()
        elif listCompleted.upper() == 'Y':
            again = False
            #print items in the list
            print("\n{}'s Grocery List".format(userName))
            items = enumerate(groceryList, start = 1)
            for index,item in items:
                print('{}.'.format(index), item)
            print('\nHappy Shopping!')    
        else:
            print('Incorrect input. Try again.')
            continue



def main():   
    #collect grocery item and create grocery list.
    listItems()
    #to determine end of list.
    lastItem()
        
if __name__ == '__main__':
    main()
