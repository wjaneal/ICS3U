#Item sorting program
#Debugging a program.
#
#Program distributes items evenly in n lists
def Largest(List1):
    largest = List1[0]
    for i in range(1,len(List1)):
        if largest < List1[i]:
            largest = List1[i]
    #print(largest)
    return largest
n = 3 #How many groups to sort into
List1 = [5,7,2,78,23,67,45,89,123,6,8,123,454,565,7665,6676,322,4443] 
Groups = [0]*len(List1)
#print(Groups)
not_done = True
i=0
index1=0
index2=0
#repeat until List1 is empty:
while not_done==True:
    if (len(List1)!=0 and i%2==0):
        for k in range(0,n):
            x=Largest(List1)
            #print(x)
            Groups[n*index1+k]=x
            #print(Groups)
            List1.remove(x)
        i+=1
        index1+=2
    if (len(List1)!=0 and i%2==1):
        for j in range(0,n):
            x=Largest(List1)
            #print(x)
            Groups[n*index2+n+n-1-j]=x
            #print(Groups)
            List1.remove(x)
        i+=1
        index2+=2
    else:
        not_done = False
print(Groups)
Group1=[]
Group2=[]
Group3=[]
for m in range(0,len(Groups)):
    if(m%3==0):
        Group1.append(Groups[m])
    elif(m%3==1):
        Group2.append(Groups[m])
    else:
        Group3.append(Groups[m])
print(Group1)
print(Group2)
print(Group3)
#print(Groups)
    #for each group, 1,2,3...n distribute the largest item in the list
    #for each group, n,n-1,n-2...1 distribute the largest item in the list


