#
# @lc app=leetcode id=874 lang=python3
#
# [874] Walking Robot Simulation
#
# https://leetcode.com/problems/walking-robot-simulation/description/
#
# algorithms
# Easy (31.18%)
# Total Accepted:    8.6K
# Total Submissions: 27.4K
# Testcase Example:  '[4,-1,3]\n[]'
#
# A robot on an infinite grid starts at point (0, 0) and faces north.  The
# robot can receive one of three possible types of commands:
# 
# 
# -2: turn left 90 degrees
# -1: turn right 90 degrees
# 1 <= x <= 9: move forward x units
# 
# 
# Some of the grid squares are obstacles. 
# 
# The i-th obstacle is at grid point (obstacles[i][0], obstacles[i][1])
# 
# If the robot would try to move onto them, the robot stays on the previous
# grid square instead (but still continues following the rest of the route.)
# 
# Return the square of the maximum Euclidean distance that the robot will be
# from the origin.
# 
# 
# 
# Example 1:
# 
# 
# Input: commands = [4,-1,3], obstacles = []
# Output: 25
# Explanation: robot will go to (3, 4)
# 
# 
# 
# Example 2:
# 
# 
# Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
# Output: 65
# Explanation: robot will be stuck at (1, 4) before turning left and going to
# (1, 8)
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= commands.length <= 10000
# 0 <= obstacles.length <= 10000
# -30000 <= obstacle[i][0] <= 30000
# -30000 <= obstacle[i][1] <= 30000
# The answer is guaranteed to be less than 2 ^ 31.
# 
# 
#
class Solution:
    def robotSim(self, commands, obstacles):
        px = py = vi = 0
        obs = set([tuple(o) for o in obstacles])
        vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        maxi = 0
        for i, v in enumerate(commands):
            vx ,vy = vectors[vi%4]
            if v >= 0:
                for _ in range(v):
                    next_p = (px+vx, py+vy)
                    if next_p in obs:
                        break
                    else:
                        px += vx
                        py += vy
                        #print(px, py, vi)
                        cur = px**2+py**2
                        if cur > maxi:
                            maxi = cur
            else:
                if v == -1:
                    vi += 1
                if v == -2:
                    vi -= 1
        return maxi
Solution().robotSim([4,-1,3], [])
