package com.roger.taxi

import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.feature.Normalizer
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkContext}

class taxiCase {

}
object taxiCase {
  def main(args: Array[String]) {
    val sc = new SparkContext("local[4]","TestKmeans")
    val data = sc.textFile("data/clustering/taxi.txt")
    val parsedData = data.map(s => Vectors.dense(s.split(',').map(_.toDouble)))

    //Normalizer()
    val nor = new Normalizer() // 正则化
    val nordata = nor.transform(parsedData).cache()

    val algorithm = new KMeans()
    algorithm.setK(6)
    algorithm.setMaxIterations(100)
    val clusters=algorithm.run(nordata)

    val Kdata = clusters.predict(nordata).zip(parsedData)
    val Kdata_res = Kdata.map(num => (num,1)).reduceByKey(_ + _)
    Kdata_res.saveAsTextFile("dataOut/taxi/One")
    Kdata.saveAsTextFile("dataOut/taxi/Two")

    val Kpoint =sc.parallelize(clusters.clusterCenters)
    Kpoint.saveAsTextFile("dataOut/taxi/Kpoint")

    sc.stop()
  }
}
