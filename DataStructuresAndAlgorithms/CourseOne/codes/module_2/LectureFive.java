package DataStructuresAndAlgorithms.CourseOne.codes.module_2;

import java.util.Stack;

@SuppressWarnings("unchecked")
public class LectureFive {
    public static void main(String[] args) {
        String s = "{[()()]}";
        System.out.println(isLegal(s));
        // 合法
    }

    private static int isLeft(char c) {
        if (c == '{' || c == '(' || c == '[') {
            return 1;
        } else {
            return 2;
        }
    }

    private static int isPair(char p, char curr) {
        if ((p == '{' && curr == '}') || (p == '[' && curr == ']') || (p == '(' && curr == ')')) {
            return 1;
        } else {
            return 0;
        }
    }

    private static String isLegal(String s) {
        Stack stack = new Stack();
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i);
            if (isLeft(curr) == 1) {
                stack.push(curr);
            } else {
                if (stack.empty()) {
                    return "非法";
                }
                char p = (char) stack.pop();
                if (isPair(p, curr) == 0) {
                    return "非法";
                }
            }
        }
        if (stack.empty()) {
            return "合法";
        } else {
            return "非法";
        }
    }
}
