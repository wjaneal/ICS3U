#Item sorting program
#Debugging a program.
#
#Program distributes items evenly in n lists
def Largest(List1):
    largest = List1[0]
    for i in range(1,len(List1)):
        if largest < List1[i-1]:
            largest = List1[i-1]
    return Largest
n = 3 #How many groups to sort into
List1 = [5,7,2,78,23,67,45,89,123,6,8,123,454,565,7665,6676,322,4443] 
#Sorted groups:
#Groups = [[7665,322,123],[6676,454,],[4443,565]]
Groups = []*n
not_done = True
#repeat until List1 is empty:
while not_done==True:
    for i in range(0,len(Groups)):
        groups[i] = largest(List1)
        #Remove it from the list
    #If len(List1) == 0:
        #not_done = False
    for i in range(0,len(Groups)):
        groups[n+1-i]= largest(List0)
        #Remove it from the list
    #If len(List1) == 0:
        #not_done = False
print(groups)

    #for each group, 1,2,3...n distribute the largest item in the list
    #for each group, n,n-1,n-2...1 distribute the largest item in the list


