# @author Sonia Abtahi - 983663036
# FAZE 2 - Part 1
class Student:
    def __init__(self,stdn):
        self.student = stdn
        self.prev_student = None
        self.next_student = None
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    def Add_student(self,stdn):
        if self.last is None:
            self.first = Student(stdn)
            self.last = self.first
        else:
            self.last.next_student = Student(stdn)
            self.last.next_student.prev_student = self.last
            self.last = self.last.next_student
    """def Show_Queue(self):
        temp = self.first
        while temp is not None:
            print(temp.student)
            temp = temp.next_student"""
    def getStudent(self,index):
        temp = self.first
        counter = 1
        while temp is not None:
            if counter is index:
                return temp.student
            counter = counter + 1
            temp = temp.next_student
    def swap(self,std1,std2):
        start = self.first
        end = self.first
        if std1 >= std2:
            return
        for i in range(std2 - 1):
            end = end.next_student
        for i in range(std1 - 1):
            start = start.next_student
        temp = start.student
        start.student = end.student
        end.student = temp
        start = start.next_student
        end = end.prev_student
        return self.swap(std1+1,std2-1)
#Main
if __name__=='__main__':
    Yas_Queue = Queue()
    orders = list()
    output = list()
    print("Welcome to Yas Restuarant")
    print("------------------------------------------------")
    lenght = int(input("Please enter the lenght of your Yas's Queue :"))
    print("--------------------------------------------------")
    if lenght != 0:
        for i in range(lenght):
            Yas_Queue.Add_student(int(input("Please enter the student number :")))
        print("--------------------------------------------------")
        mistakes = int(input("Please enter the number of mistakes :"))
        for i in range(mistakes):
            orders.append(input("Enter the order :").split())
        for each in orders:
            if each[0] == "GET":
                output.append(Yas_Queue.getStudent(int(each[1])))
            if each[0] == "SWAP":
                Yas_Queue.swap(int(each[1]),int(each[2]))
            else:
                continue
        print("--------------------------------------------------")
        print("The output is :")
        for each in output:
            print(each)
    else:
        print("Oops! It seems you can't have a Queue :(")
        print("BYE BYE !")
        input = quit()

