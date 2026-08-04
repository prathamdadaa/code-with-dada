import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final String[] KEYPAD = {
        "",     "",     "abc",  "def", 
        "ghi",  "jkl",  "mno", 
        "pqrs", "tuv",  "wxyz"
    };

    public List<String> letterCombinations(String digits) {
        List<String> result = new ArrayList<>();
        if (digits == null || digits.length() == 0) {
            return result;
        }

        backtrack(result, digits, 0, new StringBuilder());
        return result;
    }

    private void backtrack(List<String> result, String digits, int index, StringBuilder path) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }

        String letters = KEYPAD[digits.charAt(index) - '0'];
        for (char c : letters.toCharArray()) {
            path.append(c);
            backtrack(result, digits, index + 1, path);
            path.deleteCharAt(path.length() - 1); // Backtrack
        }
    }
}