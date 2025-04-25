

class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, value):
        self.queue.append(value)
        print(f'{value} added to the queue')
    
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
        else:
            removed_value = self.queue.pop(0)  
            print(f'{removed_value} removed from the queue')
    
    def front(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f'Front element is: {self.queue[0]}')
    
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements are:", self.queue)

def menu():
    queue = Queue()
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Front")
        print("4. Display")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            value = int(input("Enter the value to enqueue: "))
            queue.enqueue(value)
        elif choice == 2:
            queue.dequeue()
        elif choice == 3:
            queue.front()
        elif choice == 4:
            queue.display()
        elif choice == 5:
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please try again.")


menu()
