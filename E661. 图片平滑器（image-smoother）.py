class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        def cell_smoother(x, y):
            return mean(img[i][j] for i in range(max(x-1, 0), min(x+2, m)) for j in range(max(y-1, 0), min(y+2, n)))
        
        return [[int(cell_smoother(x, y)) for y in range(n)] for x in range(m)]       
