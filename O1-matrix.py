'''Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two cells sharing a common edge is 1.'''

# // Time Complexity : O(m*n)
# // Space Complexity : O(m*n)
# // Did this code successfully run on Leetcode : yes
# // Any problem you faced while coding this : no

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # get the data & data structures we need
        m, n = len(mat), len(mat[0])
        q = deque()
        dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]

        # load q with 0 nodes
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append([i, j])
                else:
                    mat[i][j] = -1 # mark unvisited
        
        # go through q
        while q:
            curr = q.popleft()
            for cr,cc in dirs:
                nr, nc = curr[0]+cr, curr[1]+cc
                if m > nr >= 0 and n > nc >= 0 and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[curr[0]][curr[1]] + 1    
                    q.append([nr, nc])

        return mat 
