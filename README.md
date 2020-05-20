# AutoML-Benchmark
A Performance Benchmark of Different AutoML Frameworks

---

## Frameworks
In the benchmark framework:
* [H2o](http://docs.h2o.ai/h2o/latest-stable/h2o-docs/automl.html)
* [TPOT](https://github.com/EpistasisLab/tpot)
* [Auto_ml](https://github.com/ClimbsRocks/auto_ml)
* [CatBoost](https://github.com/catboost/catboost) (default params)
* [LightGBM](https://github.com/microsoft/LightGBM) (default params)
* [AutoML_Alex](https://github.com/Alex-Lekov/AutoML_Alex) 
* AutoML_Alex (only LightGBM)

## Binary-Classification
Sum of positions in the rating for all datasets. (The bigger, the better):

<img width=800 src="./img/AUC_place_v2.png" alt="bench">


| Framework | AUC place |
| ------ | ------ |

| AutoML_Alex | 30 |
| AutoML_Alex (only LightGBM) | 26 |
| CatBoost (default) | 25 |
| H2o | 20 |
| Auto_ml | 19 |
| LightGBM (default) | 13 |
| TPOT | 7 |


Total AUC on datasets:


<table>
  <tr>
   <td>Framework/dataset
   </td>
   <td colspan="2" ><strong>adult</strong>
   </td>
   <td colspan="2" ><strong>Amazon_employee_access</strong>
   </td>
   <td colspan="2" ><strong>bank-marketing</strong>
   </td>
   <td colspan="2" ><strong>Click_prediction_small</strong>
   </td>
   <td colspan="2" ><strong>credit-g</strong>
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
   <td>LightGBM (default)
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
0,0144</p>

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
   <td>AutoML_Alex (only LightGBM)
   </td>
   <td><p style="text-align: right">
0,9148</p>

   </td>
   <td>0,0036
   </td>
   <td><p style="text-align: right">
0,8577</p>

   </td>
   <td><p style="text-align: right">
0,0080</p>

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
   <td>CatBoost (default)
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