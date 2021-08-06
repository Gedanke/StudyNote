package DataStructuresAndAlgorithms.CourseOne.codes.module_1;

import java.util.HashMap;
import java.util.Map;

public class LectureTwo {
    public static void main(String[] args) {
        // fun_2_1();
        // 134
        // fun_2_2();
        // 134
        // fun_2_3();
        // 5
        // fun_2_4();
        // 5
    }

    public static void fun_2_1() {
        int count = 0;
        for (int i = 0; i <= (100 / 7); i++) {
            for (int j = 0; j <= (100 / 3); j++) {
                for (int k = 0; k <= (100 / 2); k++) {
                    if (i * 7 + j * 3 + k * 2 == 100) {
                        count += 1;
                    }
                }
            }
        }
        System.out.println(count);
    }

    public static void fun_2_2() {
        int count = 0;
        for (int i = 0; i <= (100 / 7); i++) {
            for (int j = 0; j <= (100 / 3); j++) {
                if ((100 - i * 7 - j * 3 >= 0) && ((100 - i * 7 - j * 3) % 2 == 0)) {
                    count += 1;
                }
            }
        }
        System.out.println(count);
    }

    public static void fun_2_3() {
        int a[] = { 1, 2, 3, 4, 5, 5, 6 };
        int val_max = -1;
        int time_max = 0;
        int time_tmp = 0;
        for (int i = 0; i < a.length; i++) {
            time_tmp = 0;
            for (int j = 0; j < a.length; j++) {
                if (a[i] == a[j]) {
                    time_tmp += 1;
                }
                if (time_tmp > time_max) {
                    time_max = time_tmp;
                    val_max = a[i];
                }
            }
        }
        System.out.println(val_max);
    }

    public static void fun_2_4() {
        int a[] = { 1, 2, 3, 4, 5, 5, 6 };
        Map<Integer, Integer> d = new HashMap<>();
        for (int i = 0; i < a.length; i++) {
            if (d.containsKey(a[i])) {
                d.put(a[i], d.get(a[i]) + 1);
            } else {
                d.put(a[i], 1);
            }
        }
        int val_max = -1;
        int time_max = 0;
        for (Integer key : d.keySet()) {
            if (d.get(key) > time_max) {
                time_max = d.get(key);
                val_max = key;
            }
        }
        System.out.println(val_max);
    }
}
