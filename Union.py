def OneByOne():
    one_by_one = []
    a = "33x^3+22x^1+1"
    for i in a:
        one_by_one.append(i)
    print(one_by_one)
    
OneByOne()

def ConvertToInt():
    list3 = []
    one_by_one = ['3', '3', 'x', '^', '3', '+', '2', '2', 'x', '^', '1', '+', '1']
    for term in one_by_one:
        if term == 'x' or term == '^' or term == '+':
            list3.append(term)
        else:
            list3.append(int(term))
    print(list3)
ConvertToInt()



def seperate():
    list3 = [3, 3, 'x', '^', 3, '+', 2, 2, 'x', '^', 1, '+', 1, '+']
    sub_lists = []
    current_start = 0
    current_end = 0
    i = 0
    n = 0 #trace the number of sub lists
    while i < len(list3):
        current_end=i
        if list3[i]=="+":
            sub_lists.append(list3[current_start:current_end])
            current_start = i+1
            n+=1
        i+=1  
    print(sub_lists)

seperate()

def RestoreCoe():
    sub_lists = [[3, 3, 'x', '^', 3], [2, 2, 'x', '^', 1], [1]]
    n = 3
    temp_coe = 0
    coe = []
    for i in range(0,n):
        a = 0 # to trace the begining 
        b = 0 # to trace 'x'
        for term in range(0,len(sub_lists[i])):
            if sub_lists[i][term] == 'x':
                b = term
        num_numbers = b-a
        for number in range(0,num_numbers):
            temp_coe += sub_lists[i][number]*10**(num_numbers-1)
            num_numbers-=1
        coe.append(temp_coe)
        temp_coe = 0
        a = 0
        b = 0
    print(coe)

RestoreCoe()
        
def RestorePower():
    sub_lists = [[3, 3, 'x', '^', 3], [2, 2, 'x', '^', 1], [1]]
    n = 3
    temp_power = 0
    power = []
    for i in range(0,n):
        a = 0 # to trace the begining 
        b = 0 # to trace the end
        for term in range(0,len(sub_lists[i])):
            if sub_lists[i][term] == '^':
                a = term
            b = len(sub_lists[i])-1
        num_numbers = b-a
        for number in range(a+1,b+1):
            temp_power += sub_lists[i][number]*10**(num_numbers-1)
            num_numbers-=1
        power.append(temp_power)
        temp_power = 0
        a = 0
        b = 0
    print(power)
    
RestorePower()

def TermOne():
    coe = [33, 22, 0]
    power = [3, 1, 0]
    term1 = [coe[n]*power[n] for n in range(len(coe))]
    print(term1)
    
TermOne()

def TermTwo():
    power = [3, 1, 0]
    term2 = [power[n]-1 for n in range(len(power))]
    print(term2)
    
TermTwo()


term1 = [99, 22, 0]
term2 = [2, 0, -1]
for i in range(0,2):
    print(term1[i], "X^", term2[i])
    
    
    

            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            