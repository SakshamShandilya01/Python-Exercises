def validation():
     while True:
         try:
             username = input("Enter the username")

             if username == "":
                 print("Username can't be empty")

             elif len(username) < 5:
                 print("Username is too short")

             elif " " in username:
                 print("Space is not valid ")

             else:
                 print("Valid username")

         except:
             print("something is wrong")

validation()
