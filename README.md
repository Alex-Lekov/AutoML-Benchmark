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
