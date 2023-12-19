from donations_pkg.homepage import show_homepage, donate, show_donations 

from donations_pkg.user import login,register


database = {"admin": "password123"}
donations = []
authorized_user = ""

show_homepage(authorized_user)

if authorized_user == "":
     print ("You must be logged in to donate.")
else:
     print ("Logged in as:",authorized_user)

while True:
   show_homepage(authorized_user) 
   choice = input("Choose an option: ")

   if choice == '1' :
      username = input("Enter username: ")
      password = input ("Enter password: ")
      authorized_user = login(database, username, password)
   elif choice == '2':
      username = input("Enter username: ")
      password = input("Enter password: ")
      authorized_user = register(database,username,password)
      if authorized_user != "":
        database[username] = password

   elif choice == '3':
      if authorized_user == "":
        print("You are not logged in.")
      else:
         donation_string = donate(authorized_user)
         donations.append(donation_string)

   elif choice == '4':
      show_donations(donations)
    
   elif choice == '5':
      print("Leaving DonateMe...")   
      break




