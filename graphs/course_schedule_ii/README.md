<h2><a href="https://leetcode.com/problems/course-schedule-ii/">207. Course Schedule II
</a></h2><h3>Medium</h3><hr><div><p>There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> numCourses = 2, prerequisites = [[1,0]]
<strong>Output:</strong> [0,1]
<string>Explanation:</strong> There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
<strong>Output:</strong> [0,2,1,3]
<strong>Explanation:</strong> There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> numCourses = 1, prerequisites = []
<strong>Output:</strong> [0]


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= numCourses <= 2000</code></li>
    <li><code>0 <= prerequisites.length <= numCourses * (numCourses - 1)</code></li>
    <li><code>prerequisites[i].length == 2</code></li>
    <li><code>0 <= ai, bi < numCourses</code></li>
    <li><code>ai != bi</code></li>
    <li>All the pairs <code>[ai, bi]</code> are distinct.</li>
</ul>
</div>