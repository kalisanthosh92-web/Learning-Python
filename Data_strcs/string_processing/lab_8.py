import customtkinter as ctk
from tkinter import Canvas
from collections import deque

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTreeApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Binary Tree Visualizer")
        self.geometry("800x650")
        
        # Build Binary Tree Structure
        self.root_node = Node("A")
        self.root_node.left = Node("B")
        self.root_node.right = Node("C")
        self.root_node.left.left = Node("D")
        self.root_node.left.left.left = Node("H")
        self.root_node.left.right = Node("E")
        self.root_node.right.left = Node("F")
        self.root_node.right.right = Node("G")
        
        self.order = []
        self.visited = []
        
        # Layout UI Elements
        title = ctk.CTkLabel(
            self, text="Binary Tree Traversal", font=ctk.CTkFont(size=24, weight="bold")
        )
        title.pack(pady=12)
        
        self.canvas = Canvas(
            self, width=760, height=350, bg="white", highlightthickness=1, highlightbackground="#cccccc"
        )
        self.canvas.pack(padx=15, pady=8, fill="both", expand=True)
        
        buttons = ctk.CTkFrame(self)
        buttons.pack(padx=15, pady=8, fill="x")
        
        ctk.CTkButton(
            buttons, text="Preorder", command=lambda: self.choose_order("preorder")
        ).pack(side="left", padx=5, pady=10, expand=True)
        
        ctk.CTkButton(
            buttons, text="Inorder", command=lambda: self.choose_order("inorder")
        ).pack(side="left", padx=5, pady=10, expand=True)
        
        ctk.CTkButton(
            buttons, text="Postorder", command=lambda: self.choose_order("postorder")
        ).pack(side="left", padx=5, pady=10, expand=True)
        
        ctk.CTkButton(
            buttons, text="Level-order", command=lambda: self.choose_order("level")
        ).pack(side="left", padx=5, pady=10, expand=True)
        
        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.pack(pady=5)

        ctk.CTkButton(
            actions, text="Count Nodes", command=self.count_nodes, width=130
        ).pack(side="left", padx=6)
                
        ctk.CTkButton(
            actions, text="Next Step", command=self.next_step, width=130
        ).pack(side="left", padx=6)
        
       
        ctk.CTkButton(
            actions, text="Reset", command=self.reset, width=100, fg_color="gray"
        ).pack(side="left", padx=6)
        
        self.status = ctk.CTkLabel(
            self, text="Choose a traversal method.", font=ctk.CTkFont(size=15)
        )
        self.status.pack(pady=5)
        
        self.sequence = ctk.CTkLabel(
            self, text="Visited nodes: —", font=ctk.CTkFont(size=15, weight="bold"), wraplength=750
        )
        self.sequence.pack(pady=(0, 12))
        
        self.draw_tree()

    def draw_tree(self):
        self.canvas.delete("all")
        
        # Node positions
        positions = {
            "A": (380, 55),
            "B": (250, 150),
            "C": (510, 150),
            "D": (180, 250),
            "H": (130, 320),
            "E": (320, 250),
            "F": (440, 250),
            "G": (580, 250)
        }
        
        # Draw connecting lines first
        edges = [
            ("A", "B"), ("A", "C"),
            ("B", "D"), ("B", "E"),
            ("C", "F"), ("C", "G"),
            ("D", "H")
        ]
        
        for parent, child in edges:
            x1, y1 = positions[parent]
            x2, y2 = positions[child]
            self.canvas.create_line(x1, y1, x2, y2, width=3, fill="#777777")
            
        # Draw the nodes
        for value, (x, y) in positions.items():
            if value in self.visited:
                color = "#2EAD68"
            else:
                color = "#CFE5FF"
                
            self.canvas.create_oval(
                x - 25, y - 25, x + 25, y + 25, fill=color, outline="#2766A5", width=2
            )
            self.canvas.create_text(
                x, y, text=value, font=("Arial", 16, "bold"),
                fill="#123456" if value not in self.visited else "white"
            )

    def preorder(self, node, result):
        if node is None:
            return
        result.append(node.value)
        self.preorder(node.left, result)
        self.preorder(node.right, result)

    def inorder(self, node, result):
        if node is None:
            return
        self.inorder(node.left, result)
        self.result = result.append(node.value)
        self.inorder(node.right, result)

    def postorder(self, node, result):
        if node is None:
            return
        self.postorder(node.left, result)
        self.postorder(node.right, result)
        result.append(node.value)

    def level_order(self):
        result = []
        queue = deque([self.root_node])
        while queue:
            node = queue.popleft()
            result.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def count(self, node):
        if node is None:
            return 0    
        return 1 + self.count(node.left) + self.count(node.right)

    
    def count_nodes(self):
        total_nodes = self.count(self.root_node)
        self.sequence.configure(
            text="Total nodes: " + str(total_nodes)
        )

        

    def choose_order(self, method):
        result = []
        if method == "preorder":
            self.preorder(self.root_node, result)
        elif method == "inorder":
            self.inorder(self.root_node, result)
        elif method == "postorder":
            self.postorder(self.root_node, result)
        else:
            result = self.level_order()
            
        self.order = result
        self.visited = []
        self.status.configure(
            text=f"Traversal order: {' → '.join(self.order)}"
        )
        self.sequence.configure(text="Visited nodes: —")
        self.draw_tree()

    def next_step(self):
        if not self.order:
            self.status.configure(text="Choose a traversal method first.")
            return
            
        if len(self.visited) == len(self.order):
            self.status.configure(text="Traversal complete! Choose another method or Reset.")
            return
            
        next_value = self.order[len(self.visited)]
        self.visited.append(next_value)
        self.sequence.configure(
            text="Visited nodes: " + " → ".join(self.visited)
        )
        
        if len(self.visited) == len(self.order):
            self.status.configure(text=f"Visited {next_value}. Traversal complete!")
        else:
            self.status.configure(text=f"Visited node: {next_value}")
            
        self.draw_tree()

    def reset(self):
        self.order = []
        self.visited = []
        self.status.configure(text="Choose a traversal method.")
        self.sequence.configure(text="Visited nodes: —")
        self.draw_tree()

if __name__ == "__main__":
    app = BinaryTreeApp()
    app.mainloop()
