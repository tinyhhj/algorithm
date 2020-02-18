package codejam.qr2019.q2;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.Scanner;

/**
 * https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
 * 거꾸로 올라가는방식은?
 * 일단 첫번째와 끝은 이미 정해져있음
 * 만날때에는 서로 다른방향으로 가야하기 때문에 방향이 강제됨
 * n칸이라고할때 n을 두가지 방향으로 어떻게 배치할것인가 S n-1번 E n-1번 움직여야함
 * 상대가 s로 n-1번움직였다면 아래에있으면 안됨 즉 s를 다쓰면 안됨
 * 상대가 s를 n-1번쓸때까지 s를 남겨두려면 s를 쓸때 e를 쓰면됨?
 * 반대방향으로 갈경우 겹치지 않는 이유는 반대의 경우를 가정하고 생각한다.
 * (가정)반대방향으로만 갔을경우에 어느순간 상대방과 같은 방향으로 이동한다.
 * 어느지점에서 마주쳤다고 가정했을경우 상대방과 나는 (결과론적으로) 같은 수의 동쪽과 같은수의 남쪽을 사용했을 경우이다.
 * 그 경우에 다음 이동방향은 상대방과 무조건 반대이므로 겹치지 않게된다.
 */
public class Solution {
    public static void main(String[] args) throws FileNotFoundException {
//        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(new FileInputStream("codejam/qr2019/q2/input.txt"))));
        int tc = sc.nextInt();
        backtracking(sc, tc);
    }

    private static void inverseDirection(Scanner sc, int tc) {
        for(int i =0 ; i < tc ; i++) {
            int n = sc.nextInt();
            sc.nextLine();
            String move = sc.nextLine();
            char[] newMove = new char[move.length()];
            int j = 0;
            for( char a : move.toCharArray()) {
                if( a == 'S') newMove[j++] = 'E';
                else newMove[j++] = 'S';
            }
            System.out.println(String.format("Case #%d: %s",i+1, new String(newMove)));
        }
    }

    private static void backtracking(Scanner sc, int tc) {
        for( int i = 0 ; i < tc; i++) {
            int n = sc.nextInt();
            sc.nextLine();
            String move = sc.nextLine();
            String path = backtrackingInternal(n,new int[]{0,0},new int[]{0,0},move,"SE");
            System.out.println(path);
        }
    }
    private static boolean samePosition(int[] e, int[]m) {
        return e[0] == m[0] && e[1] == m[1];
    }
    private static boolean boundGrid(int y,int x, int n) {
        return y >= 0 && y < n && x >= 0 && x < n;
    }
    //input : 현재상태 상대방과 나의 위치와 상대방의 이동방향, 나의 가능한 이동방향
    //output : 중복되지 않는 경로
    private static String backtrackingInternal(int n, int[] e, int[] m, String ep, String mps) {
        if( samePosition(new int[]{n-1,n-1},m) && ep.length() == 0 ) {
            return "";
        }

        // 이동가능 후보가 없거나 패스가 중복되거나
        if( (samePosition(e,m) && ep.substring(0,1).equals(mps))) {
            return null;
        } else if(mps.contains(ep.substring(0,1)) && samePosition(e,m)){
            mps = mps.replace(ep.substring(0,1),"");
        }


        for( char d : mps.toCharArray()) {

            if( d == 'E' ) {
                //이동
                m[1]++;
                if( ep.charAt(0) == 'E') {
                    e[1]++;
                } else {
                    e[0]++;
                }
                //후보군설정
                String candidates = boundGrid(m[0],m[1]+1,n) ? "E": "";
                candidates += (boundGrid(m[0]+1,m[1],n)) ? "S" : "";
                String path = backtrackingInternal(n, e,m,ep.substring(1),candidates);
                m[1]--;
                if( ep.charAt(0) == 'E') {
                    e[1]--;
                } else {
                    e[0]--;
                }
                if(  path != null) {
                    return  "E" + path;
                }


            } else {
                m[0]++;
                if( ep.charAt(0) == 'E') {
                    e[1]++;
                } else {
                    e[0]++;
                }
                String candidates = boundGrid(m[0],m[1]+1,n) ? "E":"";
                candidates += (boundGrid(m[0]+1,m[1],n))?"S":"";
                String path = backtrackingInternal(n,e,m,ep.substring(1),candidates);
                m[0]--;
                if( ep.charAt(0) == 'E') {
                    e[1]--;
                } else {
                    e[0]--;
                }
                if( path != null) {
                    return "S" + path;
                }


            }
        }


        return null;
    }



}
