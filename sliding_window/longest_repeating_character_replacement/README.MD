<h2><a href="https://leetcode.com/problems/longest-repeating-character-replacement/description/">424. Longest Repeating Character Replacement</a></h2><h3>Medium</h3><hr><div><p>You are given a string <code>s</code> and an integer <code>k</code>. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most <code>k</code> times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.


<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "ABAB", k = 2
<strong>Output:</strong> 4
<strong>Explanation:</strong> Replace the two 'A's with two 'B's or vice versa.

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s1 = "ab", s2 = "eidboaoo"
<strong>Output:</strong> false
<strong>Explanation:</strong> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 <= s.length <= 10^5</code></li>
	<li><code>s</code> consists of only uppercase English letters.</li>
    <li><code>0 <= k <= s.length</code></li>
</ul>
</div>