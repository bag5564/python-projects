#
# This program utilizes four 2-dimensional arrays to store needed information.
#
# 1) booklist - stores the books in the library
#    data per book: [0] book name, [1] number of copies owned by library,
#                   [2] important flag, [3]number of copies available,
#                   [4] day book was acquired
# 2) log - stores the activity log. When the entries in this array are
#          processed it creates/updates entries in the other 3 arrays.
# 3) checkedOut - stores the books that have been borrowed
#     data per loan: [0] checkout day, [1] book name, [2] customer name,
#                    [3] expected number of days out, [4] day returned
# 4) lateFee - stores the dollar amounts customer owed due to late fees
#     data per customer: [0] customer name, [1] amount owed
# 5) sortedFee - same as lateFee
# 6) bookUsage - [0] book name, [1] days available, [2] total days out, [3] usage
# 7) sortedUsage - same as bookUsage

# FUNCTIONS
# ---------
# add a book to the booklist array or increase the number of copies if already there
def addBook(day, book, important):
    libraryIndex = -1
    for i in range(0, len(booklist)):
            if book == booklist[i][0]:
                libraryIndex = i
    if libraryIndex == -1:
        entry = []
        entry.append(book)
        entry.append(1)
        entry.append(important)
        entry.append(1)
        entry.append(int(day))
        booklist.append(entry)
    else:
        booklist[libraryIndex][1] = 1 + booklist[libraryIndex][1]

# checkout a book by keeping track of borrower and number of copies available
def checkOut(day, book, name, numDays):
    day = int(day)
    numDays = int(numDays)
    # find the book in the booklist array and decrease number of copies available
    index =  -1
    for i in range(0, len(booklist)):
        if book == booklist[i][0]:
            index = i

    if index != -1:
      booklist[index][3] = booklist[index][3] - 1
      # add entry to checkedOut array
      entry = []
      entry.append(day)
      entry.append(book)
      entry.append(name)
      entry.append(numDays)
      entry.append(0)
      checkedOut.append(entry)
    return

# return a book by filling out return day and increasing number of copies available
def returnBook(day, book, name):
    day = int(day)
    # find the book in the array of books checkedOut
    index = -1
    for i in range(0, len(checkedOut)):
        if book == checkedOut[i][1] and name == checkedOut[i][2]:
            index = i
    if index != -1:
      # verify if there are late fees applicable
      startDay = checkedOut[index][0]
      numDays = checkedOut[index][3]
      timeCheckedOut = day - startDay
      calculateFee(name, book, timeCheckedOut, numDays)
      checkedOut[index][4] = day
      #increase number of books available
      libraryindex =  -1
      for i in range(0, len(booklist)):
          if book == booklist[i][0]:
              libraryindex = i
      if libraryindex != -1:
          booklist[libraryindex][3] = 1 + booklist[libraryindex][3]
    return

# calculate late fee and keep track of the amount owed
def calculateFee(name, book, timeCheckedOut, numDays):
    if timeCheckedOut > numDays:
        overdue = timeCheckedOut - numDays
        # find the type of book to apply the correspondent rate
        libraryIndex = -1
        
        # calculate fine
        for i in range(0, len(booklist)):
            if book == booklist[i][0]:
                libraryIndex = i
        if booklist[libraryIndex][2] == "True":
            fee = overdue * 15
        else:
            fee = overdue * 5
        # find if person already has late fee
        personIndex = -1
        for j in range(0, len(lateFee)):
            if name == lateFee[j][0]:
                personIndex = j
        if personIndex == -1:
            entry = []
            entry.append(name)
            entry.append(fee)
            lateFee.append(entry)
        else:
            lateFee[personIndex][1] = lateFee[personIndex][1] + fee
    return

# pay a fee by reducing the amount owed by payee
def payFee(name, amount):
    index = -1
    amount = int(amount)
    # find the payer's name in the lateFee array and reduce the amount owed
    for i in range(0, len(lateFee)):
        if name == lateFee[i][0]:
            index = i
    lateFee[i][1] = lateFee[i][1] - amount
    #Removing people who paid their debt
    if lateFee[i][1] <= 0:
        lateFee.pop(i)
    return

def canCheckOut(name, book, numDays):
    # find the book in the booklist array
    index =  -1
    for i in range(0, len(booklist)):
        if book == booklist[i][0]:
            index = i
    # check if borrower has late fees
    feeIndex = -1
    for i in range(0, len(sortedFee)):
        if name == sortedFee[i][0]:
            feeIndex = i
   
    # check if borrower has already checked out this book
    checkoutIndex = -1
    for i in range(0, len(checkedOut)):
        if name == checkedOut[i][2] and book == checkedOut[i][1] and checkedOut[i][4] == 0:
            checkoutIndex = i
    if index != -1:
      # are there copies available?
      if  booklist[index][3] == 0:
          return False
      # important books cannot be lent for more than 7 days
      elif booklist[index][2] == "True" and numDays > 7:
          return False
      # other books cannot be lent for more than 28 days
      elif booklist[index][2] == "False" and numDays > 28:
          return False
      # does the borrower has already checked out this book:
      elif checkoutIndex != -1:
          return False
      # does the borrower has more than $50 in late fees?
      elif feeIndex != -1 and sortedFee[feeIndex][1] > 50:
          return False
      else:
          return True
    else:
        return False

def canReturnBook(name, book):
    # find out if the person has checked out the book
    index = -1
    for i in range(0, len(checkedOut)):
          if checkedOut[i][1] == name and checkedOut[i][2] == book:
            index = i
    if index != -1:
        return True
    else:
        return False

def seeLateFees(top):
    # print late fees
    
    if len(sortedFee) == 0:
        print("None")
        return
    if len(sortedFee) < top:
        top = len(sortedFee)
    for i in range(0, top):
        print("Name: ", sortedFee[i][0], " Late Fee: $", sortedFee[i][1])
    return

def seeUsage(top):
    if len(sortedUsage) < top:
        top = len(sortedUsage)
    for i in range(0, top):
      print(sortedUsage[i][0], " with usage ", sortedUsage[i][3],"%")
    return
# -----------------------------------------------------------------------------

# MAIN PROGRAM
# ------------

# Read booklist file and create a booklist array (book name, number of coopies, important flag)
read = open("finalbooklist.txt", "r")
line = read.readline()
line = line.rstrip("\n")
booklist = []

while line != "":
    a = line.split("#")
    booklist.append(a)
    line = read.readline()
    line = line.rstrip("\n")
read.close()

# Convert numbers of copies to an integer number
# Add 2 extra elements per book: number of copies available, day book was acquired
# (all the books in booklist were in the library since day 1)
length = len(booklist)
for i in range(0,length):
    booklist[i][1] = int(booklist[i][1])
    j = booklist[i][1]
    booklist[i].append(j)
    booklist[i].append(1)

# Read library log file and store transactions in a 2-dimensional array
read = open("finallibrarylog.txt", "r")
line = read.readline()
line = line.rstrip("\n")
log = []

while line != "":
    a = line.split("#")
    log.append(a)
    line = read.readline()
    line = line.rstrip("\n")
read.close()

# Create arrays to hold books checked out and late fees owed
checkedOut = []
lateFee = []


# Process activities in log
currentDay = -1
for i in range(0, len(log)):
    if len(log[i]) == 1:
        currentDay = int(log[i][0])
    elif log[i][0] == "PAY":
        payFee(log[i][2],log[i][3])
    elif len(log[i]) == 3:
        addBook(log[i][0],log[i][1],log[i][2])
    elif log[i][3] == "RET":
        returnBook(log[i][0],log[i][1],log[i][2])
    else:
        checkOut(log[i][0],log[i][1],log[i][2],log[i][3])

# Sort the Lists
# calculate late fees for books that have not been returned yet
for i in range(0, len(checkedOut)):
    if checkedOut[i][4] == 0:
        timeCheckedOut = currentDay - checkedOut[i][0]
        calculateFee(checkedOut[i][2], checkedOut[i][1], timeCheckedOut, checkedOut[i][3])

sortedFee = []
length = len(lateFee)
n = 0
while n < length:
    large = 0
    i = 0
    while i < len(lateFee):
        if lateFee[i][1] > lateFee[large][1]:
            large = i
        i = i+1
    sortedFee.append(lateFee[large])
    lateFee.pop(large)
    n = n+1

#Calculate Book Usage
bookUsage =[]

for i in range(0, len(booklist)):
      entry = []
      entry.append(booklist[i][0])
      # calculate book availability
      availability = (currentDay - booklist[i][4]) * booklist[i][1]
      entry.append(availability)
      # calculate how many days book was on loan
      totalDaysOut = 0
      for j in range(0, len(checkedOut)):
        if checkedOut[j][1] == booklist[i][0]:
          # the book might still be out
          if checkedOut[j][4] == 0:
            totalDaysOut = totalDaysOut + (currentDay - checkedOut[j][0])
          else:
            totalDaysOut = totalDaysOut + (checkedOut[j][4] - checkedOut[j][0])
      # calculate usage
      entry.append(totalDaysOut)
      usage = totalDaysOut * 100 / availability
      entry.append(usage)
      bookUsage.append(entry)

#Sort Book Usage
sortedUsage = []
length = len(bookUsage)
n = 0
while n < length:
    large = 0
    i = 0
    while i < len(bookUsage):
        if bookUsage[i][3] > bookUsage[large][3]:
            large = i
        i = i+1
    sortedUsage.append(bookUsage[large])
    bookUsage.pop(large)
    n = n+1

# User interaction
action = -1
while action != 5:
    print("What would you like to do? Press the number to select an action.")
    print("1: Check Out a book")
    print("2: Return a book")
    print("3: See the list of late fees")
    print("4: See the usage of books")
    print("5: Exit the program")
    action = int(input())

    if action == 1:
        print("What is your name?")
        uname = input();
        print("What book do you wish to borrow?")
        bookname = input()
        print("For how many days?")
        numdays = input()
        if numdays != "":
            numdays = int(numdays)
        else:
            numdays = 1
        if canCheckOut(uname,bookname,numdays) == True:
            print("yes you may check out the book")
        else:
            print("no you may not check out the book")
    elif action == 2:
        print("What is your name?")
        uname = input();
        print("What book do you wish to return?")
        bookname = input()
        if canReturnBook(uname, bookname)== True:
            print("yes you may not return the book")
        else:
            print("no you not return the book")
    elif action == 3:
        print("List the top _ student/s with the largest late fee.")
        topstud = int(input())
        seeLateFees(topstud)
    elif action == 4:
        print("List the top _ used books in the library.")
        topbook = int(input())
        seeUsage(topbook)
    elif action == 5:
        print("Exiting Program...")
    else:
        print("Invalid action")
