/**
 */
import java.math.BigInteger;
import java.util.*;


public class Solver {

    private static void p26() {
        // Look for division of powers of 10 that have the same remainder indicating that the decimals numbers
        // will start looping.
        int longestCycle = -1;
        int longestCycleNumber = 0;
        Map<Integer, Integer> remainders = new HashMap<Integer, Integer>();
        for(int i = 1; i < 1000; i++){
            int place = 0;
            int r = 1;
            remainders.clear();
            while(r!= 0 && !remainders.containsKey(r)) {
                remainders.put(r, place);;
                 r = r * 10 % i;
                place++;
            }
            if(r == 0) {
                System.out.printf("Number %d was not looping\n", i);
            } else {
                System.out.printf("Number %d looped from %d to %d\n", i, remainders.get(r), place);
                int cycleLength = place - remainders.get(r);
                if (cycleLength > longestCycle) {
                    longestCycle = cycleLength;
                    longestCycleNumber = i;
                }
            }
        }
        System.out.printf("Longest number was %d was %d length cycle\n", longestCycleNumber, longestCycle);
    }


    private static void p25() {
        // The good old brute force approach
        BigInteger lastFib = BigInteger.valueOf(1);
        BigInteger curFib = BigInteger.valueOf(1);
        BigInteger divisor = BigInteger.valueOf(10).pow(999);
        int term = 2;
        while(curFib.divide(divisor).intValue() != 1) {
            BigInteger tmp = curFib;
            curFib = curFib.add(lastFib);
            lastFib = tmp;
            term += 1;
        }
        System.out.println(term);
    }

    private static void p24() {
        // The strategy here will be to solve for each digit at a time from left to right by
        // the largest digit we can afford to without forcing ourself into picking an output
        // that is a too low permutation.

        int targetPermutation = 1000000;
        int nDigits = 10;

        // Digits we have not used so far in our output
        List<Integer> unusedDigits = new ArrayList<Integer>();

        // Precomputed factorials
        int[] factorials = new int[nDigits];

        factorials[0] = 1;
        unusedDigits.add(0);
        for(int i = 1; i < factorials.length; i++) {
            factorials[i] = factorials[i - 1] * i;
            unusedDigits.add(i);
        }

        String output = "";
        int onPermutation = 1;
        List<Integer> digits = new ArrayList<Integer>();
        int onPlace = nDigits - 1;
        while(onPlace >= 0) {
            int perIncrement = factorials[onPlace];
            int increments = (targetPermutation - onPermutation) / perIncrement;
            onPermutation += perIncrement * increments;
            digits.add(increments);
            output += unusedDigits.get(increments);
            unusedDigits.remove(increments);
            onPlace--;
        }
        System.out.println(output);
    }

    public static void main(String[] args){
        Solver.p26();
    }
}
