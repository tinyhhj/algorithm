package codejam.qr2019.q4;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Solution {
    static int[] input;
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int tc = sc.nextInt();
        System.err.println("testcase: " + tc);
        for( int i = 0 ; i < tc ; i++) {
            int n = sc.nextInt(), b = sc.nextInt(), f = sc.nextInt();
            sc.nextLine();
            System.err.println(String.format("nbf: %s %s %s",n,b,f));
            String response = "";
            List<String> query = new ArrayList<>();
            List<String> responses = new ArrayList<>();
            input = new int[1024];
            for( int j = 0 ; j < f ; j++) {

                // guessing from responses
                String guess = guessBits(n,b,f,query,responses);
                query.add(guess);

                String res = sc.nextLine();
                responses.add(res);
                System.err.println("res: " + res);

               if ( cantIproceed(res)) {
                    System.exit(1);
                }

            }
            // can i solve this problem?
            if( canSolve(n,b,f,query,responses)) {
                doAnswer(n,b,f,query,responses);
                sc.nextInt();
            }
        }
    }

    private static boolean cantIproceed(String response) {
        return response.equals("-1");
    }

    private static void doAnswer(int n,int b, int f, List<String> query,List<String> response) {
        boolean[] res = new boolean[n];
        for( int i = 0 ; i < n-b ; i++) {
            int num = 0;
            for(int j = f-1 ; j >= 0 ; j--) {
                if(response.get(j).getBytes()[i]-'0' ==1) {
                    num = num ^ 1;
                }
                num = num << 1;
            }
            System.err.println("num: " + num);
            res[num >> 1] = true;
        }
        StringBuilder sb = new StringBuilder();
        for( int i = 0 ; i < n ; i++) {
            if(!res[i]) {
                sb.append(i + " ");
            }
        }
        System.out.println(sb.substring(0,sb.length()-1));
    }

    private static boolean canSolve(int n,int b, int f, List<String> query,List<String> response) {
        return response.size() == f;
    }

    // n b f response guessing number
    // if hit the answer response answer
    private static String guessBits(int n,int b, int f, List<String> query,List<String> response) {
        String number = "";
        int size = query.size();
        for( int i = 0 ; i < n ; i++) {
            number += ((i >> size) & 1) == 1 ? "1":"0";
        }
        System.err.println(String.format("guessing: %s",number));
        System.out.println(number);
        System.out.flush();
        return number;
    }
}
