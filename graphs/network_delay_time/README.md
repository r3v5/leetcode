<h2><a href="https://leetcode.com/problems/network-delay-time/">743. Network Delay Time
</a></h2><h3>Medium</h3><hr><div><p>You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
<strong>Output:</strong> 2
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 1
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> times = [[1,2,1]], n = 2, k = 2
<strong>Output:</strong> -1


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= k <= n <= 100</code></li>
    <li><code>1 <= times.length <= 6000</code></li>
    <li><code>times[i].length == 3</code></li>
    <li><code>1 <= ui, vi <= n</code></li>
    <li><code>ui != vi</code></li>
    <li><code>0 <= wi <= 100</code></li>
    <li>All the pairs (ui, vi) are unique. (i.e., no multiple edges.)</li>
</ul>
</div>