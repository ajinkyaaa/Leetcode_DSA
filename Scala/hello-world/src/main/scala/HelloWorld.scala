import scala.collection.immutable.{TreeMap, TreeSet}

class Point(val xc: Int, val yc: Int) {
   var x = xc
   var y = yc
   
   def move(dx: Int, dy: Int):Unit= {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}

class Location(override val xc:Int,override val yc:Int,val zc:Int) extends Point(xc,yc) {
   var z: Int = zc

   def move(dx: Int, dy: Int, dz: Int):Unit= {
      x = x + dx
      y = y + dy
      z = z + dz
      println ("Point x location : " + x);
      println ("Point y location : " + y);
      println ("Point z location : " + z);
   }
}

object HelloWorld {
   /* This is my first java program.  
   * This will print 'Hello World' as the output
   */



   def main(args: Array[String]):Unit= {
      val loc = new Location(10, 20, 15);

      // Move to a new location
      loc.move(10, 10, 5);
   }
}
