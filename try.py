first = "Seif "
last = "Amr"
print(first + last)
if first + last == "Seif Amr":
    print(True)
else:
    print (False)

def enter():
    entery = input("enter your name: ")
    if entery == first + last:
        print (True)
    else:
        print (False)
        
enter()


def check_enter():
    gmail = input("Enter your gmail: ")
    
    while not gmail.endswith("@gmail.com"):
        print("...Access Denied. Try again.\n")
        gmail = input("Enter your gmail: ")
    
    print("...Access Allowed")

check_enter()