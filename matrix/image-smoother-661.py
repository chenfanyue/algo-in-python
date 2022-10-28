class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def calc(i: int, j: int) -> int:
            total, cnt = 0, 0
            y_low, y_high = max(0, j-1), min(n, j+2)
            for x in range(max(0, i-1), min(m, i+2)):
                for y in range(y_low, y_high):
                    total += img[x][y]
                    cnt += 1
            return total // cnt
        
        m, n = len(img), len(img[0])
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = calc(i, j)
        return res
