﻿## Предсказание цен на автомобили с помощью бустингов и AutoML.
### Лучшие метрики: MAPE - 14.58%, R2 - 0.952.

В качестве обучающего датасета использовались данные с сайта доски объявлений Avito, полученные с помощью парсера на Selenium.

- avito_parser.py (parser_selenium.ipynb) - парсер объявлений с Avito.
- dataset.rar - собранный датасет(>70к строк)
- prepare_data.ipynb (data_analyze.ipynb) - предобработка и чистка распаршенных данных
- models/ - папка со скриптами для обучения моделей + их результаты (catboost, lightGBM, RandomForest, LightAutoML, pyBoost)
