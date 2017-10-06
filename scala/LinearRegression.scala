package com.roger.mlibTest

import org.apache.spark.SparkContext
import org.apache.spark.mllib.regression.{LinearRegressionWithSGD, LabeledPoint}
import org.apache.spark.mllib.util.MLUtils
class LinearRegression {

}
object LinearRegression {
  def main(args: Array[String]) {
    val sc = new SparkContext("local[8]", "LinearRegression")
    val examples=MLUtils.loadLibSVMFile(sc,"data/regression/sample_linear_regression_data.txt").cache()

    //2 样本数据划分训练样本与测试样本
    val splits = examples.randomSplit(Array(0.9, 0.1))
    val training = splits(0).cache()
    val test = splits(1).cache()

    val numTraining = training.count()
    val numTest = test.count()
    println(s"Training: $numTraining, test: $numTest.")

    //3 新建线性回归模型，并设置训练参数
    val numIterations = 100 //numIterations 渐变下降的迭代数
    val model = LinearRegressionWithSGD.train(training, numIterations)
    println(s"Intercept: ${model.intercept} Coefficients: ${model.weights}")
    //4 对测试样本进行测试

    //    test.map(_.features).saveAsTextFile("dataOut/regression/features")
    //    test.map(_.label).saveAsTextFile("dataOut/regression/labels")

    val prediction = model.predict(test.map(_.features)) // 用测试集的特征来预测标签
    val predictionAndLabel = prediction.zip(test.map(_.label)) //对预测结果和原始标签进行拉链操作
    predictionAndLabel.take(10).foreach(println) // 打印前10行
    //5 计算测试误差  =>方差
    val loss = predictionAndLabel.map {
      case (p1, p2) =>
        val err = p1-p2
        err * err
    }.reduce(_ + _)
    val rmse = math.sqrt(loss / numTest)
    println(s"Test RMSE = $rmse.")
  }
}
