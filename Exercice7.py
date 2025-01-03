def sum_of_even_num(lst):
    sum = 0  
    for i in lst:  
        if i % 2 == 0:  
            sum += i  
    return sum  

lst = [2, 1, 6]
print(sum_of_even_num(lst))  
