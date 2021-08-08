package DataStructuresAndAlgorithms.CourseOne.codes.module_4;

public class LectureEighteen {
    public static void main(String[] args) {
        // fun_1_1();
        // 5
        // 0
        // 1
        // 2
        // 3
        // 4
        // fun_1_2();
        // 4
    }

    public static void fun_1_1() {
        int[] nums = { 0, 0, 1, 1, 1, 2, 2, 3, 3, 4 };
        int temp = nums[0];
        int len = 1;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != temp) {
                nums[len] = nums[i];
                temp = nums[i];
                len++;
            }
        }
        System.out.println(len);
        for (int i = 0; i < len; i++) {
            System.out.println(nums[i]);
        }
    }

    public static void fun_1_2() {
        int[] nums1 = { 1, 2, 3, 4, 5 };
        int[] nums2 = { 6, 7, 8 };
        int median = getMedian(nums1, 0, nums1.length - 1, nums2, 0, nums2.length - 1);
        System.out.println(median);
    }

    public static int getMedian(int[] a, int begina, int enda, int[] b, int beginb, int endb) {
        if (enda - begina == 0) {
            return a[begina] > b[beginb] ? b[beginb] : a[begina];
        }
        if (enda - begina == 1) {
            if (a[begina] < b[beginb]) {
                return b[beginb] > a[enda] ? a[enda] : b[beginb];
            } else {
                return a[begina] < b[endb] ? a[begina] : b[endb];
            }
        }
        if (endb - beginb < 2) {
            if ((endb - beginb == 0) && (enda - begina) % 2 == 0) {
                int m = b[beginb];
                int bb = a[(enda + begina) / 2 - 1];
                int c = a[(enda + begina) / 2];
                return (m < bb) ? bb : (m < c ? m : c);
            } else if ((endb - beginb == 0) && (enda - begina) % 2 != 0) {
                int m = b[beginb];
                int c = a[(enda + begina) / 2];
                int d = a[(enda + begina) / 2 + 1];
                return m < c ? c : (m < d ? m : d);
            } else {
                int m = b[beginb];
                int n = b[endb];
                int bb = a[(enda + begina) / 2 - 1];
                int c = a[(enda + begina) / 2];
                int d = a[(enda + begina) / 2 + 1];
                if (n < bb) {
                    return bb;
                } else if (n > bb && n < c) {
                    return n;
                } else if (n > c && n < d) {
                    return m > c ? m : c;
                } else {
                    return m < c ? c : (m < d ? m : d);
                }
            }
        } else {
            int mida = (enda + begina) / 2;
            int midb = (endb + beginb) / 2;
            if (a[mida] < b[midb]) {
                int step = endb - midb;
                return getMedian(a, begina + step, enda, b, beginb, endb - step);
            } else {
                int step = midb - beginb;
                return getMedian(a, begina, enda - step, b, beginb + step, endb);
            }
        }
    }
}
