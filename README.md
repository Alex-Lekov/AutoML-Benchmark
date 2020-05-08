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
* AutoML_Alex (only LightGBM)

## Binary-Classification
Sum of positions in the rating for all datasets. (The bigger, the better):

<img width=800 src="./img/AUC_place.png" alt="bench">


| Framework | AUC place |
| ------ | ------ |
| AutoML_Alex (only LightGBM) | 25 |
| CatBoost (default) | 24 |
| Auto_ml | 18 |
| H2o | 18 |
| LightGBM (default) | 13 |
| TPOT | 7 |


Total AUC on datasets:
<table>
  <tr>
   <td><strong>Framework / dataset</strong>
   </td>
   <td><strong>adult</strong>
   </td>
   <td><strong>Amazon_employee_access</strong>
   </td>
   <td><strong>bank-marketing</strong>
   </td>
   <td><strong>Click_prediction_small</strong>
   </td>
   <td><strong>credit-g</strong>
   </td>
  </tr>
  <tr>
   <td>TPOT
   </td>
   <td>0.9126
   </td>
   <td>0.7895
   </td>
   <td>0.84918
   </td>
   <td>0.71136
   </td>
   <td>0.78164
   </td>
  </tr>
  <tr>
   <td>H2o
   </td>
   <td>0.91428
   </td>
   <td>0.8551
   </td>
   <td>0.9371
   </td>
   <td>0.72056
   </td>
   <td>0.77646
   </td>
  </tr>
  <tr>
   <td>LightGBM (default)
   </td>
   <td>0.91444
   </td>
   <td>0.8463
   </td>
   <td>0.93646
   </td>
   <td>0.71598
   </td>
   <td>0.77954
   </td>
  </tr>
  <tr>
   <td>Auto_ml
   </td>
   <td>0.91466
   </td>
   <td>0.8286
   </td>
   <td>0.90354
   </td>
   <td>0.71884
   </td>
   <td><strong>0.79252</strong>
   </td>
  </tr>
  <tr>
   <td>AutoML_Alex (only LightGBM)
   </td>
   <td>0.91482
   </td>
   <td><strong>0.8577</strong>
   </td>
   <td><strong>0.93848</strong>
   </td>
   <td>0.71728
   </td>
   <td>0.78524
   </td>
  </tr>
  <tr>
   <td>CatBoost (default)
   </td>
   <td><strong>0.91498</strong>
   </td>
   <td>0.8467
   </td>
   <td>0.93792
   </td>
   <td><strong>0.71912</strong>
   </td>
   <td>0.78374
   </td>
  </tr>
</table>