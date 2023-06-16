import scala.util.Success
/*
object Test {
def main(args: Array[String]) {
    println( apply( layout, 10) )
}
def apply(f: Int => String, v: Int) = f(v)
def layout[A](x: A) = "[" + x.toString() + "]"


val myNewString = new Array[String](3)
myNewString(0) = "have "
myNewString(1) = "a "
myNewString(2) = "good day!"

*/

object test extends App{
    val aList:List[String] = List("Apple","Banana","Cherry")
    val abList = aList.updated(1, "Pineapple")
    println(abList(1))
    var myMap = Map[String,String]()
    myMap = myMap + ("key3" -> "value3")
    
    val s = Seq("apple", "oranges", "apple", "banana", "apple", "oranges", "oranges")
    val newMap = s.groupBy(l => l).map(t => (t._1 -> t._2.length)).toMap
    
    println("newMap",newMap)
    // Using the + operator

    def unsafeMethodwhichcanreturnNull():String = null
    val anOption = Option(unsafeMethodwhichcanreturnNull())

    val stringProcessing:Any = anOption match{
        case Some(value) => s"I have obtained a valid string"
        case None => "I have obtained nothing"
        case null =>  "I have obtained null"
    
    }


    println(stringProcessing)
    /*
    val methodWhichCanThrowException():String = throw new RuntimeException
    val aTry = Try(methodWhichCanThrowException())
    val anotherStringProcessing = aTry match{
        case Success(validValue) => "success"
        case Failure(ex) => "error"
    }
    */
    //val result = (1 to 10).map(_ => println(_))
}


    
    