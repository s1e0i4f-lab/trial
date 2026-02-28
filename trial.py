# checker 1
def checker():
    check = input("Enter you name: ").strip().lower()
    while True:
        print("Access allowed")
        break

checker()

#Question game 2
def game():
    # Question 1
    question1 = "What is the biggest sea creature?"
    solution1 = "whale"
    print(question1)
    enter = input("Enter your response: ").strip().lower()
    
    while enter != solution1:
        print("Wrong answer...Try Again")
        enter = input("Enter your response: ").strip().lower()
    print("Great job...Go through the next question")
    
    # Question 2
    question2 = "What is the longest river?"
    solution2 = "nile river"
    print(question2)
    enter = input("Enter your response: ").strip().lower()
    
    while enter != solution2:
        print("Wrong answer...Try Again")
        enter = input("Enter your response: ").strip().lower()
    print("Great job...keep going you are almost there!")
    
    # Question 3
    question3 = "What is the fastest animal on land?"
    solution3 = "cheetah"
    print(question3)
    enter = input("Enter your response: ").strip().lower()
    
    while enter != solution3:
        print("Wrong answer...Try Again")
        enter = input("Enter your response: ").strip().lower()
    print("Great job...you win!")

game()