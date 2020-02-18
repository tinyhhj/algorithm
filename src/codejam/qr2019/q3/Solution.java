package codejam.qr2019.q3;

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.*;

public class Solution {

    public static void main(String[] args) throws FileNotFoundException {
        Scanner sc = new Scanner(new BufferedReader(new InputStreamReader(System.in)));
        int tc = sc.nextInt();
        sc.nextLine();
        for( int i = 0 ; i < tc ; i++ ) {
            SortedSet<BigInteger> primes = new TreeSet<>();
            BigInteger n = sc.nextBigInteger();
            int l = sc.nextInt();
            List<BigInteger> input = new ArrayList<>();
            List<BigInteger> primesOrder = new ArrayList<>();
            BigInteger prev = sc.nextBigInteger();
            int idx = 0;
            for( int j = 1 ; j < l; j++) {
                BigInteger number = sc.nextBigInteger();
                BigInteger prevNumber =prev;
                if( prevNumber.compareTo(number) != 0 ) {
                    BigInteger prime = gcd(number, prevNumber);
                    if( j % 2 != 0) {
                        //BABAA ABABB
                        //BAC
                        // AAAAB
                        BigInteger other = prevNumber.divide(prime);
                        for( int k = 0 ; k <= j ; k++) {
                            primesOrder.add(k %2 == 0 ? other: prime);
                        }
                        primesOrder.add(number.divide(prime));
                    } else {
                        //ABABAA
                        BigInteger other = prevNumber.divide(prime);
                        for( int k = 0 ; k <= j ; k++) {
                            primesOrder.add(k %2 == 0 ? prime: other);
                        }
                        primesOrder.add(number.divide(prime));
                    }
                    idx = j;
                    break;
                }
            }
            for( int j = idx+1; j < l ; j++) {
                // 12 23 34 ..  end-1 end
                BigInteger num = sc.nextBigInteger();
                BigInteger prevNum = primesOrder.get(primesOrder.size()-1);
                BigInteger number = num.divide(prevNum);
                primesOrder.add(number);
            }
//            primesOrder.add(input.get(input.size()-1).divide(primesOrder.get(primesOrder.size()-1)));
            primes.addAll(primesOrder);

//            Assert.check(primes.size() == 26);
//            Assert.check(primes.first().compareTo(primes.last()) < 0);

            Iterator<BigInteger> it = primes.iterator();
            Map<BigInteger, Integer> mapping = new HashMap<>();
            int cnt = 0 ;
            while(it.hasNext()) {
                mapping.put(it.next(), cnt++);
            }
            char[] alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".toCharArray();
            System.out.print(String.format("Case #%d: ",i+1));
            for( BigInteger p : primesOrder) {
                System.out.print(alphabet[mapping.get(p)]);
            }
            System.out.println("");

        }


    }

    public static BigInteger gcd(BigInteger a , BigInteger b) {
        if( a.compareTo(b) < 0) {
            BigInteger tmp = a;
            a = b;
            b = tmp;
        }
        while(b.compareTo(BigInteger.ZERO) != 0) {
            BigInteger r = a.mod(b);
            a = b;
            b = r;
        }
        return a;
    }
}
