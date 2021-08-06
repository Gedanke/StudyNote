package DataStructuresAndAlgorithms.CourseOne.codes.module_2;

import java.util.LinkedList;

public class LectureSix {
    public static void main(String[] args) {
        ring(10, 5);
        // 6 1 7 3 10 9 2 5 8 4
    }

    public static void ring(int n, int m) {
        LinkedList<Integer> q = new LinkedList<Integer>();
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }
        int k = 2;
        int element = 0;
        int i = 1;
        for (; i < k; i++) {
            element = q.poll();
            q.add(element);
        }
        i = 1;
        while (q.size() > 0) {
            element = q.poll();
            if (i < m) {
                q.add(element);
                i++;
            } else {
                i = 1;
                System.out.print(element + " ");
            }
        }
        System.out.println();
    }
}
