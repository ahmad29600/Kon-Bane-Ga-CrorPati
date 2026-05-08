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

# KBC Inspired Quiz Game

questions = [
    ["What is the capital of India?", "Mumbai", "Delhi", "Kolkata", "Chennai", 2],

    ["Which language is mainly used for AI?", "Python", "HTML", "CSS", "MS Word", 1],

    ["Who is known as the Missile Man of India?", "Virat Kohli", "A.P.J Abdul Kalam", "Modi", "Einstein", 2],

    ["Which planet is called the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],

    ["How many states are there in India?", "28", "29", "30", "27", 1]
]

money = [1000, 5000, 10000, 50000, 100000]

total_money = 0

print("Welcome to KBC Python Edition")
print("--------------------------------")

for i in range(len(questions)):

    question = questions[i]

    print("\nQuestion for Rs.", money[i])
    print(question[0])

    print("1.", question[1])
    print("2.", question[2])
    print("3.", question[3])
    print("4.", question[4])

    answer = int(input("Enter your answer (1-4): "))

    if answer == question[5]:
        print("Correct Answer!")
        total_money = money[i]

    else:
        print("Wrong Answer!")
        print("Correct answer was:", question[question[5]])
        break

print("\nGame Over")
print("You won Rs.", total_money)