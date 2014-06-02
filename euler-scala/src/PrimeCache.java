import java.util.ArrayList;
import java.util.List;

/**
 * Created by chris on 01/06/14.
 */
public class PrimeCache {

    private List<Long> primes;

    public PrimeCache() {
        primes = null;
    }

    public Long getPrime(int prime) {
        prime--; // So the primes index as we would expect rather then zero based
        if (primes == null) {
            primes = new ArrayList<Long>();
            primes.add(2L);
            primes.add(3L);
        }
        Long candidatePrime = primes.get(primes.size() - 1) + 2;
        while (primes.size() < prime + 1) {
            boolean isPrime = true;
            int onFactor = 1;
            while (true) {
                Long factor = primes.get(onFactor);
                if (candidatePrime % factor == 0) {
                    isPrime = false;
                    break;
                }
                if (factor <= Math.sqrt(candidatePrime)) {
                    onFactor += 1;
                } else {
                    break;
                }
            }
            if (isPrime) {
                primes.add(candidatePrime);
            }
            candidatePrime += 2;
        }
        return primes.get(prime);
    }

    public void clear() {
        primes.clear();
    }
}
