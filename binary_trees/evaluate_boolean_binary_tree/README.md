<h2><a href="https://leetcode.com/problems/evaluate-boolean-binary-tree/">2331. Evaluate Boolean Binary Tree</a></h2><h3>Easy</h3><hr><div><p>You are given the <code>root</code> of a full binary tree with the following properties:

- Leaf nodes have either the value <code>0</code> or <code>1</code>, where <code>0</code> represents <code>False</code> and <code>1</code> represents <code>True</code>.
- Non-leaf nodes have either the value <code>2</code> or <code>3</code>, where <code>2</code> represents the boolean <code>OR</code> and <code>3</code> represents the boolean <code>AND</code>.

The evaluation of a node is as follows:
- If the node is a leaf node, the evaluation is the value of the node, i.e. <code>True</code> or <code>False</code>.
- Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.

Return the boolean result of evaluating the <code>root</code> node.

A full binary tree is a binary tree where each node has either <code>0</code> or <code>2</code> children.

A leaf node is a node that has zero children.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/16/example1drawio1.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [2,1,3,null,null,0,1]
<strong>Output:</strong> true
<strong>Explanation:</strong> The above diagram illustrates the evaluation process.
The AND node evaluates to False AND True = False.
The OR node evaluates to True OR False = True.
The root node evaluates to True, so we return true.
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> root = [0]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node is a leaf node and it evaluates to false, so we return false.

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>0 <= Node.val <= 3</code></li>
    <li>Every node has either <code>0</code> or <code>2</code> children.</li>
    <li>Leaf nodes have a value of <code>0</code> or <code>1</code>.</li>
    <li>Non-leaf nodes have a value of <code>2</code> or <code>3</code>.</li>
</ul>
</div>