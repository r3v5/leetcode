<h2><a href="https://leetcode.com/problems/string-to-integer-atoi/description/">8. String to Integer (atoi)</a></h2><h3>Medium</h3><hr><div>Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.


<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "42"
<strong>Output:</strong> 42
<strong>Explanation:</strong> The underlined characters are what is read in and the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)


<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong>  s = " -042"
<strong>Output:</strong> -42
<p>&nbsp;</p>

<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 <= s.length <= 200</code></li>
	<li><code>s</code> consists of English letters (lower-case and upper-case), digits (<code>0-9</code>), <code>' '</code>, <code>'+'</code>, <code>'-'</code>, and <code>'.'</code>.</li>
</ul>
</div>