package algospot.boggle;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {
    static char[][] arr;
    static int[][] directions = {
            {-1,-1},
            {-1,0},
            {-1,1},
            {0,-1},
            {0,1},
            {1,-1},
            {1,0},
            {1,1}
    };
    static int[][][] cache ;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader((new InputStreamReader(new FileInputStream("algospot/boggle/test.txt"))));
//        BufferedReader br = new BufferedReader((new InputStreamReader(System.in)));
        int tc = Integer.valueOf(br.readLine());
        for( int i = 0 ; i < tc ; i++) {
            arr = new char[5][5];
            arr[0] = br.readLine().toCharArray();
            arr[1] = br.readLine().toCharArray();
            arr[2] = br.readLine().toCharArray();
            arr[3] = br.readLine().toCharArray();
            arr[4] = br.readLine().toCharArray();


            int wordNum = Integer.valueOf(br.readLine());

            for( int j = 0 ; j < wordNum ; j++) {
                cache = new int[5][5][10];
                String word = br.readLine();
                if( findWord(word)) {
                    System.out.println(String.format("%s %s",word,"YES"));
                } else {
                    System.out.println(String.format("%s %s",word,"NO"));
                }
            }
        }

    }

    public static boolean findWord(String word) {
        return IntStream
                .range(0,25)
                .anyMatch(i->{
                    int y = i / 5;
                    int x = i % 5;
                    return findWord(y,x,word.toCharArray());
                });
    }

    public static boolean findWord(int y, int x , char[] word) {
        if( cache[y][x][word.length-1] == 1) {
            return true;
        } else if( cache[y][x][word.length-1] == -1) {
            return false;
        }
        if(word.length == 1 ) {
            return word[0] == arr[y][x];
        }

        if( word[0] == arr[y][x]) {
            boolean res = Stream.of(directions)
                    .anyMatch(i->{
                        int yy = y + i[0];
                        int xx = x + i[1];
                        if( yy >= 0 && yy < 5 && xx >=0 && xx < 5) return findWord(yy,xx,new String(word).substring(1).toCharArray());
                        return false;
                    });
            if(res) cache[y][x][word.length-1]= 1;
            else cache[y][x][word.length-1] = -1;
            return res;
        }

        return false;
    }
}