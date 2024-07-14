Stack Trace Explanation

Let’s walk through the stack trace for nums = [1, 2, 3]:

	1.	Initial State:
	•	stack = [([], 0)]
	•	res = []
	2.	First Iteration:
	•	Pop: current_subset = [], index = 0
	•	Add current_subset to res: res = [[]]
	•	Push new subsets to the stack:
	•	stack = [([1], 1), ([2], 2), ([3], 3)]
	3.	Second Iteration:
	•	Pop: current_subset = [3], index = 3
	•	Add current_subset to res: res = [[], [3]]
	•	No new elements to add, so the stack remains: stack = [([1], 1), ([2], 2)]
	4.	Third Iteration:
	•	Pop: current_subset = [2], index = 2
	•	Add current_subset to res: res = [[], [3], [2]]
	•	Push new subset to the stack:
	•	stack = [([1], 1), ([2, 3], 3)]
	5.	Fourth Iteration:
	•	Pop: current_subset = [2, 3], index = 3
	•	Add current_subset to res: res = [[], [3], [2], [2, 3]]
	•	No new elements to add, so the stack remains: stack = [([1], 1)]
	6.	Fifth Iteration:
	•	Pop: current_subset = [1], index = 1
	•	Add current_subset to res: res = [[], [3], [2], [2, 3], [1]]
	•	Push new subsets to the stack:
	•	stack = [([1, 2], 2), ([1, 3], 3)]
	7.	Sixth Iteration:
	•	Pop: current_subset = [1, 3], index = 3
	•	Add current_subset to res: res = [[], [3], [2], [2, 3], [1], [1, 3]]
	•	No new elements to add, so the stack remains: stack = [([1, 2], 2)]
	8.	Seventh Iteration:
	•	Pop: current_subset = [1, 2], index = 2
	•	Add current_subset to res: res = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2]]
	•	Push new subset to the stack:
	•	stack = [([1, 2, 3], 3)]
	9.	Eighth Iteration:
	•	Pop: current_subset = [1, 2, 3], index = 3
	•	Add current_subset to res: res = [[], [3], [2], [2, 3], [1], [1, 3], [1, 2], [1, 2, 3]]
	•	No new elements to add, so the stack remains: stack = []