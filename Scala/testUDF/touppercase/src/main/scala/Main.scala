import org.apache.spark.sql.{SparkSession, DataFrame}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.expressions.UserDefinedFunction
import org.apache.spark.sql.types.IntegerType
import org.apache.spark.sql.{SparkSession, Row}
import org.apache.spark.sql.types.{StructType, StructField, StringType, IntegerType}

object Main {
  def main(args: Array[String]): Unit = {
    // Create a Spark session
    val spark = SparkSession.builder()
      .appName("Create DataFrame with Names")
      .getOrCreate()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF",true)
    // Sample data: create a sequence of tuples with ids and other values

        // Define the schema for the DataFrame
    val schema = StructType(Seq(
      StructField("Name", StringType, nullable = false),
      StructField("Age", StringType, nullable = false),
      StructField("City", StringType, nullable = false)
    ))
    println("===============================================================================================================================================")
    // Sample data as a list of tuples
    val data = List(
      ("John", "28", "New York"),
      ("Alice", "25", "San Francisco"),
      ("Bob", "32", "Los Angeles")
    )

    // Convert the list of tuples to Rows
    val rows = data.map { case (name, age, city) => org.apache.spark.sql.Row(name, age, city) }

    // Create a DataFrame
    var df: DataFrame = spark.createDataFrame(spark.sparkContext.parallelize(rows), schema)
    df.show()


    // To upper case function
    df = df.withColumn("test_col",lit("abc"))

    df.show()
    // Show the DataFrame

    val toUpperCaseUDF : UserDefinedFunction = udf((str:String) => {
      str.toUpperCase()
    },StringType) 

    df = df.withColumn("test_col_udf",toUpperCaseUDF(col("test_col")))

    df.show()
    println("UDF ran successfully")
    



  }
}