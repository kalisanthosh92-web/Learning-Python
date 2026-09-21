class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        print(f"Successfully pushed '{data}' onto the stack.")

    def pop(self):
        if self.is_empty():
            print("Stack Underflow! The stack is empty.")
            return None
        popped_node = self.top
        self.top = self.top.next
        print(f"Successfully popped '{popped_node.data}' from the stack.")
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("The stack is empty.")
            return None
        print(f"Top element is: {self.top.data}")
        return self.top.data

    def display(self):
        if self.is_empty():
            print("The stack is empty.")
            return
        print("Stack elements (Top -> Bottom):")
        current = self.top
        while current:
            print(f"| {current.data} |")
            current = current.next
        print("-------")

def main():
    stack = Stack()
    
    while True:
        print("=========================================")
        print("STACK USING LINKED LIST")
        print("=========================================")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Check if Empty")
        print("6. Exit")
        print("=========================================")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            data = input("Enter the value to push: ")
            stack.push(data)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.peek()
        elif choice == '4':
            stack.display()
        elif choice == '5':
            if stack.is_empty():
                print("The stack is EMPTY.")
            else:
                print("The stack is NOT EMPTY.")
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 1 to 6.")
        print()

if __name__ == "__main__":
    main()


