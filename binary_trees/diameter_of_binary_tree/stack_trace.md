      1
     / \
    2   3
   / \
  4   5


First, we initialize the following:

	•	diameter = 0
	•	stack = [[root, False]]
	•	height = {}

We’ll walk through the process step by step.

Initial State

	•	stack = [[1, False]]
	•	diameter = 0
	•	height = {}

Step-by-Step Execution

	1.	Pop [1, False]
	•	cur = 1
	•	visited = False
	•	Push [1, True] to stack.
	•	Push [3, False] and [2, False] to stack.
	•	stack = [[1, True], [3, False], [2, False]]
	2.	Pop [2, False]
	•	cur = 2
	•	visited = False
	•	Push [2, True] to stack.
	•	Push [5, False] and [4, False] to stack.
	•	stack = [[1, True], [3, False], [2, True], [5, False], [4, False]]
	3.	Pop [4, False]
	•	cur = 4
	•	visited = False
	•	Push [4, True] to stack.
	•	Since 4 has no children, no more nodes are pushed.
	•	stack = [[1, True], [3, False], [2, True], [5, False], [4, True]]
	4.	Pop [4, True]
	•	cur = 4
	•	visited = True
	•	left_height = height.get(None, -1) = -1
	•	right_height = height.get(None, -1) = -1
	•	height[4] = 1 + max(-1, -1) = 0
	•	diameter = max(0, 2 + (-1) + (-1)) = 0
	•	stack = [[1, True], [3, False], [2, True], [5, False]]
	•	height = {4: 0}
	5.	Pop [5, False]
	•	cur = 5
	•	visited = False
	•	Push [5, True] to stack.
	•	Since 5 has no children, no more nodes are pushed.
	•	stack = [[1, True], [3, False], [2, True], [5, True]]
	6.	Pop [5, True]
	•	cur = 5
	•	visited = True
	•	left_height = height.get(None, -1) = -1
	•	right_height = height.get(None, -1) = -1
	•	height[5] = 1 + max(-1, -1) = 0
	•	diameter = max(0, 2 + (-1) + (-1)) = 0
	•	stack = [[1, True], [3, False], [2, True]]
	•	height = {4: 0, 5: 0}
	7.	Pop [2, True]
	•	cur = 2
	•	visited = True
	•	left_height = height.get(4, -1) = 0
	•	right_height = height.get(5, -1) = 0
	•	height[2] = 1 + max(0, 0) = 1
	•	diameter = max(0, 2 + 0 + 0) = 2
	•	stack = [[1, True], [3, False]]
	•	height = {4: 0, 5: 0, 2: 1}
	8.	Pop [3, False]
	•	cur = 3
	•	visited = False
	•	Push [3, True] to stack.
	•	Since 3 has no children, no more nodes are pushed.
	•	stack = [[1, True], [3, True]]
	9.	Pop [3, True]
	•	cur = 3
	•	visited = True
	•	left_height = height.get(None, -1) = -1
	•	right_height = height.get(None, -1) = -1
	•	height[3] = 1 + max(-1, -1) = 0
	•	diameter = max(2, 2 + (-1) + (-1)) = 2
	•	stack = [[1, True]]
	•	height = {4: 0, 5: 0, 2: 1, 3: 0}
	10.	Pop [1, True]
	•	cur = 1
	•	visited = True
	•	left_height = height.get(2, -1) = 1
	•	right_height = height.get(3, -1) = 0
	•	height[1] = 1 + max(1, 0) = 2
	•	diameter = max(2, 2 + 1 + 0) = 3
	•	stack = []
	•	height = {4: 0, 5: 0, 2: 1, 3: 0, 1: 2}

Final State

	•	diameter = 3
	•	height = {4: 0, 5: 0, 2: 1, 3: 0, 1: 2}

The longest path in the tree is 4 -> 2 -> 1 -> 3, which has a length of 3 edges. Thus, the diameter of the tree is 3.

This step-by-step execution shows how the height of each node is calculated and how the diameter is updated iteratively.