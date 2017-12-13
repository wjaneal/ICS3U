#Item sorting program
#Debugging a program.
#
#Program distributes items evenly in n lists
def Largest(List1):
    largest = List1[0]
    for i in range(1,len(List1)):
        if largest < List1(i):
            largest = List1[i-1]
    return Largest
n = 3 #How many groups to sort into
List1 = [5,7,2,78,23,67,45,89,123,6,8,123,454,565,7665,6676,322,4443] 
Groups = []*n
not_done = True
#repeat until List1 is empty:
while not_done==True:
    for i in range(0,len(Groups)):
        Groups[i] = Largest(List1)
    for i in range(0,len(Groups)):
        Groups[n+1-i]= Largest(List1)
        print(Groups)

    #for each group, 1,2,3...n distribute the largest item in the list
    #for each group, n,n-1,n-2...1 distribute the largest item in the list


