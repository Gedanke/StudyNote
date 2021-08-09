package DataStructuresAndAlgorithms.CourseOne.codes.module_5;

import java.util.*;

class TreeNodes {
    Integer val;
    TreeNodes left;
    TreeNodes right;

    TreeNodes(Integer val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class LectureTwentyTwo {
    public static void main(String[] args) {

    }

    public ArrayList<Integer> Print(TreeNodes pRoot) {
        // 先右后左
        Stack<TreeNodes> s1 = new Stack<TreeNodes>();
        // 先左后右
        Stack<TreeNodes> s2 = new Stack<TreeNodes>();
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(pRoot.val);
        s1.push(pRoot);
        while (s1.isEmpty() || s2.isEmpty()) {
            if (s1.isEmpty() && s2.isEmpty()) {
                break;
            }
            if (s2.isEmpty()) {
                while (!s1.isEmpty()) {
                    if (s1.peek().right != null) {
                        list.add(s1.peek().right.val);
                        s2.push(s1.peek().right);
                    }
                    if (s1.peek().left != null) {
                        list.add(s1.peek().left.val);
                        s2.push(s1.peek().left);
                    }
                    s1.pop();
                }
            } else {
                while (!s2.isEmpty()) {
                    if (s2.peek().left != null) {
                        list.add(s2.peek().left.val);
                        s1.push(s2.peek().left);
                    }
                    if (s2.peek().right != null) {
                        list.add(s2.peek().right.val);
                        s1.push(s2.peek().right);
                    }
                    s2.pop();
                }
            }
        }
        return list;
    }

    public static void fun() {
        Stack<Object> stack = new Stack<Object>();
        String s = "* + 2 2 3";
        String attr[] = s.split(" ");
        for (int i = attr.length - 1; i >= 0; i--) {
            if (!(attr[i].equals("+") || attr[i].equals("-") || attr[i].equals("*") || attr[i].equals("/"))) {
                stack.push(Integer.parseInt(attr[i]));
            } else {
                int a = (int) stack.pop();// 出栈
                int b = (int) stack.pop();// 出栈
                int result = Cal(a, b, attr[i]); // 调用函数计算结果值
                stack.push(result); // 结果进栈
            }
        }
        int ans = (int) stack.pop();
        System.out.print(ans);
    }

    public static int Cal(int a, int b, String s) {
        switch (s) {
            case "+":
                return a + b;
            case "-":
                return a - b;
            case "*":
                return a * b;
            case "/":
                return a / b;
        }
        return 0;
    }

}
