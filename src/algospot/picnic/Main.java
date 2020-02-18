package algospot.picnic;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {

//        Scanner sc = new Scanner(new FileInputStream("algospot/picnic/test.txt"));
        Scanner sc=  new Scanner(System.in);
        int tc = sc.nextInt();
        for( int i = 0; i < tc ; i++ ) {
            int total = sc.nextInt();
            int friend = sc.nextInt();
            int[][] friends = new int[10][10];
            for(int j = 0 ; j < friend ; j++) {
                int a = sc.nextInt();
                int b = sc.nextInt();
                friends[a][b] = 1;
                friends[b][a] = 1;
            }
            System.out.println(getFriendNumber(new int[total], friends, total));

        }
    }

    // 친구 목록이 주어졌을 때의 친구들끼리 짝을 맺을 수 있는 경우의 수
    static int getFriendNumber(int[] children, int[][] friends, int remain) {
        // 짝이 다 맞으면 경우의 수 1 추가
        if( remain == 0 ) {
            return 1;
        }
        final int[] res = {0};
        // 가장 첫번째부터 짝을 맺어준다
        int first=IntStream.range(0,children.length)
                .filter(i->children[i] == 0)
                .findFirst().getAsInt();
        IntStream.range(first,children.length)
                .filter(j->friends[first][j] == 1 && children[j] == 0)
                .forEach(j->{
                    children[first]=1;
                    children[j]=1;

                    res[0] +=getFriendNumber(children,friends,remain-2);
                    children[first]=0;
                    children[j]=0;


                });

        return res[0];
    }

}
