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
      .appName("Create DataFrame with Ids")
      .getOrCreate()
    spark.conf.set("spark.sql.legacy.allowUntypedScalaUDF",true)
    // Sample data: create a sequence of tuples with ids and other values
    val data = Seq.tabulate(10)(i => (i + 1, s"Value${i + 1}", i * 2))

    // Define the schema for the DataFrame
    val schema = StructType(Seq(
      StructField("id", IntegerType, nullable = false),
      StructField("value1", StringType, nullable = false),
      StructField("value2", IntegerType, nullable = false)
    ))

    // Convert the data to Rows with proper types
    val rows = data.map { case (id, value1, value2) => Row(id, value1, value2) }

    // Create the DataFrame with headers
    val df = spark.createDataFrame(spark.sparkContext.parallelize(rows), schema)
        // Define your UDF function
    val myUdfFunction: Int => Int = (value: Int) => value * 2

    // Register the UDF with Spark's UDFRegistration
    val myUdf: UserDefinedFunction = udf(myUdfFunction, IntegerType)
    spark.udf.register("my_udf", myUdf)

        // Use the UDF in your DataFrame operations
    val dfUdf = df.withColumn("id", myUdf(col("id"))).select("id")

   val arrayConfig=spark.sparkContext.getConf.getAll
    for (conf <- arrayConfig)
    println(conf._1 +", "+ conf._2)
    // Show the result
    dfUdf.show()


  }
}