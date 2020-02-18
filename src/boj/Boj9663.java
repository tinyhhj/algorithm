package boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

import static java.lang.Math.abs;

public class Boj9663 {
    boolean[][] board;
    static boolean[] x;
    static boolean[] ru;
    static boolean[] rd;
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int n = sc.nextInt();
        x = new boolean[14];
        ru = new boolean[27];
        rd = new boolean[27];
        System.out.println(putQueen(n,0,n, new boolean[n][n], new ArrayList<>()));
    }

    //backtracking
    //input: n, st-index, board
    //output: int
    public static int putQueen(int n, int cur, int remain, boolean[][] board, List<Integer> queens) {
        if( cur >= n && remain > 0) {
            return 0;
        } else if( cur >= n ) {
            return 1;
        }
       // can put?
        int res = 0;
        for( int i = 0; i < n ; i++) {
            if( canPut(cur , i , board, queens)) {
                x[i] = ru[cur+i] = rd[cur-i+board.length-1] = true;
                res += putQueen(n,cur+1, remain-1, board, queens);
                x[i] = ru[cur+i] = rd[cur-i+board.length-1] = false;
            }
        }
        return res;

    }

    private static boolean canPut(int y, int xx, boolean[][] board, List<Integer> queens) {
        return !x[xx] && !ru[y+xx] && !rd[y-xx+board.length-1];
    }
}
