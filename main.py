# KBC Game
# score = 0
# question1 = input("What is the caiptal of Pakistan?: ").lower()
# if question1 == "islamabad":
#     score += 1
#     print("Correct!")
#     question2 = input("What is the first caiptal of Pakistan: ").lower()
#     if question2 == "karachi":
#         score += 1
#         print("Correct!")
#         question3 = input("What is the national flower of Pakistan?: ").lower()
#         if question3 == "jasmine":
#             score += 1
#             print("Correct!")
#         else:
#             print("Wrong!")
#     else:
#         print("Wrong!")
# else:
#     print("Wrong!")
# print("You have scored", score ,"marks.")



questions = [
    ["What does the white color in Pakistan flag represent?", "Agriculture", "Peace", "Minority", 3],
    ["Who is known as Father of Nation of Pakistan?", "Quid-e-Azam", "Sir Syed Ahmad Khan", "Allama Iqbal", 1],
    ["The national sport of Pakistan is?", "Cricket", "Hockey", "Basketball", 2],
]

money = [1000, 2000, 3000]
total_money = 0

print("---------------------")
print("Welcome to KBC")

for i in range(len(questions)):

    question = questions[i]

    print("\nQuestion for Rs. ", money[i])
    print(question[0])

    print("1." , question[1])
    print("2." , question[2])
    print("3." , question[3])

    answer = int(input("Enter your answer (1-3): "))

    if answer == question[4]:
        print("Your answer is correct!")
        total_money = money[i]
    else:
        print("Wrong Answer!")
        print("Correct answer was", question[question[4]])
        break
print("Game Over!")
print("You won", total_money)