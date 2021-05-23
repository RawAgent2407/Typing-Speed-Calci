import datetime
import random
list1 = ["Python is a good programming language for beginners. It is a high-level language, which means a programmer can focus on what to do instead of how to do it. Writing programs in Python"
         "takes less time than in some other languages","It is essentially the brain of the computer and though it is the main determining factor in the processing power of the computer as a "
         "whole","A computer does not have enough creativity to make tasks for which it is not programmed, so it can only follow the instructions of the programs that it has been programmed for."
         "The ones in charge to generate programs so that the computers may perform new tasks are programmers.","A day in the future will come when human civilization won’t be able to survive without"
         "computers as we depend on them too much. Till now it is a great discovery of mankind that has helped in saving thousands and millions of lives.","Programme is a sequence of instructions"
         "written in a proper language through which the computer can understand and solve the problem given to it. It is the method by which the whole computing process is directed and controlled.",
         "A flow chart illustrates the sequence of operations to be performed to arrive at the solution of a problem. The operating instructions are placed in boxes which are connected by arrows to"
         "indicate the order of execution.","Artificial Intelligence refers to the intelligence of machines. This is in contrast to the natural intelligence of humans and animals. With Artificial"
         "Intelligence, machines perform functions such as learning, planning, reasoning and problem-solving. Most noteworthy, Artificial Intelligence is the simulation of human intelligence by machines."]
a = random.choice(list1)
a.replace(".","")
a.replace(",","")
print(a)
l = len(a.split())
initTime = datetime.datetime.now()
b = input("Type here: ")
elem1 = [x for x in a.split()]
elem2 = [x for x in b.split()]
correct,false = 0,0
for item in elem1:
    if item in elem2:
        correct+=1
    else:
        false+=1
endTime = datetime.datetime.now()
Time = round(((endTime - initTime).total_seconds())/60,2)
n1 = round(correct/Time,0)
n2 = round((correct-false)/Time,0)
if n2 != 0:
    n3 = round((n2/n1)*100,2)
else:
    n3 = 100
print(f"\nResults\nCongratulations, You have typed {correct} words correct out of {l} words in {Time} minutes\n")
print(f"Gross Speed: {n1} WPM\nNet Speed: {n2} WPM\nAccuracy: {n3}%")
