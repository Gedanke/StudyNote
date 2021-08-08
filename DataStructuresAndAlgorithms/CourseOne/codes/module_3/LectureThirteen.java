package DataStructuresAndAlgorithms.CourseOne.codes.module_3;

import java.util.Arrays;

public class LectureThirteen {
    public static void main(String[] args) {
        // int[] arr = { 1, 0, 3, 4, 5, -6, 7, 8, 9, 10 };
        // fun_1_1(arr);
        // 原始数据: [1, 0, 3, 4, 5, -6, 7, 8, 9, 10]
        // 冒泡排序: [-6, 0, 1, 3, 4, 5, 7, 8, 9, 10]
        // int[] arr = { 2, 3, 5, 1, 23, 6, 78, 34 };
        // fun_1_2(arr);
        // 原始数据: [2, 3, 5, 1, 23, 6, 78, 34]
        // 插入排序: [1, 2, 3, 5, 6, 23, 34, 78]
        // int[] arr = { 49, 38, 65, 97, 76, 13, 27, 50 };
        // fun_1_3(arr);
        // 原始数据: [49, 38, 65, 97, 76, 13, 27, 50]
        // 归并排序: [13, 27, 38, 49, 50, 65, 76, 97]
        // int[] arr = { 6, 1, 2, 7, 9, 11, 4, 5, 10, 8 };
        // fun_1_4(arr);
        // 原始数据: [6, 1, 2, 7, 9, 11, 4, 5, 10, 8]
        // 快速排序: [1, 2, 4, 5, 6, 7, 8, 9, 10, 11]
    }

    public static void fun_1_1(int[] arr) {
        // int[] arr = { 1, 0, 3, 4, 5, -6, 7, 8, 9, 10 };
        System.out.println("原始数据: " + Arrays.toString(arr));
        for (int i = 1; i < arr.length; i++) {
            for (int j = 0; j < arr.length - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
        System.out.println("冒泡排序: " + Arrays.toString(arr));
    }

    public static void fun_1_2(int[] arr) {
        // int[] arr = { 2, 3, 5, 1, 23, 6, 78, 34 };
        System.out.println("原始数据: " + Arrays.toString(arr));
        for (int i = 1; i < arr.length; i++) {
            int temp = arr[i];
            int j = i - 1;
            for (; j >= 0; j--) {
                if (arr[j] > temp) {
                    arr[j + 1] = arr[j];
                } else {
                    break;
                }
            }
            arr[j + 1] = temp;
        }
        System.out.println("插入排序: " + Arrays.toString(arr));
    }

    public static void fun_1_3(int[] arr) {
        // int[] arr = { 49, 38, 65, 97, 76, 13, 27, 50 };
        int[] tmp = new int[arr.length];
        System.out.println("原始数据: " + Arrays.toString(arr));
        customMergeSort(arr, tmp, 0, arr.length - 1);
        System.out.println("归并排序: " + Arrays.toString(arr));
    }

    public static void customMergeSort(int[] a, int[] tmp, int start, int end) {
        if (start < end) {
            int mid = (start + end) / 2;
            // 对左侧子序列进行递归排序
            customMergeSort(a, tmp, start, mid);
            // 对右侧子序列进行递归排序
            customMergeSort(a, tmp, mid + 1, end);
            // 合并
            customDoubleMerge(a, tmp, start, mid, end);
        }
    }

    public static void customDoubleMerge(int[] a, int[] tmp, int left, int mid, int right) {
        int p1 = left, p2 = mid + 1, k = left;
        while (p1 <= mid && p2 <= right) {
            if (a[p1] <= a[p2])
                tmp[k++] = a[p1++];
            else
                tmp[k++] = a[p2++];
        }
        while (p1 <= mid)
            tmp[k++] = a[p1++];
        while (p2 <= right)
            tmp[k++] = a[p2++];
        // 复制回原素组
        for (int i = left; i <= right; i++)
            a[i] = tmp[i];
    }

    public static void fun_1_4(int[] arr) {
        // int[] arr = { 6, 1, 2, 7, 9, 11, 4, 5, 10, 8 };
        System.out.println("原始数据: " + Arrays.toString(arr));
        customQuickSort(arr, 0, arr.length - 1);
        System.out.println("快速排序: " + Arrays.toString(arr));
    }

    public static void customQuickSort(int[] arr, int low, int high) {
        int i, j, temp, t;
        if (low >= high) {
            return;
        }

        i = low;
        j = high;
        temp = arr[low];
        while (i < j) {
            // 先看右边，依次往左递减
            while (temp <= arr[j] && i < j) {
                j--;
            }
            // 再看左边，依次往右递增
            while (temp >= arr[i] && i < j) {
                i++;
            }
            t = arr[j];
            arr[j] = arr[i];
            arr[i] = t;
        }
        arr[low] = arr[i];
        arr[i] = temp;
        // 递归调用左半数组
        customQuickSort(arr, low, j - 1);
        // 递归调用右半数组
        customQuickSort(arr, j + 1, high);
    }
}
