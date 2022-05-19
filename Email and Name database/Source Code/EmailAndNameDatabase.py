### Main function ###
def main():
    ### Initializing global dictionary ###
    global EmailNameDict
    EmailNameDict = {}

    print ("Hello, welcome to the name and email address database!")

    ### Menu ###
    print ("\nPlease enter an option from the following:")
    menu()

    ### Choice input with while loop ###
    Choice = int(input("Please enter a number from the options: "))
    while Choice:
        if Choice == 1:
            LookUp()

        elif Choice == 2:
            AddNew()

        elif Choice == 3:
            ChangeEmail()

        elif Choice == 4:
            DeleteEmail()

        elif Choice == 5:
            SaveEmailDict()
            print ("\nProgram terminated!")
            break

        ### After function choice ###
        menu()
        Choice = int(input("Please enter an option: "))



### Function to display menu ###
def menu():
    ### Printing menu options ###
    print ("1. Look up an email address")
    print ("2. Add a new name and email address")
    print ("3. Change an existing email address")
    print ("4. Delete a name and email address")
    print ("5. Quit the program")
    


### Function to load emails to be read ###
def LoadEmailDict():
    ### Opening text file into a variable for reading ###
    NameEmailTxt = open("NameEmail.txt", "r")

    ### Adding each line into the global dictionary ###
    for line in NameEmailTxt:
        line = line.split()
        EmailNameDict[line[0]] = line[1]

    ### Closing the file ###
    NameEmailTxt.close()



### Function to save emails into file ###
def SaveEmailDict():
    ### Opening file for writing ###
    NameEmaiTxt = open("NameEmail.txt", "w")

    ### Write dictionary into file line by line ###
    for k , v in EmailNameDict.items():
        NameEmaiTxt.write("{0} {1}" "\n".format(k , v))
    
    ### Closing file ###
    NameEmaiTxt.close()



### Function to look up name in database ###
def LookUp():
    ### Call LoadEmailDict() to load dictionary ###
    LoadEmailDict()
    UserInput = input("\nPlease enter a first name to look up: ")

    ### If statement to determine if UserInput is inside dictionary ###
    if UserInput not in EmailNameDict.keys():
        print ("Email not in database!\n")

    ### Display dictionary if UserInput is in dictionary ### 
    for k , v in EmailNameDict.items():
            if UserInput == k:
                print("\nEmail found!")
                print ("First Name:" , k)
                print ("Email:", v, "\n")



### Function to add new name and email to database ###
def AddNew():
    ### Call LoadEmailDict() to load dictionary ###
    LoadEmailDict()
    NameInput = input("\nPlease enter a new first name: ")
    EmailInput = input("Please enter a new email address: ") 
    

    ### If statement to determine if NameInput is inside dictionary ###
    if NameInput in EmailNameDict.keys():
        print ("Name already exists in database!\n")
    
    ### Else statement to put name and email into dictionary ###
    else:
        EmailNameDict[NameInput] = EmailInput
        print ("Name and email added to database!\n")



### Function to change email in database ###
def ChangeEmail():
    ### Call LoadEmailDict() to load dictionary ###
    LoadEmailDict()
    NameInput = input("\nPlease enter first name: ")
    EmailInput = input("Please enter a new email address: ")
    print("Email changed!\n")

    ### Iterating through all keys to see if NameInput is in dictionary ###
    for k in EmailNameDict.keys():
        if NameInput == k:
            EmailNameDict[k] = EmailInput



### Function to remove email and name in database ###
def DeleteEmail():
    ### Call LoadEmailDict() to load dictionary ###
    LoadEmailDict()

    ### Deleting NameInput from dictonary ###
    NameInput = input("\nPlease enter first name to remove information from database: ")

    if NameInput not in EmailNameDict.keys():
        print ("Error name not in database!\n")
    else:
        del EmailNameDict[NameInput]
        print("Information Removed!\n")



### Calling main function ###
main()
