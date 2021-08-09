package DataStructuresAndAlgorithms.CourseOne.codes.module_4;

import java.util.*;

public class LectureNineteen {
    public static void main(String[] args) {
        // fun_1_1();
        // YES
        // fun_1_2();
        // 1
        // fun_1_3();
        // 2
    }

    public static void fun_1_1() {
        int[] arr = { 1, 2, 3 };
        boolean isUniquel = isUniquel(arr);
        if (isUniquel) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    public static boolean isUniquel(int[] arr) {
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            if (d.containsKey(arr[i])) {
                return false;
            }
            d.put(arr[i], 1);
        }
        return true;
    }

    public static void fun_1_2() {
        int[] a = { 1, 2, 2, 1, 1, 4, 1, 5, 1 };
        int result = a[0];
        int times = 1;
        for (int i = 1; i < a.length; i++) {
            if (a[i] != result) {
                times--;
            } else {
                times++;
            }
            if (times == -1) {
                times = 1;
                result = a[i];
            }
        }
        System.out.println(result);
    }

    public static void fun_1_3() {
        int[][] m = { { 1, 1, 1, 1, 1, 1 }, { 1, 1, -1, -1, 1, 1 }, { 1, 1, -1, 1, -1, 1 } };
        int path = getpath(m, 2, 5);
        System.out.println(path);
    }

    public static int getpath(int[][] m, int i, int j) {
        if (m[i][j] == -1) {
            return 0;
        }
        if ((i > 0) && (j > 0)) {
            return getpath(m, i - 1, j) + getpath(m, i, j - 1);
        } else if ((i == 0) && (j > 0)) {
            return getpath(m, i, j - 1);
        } else if ((i > 0) && (j == 0)) {
            return getpath(m, i - 1, j);
        } else {
            return 1;
        }
    }

}
