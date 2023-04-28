questions = [["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ["Which of the following language most sutaible for machine learning?"
              ,"c", "C++","Javascript", "Python",4],
              ]
levels = [100, 2000, 3000, 5000, 10000, 20000, 30000, 50000, 100000, 320000, 640000, 1200000, 2500000, 5000000, 10000000]

money = 0

for i in range(0, len(questions)):
    question = questions[i]
    print(f"\n \n Question for Rs. {levels[i]}")
    print(f" a.{question[1]}         b.{question[2]}")
    print(f" a.{question[3]}        b.{question[4]}")
    reply = int(input("Enter your answer (1-4) : "))
    if(reply == question[-1]):
        print(f"Correct Answer, aRREY Bhaishabh huh bhai aap jeet gye hai {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i ==9):
            money = 320000
        elif(i== 14):
            money = 10000000     
    else:
        print("Wrong Answer!!!")
        break
print(f"Your Take home money is {money}")

