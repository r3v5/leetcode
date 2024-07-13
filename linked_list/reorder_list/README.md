<h2><a href="https://leetcode.com/problems/reorder-list/">143. Reorder List</a></h2><h3>Medium</h3><hr><div><p>You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 400px; height: 277px">
<pre><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 400px; height: 277px">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10^4]</code>.</li>
	<li><code>1 <= Node.val <= 1000</code></li>
</ul>
</div>