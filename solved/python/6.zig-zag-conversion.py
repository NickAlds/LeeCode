#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    # 使用矩阵
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s
        n = len(s)
        max_col = (n//(2*numRows-2)+1)*(numRows-1)
        # print(max_col)
        map = [[""]*max_col for _ in range(numRows)]
        i = j = 0
        col_step = 0
        row_step = 1
        for char in s:
            print(i, j)
            map[i][j] = char
            i += row_step
            j += col_step
            if i == numRows-1:
                col_step = 1
                row_step = -1
            if i == 0 and col_step == 1:
                col_step = 0
                row_step = 1
        # [print(i) for i in map]
        return "".join(["".join(i) for i in map])

    # 使用字符串列表
    def convert(self, s: str, numRows: int) -> str:
        if numRows<2:
            return s
        rows = [""]*numRows
        row_step = 1
        cur_row = 0
        for char in s:
            rows[cur_row]+=char
            cur_row += row_step
            if cur_row == numRows-1:
                row_step = -1
            if cur_row == 0:
                row_step = 1
        return "".join(rows)

# @lc code=end
if __name__ == '__main__':
    print(Solution().convert("abcdefg", 2))
