<h2><a href="https://leetcode.com/problems/binary-tree-maximum-path-sum/description/">124. Binary Tree Maximum Path Sum</a></h2><h3>Hard</h3><hr><div><p>A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the <code>root</code> of a binary tree, return the maximum path sum of any non-empty path.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [1,2,3]
<strong>Output:</strong> 6
<strong>Explanation:</strong> The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [-10,9,20,null,null,15,7]
<strong>Output:</strong> 42
<strong>Explanation:</strong> The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 3 * 10^4]</code>.</li>
	<li><code>-1000 <= Node.val <= 1000</code></li>
</ul>
</div>