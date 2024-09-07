<h2><a href="https://leetcode.com/problems/count-good-nodes-in-binary-tree/">1448. Count Good Nodes in Binary Tree</a></h2><h3>Medium</h3><hr><div><p>Given the <code>root</code> of a binary tree, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.


<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [3,1,4,3,null,1,5]
<strong>Output:</strong> 4
<strong>Explanation:</strong> Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [3,3,null,4,2]
<strong>Output:</strong> 3
<strong>Explanation:</strong>  Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = [1]
<strong>Output:</strong> 1
<strong>Explanation:</strong>  Root is considered as good.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the binary tree is in the range <code>[1, 10^5]</code>.</li>
	<li>Each node's value is between <code>[-10^4, 10^4]</code></li>
</ul>
</div>