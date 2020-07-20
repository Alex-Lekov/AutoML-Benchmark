# AutoML-Benchmark
A Performance Benchmark of Different AutoML Frameworks

---

# Frameworks
In the benchmark framework:
* [H2o](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html)
* [TPOT](https://github.com/EpistasisLab/tpot)
* [Auto_ml](https://github.com/ClimbsRocks/auto_ml)
* [CatBoost](https://github.com/catboost/catboost) (default params)
* [LightGBM](https://github.com/microsoft/LightGBM) (default params)
* [AutoML_Alex](https://github.com/Alex-Lekov/AutoML_Alex) 


# Benchmark Settings
* Repeated 5 times (on 5 K-folds)
* Time Limit 1 hour on fold
* Chose datasets from 1000 and more rows/examples
* Docker


# Binary-Classification
Sum of revers positions in the rating for all datasets. (The bigger, the better):

<img width=800 src="./img/AUC_place_v2.png" alt="bench">


| Framework | Place |
| ------ | ------ |
| AutoML_Alex | 30 |
| CatBoost | 25 |
| H2o | 20 |
| Auto_ml | 19 |
| LightGBM | 13 |
| TPOT | 7 |


## Total AUC on datasets:


<table>
  <tr>
   <td>Framework/dataset
   </td>
   <td colspan="2" ><strong><a href="./binary-classification/datasets/adult">adult</a></strong>
   </td>
   <td colspan="2" ><strong><a href="./binary-classification/datasets/Amazon_employee_access">amazon</a></strong>
   </td>
   <td colspan="2" ><strong><a href="./binary-classification/datasets/bank-marketing">bank-marketing</a></strong>
   </td>
   <td colspan="2" ><strong><a href="./binary-classification/datasets/Click_prediction_small">click_predict</a></strong>
   </td>
   <td colspan="2" ><strong><a href="./binary-classification/datasets/credit-g">credit-g</a></strong>
   </td>
  </tr>
  <tr>
   <td>
   </td>
   <td>auc
   </td>
   <td>auc_std
   </td>
   <td>auc
   </td>
   <td>auc_std
   </td>
   <td>auc
   </td>
   <td>auc_std
   </td>
   <td>auc
   </td>
   <td>auc_std
   </td>
   <td>auc
   </td>
   <td>auc_std
   </td>
  </tr>
    <tr>
   <td><b>AutoML_Alex</b>
   </td>
   <td><p style="text-align: right">
<b>0,9156</b></p>

   </td>
   <td>0,0037
   </td>
   <td><p style="text-align: right">
<b>0,8668</b></p>

   </td>
   <td><p style="text-align: right">
0,0125</p>

   </td>
   <td><p style="text-align: right">
0,9385</p>

   </td>
   <td><p style="text-align: right">
0,0030</p>

   </td>
   <td><p style="text-align: right">
0,7173</p>

   </td>
   <td><p style="text-align: right">
0,0044</p>

   </td>
   <td><p style="text-align: right">
0,7852</p>

   </td>
   <td><p style="text-align: right">
0,0311</p>
   </td>
  </tr>

  <tr>
   <td>TPOT
   </td>
   <td><p style="text-align: right">
0,9126</p>

   </td>
   <td>0,0026
   </td>
   <td><p style="text-align: right">
0,7895</p>

   </td>
   <td><p style="text-align: right">
0,0339</p>

   </td>
   <td><p style="text-align: right">
0,8492</p>

   </td>
   <td><p style="text-align: right">
0,0070</p>

   </td>
   <td><p style="text-align: right">
0,7114</p>

   </td>
   <td><p style="text-align: right">
0,0045</p>

   </td>
   <td><p style="text-align: right">
0,7816</p>

   </td>
   <td><p style="text-align: right">
0,0189</p>

   </td>
  </tr>
  <tr>
   <td>H2o
   </td>
   <td><p style="text-align: right">
0,9143</p>

   </td>
   <td>0,0020
   </td>
   <td><p style="text-align: right">
0,8551</p>

   </td>
   <td><p style="text-align: right">
0,0030</p>

   </td>
   <td><p style="text-align: right">
0,9371</p>

   </td>
   <td><p style="text-align: right">
0,0037</p>

   </td>
   <td><p style="text-align: right">
0,7206</p>

   </td>
   <td><p style="text-align: right">
0,0041</p>

   </td>
   <td><p style="text-align: right">
0,7765</p>

   </td>
   <td><p style="text-align: right">
0,0479</p>

   </td>
  </tr>

  <tr>
   <td>Auto_ml
   </td>
   <td><p style="text-align: right">
0,9147</p>

   </td>
   <td>0,0033
   </td>
   <td><p style="text-align: right">
0,8286</p>

   </td>
   <td><p style="text-align: right">
0,0143</p>

   </td>
   <td><p style="text-align: right">
0,9035</p>

   </td>
   <td><p style="text-align: right">
0,0058</p>

   </td>
   <td><p style="text-align: right">
0,7188</p>

   </td>
   <td><p style="text-align: right">
0,0066</p>

   </td>
   <td><p style="text-align: right">
0,7925</p>

   </td>
   <td><p style="text-align: right">
0,0227</p>

   </td>
  </tr>

  <tr>
   <td>LightGBM
   </td>
   <td><p style="text-align: right">
0,9144</p>

   </td>
   <td>0,0037
   </td>
   <td><p style="text-align: right">
0,8463</p>

   </td>
   <td><p style="text-align: right">
0,0113</p>

   </td>
   <td><p style="text-align: right">
0,9365</p>

   </td>
   <td><p style="text-align: right">
0,0034</p>

   </td>
   <td><p style="text-align: right">
0,7160</p>

   </td>
   <td><p style="text-align: right">
0,0057</p>

   </td>
   <td><p style="text-align: right">
0,7795</p>

   </td>
   <td><p style="text-align: right">
0,0274</p>

   </td>
  </tr>
  <tr>
   <td>CatBoost
   </td>
   <td><p style="text-align: right">
0,9150</p>

   </td>
   <td>0,0030
   </td>
   <td><p style="text-align: right">
0,8467</p>

   </td>
   <td><p style="text-align: right">
0,0090</p>

   </td>
   <td><p style="text-align: right">
0,9379</p>

   </td>
   <td><p style="text-align: right">
0,0040</p>

   </td>
   <td><p style="text-align: right">
0,7191</p>

   </td>
   <td><p style="text-align: right">
0,0058</p>

   </td>
   <td><p style="text-align: right">
0,7837</p>

   </td>
   <td><p style="text-align: right">
0,0222</p>

   </td>
  </tr>
</table>


## Boxplot Datasets:
<p><img width=800 src="./img/adult.png" alt="datset_adult"></p>
<p><img width=800 src="./img/Amazon_employee_access.png" alt="datset_adult"></p>