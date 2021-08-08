package DataStructuresAndAlgorithms.CourseOne.codes.module_4;

public class LectureSixteen {
    public static void main(String[] args) {
        // int x = 20;
        // System.out.println(fun(x));
        // 4181

        // int[] arr = { 4, 5, 6, 7, 0, 1, 2 };
        // int target = 7;
        // System.out.println(bs(arr, target, 0, arr.length - 1));
        // 3

        String a = "13452439";
        String b = "123456";
        getCommenStr(a, b);
        // 345
    }

    private static int fun(int n) {
        if (n == 1) {
            return 0;
        }
        if (n == 2) {
            return 1;
        }
        return fun(n - 1) + fun(n - 2);
    }

    private static int bs(int[] arr, int target, int begin, int end) {
        if (begin == end) {
            if (target == arr[begin]) {
                return begin;
            } else {
                return -1;
            }
        }
        int middle = (begin + end) / 2;
        if (target == arr[middle]) {
            return middle;
        }
        if (begin != middle && arr[begin] <= arr[middle - 1]) {
            if (arr[begin] <= target && target <= arr[middle - 1]) {
                return bs(arr, target, begin, middle);
            } else {
                return bs(arr, target, middle + 1, end);
            }
        } else {
            if (arr[middle + 1] <= target && target <= arr[end]) {
                return bs(arr, target, middle + 1, end);
            } else {
                return bs(arr, target, begin, middle);
            }
        }
    }

    public static void getCommenStr(String a, String b) {
        char[] c1 = a.toCharArray();
        char[] c2 = b.toCharArray();
        int[][] m = new int[c2.length + 1][c1.length + 1];
        for (int i = 1; i <= c2.length; i++) {
            for (int j = 1; j <= c1.length; j++) {
                if (c2[i - 1] == c1[j - 1])
                    m[i][j] = m[i - 1][j - 1] + 1;
            }
        }
        int max = 0;
        int index = 0;
        for (int i = 0; i <= c2.length; i++) {
            for (int j = 0; j <= c1.length; j++) {
                if (m[i][j] > max) {
                    max = m[i][j];
                    index = i;
                }
            }
        }
        String s = "";
        for (int i = index - max; i < index; i++)
            s += b.charAt(i);
        System.out.println(s);
    }
}
