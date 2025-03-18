"""
Sum of Elements:
Write a Python program to find the sum of all elements in a list.
"""

def count(lst):
    List_counting = {}
    for item in lst:
        if item in List_counting:
            List_counting[item] += 1
        else:
            List_counting[item] = 1
    return List_counting

lst = [1,2,1,3,4,2,7,4,5,6,4]  
print(count(lst))          
