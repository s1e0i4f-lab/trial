first = "Seif "
last = "Amr"
print(first + last)

def enter():
    correct_name = (first + last).strip().lower()
    
    entery = input("Enter your name: ").strip().lower()
    
    while entery != correct_name:
        print("...Entrance denied. Try again")
        entery = input("Enter your name: ").strip().lower()
    
    print("...Entrance allowed " + correct_name)

enter()


def check_enter():
    gmail = input("Enter your gmail: ")
    
    while not gmail.endswith("@gmail.com"):
        print("...Access Denied. Try again.\n")
        gmail = input("Enter your gmail: ")
    
    print("...Access Allowed")

check_enter()