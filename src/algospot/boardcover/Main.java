package algospot.boardcover;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {

    private static char BLACK = '#';
    private static char WHITE = '.';
    private static char[][][] block = new char[][][] {
            {{'#','#'},
                    {'#','.'}},
            {{'#','#'},
                    {'.','#'}},
            {{'.','#'},
                    {'#','#'}},
            {{'#','.'},
                    {'#','#'}},
    };

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new FileInputStream("algospot/boardcover/input.txt"));
        int tc = sc.nextInt();
        IntStream.range(0,tc)
                .forEach(i-> {
                    //tc
                    int row = sc.nextInt();
                    int col = sc.nextInt();
                    sc.nextLine();

                    char[][] map = new char[row][];

                    // map reading
                    final int[] sum = {0};
                    IntStream.range(0,row)
                            .forEach(ii->{
                                map[ii] = sc.nextLine().toCharArray();
                                sum[0] += IntStream.range(0,map[ii].length)
                                        .mapToObj(index->map[ii][index])
                                        .filter(c->c=='.')
                                        .count();
                            });
                    System.out.println(getBlockNum(map,sum[0]));

                });
    }

    // input: map, 남은 칸수
    // output: block을 놓을 수 있는 가능한 수
    public static int getBlockNum(final char[][] map, int remain) {
        if( remain % 3 != 0)
            return 0;
        if( remain == 0 )
            return 1;


        // 맨 왼쪽 위쪽부터 블록을 채워감
        int first = IntStream.range(0,map.length * map[0].length)
                .filter(i->map[i/map[0].length][i%map[0].length] == '.')
                .findFirst().getAsInt();
        int r = first / map[0].length;
        int c = first % map[0].length;
        int res= 0 ;

        for( int i = 0; i < 4 ; i++) {
            char[][] b = block[i];
            if( isBlockFit(map, b, r, c)) {
                addBlock(map,b,r,c);
                res += getBlockNum(map, remain-3);
                removeBlock(map,b,r,c);
            }
        }
        return res;
    }

    private static void removeBlock(char[][] map, char[][] b, int r, int c) {
        if(b[0][0] == '.') c--;
        for( int i = 0; i < 2 ; i++) {
            for( int j = 0 ; j < 2 ; j++) {
                if( b[i][j] == '#') {
                    map[r+i][c+j] = '.';
                }
            }
        }
    }

    private static void addBlock(char[][] map, char[][] b, int r, int c) {
        if(b[0][0] == '.') c--;
        for( int i = 0; i < 2 ; i++) {
            for( int j = 0 ; j < 2 ; j++) {
                if( b[i][j] == '#') {
                    map[r+i][c+j] = '#';
                }
            }
        }
    }

    private static boolean isBlockFit(char[][] map, char[][] b, int r, int c) {
        if(b[0][0] == '.') c--;
        if(!(r >= 0 && r < map.length && c >=0 && c < map[0].length
        && r+1 >= 0 && r+1 < map.length && c+1>=0 && c+1 < map[0].length)) return false;
        for( int i = 0; i < 2 ; i++) {
            for( int j = 0 ; j < 2 ; j++) {
                if( map[r+i][c+j] == '#' && b[i][j] == '#') {
                    return false;
                }
            }
        }
        return true;
    }
}
