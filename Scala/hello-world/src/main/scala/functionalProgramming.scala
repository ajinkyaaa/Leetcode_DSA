import scala.collection.mutable.Map
object functionalProgramming extends App{
    //apply = constructor

    /*
    functional programming:
        -compose functions
        pass functions as args
        return functions as result

        Conclusion: functionsX = Function1,Function2...functions22


    */
    class Person(name:String){
        def apply(age:Int) = println((age))
    } 
    val bob = new Person("bob")
    bob.apply(43)
    bob(43)

    trait Carnivore[Animal]{
        def eat(animal:Animal):Unit={

        }
    }

    val simpleIncrementer = new Function1[Int,Int]{
        override def apply(arg:Int):Int = arg +1

    }

    val stringConcatinator = new Function2[String,String,String]{
        override def apply(arg1:String,arg2:String):String = arg1 + arg2
    }

    val doubler: Function1[Int,Int] = (x:Int) => x*2


    //defined a function
    //all scala functions are instances of these functionX types
    //higher order functions takes functions as arguments or return function
    val li = List(1,2,3).map(x => x+1)
    val liFlatmap = List(1,2,3).flatMap(x => List(x,x*2))
    val filter = List(1,2,3).filter((p => p>2))
    val map: Map[String,String] = Map()
    import scala.collection.mutable.Map

    val mutableMap: Map[String, Int] = Map("key1" -> 1, "key2" -> 2)

    // Add a new key-value pair
    mutableMap("key3") = 3

    // Update the value for an existing key
    mutableMap("key2") = 20

    val array: Array[Int] = Array(1, 2, 3, 4, 5)
    val middleIndex: Int = array.length / 2
    val middleElement: Int = array(middleIndex)



    println("middleElement",middleElement)
    println("flatmap",li)
    println(li) 
    simpleIncrementer(23)
    println(stringConcatinator("I love Scala","thats false"))
    println(doubler(4))
    println(liFlatmap)
    println(filter)
    print("mutableMap",mutableMap)

    
}