<h2><a href="https://leetcode.com/problems/find-duplicate-subtrees/">652. Find Duplicate Subtrees</a></h2><h3>Medium</h3><hr><div><p>Given the <code>root</code> of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e1.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [1,2,3,4,null,2,4,null,null,4]
<strong>Output:</strong> [[2,4],[4]]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e2.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [2,1,1]
<strong>Output:</strong> [[1]]

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e33.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [2,2,2,3,null,3,null]
<strong>Output:</strong> [[2,3],[3]]

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the tree will be in the range <code>[1, 5000]</code></li>
	<li><code>-200 <= Node.val <= 200</code></li>
</ul>
</div>