<h2><a href="https://leetcode.com/problems/last-stone-weight/">1046. Last Stone Weight</a></h2><h3>Easy</h3><hr><div><p>You are given an array of integers <code>stones</code> where <code>stones[i]</code> is the weight of the <code>i^th</code> stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights <code>x</code> and <code>y</code> with <code>x <= y</code>. The result of this smash is:

If <code>x == y</code>, both stones are destroyed, and
If <code>x != y</code>, the stone of weight <code>x</code> is destroyed, and the stone of weight y has new weight <code>y - x</code>.
At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return <code>0</code>.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> stones = [2,7,4,1,8,1]
<strong>Output:</strong> 1
<strong>Explanation:</strong> We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= stones.length <= 30</code></li>
	<li><code>1 <= stones[i] <= 1000</code></li>
</ul>
</div>