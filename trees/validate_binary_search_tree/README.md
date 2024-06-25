<h2><a href="https://leetcode.com/problems/validate-binary-search-tree/description/">98. Validate Binary Search Tree</a></h2><h3>Medium</h3><hr><div><p>Given the <code>root</code> of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.


<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [2,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> Nodes in blue are good.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node's value is 5 but its right child's value is 4.

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the binary tree is in the range <code>[1, 10^4]</code>.</li>
	<li><code>-2^31</code> <= Node.val <= <code>2^31 - 1</code></li>
</ul>
</div>