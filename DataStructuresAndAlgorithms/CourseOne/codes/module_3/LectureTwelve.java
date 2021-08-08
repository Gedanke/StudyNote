package DataStructuresAndAlgorithms.CourseOne.codes.module_3;

public class LectureTwelve {
    public static void main(String[] args) {
        // 需要查找的数字
        int targetNumb = 8;
        // 目标有序数组
        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        // fun_1_1(arr, targetNumb);
        /*
         * targetNumb = -1 数组不含 -1 targetNumb = 8 8 在数组中,下标值为: 7
         */
        // fun_1_2();
        // 第一个比 9 大的数字是 10
    }

    public static void fun_1_1(int[] arr, int targetNumb) {
        int middle = 0;
        int low = 0;
        int high = arr.length - 1;
        int isfind = 0;

        while (low <= high) {
            middle = high + (low - high) / 2;
            if (arr[middle] == targetNumb) {
                System.out.println(targetNumb + " 在数组中,下标值为: " + middle);
                isfind = 1;
                break;
            } else if (arr[middle] > targetNumb) {
                // 说明该数在low~middle之间
                high = middle - 1;
            } else {
                // 说明该数在middle~high之间
                low = middle + 1;
            }
        }
        if (isfind == 0) {
            System.out.println("数组不含 " + targetNumb);
        }
    }

    public static void fun_1_2() {
        int targetNumb = 9;
        // 目标有序数组
        int[] arr = { -1, 3, 3, 7, 10, 14, 14 };
        int middle = 0;
        int low = 0;
        int high = arr.length - 1;
        while (low <= high) {
            middle = high + (low - high) / 2;
            if (arr[middle] > targetNumb && (middle == 0 || arr[middle - 1] <= targetNumb)) {
                System.out.println("第一个比 " + targetNumb + " 大的数字是 " + arr[middle]);
                break;
            } else if (arr[middle] > targetNumb) {
                // 说明该数在low~middle之间
                high = middle - 1;
            } else {
                // 说明该数在middle~high之间
                low = middle + 1;
            }
        }
    }
}
