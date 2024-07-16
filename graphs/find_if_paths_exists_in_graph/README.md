<h2><a href="https://leetcode.com/problems/find-if-path-exists-in-graph/description/">1971. Find if Path Exists in Graph</a></h2><h3>Easy</h3><hr><div><p>There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
<strong>Output:</strong> true
<strong>Explanation:</strong> There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no path from vertex 0 to vertex 5.
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= n <= 2 * 10^5</code></li>
	<li><code>0 <= edges.length <= 2 * 10^5</code></li>
    <li><code>edges[i].length == 2</code></li>
    <li><code>0 <= ui, vi <= n - 1</code></li>
    <li><code>ui != vi</code></li>
    <li><code>0 <= source, destination <= n - 1</code></li>
    <li>There are no duplicate edges.</li>
    <li>There are no self edges.</li>
</ul>
</div>