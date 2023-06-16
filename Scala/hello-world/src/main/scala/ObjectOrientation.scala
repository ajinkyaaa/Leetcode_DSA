
object ObjectOrientation extends App {
    class Animal{
        val age:Int = 0
        def eat():Unit = {
            println("i am eating")
        }
    }
    val anAnimal = new Animal()

    //inheritance
    class Dog(val name:String) extends Animal{
         
        
        println("runnnnnnn")
    }
    val aDog = new Dog("Lassie")
    println(aDog.name)

    val aDeclaredAnimal:Animal = new Dog("Hachi")
    aDeclaredAnimal.eat()

    //abstract class
    abstract class WalkingAnimal {
        val hasLegs = true //public
        def walk():Unit
    }

    //interface
    trait Carnivore{
        def eat(animal:Animal):Unit={

        }
    }

    trait Philosopher{
        def ?!(thought:String):Unit
    }

    class Crocodile extends Animal with Carnivore with Philosopher{
        override def eat(animal:Animal):Unit = {
            println(" I am eating you, animal!")
        }

        override def ?!(thought:String):Unit = {
            println(thought)
        }
    }

    val dinosaur = new Carnivore {
        override def eat(animal:Animal):Unit = println("I am a dinosaur")
    }

    val aCroc = new Crocodile()
    aCroc.eat(aDog)
    aCroc eat aDog
    aCroc ?! "what if we could fly"
    dinosaur.eat(aDog)
 
    object MySingleton{
        def mySpecialMethod():Int = 3748
        def apply(x:Int):Int = x+1
    }
    val test:Int = MySingleton.mySpecialMethod()
    println(test)
    println(MySingleton(65))

    object Animal {
        //companion can access each other private fields
        //singleton animal and instance of animal are different
        val canLiveIndefinately = false
    }

    val animalsCanLiveForever = Animal.canLiveIndefinately
    println(animalsCanLiveForever)



    // if object and class same name then called companion

    
    //case classes light weight data structures
    //-sensible equals and hash codebase-serialization
    //-companion with apply
    //-serialiation
    //-pattern matching
    case class Person(name:String,age:Int)

    val bob = Person("bob",54)

    //exceptions

    try{
        val x:String = null
        x.length
    }
    catch{
        case e:Exception => "some exception"
    }
    finally{
        //execute code
    }

    //generics
    abstract class MyList[T]{
        def head:T
        def tail:MyList[T]
    }
    

    //concrete
    val aList:List[Int] = List(1,2,3)
    val first = aList.head

    val aStringList:List[String] = List("hello","Scala")
    val firstString = aList.head
    println(aList)
    


    // scala we operate in immutable value/ objects
    //any modification to object should return new object
    /*
        WORKS BETTER IN MUKTITHREADED ENV
        helps making sense of the code
    */
    // sclaa is closest to oo language
}