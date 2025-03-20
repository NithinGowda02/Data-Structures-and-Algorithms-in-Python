stack = []
def push():
    element = input("Enter the Element to Insert >> ")
    stack.append(element)
    print(stack)

def pop():
    if not stack:
        print("Stack is Empty..")
    else:
        ele = stack.pop()
        print("Item popped successfully...")
        print(f"Popped element is >> {ele}")
        print(stack)

while True:
    choice = int(input("Enter your choice (1 to push, 2 to pop, 3 to exit) >> "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print("Invalid input")        
