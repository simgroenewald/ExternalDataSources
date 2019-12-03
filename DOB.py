# Compulsory Task 1

# Opens the file for reading and writing
birthDate = open ("DOB.txt","rt+")
print ("NAME:\n")

# Will run for every line in the file and starts a new empty string every time
for line in birthDate:

    string = ""
    string = string + line # The line is stored in the variable string
    stringSplit = string.split()# String gets split into a list of words

    lstLength = len (stringSplit) # This determines the amount of words in the list
    nameLength = lstLength - 4 # This determines how many first names the person has
    fullnameLength = lstLength - 3 # This determines how lon their fullname is

    name = "" # Declares empty variable name

    # Will run for the amount of first names
    for i in range (0,nameLength):
        name = name + (string[i])
    # Will run for only the Surname
    for i in range (nameLength,fullnameLength):
        name = name + ". " + (stringSplit[i])

    print (name)

# Closes the file
birthDate.close()

# Leaves white space
print ("\n")

# Reopens the file
birthDate = open ("DOB.txt","rt+")
print ("Birthdate:\n")

# Will run for every line in the fie
for line in birthDate:

    string = ""
    string = string + line # The line is stored in the variable string
    stringSplit = string.split() # String gets split into a list of words 

    lstLength = len (stringSplit) # This determines the amount of words in the l
    nameLength = lstLength - 4 # This determines how many first names the person
    fullnameLength = lstLength - 3 # This determines how lon their fullname is

    date = "" # Declares empty variable
    
    # Will run from the fullnameLength position untill the full length of the list
    for i in range (fullnameLength,lstLength):
        date = date + (stringSplit[i]) + " " 

    print (date)
birthDate.close()
    
    
