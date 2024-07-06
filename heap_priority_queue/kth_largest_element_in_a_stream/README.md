<h2><a href="https://leetcode.com/problems/kth-largest-element-in-a-stream/">703. Kth Largest Element in a Stream</a></h2><h3>Easy</h3><hr><div><p>Design a class to find the <code>k^th</code> largest element in a stream. Note that it is the <code>k^th</code> largest element in the sorted order, not the <code>k^th</code> distinct element.

Implement <code>KthLargest</code> class:

<code>KthLargest(int k, int[] nums)</code> Initializes the object with the integer k and the stream of integers <code>nums</code>.
<code>int add(int val)</code> Appends the integer <code>val</code> to the stream and returns the element representing the <code>k^th</code> largest element in the stream.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> ["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
<strong>Output:</strong> [null, 4, 5, 5, 8, 8]
<strong>Explanation:</strong> KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= k <= 10^4</code></li>
	<li><code>0 <= nums.length <= 10^4</code></li>
    <li><code>-10^4 <= nums[i] <= 10^4</code></li>
    <li><code>-10^4 <= val <= 10^4</code></li>
    <li>At most <code>10^4</code> calls will be made to add.</li>
    <li>It is guaranteed that there will be at least <code>k</code> elements in the array when you search for the <code>k^th</code> element.</li>
</ul>
</div>