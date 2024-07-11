<h2><a href="https://leetcode.com/problems/find-k-closest-elements/description/">658. Find K Closest Elements</a></h2><h3>Medium</h3><hr><div><p>Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = 3
<strong>Output:</strong> [1,2,3,4]

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> arr = [1,2,3,4,5], k = 4, x = -1
<strong>Output:</strong> [1,2,3,4]

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= k <= arr.length</code></li>
	<li><code>1 <= arr.length <= 10^4</code></li>
    <li><code>arr</code> is sorted in ascending order.</li>
    <li><code>-10^4 <= arr[i], x <= 10^4</code></li>
</ul>
</div>