<h2><a href="https://leetcode.com/problems/search-in-rotated-sorted-array/description/">33. Search in Rotated Sorted Array</a></h2><h3>Medium</h3><hr><div><p>There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 0
<strong>Output:</strong> 4
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [4,5,6,7,0,1,2], target = 3
<strong>Output:</strong> -1
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> -1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= nums.length <= 5000</code></li>
	<li><code>-10^4 <= nums[i] <= 10^4</code></li>
    <li>All values of nums are unique.</li>
    <li>nums is an ascending array that is possibly rotated.</li>
    <li><code>-10^4 <= target <= 10^4</code></li>
</ul>
</div>