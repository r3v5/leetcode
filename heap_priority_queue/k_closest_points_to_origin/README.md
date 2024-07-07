<h2><a href="https://leetcode.com/problems/k-closest-points-to-origin/">973. K Closest Points to Origin</a></h2><h3>Medium</h3><hr><div><p>Given an array of <code>points</code> where <code>points[i] = [xi, yi]</code> represents a point on the X-Y plane and an integer <code>k</code>, return the k closest points to the origin <code>(0, 0)</code>.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., <code>√(x1 - x2)^2 + (y1 - y2)^2</code>).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> points = [[1,3],[-2,2]], k = 1
<strong>Output:</strong> [[-2,2]]
<strong>Explanation:</strong> The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> points = [[3,3],[5,-1],[-2,4]], k = 2
<strong>Output:</strong> [[3,3],[-2,4]]
<strong>Explanation:</strong> The answer [[-2,4],[3,3]] would also be accepted.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= k <= points.length <= 10^4</code></li>
	<li><code>-10^4 <= xi, yi <= 10^4</code></li>
</ul>
</div>