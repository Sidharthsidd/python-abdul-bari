import datetime

dsa_plan = [
    # Week 1: Basics
    "Python Essentials (Lists, Tuples, Dicts, Loops, Functions)",
    "Understanding Time & Space Complexity",
    "Recursion Basics",
    "Simple Problems (Factorial, Fibonacci, GCD using Recursion)",
    "Intro to Arrays (Traversal, Insertion, Deletion)",
    "Solve 5 Array problems on LeetCode",
    # Week 2: Sorting & Searching
    "Selection Sort, Bubble Sort, Insertion Sort",
    "Merge Sort, Quick Sort",
    "Binary Search & its Variations",
    "Solve 5 problems on Sorting",
    "Solve 5 problems on Searching",
    "Sliding Window & Two Pointer Approach",
    "Solve 5 problems using Two Pointer / Sliding Window",
    # Week 3: Linked List & Stack
    "Singly & Doubly Linked List (Implementation + Problems)",
    "Stack (Using List & Linked List)",
    "Solve Stack-based problems",
    "Queue (Using List & Linked List), Circular Queue",
    "Solve Queue-based problems",
    # Week 4: Trees & Graphs
    "Binary Tree Basics",
    "Tree Traversals (Inorder, Preorder, Postorder)",
    "Binary Search Tree (BST) Operations",
    "Graph Basics (Adjacency List, BFS, DFS)",
    "Solve 5 Graph Problems",
    "Dynamic Programming Basics (Recursion + Memoization)",
    "Solve 5 DP Problems"
]

def generate_study_plan(start_date):
    print("\n--- Your DSA Study Plan ---\n")
    for i, topic in enumerate(dsa_plan):
        study_date = start_date + datetime.timedelta(days=i)
        print(f"Day {i+1} ({study_date.strftime('%Y-%m-%d')}): {topic}")

# Set your start date
start_date = datetime.date.today()
generate_study_plan(start_date)


