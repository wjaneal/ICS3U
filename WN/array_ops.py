#Item sorting program
#Debugging a program.
#
#Program distributes items evenly in n lists
def Largest(List1):
    largest = List1[0]
    for i in range(1,len(List1)):
<<<<<<< HEAD
        if largest < List1(i):
            largest = List1[i-1]
    return Largest
=======
        if largest < List1[i]:
            largest = List1[i]
    #print(largest)
    return largest
>>>>>>> fbb0af169a61ceda0da94a9ce5a229fb598b4e07
n = 3 #How many groups to sort into
List1 = [5,7,2,78,23,67,45,89,123,6,8,123,454,565,7665,6676,322,4443] 
Groups = []*n  
'''Group1=[]
Group2=[]
Group3=[]'''
#print(Groups)
not_done = True
i=0
#repeat until List1 is empty:
while not_done==True:
<<<<<<< HEAD
    for i in range(0,len(Groups)):
        Groups[i] = Largest(List1)
    for i in range(0,len(Groups)):
        Groups[n+1-i]= Largest(List1)
        print(Groups)
=======
    if (i%2==0 and len(List1)!=0):
        for i in range(0,n):
            x=Largest(List1)
            Groups.append(x)
            List1.remove(x)
        i+=1
        #print(i)
    elif(i%2==1 and len(List1)!=0):
        for i in range(0,n):
            
            x=Largest(List1)
            Groups[3-n+].append(x)
            List1.remove(x)
        i+=1
        #print(i)
    else:
        not_done = False
print(Group1,Group2,Group3)
>>>>>>> fbb0af169a61ceda0da94a9ce5a229fb598b4e07

    #for each group, 1,2,3...n distribute the largest item in the list
    #for each group, n,n-1,n-2...1 distribute the largest item in the list


