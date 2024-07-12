<h2><a href="https://leetcode.com/problems/baseball-game/description/">682. Baseball Game</a></h2><h3>Easy</h3><hr><div><p>You are keeping the scores for a baseball game with strange rules. At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.

The test cases are generated such that the answer and all intermediate calculations fit in a 32-bit integer and that all operations are valid.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> ops = ["5","2","C","D","+"]
<strong>Output:</strong> 30

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> ops = ["5","-2","4","C","D","9","+","+"]
<strong>Output:</strong> 27

<p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> ops = ["1","C"]
<strong>Output:</strong> 0

<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= operations.length <= 1000</code></li>
	<li>operations[i] is "C", "D", "+", or a string representing an integer in the range <code>[-3 * 10^4, 3 * 10^4]</code>.</li>
    <li>For operation <code>"+"</code>, there will always be at least two previous scores on the record.</li>
    <li>For operations <code>"C"</code> and <code>"D"</code>, there will always be at least one previous score on the record.</li>
</ul>
</div>