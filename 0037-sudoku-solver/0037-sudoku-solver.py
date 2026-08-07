class Solution:

  def solveSudoku(self, board: list[list[str]]) -> None:
    """Modifies board in-place to solve the Sudoku puzzle."""
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty_cells = []

    # Step 1: Pre-fill constraints and locate empty cells
    for r in range(9):
      for c in range(9):
        val = board[r][c]
        if val != ".":
          rows[r].add(val)
          cols[c].add(val)
          boxes[(r // 3) * 3 + (c // 3)].add(val)
        else:
          empty_cells.append((r, c))

    # Step 2: Backtracking helper function
    def backtrack(idx: int) -> bool:
      if idx == len(empty_cells):
        return True  # All empty cells filled successfully

      r, c = empty_cells[idx]
      box_idx = (r // 3) * 3 + (c // 3)

      for digit in "123456789":
        if (
            digit not in rows[r]
            and digit not in cols[c]
            and digit not in boxes[box_idx]
        ):
          # Make move
          board[r][c] = digit
          rows[r].add(digit)
          cols[c].add(digit)
          boxes[box_idx].add(digit)

          if backtrack(idx + 1):
            return True

          # Backtrack (Undo move)
          board[r][c] = "."
          rows[r].remove(digit)
          cols[c].remove(digit)
          boxes[box_idx].remove(digit)

      return False

    backtrack(0)