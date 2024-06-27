<h2><a href="https://leetcode.com/problems/product-of-array-except-self/description/">238. Product of Array Except Self.</a></h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, return an array <code>answer</code> such that <code>answer[i]</code> is equal to the product of all the elements of <code>nums</code> except <code>nums[i]</code>.

The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in <code>O(n)</code> time and without using the division operation.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 <= nums.length <= 10^5</code></li>
	<li>-30 <= nums[i] <= 30</code></li>
    <li>The product of any prefix or suffix of <code>nums</code> is guaranteed to fit in a 32-bit integer.</li>
</ul>
</div>