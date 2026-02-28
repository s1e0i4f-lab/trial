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