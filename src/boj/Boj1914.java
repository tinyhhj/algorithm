package boj;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Boj1914 {
    int res;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        BigInteger res = BigInteger.valueOf(2).pow(n).subtract(BigInteger.ONE);
        System.out.println(res);
        if( n <= 20) hanoi(n,1,3);
    }

    // 문제의 조각 n개의 조각을 1->3으로 옮기는 문제
    // 처음 시작하는 판의 갯수 n의 크기에 따라 재귀함수의 크기가 달라진다.
    // n = 1 1->3 단순히 옮기면 됨
    // n = 2 1->2, 1->3 , 2->3
    // n = 3 1->3, 1->2, 3->2, 1->3, 2->1, 2->3, 1->3
    // n = 4 1->2, 1->3, 2->3, 1->2, 3->1, 3->2, 1->2, 1->3, 2->3, 2->1, 3->1, 2->3, 1->2, 1->3, 2->3
    // n = k 일때 추상적 흐름
    // k-1개의 원반을 목적지 이외의 기둥에 옮겨놓는다.(구체적으로는 모름)
    // k 번째 원반을 목적지에 옮겨놓음
    // k-1개의 원반을 다시 목적지로 옮긴다.( 구체적으로는 모름)
    // 문제의 조각: n(원판의 갯수), st(시작점), end(목표), 순서기록여부 리턴: 횟수
    // 기저조건: n = 1 인경우 그냥 옮기면 됨
    // 문제의 조각 내에 순서를 리턴하게 되면 안됨. 20 이하일때만 리턴하도록 되있기 때문에
    // 시간 초과가 나므로 캐시를 사용해야하는데 n, st,end에 대해서 순서도를 캐시할거임
    // 1. 맥스값 오류 - long을 벗어남
    // 2. 메모리 오버 - 여러 풀이들을 보니 그냥 2^n-1 최소횟수를 리턴하도록 되있음


    public static long hanoi(int n , int st, int end ) {
        if( n == 1) {
            System.out.println(""+st +" " + end);
//            wrapper.add(new int[]{st,end});
            return 1;
        }

        long cnt1 = hanoi(n-1, st, 6-st-end);
        long cnt2 = hanoi(1,st,end);
        long cnt3 = hanoi(n-1,6-st-end,end);

        return cnt1+cnt2+cnt3;
    }


}
