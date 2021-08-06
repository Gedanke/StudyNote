package DataStructuresAndAlgorithms.CourseOne.codes.module_1;

import java.util.Arrays;

public class LectureOne {
    public static void main(String[] args) {
        // fun_1_1();
        // [5, 4, 3, 2, 1]
        // fun_1_2();
        // [5, 4, 3, 2, 1]
        // fun_1_3();
        // 4
        // fun_1_4();
        // 3
    }

    public static void fun_1_1() {
        int a[] = { 1, 2, 3, 4, 5 };
        int b[] = new int[5];
        for (int i = 0; i < a.length; i++) {
            b[i] = a[i];
        }
        for (int i = 0; i < a.length; i++) {
            b[a.length - i - 1] = a[i];
        }
        System.out.println(Arrays.toString(b));
    }

    public static void fun_1_2() {
        int a[] = { 1, 2, 3, 4, 5 };
        int tmp = 0;
        for (int i = 0; i < (a.length / 2); i++) {
            tmp = a[i];
            a[i] = a[a.length - i - 1];
            a[a.length - i - 1] = tmp;
        }
        System.out.println(Arrays.toString(a));
    }

    public static void fun_1_3() {
        int a[] = { 1, 4, 3 };
        int max_val = -1;
        for (int i = 0; i < a.length; i++) {
            if (a[i] > max_val) {
                max_val = a[i];
            }
        }
        System.out.println(max_val);
    }

    public static void fun_1_4() {
        int a[] = { 1, 3, 4, 3, 4, 1, 3 };
        int val_max = -1;
        int time_max = 0;
        int time_tmp = 0;
        for (int i = 0; i < a.length; i++) {
            time_tmp = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[i] == a[j]) {
                    time_tmp += 1;
                }
            }
            if (time_tmp > time_max) {
                time_max = time_tmp;
                val_max = a[i];
            }
        }
        System.out.println(val_max);
    }
}
