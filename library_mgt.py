# This programme is written for a library to manage book checkouts, 
# collections and reservations effectiently.

from datetime import datetime, timedelta

# Creating a library for the books' details
library_collection = {"B1" : {"book name" : "Harry Potter - One", "copies" : 1,
                               "borrowers": [], "reservers":[], 
                               "borrowed date" : [], "due date" : []},
                      "B2" : {"book name" : "Harry Potter - Two", "copies" : 1,
                               "borrowers": [], "reservers":[],
                               "borrowed date" : [], "due date" : []},
                      "B3" : {"book name" : "Harry Potter - Three", "copies" : 1,
                               "borrowers": [], "reservers":[],
                               "borrowed date" : [], "due date" : []},
                      "B4" : {"book name" : "Harry Potter - Four", "copies" : 1,
                               "borrowers": [], "reservers":[], 
                               "borrowed date" : [], "due date" : []},
                      "B5" : {"book name" : "Harry Potter- Five", "copies" : 1,
                               "borrowers": [], "reservers":[], 
                               "borrowed date" : [], "due date" : []},
                      "B6" : {"book name" : "Harry Potter - Six", "copies" : 1,
                               "borrowers": [], "reservers":[], 
                               "borrowed date" : [], "due date" : []},
                      "B7" : {"book name" : "Harry Potter - Seven", "copies" : 1,
                               "borrowers": [], "reservers":[], 
                               "borrowed date" : [], "due date" : []},
                      }

# Creating a library for the users' details
library_users = {"L1" : {"user name" : "George", "borrowings":[],
                          "reservations" : [], "fines" : []},
                 "L2" : {"user name" : "John", "borrowings":[], 
                         "reservations" : [], "fines" : []},
                 "L3" : {"user name" : "Olive", "borrowings":[], 
                         "reservations" : [], "fines" : []}
                }

# Defining a function to check out a book
def checkout_book(user_id,book_id,borrow_date):
    
    if len(library_users[user_id]["borrowings"]) < 3:

        if library_collection[book_id]["copies"] > 0: 

            if len(library_collection[book_id]["reservers"]) == 0:
                
                # Check out the book if noone reserved it
                end_date = borrow_date + timedelta(days = 21)
                library_collection[book_id]["copies"] -= 1
                library_collection[book_id]["borrowers"].append(user_id)
                library_users[user_id]["borrowings"].append(book_id)
                library_collection[book_id]["borrowed date"].append(borrow_date)
                library_collection[book_id]["due date"].append(end_date)

                print("Your check-out is successful")
                print(f"The last date to be returned: {end_date}")
                print(library_users[user_id])

            elif user_id in library_collection[book_id]["reservers"]:

                # Check out the book if the member who reserved it tries to check out
                library_collection[book_id]["reservers"].remove(user_id)
                library_users[user_id]["reservations"].remove(book_id)
                end_date = borrow_date + timedelta(days = 21)
                library_collection[book_id]["copies"] -= 1
                library_collection[book_id]["borrowers"].append(user_id)
                library_users[user_id]["borrowings"].append(book_id)
                library_collection[book_id]["borrowed date"].append(borrow_date)
                library_collection[book_id]["due date"].append(end_date)

                print("Your check-out is successful")
                print(f"The last date to be returned: {end_date}")
                print(library_users[user_id])
                                  
            else:
                print("This book is already reserved")
        else:
            print("Sorry, This book is not available right now")

    else:
        print("Sorry, Your borrowings have already reached 3")

# Defining a function to reserve a book
def reserving_book(user_id, book_id):

    if (len(library_users[user_id]["borrowings"]) < 3 
        and book_id not in library_users[user_id]["borrowings"]):

            library_collection[book_id]["reservers"].append(user_id)
            library_users[user_id]["reservations"].append(book_id)
            print("Your book is succefully reserved")
            print(library_users[user_id])          
        
    else:
        print("Sorry, You can't reserve this book") 

# Defining a function to renew a book
def renewing_book(user_id,book_id,renew_date):

    if user_id in library_collection[book_id]["borrowers"]:

        if len(library_collection[book_id]["reservers"]) == 0:
            # The book will be renewed if noone reserved it
            
            end_date = renew_date + timedelta(days = 21)
            library_collection[book_id]["borrowed date"].pop()
            library_collection[book_id]["borrowed date"].append(renew_date)
            library_collection[book_id]["due date"].pop()
            library_collection[book_id]["due date"].append(end_date)
            print("Your renewal is successful")
            print(f"The last date to be returned: {end_date}")            
            print(library_users[user_id])

        else:
            print("Sorry, The book is reserved")

    else:
        print("Sorry, You did not borrow this book to renew")

# Defining a function to return a book
def returning_book(user_id,book_id,return_date):

    if book_id in library_users[user_id]["borrowings"]:

        penalty_days = return_date - library_collection[book_id]["due date"][0]
        penalty_days = penalty_days.days

        if penalty_days > 0:
            fine = penalty_days * 0.15
            library_users[user_id]["fines"].append(fine)

        library_collection[book_id]["copies"] += 1
        library_collection[book_id]["borrowers"].remove(user_id)
        library_collection[book_id]["borrowed date"].pop()
        library_collection[book_id]["due date"].pop()      
        library_users[user_id]["borrowings"].remove(book_id)

        print("Your book is successfully returned")
        print(library_users[user_id])
    
    else:
        print("The user did not borrow this book")

# Take the input of user id    
user_id = input("Please enter your id:  ")
user_id = user_id.capitalize()
date_format = "%d/%m/%Y"
today_date = datetime.today().strftime(date_format)
today_date = datetime.strptime(today_date,date_format)

if user_id in library_users:
    # Checks if the user id is registered with the library

    print("Welcome to the local library!")
    service = 0
    while service != '5':
        # Loop continues until the user's choice is to quit

        service = input('''Please enter one of the services below.\n
                    1 : To borrow a book  
                    2 : To reserve a book  
                    3 : To return a book 
                    4 : To renew a book 
                    5 : To exit       \n''')
        
        if service in ['1','2','3','4','5']:

            if service == '5':
                print("Thank you for using our services!")
                break

            else:
                book_id = '0'
                while book_id not in library_collection:
                    # Loop executes until the user chooses the book registered with the library

                    book_id = input('''Please enter the name of the book from the below.  
                                B1 : Harry Potter - One
                                B2 : Harry Potter - Two
                                B3 : Harry Potter - Three
                                B4 : Harry Potter - Four
                                B5 : Harry Potter - Five
                                B6 : Harry Potter - Six
                                B7 : Harry Potter - Seven \n''')
                    book_id = book_id.capitalize()
                    
                    if book_id in library_collection:   

                        if service == '1':
                            checkout_book(user_id,book_id,today_date)
                            
                        elif service == '2':
                            reserving_book(user_id,book_id,today_date)
                            
                        elif service == '3':
                            returning_book(user_id,book_id,today_date)
                            
                        elif service == '4':
                            renewing_book(user_id,book_id,today_date)
                            
                    else:
                        print("This book is not in our collection. Plz enter a valid input")

        else:
            print("Please enter a valid input")         
           
else:
    print("Your name is not registered with our library")
    

    