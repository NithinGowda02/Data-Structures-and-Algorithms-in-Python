"""
Given a list and a number k, rotate the list to the right by k positions
"""
def rotate_list(lst,k):
    if not lst or k == 0:
        return lst
    k = k % len(lst)
    return lst[-k:] + lst[:-k]

print(rotate_list([1,2,3,4,5,6],2))
print(rotate_list([10,20,30,40,50],3))
         
