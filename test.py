#write a python function that takes two list and return true if they have at least one common member

def common(list_1, list_2):
    return any(element in list_2 for element in list_1)

list_1= [1,2,3,5,6]
list_2=[7,6,8,9,10]

print(common(list_1,list_2))
