#Developer Name: Than Myint Wai-13119134
#Date          : 8th to 20th April 2016
#Description   : In this program, there are 4 main features. These are as follow:
#                   - Let the user to retrieve the data(item information-ID,Name,Description,Price,AvailableToHire)
#                   - Let the user to hire the items these are available
#                   - Let the user to return the items these were hired
#                   - Let the user to add new items
#               : All of these information or data about items are stored in a csv file
#Total Number of Functions: 14

#sample format of CSV file used in this program
#This can be download from the internet via the application OR
#Use the auto genarated file
'''

0,Zero,8505,n
1,One,10,n
2,Two,29440,n
3,Three,30,n
4,Testing1,99,n
5,Testing2,999,n
6,testing6,9,n
7,Testing5,90,n

'''
import os
import os.path
import csv
keepGoing = True
import requests
from requests.exceptions import ConnectionError

#-------------------------------------------------------------------------------------------
def displayBy(inputList,sortedByValue,whatFor):
    forWhat = whatFor
    reader_list = inputList #string list
    sortedValueAgent = sortedByValue #integer list

    for i in range(len(sortedValueAgent)):
        for j in range(len(reader_list)):
            id = int(reader_list[j][0])
            available = str(reader_list[j][3])
            price = float(reader_list[j][2])
            if(id == sortedValueAgent[i]):
                if ((available == 'y' and forWhat == 'L')or(available == 'y' and forWhat == 'H')):
                    #print(reader_list[j][0].ljust(3),"-","\t",reader_list[j][1].ljust(50),"\t","=$",format(float(reader_list[j][2]),"6.2f"))
                    print(reader_list[j][0].ljust(3),"-","\t",reader_list[j][1].ljust(50),"\t","= $",format(price,"6.2f").rjust(9))
                else:#((available == 'n' and forWhat == 'L')or(available == 'n' and forWhat == 'R')):
                    if(available == 'n' and forWhat == 'L'):
                        print(reader_list[j][0].ljust(3),"-","\t",reader_list[j][1].ljust(50),"\t","= $",format(price,"6.2f").rjust(9),"\t","*")
                    if (available == 'n' and forWhat == 'R'):
                        print(reader_list[j][0].ljust(3),"-","\t",reader_list[j][1].ljust(50),"\t","= $",format(price,"6.2f").rjust(9))
def sortingBy(inputListReader,byWhat):
    reader_List = inputListReader
    howTo = str(byWhat)
    sortedItem = []
    unsortedItem = []
    tempSortedID = []
    listSize = len(reader_List)

    if howTo == 'N':
        for i in range(listSize):
            sortedItem.append(reader_List[i][1])
            unsortedItem.append((reader_List[i][1]))
        #print("BeforeSorting",sortedItem)
        sortedItem.sort()
        #print("AfterSorting",sortedItem)
        for j in range(len(sortedItem)):
            for k in range(len(sortedItem)):
                if sortedItem[j] == unsortedItem[k]:
                    tempSortedID.append(k)
        #print("SortedID",tempSortedID)
        #print(reader_List)
        displayBy(reader_List,tempSortedID,'L')
    elif howTo == 'P':
        for i in range(listSize):
            sortedItem.append(float(reader_List[i][2]))
            unsortedItem.append(float(reader_List[i][2]))
        #print("BeforeSorting",sortedItem)
        sortedItem.sort()
        #print("AfterSorting",sortedItem)
        for j in range(len(sortedItem)):
            for k in range(len(sortedItem)):
                if sortedItem[j] == unsortedItem[k]:
                    tempSortedID.append(k)
        #print("SortedID",tempSortedID)
        #print(reader_List)
        displayBy(reader_List,tempSortedID,'L')
    else:
        for i in range(listSize):
            tempSortedID.append(i)
        displayBy(reader_List,tempSortedID,'L')
def listingTitile(whatFor):
    if whatFor == "L":
        print("All items on file (* indicates item is currently out):")
        print("ID".ljust(3)," ","\t","Description".ljust(50),"\t","    ","Price".ljust(6),"\t","Hired".ljust(6))
    else:
        print("ID".ljust(3)," ","\t","Description".ljust(50),"\t","    ","Price".ljust(6),"\t")
def listing():
    validCommand = False
    with open("items.csv") as f_obj_read:
        reader_List = csv.reader(f_obj_read)
        reader_List = list(reader_List)
        while validCommand==False:
            #print("Sorted By :")
            #print('            ID    --> Type in  I ')
            #print('            Name  --> Type in  N')
            #print("            Price --> Type in  P")
            print("""Sorted By:
            (I)ID
            (N)Name
            (P)Price""")
            listBy = input(">>")
            if(listBy == 'I' or listBy == 'i'):
                validCommand = True
                listingTitile('L')
                sortingBy(reader_List,'I')
            elif(listBy == 'N' or listBy == 'n'):
                validCommand = True
                listingTitile('L')
                sortingBy(reader_List,'N')
            elif(listBy == 'P' or listBy == 'p'):
                validCommand = True
                listingTitile('L')
                sortingBy(reader_List,'P')
            else:
                print("*****Invalid Command*****")
                validCommand = False
    f_obj_read.close()
#---------------------------------------------------------------------------------
def hireAndreturnUpdate(id,whatIs):
    itemID = int(id)
    data = []
    whatIsIt = whatIs
    with open("items.csv") as file_object:
        reader = csv.reader(file_object)
        your_list = list(reader)
        if whatIsIt == 'H':
            your_list[itemID][3] = 'n'
        #print (your_list[itemID])
        else:
            your_list[itemID][3] = 'y'
        data = your_list
    file_object.close()
    with open("items.csv","w")as file_writer_obj:
        writer = csv.writer(file_writer_obj,lineterminator='\n')
        writer.writerows(data)
    file_writer_obj.close()
    #print (data)
    if whatIsIt == 'H':
        print("******",data[itemID][1],"hired for $",float(data[itemID][2]),"******")
    else:
        print("******",data[itemID][1],"has been succesfully returned","******")
def hireAndReturnListing(what):
    whatIsIt = what
    validID = []#integer
    allList = []

    with open("items.csv") as f_object:
        reader = csv.reader(f_object)
        my_list = list(reader)
        allList = my_list
        if whatIsIt == 'H':
            for i in range(len(my_list)):
                if my_list[i][3] == 'y':
                    validID.append(i)
            listingTitile('H')
            displayBy(my_list,validID,'H')
        else:
            for i in range(len(my_list)):
                if my_list[i][3]=='n':
                    validID.append(i)
            listingTitile('R')
            displayBy(my_list,validID,'R')
    #reader.close()

    #-----------------------------------------
    if whatIsIt == 'H':
        loopExit = False
        isOK = False
        if len(validID) > 0:
            isOK = True
        else:
            isOK = False
        if isOK == True:
            def validationCheck(receive):
                receiver = receive
                loopExitAgient = False
                #If Quick
                if(receiver == 'Q' or receiver == "q"):
                    loopExitAgient = True
                #if invaid character
                elif(len(receiver)>len(str(validID[-1]))):
                    print("\t\t***************************")
                    print("\t\t******INVALID COMMAND******")
                    print("\t\t***************************")
                    listingTitile('H')
                    displayBy(allList,validID,'H')
                    loopExitAgient = False
                else:
                    #print(receiver)
                    isFound = False
                    onWhat = []
                    #print(validID)
                    for i in range(len(validID)):
                        if receiver == str(validID[i]):
                            isFound = True
                            onWhat.append(validID[i])
                        #print(isFound)
                        #print(onWhat)

                    if isFound==True:
                        #print("Data Updated")
                        loopExitAgient = True
                        hireAndreturnUpdate(onWhat[0],'H')
                        #print ("Character match")
                    else:
                        #----new
                        isInt = False
                        try:
                            receiver = int(receiver)
                            isInt = True
                        except ValueError:
                            print("****************************************************************************")
                            print("**Invalid Input(Character): Please type only item ID number(not character)**")
                            print("****************************************************************************")
                        if isInt == True:
                            print("*************************************************************")
                            print("***That item is not available to hire or not in the system***")
                            print("*************************************************************")
                        listingTitile('H')
                        displayBy(allList,validID,'H')
                        loopExitAgient = False
                        #----new
                        #------old
                        ##print("\t\t***************************")
                        ##print("\t\t******INVALID COMMAND******")
                        ##print("\t\t***************************")
                        #print("***That item is not available to hrie***")
                        #listingTitile('H')
                        #displayBy(allList,validID,'H')
                        #loopExitAgient = False
                        ##print("Character didn't match")
                        #-----old
                return loopExitAgient
            hireID = input("\t\tEnter the ID number of an item to hire 'OR'  Type Q if you want to quit from hiring\n>>>")
            loopExit = validationCheck(hireID)
            #loopExit = validationCheck(input("\t\tEnter the ID number of an item to hire 'OR'  Type Q if you want to quit from hiring"))
            while loopExit == False:
                #loopExit = validationCheck(input("\t\tEnter the ID number of an item to hire 'OR'  Type Q if you want to quit from hiring"))
                hireID = input("\t\tEnter the ID number of an item to hire 'OR'  Type Q if you want to quit from hiring\n>>>")
                loopExit = validationCheck(hireID)
        else:
            print("**************************************")
            print("****There is no item left to hire*****")
            print("**************************************")
    else:
        #----------------Return---
        loopExit = False
        isOK = False
        if len(validID) > 0:
            isOK = True
        else:
            isOK = False
        if isOK == True:
            def validationCheck(receive):
                receiver = receive
                loopExitAgient = False
                #If Quick
                if(receiver == 'Q' or receiver == "q"):
                    loopExitAgient = True
                #if invaid character
                elif(len(receiver)>len(str(validID[-1]))):
                    print("\t\t***************************")
                    print("\t\t******INVALID COMMAND******")
                    print("\t\t***************************")
                    listingTitile('R')
                    displayBy(allList,validID,'R')
                    loopExitAgient = False
                else:
                    #print(receiver)
                    isFound = False
                    onWhat = []
                    #print(validID)
                    for i in range(len(validID)):
                        if receiver == str(validID[i]):
                            isFound = True
                            onWhat.append(validID[i])
                        #print(isFound)
                        #print(onWhat)
                    if isFound==True:
                        #print("Data Updated")
                        loopExitAgient = True
                        hireAndreturnUpdate(onWhat[0],'R')
                        #print ("Character match")
                    else:
                        isInt = False
                        try:
                            receiver = int(receiver)
                            isInt = True
                        except ValueError:
                            print("****************************************************************************")
                            print("**Invalid Input(Character): Please type only item ID number(not character)**")
                            print("****************************************************************************")
                        if isInt == True:
                            print("*************************************************************")
                            print("***That item is not hired or not in the system***")
                            print("*************************************************************")

                        #print("\t\t***************************")
                        #print("\t\t******INVALID COMMAND******")
                        #print("\t\t***************************")
                        listingTitile('R')
                        displayBy(allList,validID,'R')
                        loopExitAgient = False
                        #print("Character didn't match")
                return loopExitAgient
            #loopExit = validationCheck(input("\t\tEnter the ID number of an item to return 'OR'  Type Q if you want to quit from returning"))
            #while loopExit == False:
            #    loopExit = validationCheck(input("\t\tEnter the ID number of an item to return 'OR'  Type Q if you want to quit from returning"))
            returnID = input("\t\tEnter the ID number of an item to return 'OR'  Type Q if you want to quit from returning\n>>>")
            loopExit = validationCheck(returnID)
            while loopExit == False:
                returnID = input("\t\tEnter the ID number of an item to return 'OR'  Type Q if you want to quit from returning\n>>>")
                loopExit = validationCheck(returnID)
        else:
            print("****************************************")
            print("*****No items are currently on hire*****")
            print("****************************************")
#---------------------------------------------------------------------------------
def addNewItem():

    name = input("Item name:")
    if not name:
        print("Input can not be blank")
    while not name:
        name = input("Item name:")
        if not name:
            print("Input can not be blank")

    description = input("Description:")
    if not description:
       print("Input can not be blank")
    while not description:
        description = input("Description:")
        if not description:
            print("Input can not be blank")
    itemname = name + ":" + description
    '''
    def check():

        value = []
        price = 0
        ok = False
        rece = []
        noinput = False

        valid = False
        while valid == False:
            #try:
            #    inp = input("Price per day: $")
            #except SyntaxError:
            #    inp = None
            nonInpCheck = False
            while nonInpCheck == True:
                try:
                    inp = input("Price Per day: $")
                except:
                    if not inp:
                        raise ValueError('Please put any data')
                        nonInpCheck = False
                    else:
                        nonInpCheck = True
            while True:
                try:
                    int(inp)
                except ValueError:
                    inp = input ("Invalid input: please type numeric value")
                    continue
                else:
                    break

            print(type(inp))

            itisnotNegative = False
            if inp < 0:
                print ("Price must be >= $0 \n Invalid input: enter a valid number")
                itisnotNegative = False
            else:
                itisnotNegative = True
                price = inp
                valid = True

        value.append(ok)
        value.append(price)
        return value
    '''
    while True:
        try:
            price = float(input("Price per day $: "))
        except ValueError:
            print("Invalid Input")
            continue
        if price < 0:
            print("Invalid Input-Negative Value")
            continue
        else:
            break

    data = [0,itemname,price,'y']
    #print(data)

    position = 0
    with open("items.csv") as file_object:
        reader = csv.reader(file_object)
        your_list = list(reader)
        toAddPosition = len(your_list)
        data[0] = toAddPosition
        position = toAddPosition
        your_list.append(data)
        data = your_list
    file_object.close()
    with open("items.csv","w")as file_writer_obj:
        writer = csv.writer(file_writer_obj,lineterminator='\n')
        writer.writerows(data)
    file_writer_obj.close()
    #...................................................
    print(data[position][1],", $",data[position][2]," now available for hire")
#---------------------------------------------------------------------------------
def savingToAndFrom():
    with open("items.csv") as f_object:
        reader = csv.reader(f_object)
        my_list = list(reader)
        oldItem = []
        newItemStart = 0

    return (len(my_list))


#---------------------------------------------------------------------------------

def fileCheck(fpath):
    if os.path.isfile(fpath):
        return True
    else:
        return False

def download(URL):
    try:
        r = requests.get(URL,timeout=5)
        with open("items.csv","wb") as code:
            code.write(r.content)
    except ConnectionError as e:
        print ("Can't connect to server")
        #print ("try to use function")
        r = "No reposne"

def autoGenerate():
    tempList = [
            [0,'item1:Description',1.0,'y'],
            [1,'item2:Description',2.0,'y'],
            [2,'iem2:Description',3.0,'y'],
            ]
    with open("items.csv","w")as file_writer_obj:
        writer = csv.writer(file_writer_obj,lineterminator='\n')
        writer.writerows(tempList)
    file_writer_obj.close()

def welcomScreen():
    #print ("*********Welcome To Item Hiring and Management Program*********")
    #print ("*********         Created By Than Myint Wai           *********")
    fileExist = False
    commandValid = False
    URL = 'https://www.dropbox.com/s/0jq4t7sap9qdhpy/items.csv?dl=1'
    PATH = './items.csv'

   #----------------------------------------------
    if fileCheck(PATH) == True:
        #print ("File Exist")
        fileExist = True
    else:
        #print("Not Exist")
        print("*****************CSV file desn't exist!******************************")
        print("If you want to download the file from the inernet, please type I or i")
        print("Or if you want to use auto generated file, please type A or a")
        print("**********************************************************************")
        ans = input("")

        if ans =='A' or ans == 'a':
            autoGenerate()
            commandValid = True
        elif ans == 'I' or ans == 'i':
            '''Adding Codes'''
            download(URL)
            subExit = fileCheck(PATH)
            commandValid = True
            while subExit == False:
                print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print ("Couldn't successfully download the file, Please check your internet Connection")
                print("If you want to use auto generated csv file, please type Y or y or else type N or n")
                print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                newQuestion = input("")
                if newQuestion == "Y" or newQuestion == 'y':
                    autoGenerate()
                    subExit = True
                    commandValid = True
                    #exit()
                else:

                    download(URL)
                    subExit = fileCheck(PATH)
                    if subExit == True:
                        subExit = True
                    else:
                        subExit = False
            '''End of Adding Codes'''
            commandValid = True
        else:

            print ("                 *****Invalid Command*****                           ")
            commandValid = False


        while commandValid == False:
            #ans = input("A or I")
            print("*****************CSV file desn't exist!******************************")
            print("If you want to download the file from the inernet, please type I or i")
            print("Or if you want to use auto generated file, please type A or a")
            print("**********************************************************************")
            ans = input("")
            if ans == "A" or ans == 'a':
                autoGenerate()
                commandValid = True
            elif ans == "I" or ans == 'i':
                #print("Internet")
                '''Adding Codes'''
                download(URL)
                subExit = fileCheck(PATH)
                while subExit == False:
                    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print ("Can't successfuly dowload the file, Please check your internet Connection")
                    print("If you want to use auto generated csv file, please type Y or y or else type N or n")
                    print ("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    newQuestion = input("")
                    if newQuestion == "Y" or newQuestion == 'y':
                        autoGenerate()
                        subExit = True
                        commandValid = True
                    else:
                        download(URL)
                        subExit = fileCheck(PATH)
                        if subExit == True:
                            subExit = True
                        else:
                            subExit = False
                '''End of Adding Codes'''
                commandValid = True
            else:
                print ("                 *****Invalid Command*****                           ")
                commandValid == False


    #--------------------------------------------


    print("Items for Hire - by Than Myint Wai")
    print(savingToAndFrom()," items loaded from item.csv")


def showMenu():

        print ("""Menu:
        (L)List all items
        (H)Hire an item
        (R)Return an item
        (A)Add new item to stock
        (Q)Quit
            """)
        answer = input(">>")
        return answer
def checkMenu():
    global keepGoing
    selectMenu = showMenu()
    if (selectMenu == "L" or selectMenu == "l") :
        listing()
    elif (selectMenu == "H" or selectMenu == "h"):
        hireAndReturnListing('H')
    elif (selectMenu == "R" or selectMenu == "r"):
        hireAndReturnListing('R')
    elif (selectMenu == "A" or selectMenu == "a"):
        addNewItem()
    elif (selectMenu == "Q" or selectMenu == "q"):
        keepGoing = False
        itemNumber = savingToAndFrom()
        print(itemNumber," items saved to the file \nHave a nice day")

    else:
        print("Invalid Menu")
##------------------------------
welcomScreen()
checkMenu()
while keepGoing:
    checkMenu()
