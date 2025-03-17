"""
Remove Duplicates:
Given a list, remove all duplicate elements and return the new list.
"""

l=[22,34,22,34,67,89,46,78,46,2,2]

removed = []
for i in l:
    if i not in removed:
        removed.append(i)
print(removed)    
