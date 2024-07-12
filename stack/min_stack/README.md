<h2><a href="https://leetcode.com/problems/min-stack/description/">155. Min Stack</a></h2><h3>Medium</h3><hr><div><p>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> ["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
<strong>Output:</strong> [null,null,null,null,-3,null,0,-2]
<strong>Explanation:</strong> MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-2^31 <= val <= 2^31 - 1</code></li>
	<li>Methods <code>pop</code>, <code>top</code> and <code>getMin</code> operations will always be called on non-empty stacks.</li>
    <li>At most <code>3 * 10^4</code> calls will be made to <code>push</code>, <code>pop</code>, <code>top</code>, and <code>getMin</code>.</li>
</ul>
</div>