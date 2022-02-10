# @author Sonia Abtahi - 983663036
# FAZE 1 - Part 2
print(" Hello , Welcome to Yas Restuarant . ")
print("--------------------------------------------------")
TEST_CASE = int(input(" Please enter the number of Test case : "))
print("--------------------------------------------------")
for test in range(1,TEST_CASE+1) :
    print_type = list()
    sentence = " Scenario #" + str(test)
    print_type.append(sentence)
    answer1 = input(" Do you want to make a Yas's Queue ? please enter Yes(yes) Or No(no) : ")
    if answer1 in "YESYesyes":
        print("-------------------------------------------------")
        fields = int(input(" Please enter the of number fields : "))
        print("-------------------------------------------------")
        if fields != 0:
            Total_Queue = []
            for i in range(fields):
                sub = [-1]
                Total_Queue.append(sub)
                sub_queue = input().split()
                for j in range(len(sub_queue)):
                    sub_queue[j] = int(sub_queue[j])
            counter = 0
            while True:
                answer2 = input(" Please enter your student number and it's action [ ENQUEUE student_number , DEQUEUE ] : ").split()
                if answer2[0] == "ENQUEUE":
                    pointer = int(answer2[1][0:2])
                    stdn = int(answer2[1])
                    index = -1
                    for i in range(len(Total_Queue)):
                        if pointer == Total_Queue[i][0]:
                            index = i
                            break
                    if index == -1:
                        Total_Queue[counter][0] = pointer
                        Total_Queue[counter].append(stdn)
                        counter += 1
                    else:
                        Total_Queue[index].append(stdn)
                if answer2[0] == "DEQUEUE":
                    for i in range(len(Total_Queue)):
                        if len(Total_Queue[i]) > 1:
                            print_type.append(Total_Queue[i].pop(1))
                            break
                if answer2[0] == "STOP":
                    int(input())
                    for each in print_type:
                        print(each)
                    break
    if answer1 in "NONono":
        print(" --------------------------------------------------- ")
        print(" Ok , You don't want to make a Yas's Queue ! ")
        print(" -------------------- BYE BYE ! -------------------- ")
        print(" --------------------------------------------------- ")
        continue








