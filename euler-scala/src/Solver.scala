/**
 * Created by chris on 01/06/14.
 */
object Solver extends App {

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
    p28()
  }
}
