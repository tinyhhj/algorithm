package codejam.qr2019.q1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner in = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int tc = in.nextInt();
        in.nextLine();
        for(int i = 0; i < tc ; i++) {
            String num = in.nextLine();
            String num1 = num.replaceAll("4","2");
            String num2 = num.replaceAll("[^4]","0")
                    .replaceAll("4","2")
                    .replaceAll("^0*2","2")
                    ;
            System.out.println(String.format("Case #%d: %s %s",i+1,num1,num2));
        }

    }
}
