# @author Sonia Abtahi - 983663036
# FAZE 2 - Part 2
def findIndex(Inorder,value,nodes):
    for index in range(nodes):
        if Inorder[index] == value:
            return index
    return -1
def Postorder(Inorder,Preorder,nodes):
    root = findIndex(Inorder,Preorder[0],nodes)
    if root != 0: # for check left sub tree
        Postorder(Inorder,Preorder[1:nodes],root)
    if root != nodes-1: # for check right sub tree
        Postorder(Inorder[root+1:nodes],Preorder[root+1:nodes],nodes-root-1)
    print_list.append(Preorder[0])
nodes = int(input("Please Enter the number of nodes :"))
print("--------------------------------------------------")
Preorder = input("Enter the preorder traverse :").split()
print("--------------------------------------------------")
Inorder = input("Enter the inorder traverse :").split()
print_list = list()
output = ""
for i in range(nodes):
    Preorder[i] = int(Preorder[i])
    Inorder[i] = int(Inorder[i])
Postorder(Inorder,Preorder,nodes)
for each in print_list:
    output = output + " " + str(each)
print("--------------------------------------------------")
print("The postorder traverse of your tree is :")
print(output)