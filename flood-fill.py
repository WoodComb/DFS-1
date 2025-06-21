'''
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.
'''

# // Time Complexity : O(m*n)
# // Space Complexity : O(m*n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # #Directions array
        # dirs = [[0, -1], [1, 0], [0, 1], [-1,0]]

        # m,n = len(image), len(image[0])
        # init_color = image[sr][sc]
        # # edge case
        # if init_color == color:
        #     return image
        # q = deque()
        # q.append([sr, sc])
        # # color starting pixel
        # image[sr][sc] = color

        # while q:
        #     size = len(q)
        #     curr = q.popleft()
        #     # check the neighbors
        #     for row, col in dirs:
        #         cr, cc = curr[0] + row, curr[1] + col
        #         if cr >= 0 and cc >= 0 and cr < m and cc < n and image[cr][cc] == init_color:
        #             q.append([cr,cc])
        #             image[cr][cc] = color
        # return image


        m,n = len(image), len(image[0])
        init_color = image[sr][sc]
        # edge case
        if init_color == color:
            return image

        #Directions array
        dirs = [[0, -1], [1, 0], [0, 1], [-1,0]]

        def dfs(image, sr, sc, color, init_color):
            # base
            # bounds - we only go to the nodes that we need to color
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != init_color:
                return

            # logic
            image[sr][sc] = color # this is where we color
            for cr, cc in dirs: # this is how we travel. Where ever we travel, we color
                nr, nc = sr+cr, sc+cc
                dfs(image, nr, nc, color, init_color)

        dfs(image, sr, sc, color, init_color)
        return image        
