<h2><a href="https://leetcode.com/problems/subtree-of-another-tree/description/">572. Subtree of Another Tree</a></h2><h3>Easy</h3><hr><div><p>Given the roots of two binary trees <code>root</code> and <code>subRoot</code>, return <code>true</code> if there is a subtree of <code>root</code> with the same structure and node values of <code>subRoot<code> and <code>false</code> otherwise.

A subtree of a binary tree <code>tree<code> is a tree that consists of a node in <code>tree</code> and all of this node's descendants. The tree <code>tree</code> could also be considered as a subtree of itself.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [3,4,5,1,2], subRoot = [4,1,2]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
<strong>Output:</strong> false

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the <code>root</code> tree is in the range <code>[1, 2000]</code>.</li>
    <li>The number of nodes in the <code>subRoot</code> tree is in the range <code>[1, 1000]</code>.</li>
	<li><code>-10^4 <= root.val <= 10^4</code></li>
    <li><code>-10^4 <= subRoot.val <= 10^4</code></li>
</ul>
</div>