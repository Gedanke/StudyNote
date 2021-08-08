package DataStructuresAndAlgorithms.CourseOne.codes.module_4;

import java.util.*;

public class LectureFifteen {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5, 6 };
        int target = 4;
        System.out.println(Arrays.toString(twoSum(arr, target)));
        // [2, 0]
    }

    private static int[] twoSum(int[] arr, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            map.put(arr[i], i);
        }
        for (int i = 0; i < arr.length; i++) {
            int complement = target - arr[i];
            if (map.containsKey(complement) && map.get(complement) != i) {
                return new int[] { map.get(complement), i };
            }
        }
        return null;
    }

}
