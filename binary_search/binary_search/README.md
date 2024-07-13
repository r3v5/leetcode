<h2><a href="https://leetcode.com/problems/binary-search/">704. Binary Search</a></h2><h3>Easy</h3><hr><div><p>Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 9
<strong>Output:</strong> 4
<strong>Explanation:</strong> 9 exists in nums and its index is 4
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,0,3,5,9,12], target = 2
<strong>Output:</strong> -1
<strong>Explanation:</strong> 2 does not exist in nums so return -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= nums.length <= 10^4</code></li>
	<li><code>-10^4 < nums[i], target < 10^4</code></li>
    <li>All the integers in nums are unique.</li>
    <li>nums is sorted in ascending order.</li>
</ul>
</div>