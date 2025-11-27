class Solution:
    def generate(self, numRows: int):
        triangle = []

        for r in range(numRows):
            row = [1] * (r + 1)                        
            for i in range(1, r):
                row[i] = triangle[r-1][i-1] + triangle[r-1][i]
            triangle.append(row)

        return triangle


sol = Solution()
numRows = 5
result = sol.generate(numRows)

print("Pascal Triangle with", numRows, "rows:")
for row in result:
    print(row)