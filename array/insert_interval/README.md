<h2><a href="https://leetcode.com/problems/insert-interval/">57. Insert Interval</a></h2><h3>Medium</h3><hr><div><p>You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.

<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,3],[6,9]], newInterval = [2,5]
<strong>Output:</strong> [[1,5],[6,9]]

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
<strong>Output:</strong> [[1,2],[3,10],[12,16]]
<strong>Explanation:</strong> Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 <= intervals.length <= 10^4</code></li>
	<li><code>intervals[i].length == 2</code></li>
    <li><code>0 <= starti <= endi <= 10^5</code></li>
    <li><code>intervals is sorted by starti in ascending order.</code></li>
    <li><code>newInterval.length == 2</code></li>
    <li><code>0 <= start <= end <= 10^5</code></li>
</ul>
</div>