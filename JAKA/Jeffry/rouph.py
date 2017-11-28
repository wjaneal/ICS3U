sub_lists = []
list1 = ['3', '3', 'x', '^', '3', '+', '2', '2', 'x', '^', '1', '+', '1']
current_start = 0
current_end = 0
i = 0
while i < len(list1)-1:
    current_end=i
    if list1[i]=="+":
        sub_lists.append(list1[current_start:current_end])
        current_start = i+1
    i+=1
print(sub_lists)
        
