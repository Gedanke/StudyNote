package DataStructuresAndAlgorithms.CourseOne.codes.module_4;

import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Stack;

class Node {
    public int data;
    public Node leftChild;
    public Node rightChild;

    public Node(int data, Node leftChild, Node rightChild) {
        this.data = data;
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }
}

public class LectureSeventeen {
    int count = 0;
    static PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    static PriorityQueue<Integer> maxHeap = new PriorityQueue<>(new Comparator<Integer>() {
        @Override
        public int compare(Integer o1, Integer o2) {
            return o2.compareTo(o1);
        }
    });

    public void Insert(Integer num) {
        if (count % 2 == 0) {
            minHeap.offer(num);
            maxHeap.offer(minHeap.poll());
        } else {
            maxHeap.offer(num);
            minHeap.offer(maxHeap.poll());
        }
        count++;
        System.out.println(LectureSeventeen.GetMedian());
    }

    public static int GetMedian() {
        return maxHeap.peek();
    }

    public static void main(String[] args) {
        String ss = "This is a   good example";
        System.out.println(reverseWords(ss));
        // example good a is This
        // levelTraverse(null);
        LectureSeventeen t = new LectureSeventeen();
        t.Insert(1);
        t.Insert(2);
        t.Insert(0);
        t.Insert(20);
        t.Insert(10);
        t.Insert(22);
    }

    private static String reverseWords(String s) {
        Stack stack = new Stack();
        String temp = "";
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != ' ') {
                temp += s.charAt(i);
            } else if (temp != "") {
                stack.push(temp);
                temp = "";
            } else {
                continue;
            }
        }
        if (temp != "") {
            stack.push(temp);
        }
        String result = "";
        while (!stack.empty()) {
            result += stack.pop() + " ";
        }
        return result.substring(0, result.length() - 1);
    }

    public static void levelTraverse(Node root) {
        LinkedList<Node> queue = new LinkedList<Node>();
        Node current = null;
        queue.offer(root); // 根结点入队
        while (!queue.isEmpty()) {
            current = queue.poll(); // 出队队头元素
            System.out.print(current.data);
            // 左子树不为空，入队
            if (current.leftChild != null)
                queue.offer(current.leftChild);
            // 右子树不为空，入队
            if (current.rightChild != null)
                queue.offer(current.rightChild);
        }
    }
}
