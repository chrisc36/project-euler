/**
 * Created by chris on 01/06/14.
 */
object ScalaSolver extends App {

  def p29() {
    // We could brute force this problem without trouble using BigInteger, but I will
    // opt for an approach where numbers as stored as prime factors which will scale better

    val pc = new PrimeCache()

    /** Returns an immutable map of the prime factors -> counts of that factor */
    def getPrimeMap(num: Integer): Map[Integer, Int] = {
      var primeFactors: Seq[Integer] = Seq[Integer]()
      var onNum = num
      var onPrime = 1
      while(onNum != 1) {
        val prime: Integer = pc.getPrime(onPrime).intValue()
        if (onNum % prime == 0) {
          onNum = onNum / prime
          primeFactors = primeFactors :+ prime
          onPrime = 0
        }
        onPrime += 1
      }
      primeFactors.groupBy(x => x).map(t => (t._1, t._2.length))
    }

    var numbersFound = scala.collection.mutable.Set[Map[Integer, Int]]()
    for(a <- 2 to 100) {
      val factors = getPrimeMap(a)
      for(b <- 2 to 100) {
        numbersFound += factors.map(x=>(x._1, x._2 * b))
      }
    }
    println(numbersFound.size)
  }

  def p28() {

    // One line methods folds over (squareNum, onNum, sum)
    print(Range(2, 502).foldLeft((2, 1, 1))((a, b) =>
      (a._1 + 1, a._2 + 4 * (a._1 * 2 - 2), a._3 + 4 * a._2 + 10 * (a._1 * 2 - 2)))
    )

    // Using for loops
    var sum = 1
    var onNumber = 1

    for(squareNumber <- 1 to 500) {

      val squareLength = squareNumber * 2 + 1
      // Add in each corner, we start exactly below the upper left corner so this
      // pattern works in all cases
      for(corner <- 0 to 3) {
        onNumber += squareLength - 1
        sum += onNumber
      }
    }
    println(sum)
  }

  override def main (args: Array[String]) {
    p29()
  }
}
