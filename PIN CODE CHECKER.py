while True:
    try:
     pin = input("What's your pin? ")

     if pin == "":
        print("pin can't be empty")

     elif   len(pin) < 4 or len(pin) > 3:
        print("The length of pin should be 4")

     elif not pin.isdigit():
         print("PIN should contain numbers only")

     else:
         print("Access Granted")

    except:
        print("Error")




