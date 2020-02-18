package algospot.clocksync;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
    static int[][] switches = new int[10][];
    static int[] clocks = new int[16];
    public static void main(String[] args) throws FileNotFoundException {
        switches[0] = new int[]{0,1,2};
        switches[1] = new int[]{3, 7, 9, 11};
        switches[2] = new int[]{4, 10, 14, 15};
        switches[3] = new int[]{0, 4, 5, 6, 7};
        switches[4] = new int[]{6, 7, 8, 10, 12};
        switches[5] = new int[]{0, 2, 14, 15};
        switches[6] = new int[]{3, 14, 15};
        switches[7] = new int[]{4, 5, 7, 14, 15};
        switches[8] = new int[]{1, 2, 3, 4, 5};
        switches[9] = new int[]{3, 4, 5, 9, 13};

//        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        Scanner sc = new Scanner(new FileInputStream("algospot/clocksync/input.txt"));


        int tc = sc.nextInt();
        for( int i =0; i < tc ; i++) {
            clocks = new int[16];
            for(int j = 0 ; j < 16; j++) {
                clocks[j] = sc.nextInt();
            }

            //버튼을 한개씩 다 눌러본다
            // 4번누르면 제자리 이므로 3번씩만 눌러본다

            int res;
            if( (res = click(clocks, 0)) < Integer.MAX_VALUE )  {
                System.out.println(res);
            } else {
                System.out.println(-1);
            }
        }
    }

    //재귀
    //input: 시계들, 버튼, 누른버튼
    //output: 현상황에서의 num번부터 누를때 최소횟수
    static int click(int[] clocks,int num) {
        if( checkTime(clocks)) {
            return 0;
        }
        if( num == 10) {
            return Integer.MAX_VALUE;
        }

        //4번씩 눌러본다. 안누른거 포함
        int res = Integer.MAX_VALUE;
        for(int i=0; i < 4; i++) {
            if( i> 0) push(clocks,num);
            int min = click(clocks,num+1);
            if( min != Integer.MAX_VALUE) {
                res = Math.min(res , min + i);
            }
        }
        //3번까지 눌렀으므로 초기화해줌
        push(clocks,num);
        return res;
    }
    static void push(int[] clocks,int num) {
        for (int m : switches[num]) {
            clocks[m] = clocks[m] == 12 ? 3 : clocks[m]+3;
        }
    }
    static boolean checkTime(int[] clocks) {
        return Arrays.stream(clocks).allMatch(i->i==12);
    }
    static int total(int[] buttons) {
        return Arrays.stream(buttons).sum();
    }
}
