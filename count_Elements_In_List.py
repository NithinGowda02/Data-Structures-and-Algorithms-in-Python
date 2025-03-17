
def count_element(list_item,target):
    count = 0
    for i in list_item:
        if i == target:
            count += 1
    print(f"Count of given element >> {count}")  
list_item = [12,2,3,4,2,5,3,5,6,4,3,2,2,8,9]
target = 2 
count_element(list_item,target)         
