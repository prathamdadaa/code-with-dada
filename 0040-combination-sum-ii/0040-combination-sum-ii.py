class Solution:

  def combinationSum2(
      self, candidates: list[int], target: int
  ) -> list[list[int]]:
    candidates.sort()
    results = []

    def backtrack(start: int, remain: int, path: list[int]):
      if remain == 0:
        results.append(list(path))
        return

      for i in range(start, len(candidates)):
        # Early pruning: numbers are sorted, so larger numbers will also exceed remain
        if candidates[i] > remain:
          break

        # Skip duplicates at the same tree depth level
        if i > start and candidates[i] == candidates[i - 1]:
          continue

        path.append(candidates[i])
        # Move to next index (i + 1) as elements cannot be reused
        backtrack(i + 1, remain - candidates[i], path)
        path.pop()  # Undo choice

    backtrack(0, target, [])
    return results