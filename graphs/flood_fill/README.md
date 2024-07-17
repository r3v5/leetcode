<h2><a href="https://leetcode.com/problems/flood-fill/description/">733. Flood Fill
</a></h2><h3>Easy</h3><hr><div><p>An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/01/flood1-grid.jpg" style="width: 400px; height: 277px;">
<pre><strong>Input:</strong> image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
<strong>Output:</strong> [[2,2,2],[2,2,0],[2,0,1]]
<strong>Explanation:</strong> From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
</pre>

<p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
<strong>Output:</strong> [[0,0,0],[0,0,0]]
<strong>Explanation:</strong> The starting pixel is already colored 0, so no changes are made to the image.
</pre>


<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == image.length</code></li>
    <li><code>n == image[i].length</code></li>
    <li><code>1 <= m, n <= 50</code></li>
    <li><code>0 <= image[i][j], color < 216</code></li>
    <li><code>0 <= sr < m</code></li>
    <li><code>0 <= sc < n</code></li>
</ul>
</div>