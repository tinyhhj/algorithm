package boj;

import java.util.Scanner;

public class Boj1074 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int res = getZOrder(sc.nextInt(),sc.nextInt(),sc.nextInt())-1;
        System.out.println(res);
    }
    // z로 탐색할 때 ,n 과 (r,c)가 주어졌을때 순서를 리턴 한다.
    // 문제를 조각조각으로 나눈다.
    // 2^n에서 순서를 리턴하는 조각
    // 1. 기저조건은 어떻게 설정할것인가
    // 더이상 쪼개질 수 없는 조각을 생각 n이 0 일때는 순서가 무조건 1
    // 1 2 3 4 구역 나누기
    // 1구역이라면 1구역 내에서 순서 리턴
    // 2구역이라면 1구역 + 2구역 내에서 순서 리턴
    // 3구역이라면 1+ 2+ 3구역 내에서 순서 리턴
    // 4구역이라면 1+2+3+4 구역 내에서 순서 리턴
    static int getZOrder(int n , int r , int c) {
        if( n == 0) {
            return 1;
        }
        int num = 1 << n-1;
        //1
        if( num > r && num > c) {
           return getZOrder(n-1, r,c);
        }
        //2
        else if( num > r && num <= c) {
            return (num *num) + getZOrder(n-1, r, c- num);
        }
        //3
        else if( num <= r && num > c) {
            return (num *num * 2) + getZOrder(n-1,r-num , c);
        }
        //4
        else {
            return (num *num * 3) + getZOrder(n-1, r-num, c-num);
        }
    }
}
