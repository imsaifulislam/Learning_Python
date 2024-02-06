""" qustainIs = "Which Country Do you Live ?"
print(qustainIs)
ansListIs = ["0. Bangladesh", "1. India", "2. USA", "3. Englend"]
print(ansListIs)

index = input("Enter The ANS 0 to 3 : ")
index = int(index)
AnsIs = ansListIs[index]

if (AnsIs == "0. Bangladesh"):
    print("The COuntry Is : ", AnsIs)
    print("Its Correct")
else:
    print("The COuntry Is : ", AnsIs)
    print("Its Wrong")
 """

# -> Solution

""" questions = [
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4],
    ["Which language was used to create Facebook >",
     "python", "Javascript", "php", "None", 4]

]

print(len(questions))
print(questions[-1])
lavels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,]

money = 0

i = 0
for i in range(0, len(questions)):
    #* IN question DataStrod <----< from questions[i]
    question = questions[i]
    print(f"\n\nQustion for Taka.{lavels[i]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")

    reply = int(input("Enter Your Answer (1-4) or 0 to Quit : "))
    if (reply == question[-1]):
        print(f"Correct Answer, your have won Taka. {lavels[i]}")
        if (i == 0):
            money = lavels[i-1]
            break
        elif (i == 4):
            money = 10000
        elif (i == 9):
            money = 32000
        elif (i == 14):
            money = 10000000
    else:
        print("wrong Answer!")
        break

print(f"Your Take Home Money is {money}")
 """


# * প্রথমে লিস্ট এর মধ্যে প্রশ্ন তেরি করা হইছে।

questions = [["Whats the Capital in Bangladesh ?",
             "Dhaka", "Mirpur", "Narayangonj", "None", 1],

             ["Whats the National Food in Bangladesh ?",
             "Mango", "Jackfruit", "Payapa", "None", 2],

             ["Whats the National bird in Bangladesh ?",
             "Cocatail", "Magpai", "tiya", "None", 3],

             ["which programming use for Web Devlopment?",
             "C", "javascript", "c#", "None", 3]
             ]

lavelsTakaWin = [1000, 2000, 3000, 5000, 10000,
                 20000, 40000, 80000, 160000, 320000,]

money = 0

# * এবার লুপ তেরি করে প্রশ্নের মধ্যে এক্সেস করবে
i = 0
for i in range(0, len(questions)):
    # * question এর মধ্যে questions[i] ডাটা চলে আসবে প্রতিবার লুপ ঘুড়ে।
    question = questions[i]
    print(f"\n\nQustion for Taka.{lavelsTakaWin[i]}")
    print(f"a.{question[1]}        b.{question[2]}")
    print(f"c.{question[3]}        d.{question[4]}")

    # *
    reply = int(input("Enter the answer(1-4) or 0 to Quit : "))
    if (reply == 0):
        money = lavelsTakaWin[i-1]

        print("Game Quit")
        break
    if (reply == question[-1]):
        print(f"Correct Answer, your have won Taka. {lavelsTakaWin[i]}")

        if (i == 4):
            money = 10000
        elif (i == 9):
            money = 32000
        elif (i == 14):
            money == 1000000
    else:
        print("Wrong Answer!")
        break

print(f"Your Take Home Money is {money}")
