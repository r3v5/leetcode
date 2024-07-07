<h2><a href="https://leetcode.com/problems/task-scheduler/description/">621. Task Scheduler</a></h2><h3>Medium</h3><hr><div><p>You are given an array of CPU <code>tasks</code>, each represented by letters A to Z, and a cooling time, <code>n</code>. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least <code>n</code> intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","A","A","B","B","B"], n = 2
<strong>Output:</strong> 8
<strong>Explanation:</strong> A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","C","A","B","D","B"], n = 1
<strong>Output:</strong> 6
<strong>Explanation:</strong> A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.
</pre>

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> tasks = ["A","A","A", "B","B","B"], n = 3
<strong>Output:</strong> 10
<strong>Explanation:</strong> A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= tasks.length <= 10^4</code></li>
	<li><code>tasks[i]</code> is an uppercase English letter.</li>
    <li><code>0 <= n <= 100</code></li>
</ul>
</div>