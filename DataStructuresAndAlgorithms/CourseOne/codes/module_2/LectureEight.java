package DataStructuresAndAlgorithms.CourseOne.codes.module_2;

public class LectureEight {
    public static void main(String[] args) {
        // fun_1();
        // 1
        // fun_2();
        // 345
    }

    public static void fun_1() {
        String s = "goodgoogle";
        String t = "google";
        int isfind = 0;

        for (int i = 0; i < s.length() - t.length() + 1; i++) {
            if (s.charAt(i) == t.charAt(0)) {
                int jc = 0;
                for (int j = 0; j < t.length(); j++) {
                    if (s.charAt(i + j) != t.charAt(j)) {
                        break;
                    }
                    jc = j;
                }
                if (jc == t.length() - 1) {
                    isfind = 1;
                }
            }
        }
        System.out.println(isfind);
    }

    public static void fun_2() {
        String a = "123456";
        String b = "13452439";
        String maxSubStr = "";
        int max_len = 0;

        for (int i = 0; i < a.length(); i++) {
            for (int j = 0; j < b.length(); j++) {
                if (a.charAt(i) == b.charAt(j)) {
                    for (int m = i, n = j; m < a.length() && n < b.length(); m++, n++) {
                        if (a.charAt(m) != b.charAt(n)) {
                            break;
                        }
                        if (max_len < m - i + 1) {
                            max_len = m - i + 1;
                            maxSubStr = a.substring(i, m + 1);
                        }
                    }
                }
            }
        }
        System.out.println(maxSubStr);
    }
}
