
# created an empty dictionary in phoneBook.txt in another file

import json

def phoneBook():
    def phoneBookProfiles(userName, userSurname): 
        #print(phoneBookDict)      
        phoneBookDict[userName+userSurname] = dict()
        userPhoneBook = phoneBookDict[userName+userSurname] 


    def createContact(userPhoneBook):
        name = input('enter contacts first name:\n').lower()
        surname = input('enter contacts surname:\n').lower()
        #add code to make sure it's a real email
        email = input('enter contacts email:\n')
        workPlace = input('enter contacts work place address:\n')
        phoneNumber = []
        count = int(input('how many phone numbers do you wish to save for this contact?\n'))
        if count == 1:
            #add code to make sure the number is 11
            number = int(input('enter the phone number:\n'))
        else:
            for i in range(count):
                number = int(input('enter the phone number:\n'))
                phoneNumber.append(number)
        
        userPhoneBook[name+surname] = {}
        for i,j in userPhoneBook.items():
            if i == name+surname:
                j['name'] = name
                j['surname'] = surname
                j['email'] = email
                j['work place'] = workPlace
                j['phone number'] = phoneNumber
        print(userPhoneBook)

    def updateContact(userPhoneBook:dict):
        contactNameToBeUpdated = input('enter contact name to be updated:\n')
        contactSurnameToBeUpdated = input('enter contact surname to be updated:\n')
        print('what do you wish to update?')
        prompt = int(input('1. contact name\n2. contact surname\n3. contact email\n4. contact work place\n5. contact phone number'))
        
        if prompt == 1:
            #add code to confirm name to be updated
            newName = input('enter contacts new name')
            for i,j in userPhoneBook.items():
                if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                    j['name'] = newName
                    print('name updated\n',newName)
        elif prompt== 2:
            #add code to confirm surname to be updated
            newSurname = input('enter contacts new surname\n')
            for i,j in userPhoneBook.items():
                if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                    j['surname'] = newSurname
                    print('surname  updated\n', newSurname)
        elif prompt== 3:
            #add code to confirm email to be updated
            newEmail = input('enter contacts new email\n')
            for i,j in userPhoneBook.items():
                if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                    j['email'] = newEmail
                    print('email updated\n',newEmail)
        elif prompt== 4:
            #code to confirm work place to be updated
            newWorkPlace = input('enter contacts new work place\n')
            for i,j in userPhoneBook.items():
                if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                    j['work place'] = newWorkPlace
                    print('work place updated\n',newWorkPlace)
        elif prompt == 5:
            #code to confirm phone number to be updated
            removeOrAdd = int(input('1. remove existing phone number and add a new one.\n2. add new phone number'))
            newPhoneNumber = input('enter contacts new phone number\n')
            if removeOrAdd == 1:
                for i,j in userPhoneBook.items():
                    if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                        currentPhoneNumber = j['phone number'] 
                        noOfPhoneNumbers = len(currentPhoneNumber)
                        if noOfPhoneNumbers == 1:
                            j['phone number']  = []
                            currentPhoneNumber.append(newPhoneNumber)
                            j['phone number'] = currentPhoneNumber
                            print('phone number updated\n',currentPhoneNumber)

                        else:
                            print('there are {} phone numbers, which would you like to update?\n'.format(noOfPhoneNumbers))
                            #add code for if the phone number is not in the list
                            for i in currentPhoneNumber:
                                print(i)
                            selectedPhoneNumber = input('enter selected phone number')
                            currentPhoneNumber.remove(selectedPhoneNumber)
                            currentPhoneNumber.append(newPhoneNumber)
                            print('phone number updated\n',currentPhoneNumber)
            elif removeOrAdd == 2:
                for i,j in userPhoneBook.items():      
                    if i == contactNameToBeUpdated+contactSurnameToBeUpdated:
                        currentPhoneNumber = j['phone number'] 
                        currentPhoneNumber.append(newPhoneNumber)
                        j['phone number'] = currentPhoneNumber
                        print('phone number updated\n',currentPhoneNumber)
            else:
                print('incorrect selection.')


    def deleteContact(userPhoneBook:dict):
        contactNameToBeDeleted = input('enter contact name to be deleted:\n')
        contactSurnameToBeDeleted = input('enter contact surname to be deleted:\n')
        print('what do you wish to delete?')
        prompt = int(input('1. contact \n3. contact email\n4. contact work place\n5. contact phone number'))

        if prompt == 1:
            #add code to confirm contact name to be deleted
            newName = input('enter contacts new name')
            for i,j in userPhoneBook.items():
                if i == contactNameToBeDeleted+contactSurnameToBeDeleted:
                    del userPhoneBook[contactNameToBeDeleted+contactSurnameToBeDeleted]
                    print('contact updated\n')
        elif prompt== 2:
            #add code to confirm email to be deleted
            for i,j in userPhoneBook.items():
                if i == contactNameToBeDeleted+contactSurnameToBeDeleted:
                    j['email'] = '-'
                    print('email deleted\n',)
        elif prompt== 3:
            #add code to confirm work place to be deleted
            for i,j in userPhoneBook.items():
                if i == contactNameToBeDeleted+contactSurnameToBeDeleted:
                    j['work place'] = '-'
                    print('work place deleted\n',)
        elif prompt == 5:
            for i,j in userPhoneBook.items():
                if i == contactNameToBeDeleted+contactSurnameToBeDeleted:
                    currentPhoneNumber = j['phone number'] 
                    noOfPhoneNumbers = len(currentPhoneNumber)
                    if noOfPhoneNumbers ==1:
                        j['phone number'] = []
                    else:
                        print('there are {} phone numbers, which would you like to delete?\n'.format(noOfPhoneNumbers))
                        #add code for if the phone number is not in the list
                        for i in currentPhoneNumber:
                            print(i)
                        selectedPhoneNumber = input('enter selected phone number')
                        currentPhoneNumber.remove(selectedPhoneNumber)
                        print('phone number deleted\n')


        
       
    userName = input('enter your name\n')
    userSurname = input('enter your surname\n')
    phoneBookProfiles(userName, userSurname)
    print(phoneBookDict)

    print('hello {} {}.\nwhat would you like to do?\n'.format(userName,userSurname))

    entry = int(input('1. to create contact, enter 1.\n2. update contact, enter 2.\n3. delete contact, enter 3.\n\n'))
    
    if entry == 1:
        createContact(userPhoneBook)
        #save to phonebook()
    if entry == 2:
        updateContact(userPhoneBook)
        #save to phonebook()
    if entry == 3:
        deleteContact(userPhoneBook)
        #save to phonebook()


if __name__ == '__main__':
    phoneBookDict = json.load(open('phoneBook.txt'))
    phoneBook()



        



   

