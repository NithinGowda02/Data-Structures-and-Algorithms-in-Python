def second_largest(lst):
    unique_list = list(set(lst))
    if len(unique_list) < 2:
        return "there is no Second largest element."
    else:
        second_l = max(unique_list)
        unique_list.remove(second_l)
        return f"{max(unique_list)}"
l1 = second_largest([12,23,1,23,32,4,5,44,56,34])
l2 = second_largest([2,33,2,33,22,24,44,55,33,66]) 
print(f"{l2} is the Second largest element in the list..")       