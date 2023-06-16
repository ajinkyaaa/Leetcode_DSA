import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global
object dataStructures extends App{



    val array: Array[String] = Array("apple", "banana", "orange")

    val map: Map[String, Int] = array.zipWithIndex.map { 
        case (element, index) => (element, index)
    }.toMap

    println(map("apple"))

    val aVectors = Vector(1,2,3,4)
    println(aVectors(2))
    val aSet = Set(1,2,3,4)
   
    val aMap:Map[String,Int] = Map("Daniel" -> 123)

    // Pattern matching  = switch expression
    val aInt = 55
    val order:String = aInt match {
        case 1 => "first"
        case 2 => "Second"
        case _ => aInt + "th"
    } 

    val aTuple = ("honey singh","hiphop")
    val bandDescription = aTuple match {
        case(band,genre) => s"$band belongs to genre $genre"
    }
    println(bandDescription)
    println("order",order)
    1.toString()

    //LAZY Evaluation used in infinite collections
    // pseudo-collections: Option, Try
    println( if(None == null){println("true")}else{println("false")})  

    //scala concurrent Future
    val aFuture = Future({
        println("loading...")
        Thread.sleep(1000)
        println("i have computed value")
        67
    })
    val li:List[String] =  scala.collection.immutable.List("A","B")


    //future try are monads, option
    //global, collection of threads
}