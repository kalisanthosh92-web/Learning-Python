
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, Item ):
        current = self.head
        while current:
            if current.data == Item:
                return 'Found'
            current = current.next
        return 'Not found'

    def delete(self, Item ):
        current = self.head
        prev = None

        if current and current.data == Item:
            self.head = current.next
            return True

        while current and current.data != Item:
            prev = current
            current = current.next

        if not current:
            return False

        prev.next = current.next
        return True


class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = DNode(data)
        if self.head is not None:
            self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def add_at_end(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def display_forward(self):
        current = self.head
        while current:
            if current.next:
                print(current.data, end=" ⇄ ")
            else:
                print(current.data, end="")
            current = current.next
        print()

    def display_backward(self):
        current = self.head
        if not current:
            return
        while current.next:
            current = current.next
        
        while current:
            if current.prev:
                print(current.data, end=" ⇄ ")
            else:
                print(current.data, end="")
            current = current.prev
        print()

    def search(self, Item):
        current = self.head
        while current:
            if current.data == Item:
                return 'found'
            current = current.next
        return 'Not found'

    def delete(self, Item):
        current = self.head

        while current and current.data != Item:
            current = current.next

        if not current:
            return False

        if current == self.head:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return True

        if current.next:
            current.next.prev = current.prev
        
        if current.prev:
            current.prev.next = current.next
            
        return True




if __name__ == "__main__":
    items = ["Quiz", "Laboratory Exercise", "Midterm Examination", "Project", "Presentation"]

    # Singly Linked List 
    print("===== SINGLY LINKED LIST =====")
    sll = SinglyLinkedList()
    for item in items:
        sll.add_at_end(item)

    print("Original Activities: ")
    sll.display()

    print("\nSearching for Project: ")
    print(f"Project {sll.search('Project')}")

    print("\nSearching for Final Examination: ")
    print(f"Final Examination {sll.search('Final Examination')} ")

    print("\nDelete Midterm Examination...")
    sll.delete("Midterm Examination")

    print('\nUpdated Activies')
    sll.display()


    #Doubly Linked List
    print("\n\n===== DOUBLY LINKED LIST =====")
    dll = DoublyLinkedList()
    for item in items:
        dll.add_at_end(item)

    print("Original Activities: ")
    dll.display_forward()

    print("\nSearching for Project: ")
    print(f"Project {dll.search('Project')}")

    print("\nSearching for Final Examination: ")
    print(f"Final Examination {dll.search('Final Examination')} ")

    print("\nDeleting Midterm Examination... ")
    
    print("\nForward: ")
    dll.display_forward()

    print("\nBackward: ")
    dll.display_backward()
