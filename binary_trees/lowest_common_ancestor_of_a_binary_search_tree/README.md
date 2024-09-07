<h2><a href="https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/">235. Lowest Common Ancestor of a Binary Search Tree</a></h2><h3>Medium</h3><hr><div><p>Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes <code>p</code> and <code>q</code> as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”   
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
<strong>Output:</strong> 6
<strong>Explanation:</strong> The LCA of nodes 2 and 8 is 6.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
<strong>Output:</strong> 2
<strong>Explanation:</strong> The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> root = [2,1], p = 2, q = 1
<strong>Output:</strong> 2

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[2, 10^5]</code>.</li>
    <li><code>-10^9 <= Node.val <= 10^9</code></li>
	<li>All <code>Node.val</code> are unique.</li>
    <li><code>p != q</code>.</li>
    <li><code>p</code> and <code>q</code> will exist in the BST.</li>
</ul>
</div>