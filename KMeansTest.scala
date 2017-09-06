package com.roger.cluster

import org.apache.spark.mllib.clustering.KMeans
import org.apache.spark.mllib.feature.Normalizer
import org.apache.spark.mllib.linalg.Vectors
import org.apache.spark.{SparkContext}
class clustering {

}
object clustering {
  def main(args: Array[String]) {
    val sc = new SparkContext("local[4]","TestKmeans")
    val data = sc.textFile("data/Context/docwordkos.txt")
    val parsedData = data.map(s => Vectors.dense(s.split(' ').map(_.toDouble)))

    //Normalizer()
    val nor = new Normalizer() // 正则化
    val nordata = nor.transform(parsedData).cache()

    //clustering
    // val numClusters = 6
    //  val numIterations = 10
    //  val clusters = KMeans.train(nordata,numClusters,numIterations)//KMeansModel

    val algorithm = new KMeans()
    algorithm.setK(8)
    algorithm.setMaxIterations(100)
    val clusters=algorithm.run(nordata)

    val Kdata = clusters.predict(nordata).zip(parsedData)
    val Kdata_res = Kdata.map(num => (num,1)).reduceByKey(_ + _)
    Kdata_res.saveAsTextFile("dataOut/clustering/outputOne")
    Kdata.saveAsTextFile("dataOut/clustering/outputTwo")

    val Kpoint =sc.parallelize(clusters.clusterCenters)
    Kpoint.saveAsTextFile("dataOut/Kpoint")

    sc.stop()
  }
}