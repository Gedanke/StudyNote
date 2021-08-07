package DataStructuresAndAlgorithms.CourseOne.codes.module_3;

public class LectureEleven {
    public static void main(String[] args) {
        String x = "x";
        String y = "y";
        String z = "z";
        hanio(3, x, y, z);
        /*
            移动: x -> z
            移动: x -> y
            移动: z -> y
            移动: x -> z
            移动: y -> x
            移动: y -> z
            移动: x -> z
        */
    }
    public static void hanio(int n, String x, String y, String z) {
        if(n < 1) {
            System.out.println("汉诺塔的层数不能小于1");
        }else if (n == 1) {
            System.out.println("移动: " + x + " -> " + z);
            return;
        }else {
            hanio(n - 1, x, z, y);
            System.out.println("移动: " + x + " -> " + z);
            hanio(n - 1, y, x, z);
        }
    }
}
