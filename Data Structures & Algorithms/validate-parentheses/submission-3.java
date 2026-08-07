

class Solution {
    public boolean isValid(String s) {

        // Stack stores opening brackets that are waiting to be closed
        Stack<Character> stack = new Stack<>();

        // Traverse every character in the string
        for (char c : s.toCharArray()) {

            // If it's an opening bracket, remember it
            if (c == '(' || c == '[' || c == '{') {
                stack.push(c);
            }

            // Otherwise it's a closing bracket
            else {

                // No opening bracket available to match
                if (stack.isEmpty()) {
                    return false;
                }

                // Look at the most recent opening bracket
                char top = stack.peek();

                // Matching pair
                if (c == ')' && top == '(') {
                    stack.pop();
                }
                else if (c == ']' && top == '[') {
                    stack.pop();
                }
                else if (c == '}' && top == '{') {
                    stack.pop();
                }

                // Wrong type of bracket
                else {
                    return false;
                }
            }
        }

        // If stack is empty, every opening bracket was matched
        return stack.isEmpty();
    }
}