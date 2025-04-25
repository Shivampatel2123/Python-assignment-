

class Stack:
    def __init__(self):
        self.stack = []
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
        print(f'{value} pushed to stack')
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            removed_value = self.stack.pop()
            print(f'{removed_value} popped from stack')
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print(f'Top element is: {self.stack[-1]}')
    
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements are:", self.stack)


def menu():
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter the value to push: "))
            stack.push(value)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.peek()
        elif choice == 4:
            stack.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")

menu()

