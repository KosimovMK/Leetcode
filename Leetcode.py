class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        res = [[1]]

        for i in range(numRows-1):
            p = res[-1]
            c = [1]
            for j in range(1, len(p)):
                s = p[j]+p[j-1]
                c.append(s)
            c.append(1)
            res.append(c)
        return res