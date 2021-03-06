lab_stay_time
==============================

テーマ: 画像認識による出退勤管理の自動化

こちらは「7月Vol.6ハッカソン技育CAMP2022 by 株式会社サポーターズ」での開発を行ったリポジトリです。

発表スライド：[google slide](https://docs.google.com/presentation/d/1oTApgwo6GnOrfLRHa0wzTucgBGXmQGqU1gIDbmZVLrk/edit#slide=id.p)


# 使用方法
## YOLOの導入
参考→[【YOLO V5】AIでじゃんけん検出](https://qiita.com/PoodleMaster/items/5f2cc3248c03b03821b8)
1. `src/models`に`git clone https://github.com/ultralytics/yolov5`
2. yolo v5を起動するために必要なライブラリをインストール
   - `pip install -r yolov5/requirements.txt`
   - GPU→`pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cu113`
   - CPU→`pip install torch==1.11.0+cpu torchvision==0.12.0+cpu torchaudio==0.11.0 --extra-index-url https://download.pytorch.org/whl/cpu`
3. データを`data/processed`に置く
4. `python src/models/yolov5/train.py --img 1080 --batch 3 --epoch 10 --data 'docs/annotation.yaml' --name lab_stay_time`で学習
5. `python src/models/yolov5/detect.py --source 'src/models/yolov5/data/images/kusumoto.jpg' --weight 'src/models/yolov5/runs/train/lab_stay_time8/weights/best.pt'`で予測



## API_keyの保存方法
1. `.env` fileを一番上の階層におく
    ファイルの中身  
    ```bash
    SPREADSHEET_KEY=API_key
    JSON_KEY=Json_key
    ```
2. `./src/secret/`にJsonファイルを入れる

- put_data関数内のname_dictは名前とスプレッドシート上の名前の横軸のいちを照らし合わせるもの
- name_dictの引数は顔の予測モデルの方から渡される予測された人物の名前にしてください

## spread sheetのpython上の使い方
- https://tanuhack.com/library-gspread/
- https://kirinote.com/python-pivot-spread/

## API key と Json key の取得方法
- https://qiita.com/taqumo/items/674c1d94e1c530cd2953

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

