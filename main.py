import os
import datetime
from src.models.yolov5 import detect
from GUI.tell_score import Tell_Score
from GUI.ask_name import Ask_name
from src.score import get_data

# 予測
os.chdir('src/models/yolov5')
predicted_name = detect()
true_name = Ask_name().main(name)
put_data(datetime.datetime.today(), predicted_name)

date = now.
# スコアを受け取る
get_data(date, true_name)

# スコア表示
Tell_Score().main(score)
