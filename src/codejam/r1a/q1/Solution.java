package codejam.r1a.q1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int tc = sc.nextInt();
        for( int i = 0 ; i < tc ; i++ ) {
            int r = sc.nextInt(), c = sc.nextInt();
            int[][] path = new int[r*c][];
            boolean res = findRoute(path,new boolean[r][c], 0);
            if(res) {
                System.out.println(String.format("Case #%d: POSSIBLE",i+1));
                for( int j = 0 ; j < path.length; j++) {
                    System.out.println(path[j][0]+1 + " " + (path[j][1]+1));
                }
            } else {
                System.out.println(String.format("Case #%d: IMPOSSIBLE",i+1));
            }

        }
    }

    //backtracking
    public static boolean findRoute(int[][] path, boolean[][] visited,int leng) {
        // finish?
        if( leng == path.length) {
            return true;
        }
        // cant go anywhere
        if( cantGoAnywhere(path,visited,leng)) {
            return false;
        }

        // find other
        // x 2 x 4 x
        // x 2 x 9 1
        for ( Integer[] i: next(path,visited,leng)) {
            int rr = i[0];
            int cc = i[1];

            visited[rr][cc] = true;
            path[leng] = new int[]{rr,cc};
            if( findRoute(path,visited, leng+1)) {
                return true;
            }
            visited[rr][cc] = false;
        };
        return false;
    }

    private static boolean cantGoAnywhere(int[][] path, boolean[][] visited,int leng) {
        if (!next(path,visited,leng).isEmpty()) return false;
        return true;
    }

    private static List<Integer[]> next(int[][] path, boolean[][] visited,int leng) {
        List<Integer[]> res = new ArrayList<>();
        for( int i = 0 ; i < visited.length ; i++) {
            for( int j = 0 ; j < visited[i].length; j++) {
                if( leng ==0 ){
                    res.add(new Integer[]{i,j});
                } else if( !visited[i][j] ) {
                    int y = path[leng-1][0];
                    int x = path[leng-1][1];
                    if( y == i || x == j || i-j == y-x || i+j == y+x) continue;
                    res.add(new Integer[]{i,j});
                }
            }
        }
        return res;
    }
}
