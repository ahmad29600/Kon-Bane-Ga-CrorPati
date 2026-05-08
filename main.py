# KBC Game
score = 0
question1 = input("What is the caiptal of Pakistan?: ").lower()
if question1 == "islamabad":
    score += 1
    print("Correct!")
    question2 = input("What is the first caiptal of Pakistan: ").lower()
    if question2 == "karachi":
        score += 1
        print("Correct!")
        question3 = input("What is the national flower of Pakistan?: ").lower()
        if question3 == "jasmine":
            score += 1
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Wrong!")
else:
    print("Wrong!")
print("You have scored", score ,"marks.")