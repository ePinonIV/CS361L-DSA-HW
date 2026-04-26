from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # check if coordinate is in bounds of grid size constraints
        def safe_coord(i, j, m, n):
            if 0 <= i < m and 0 <= j < n:
                return True
            else:
                return False

        m = len(grid) 
        n = len(grid[0]) 

        q = deque()

        fresh_check = False
        rot_time = 0

        # put rotten oranges in queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_check == True

        # loop through queue and rot oranges
        while len(q) > 0:
            curr_len = len(q)
            rot_flag = False

            for orange in range(curr_len):
                i, j = q.popleft()  # normal pop makes it more of a stack, use popleft for queue

                coord_check = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for x, y in coord_check:
                    offset_i = x + i
                    offset_j = y + j
                    if safe_coord(offset_i, offset_j, m, n) and grid[offset_i][offset_j] == 1:
                        grid[offset_i][offset_j] = 2
                        q.append((offset_i, offset_j))
                        rot_flag = True

            # if at least one orange rotten, add to time
            if rot_flag:
                rot_time += 1

        # check if any fresh oranges left (diagonal edge case)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return rot_time