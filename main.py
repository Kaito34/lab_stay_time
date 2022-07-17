import os
import datetime
from src.models.yolov5 import detect

# 予測
os.chdir('src/models/yolov5')
predicted_name = detect()
Ask_name().main()
put_data(datetime.datetime.today(), predicted_name)

# スコア表示
tell_score().main()
