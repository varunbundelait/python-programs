def find_miss(lst):
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    min=lst[0] 
    for i in lst:
        if i < min:
            min =i
    list1=[]
    for num in range(min+1,max):
        if num not in lst:
            list1.append(num)
    return list1

lst=[1, 3, 5, 7,10, 13, 17]
print(find_miss(lst))                 