package boj;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Boj6603 {
    public static void main(String[] args) throws FileNotFoundException {
//        7 1 2 3 4 5 6 7
//        8 1 2 3 5 8 13 21 34
//        0
//        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(new FileInputStream("boj/6603.txt"))));
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int n = sc.nextInt();
        while(n != 0) {
            int[] arr = new int[n];
            for( int i =0 ; i < n ; i++) {
                arr[i]= sc.nextInt();
            }
            printLotto(IntStream.of(arr).boxed().collect(Collectors.toList()),6,0,new ArrayList<>());
           n = sc.nextInt();
           System.out.println("");
        }
    }

    // 조합
    // input: 집합, 뽑아야하는 조합개수, 지금까지 뽑은 숫자들
    // output: void
    // 어떻게 조합을 중복제거할 수 있을까
    public static void printLotto(List<Integer> group, int k, int cur, List<Integer> arr) {
        if( arr.size() == k) {
            out(arr);
        } else if( cur == group.size()) return;
        else {

            arr.add(group.get(cur));
            printLotto(group, k, cur + 1, arr);
            arr.remove(arr.size() - 1);
            printLotto(group, k, cur + 1, arr);
        }
    }

    public static void out(List<Integer> list) {
        StringBuilder sb = new StringBuilder();
        for(Integer i : list) {
            sb.append(" " + i);
        }
        System.out.println(sb.substring(1));
    }
}
