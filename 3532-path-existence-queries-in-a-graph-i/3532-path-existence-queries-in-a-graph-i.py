class Solution:
    def pathExistenceQueries(self, n, nums, maxDiff, queries):
        # Union-Find data structure
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX  # Union the sets

        # Connect nodes based on the maxDiff condition
        for i in range(n - 1):
            if nums[i + 1] - nums[i] <= maxDiff:
                union(i, i + 1)

        # Process queries
        answer = []
        for u, v in queries:
            answer.append(find(u) == find(v))  # Check if they are in the same component

        return answer

# Example usage:
solution = Solution()
n = 4
nums = [2, 5, 6, 8]
maxDiff = 2
queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
output = solution.pathExistenceQueries(n, nums, maxDiff, queries)
print(output)  # Output: [False, False, True, True]
