from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from datetime import datetime, timedelta
import math
import datetime
import matplotlib.pyplot as plt


otx = OTXv2("8c3b1fd2add0a2325e7edd39eeb9a0e7cd577238a65fc83f67c4b1d2c08ee625")
# Get all the indicators associated with a pulse
indicators = otx.get_pulse_indicators("606d75c11c08ff94089a9430")



print(len(indicators))

for indicator in indicators:
    print(indicator["indicator"] + " ; " + indicator["type"] + " ; " + indicator["title"] + " ; " + indicator["created"] + " ; ")

# Get everything OTX knows about google.com
otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "google.com")


base_core = input("Введите значение от 0 до 100: ")

try:
    b_core = int(base_core)
    print("Base_core = ", b_core)
except ValueError:
    print("Вы ввели некоректное значение. Попробуйте еще раз. ")

now = datetime.datetime.now()
print("Текущая дата: ", now)

last_ind = datetime.datetime(2021, 5, 30, 10, 59, 2)
print("Дата последнего замеченного индикатора: ", last_ind)

delta = now - last_ind
print("Время, прошедшее с начала последнего замеченного индикатора: ", delta)

seconds = delta.total_seconds()
hours = round(seconds // 3600)
print("В часах: ", hours)

v_rate = int(base_core)/int(hours)
print("Скорость затухания: ", round(v_rate, 2))

decay_rate = 7*24
score = float(base_core) * (1 - math.pow(float(hours)/float(decay_rate), 1/float(v_rate)))
score_s = round(score, 2)
print("Оценка рейтинга индикатора: ", score_s)


hours_1 = 1
v_rate_1 = int(base_core)/int(hours_1)
score_1 = float(base_core) * (1 - math.pow((float(hours_1)/float(decay_rate)), 1/float(v_rate_1)))
print(score_1)

hours_2 = 20
v_rate_2 = int(base_core)/int(hours_2)
score_2 = float(base_core) * (1 - math.pow(float(hours_2)/float(decay_rate), 1/float(v_rate_2)))
print(score_2)

hours_3 = 40
v_rate_3 = int(base_core)/int(hours_3)
score_3 = float(base_core) * (1 - math.pow(float(hours_3)/float(decay_rate), 1/float(v_rate_3)))
print(score_3)

hours_4 = 60
v_rate_4 = int(base_core)/int(hours_4)
score_4 = float(base_core) * (1 - math.pow(float(hours_4)/float(decay_rate), 1/float(v_rate_4)))
print(score_4)

hours_5 = 80
v_rate_5 = int(base_core)/int(hours_5)
score_5 = float(base_core) * (1 - math.pow(float(hours_5)/float(decay_rate), 1/float(v_rate_5)))
print(score_5)

hours_6 = 100
v_rate_6 = int(base_core)/int(hours_6)
score_6 = float(base_core) * (1 - math.pow(float(hours_6)/float(decay_rate), 1/float(v_rate_6)))
print(score_6)

hours_7 = 120
v_rate_7 = int(base_core)/int(hours_7)
score_7 = float(base_core) * (1 - math.pow(float(hours_7)/float(decay_rate), 1/float(v_rate_7)))
print(score_7)

hours_8 = 140
v_rate_8 = int(base_core)/int(hours_8)
score_8 = float(base_core) * (1 - math.pow(float(hours_8)/float(decay_rate), 1/float(v_rate_8)))
print(score_8)

hours_9 = 160
v_rate_9 = int(base_core)/int(hours_9)
score_9 = float(base_core) * (1 - math.pow(float(hours_9)/float(decay_rate), 1/float(v_rate_9)))
print(score_9)


plt.axis([0,180,0,100])
plt.title('График распада', fontsize=20, fontname='Times New Roman')
plt.xlabel('Hours', color='gray')
plt.ylabel('Score',color='gray')
plt.plot([1, 20, 40, 60, 80, 100, 120, 140, 160], [int(score_1), int(score_2), int(score_3), int(score_4), int(score_5), int(score_6), int(score_7), int(score_8), int(score_9)])
plt.grid(True)

plt.show()


