package algospot.tsp1;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new FileInputStream("algospot/tsp1/input.txt"));
        int tc = sc.nextInt();
        for( int i = 0; i < tc; i++) {
            int cities = sc.nextInt();
            double[][] map = new double[cities][cities];

            for( int j = 0 ; j < cities*cities;j++) {
                int y = j / cities;
                int x = j % cities;
                map[y][x] = sc.nextDouble();
            }
            double res = Double.MAX_VALUE;
            for( int k = 0 ; k < cities; k++) {
                boolean[] visits = new boolean[cities];
                visits[k] = true;
                res = Math.min(res,traverse(map, visits, k));
            }
            System.out.println(res);

        }

    }

    // input: 도시간 거리 정보 double[][], 방문여부 boolean[], 시작점 int
    // output: 최소 여행 길이
    public static double traverse(double[][] map, boolean[] visits, int st) {

        int next = -1;
        for( int i = 0;  i < visits.length ; i++) {
            if( !visits[i]) {
                next = i;
                break;
            }
        }
        // 모두 방문했다면
        if( next == -1) {
            return 0;
        }
        double minDist = Double.MAX_VALUE;
        for(int i = 0 ; i < visits.length; i++) {
            if(!visits[i]) {
                visits[i]= true;
                double dist = map[st][i] + traverse(map,visits,i);
                visits[i]= false;
                if( dist < minDist) {
                    minDist = dist;
                }
            }
        }
        return minDist;
    }
}
