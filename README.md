# otx-ioc

# О проекте:
Данный проект дает возможность произвести оценку рейтинга индикатора компрометации, взятого с платформы OTX: 
 https://otx.alienvault.com/api. При написании кода был использован язык программирования Python.

# Установка

Данный проект работает на основе модуля OTXv2. Об этом модуле подробней можно прочитать по этой ссылке: https://github.com/AlienVault-OTX/OTX-Python-SDK

Для установки Вы можете воспользоваться одним из следующих способов:

1. Клонировать предложенный репозиторий
2. Установить необходимое модули самостоятельно. Для этого используйте следующую команду: ``` pip install  ```   
3. Для корректной работы слудует установить несколько модулей: ``` OTXv2, IndicatorTypes, datetime, timedelta, math, matplotlib.pyplot ```
4. Интегрировать код в Ваш редактор кода.
5. Запустить.

 
# Обяснение работы кода:

В начале импортируем все необходимые модули:
```python
from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes
from datetime import datetime, timedelta
import math
import datetime
import matplotlib.pyplot as plt
```
Для того, чтобы тянуть индикаторы с OTX, используем личный API-ключ, и уникальный id выбранного индикатора. 

```python
otx = OTXv2("8c3b1fd2add0a2325e7edd39eeb9a0e7cd577238a65fc83f67c4b1d2c08ee625")
# Get all the indicators associated with a pulse
indicators = otx.get_pulse_indicators("606d75c11c08ff94089a9430")
```
> Личный API-ключ можно получить после регистрации на OTX

Выводим информацию об индикаторе, его ip-адрес, тип, название и дату создания:

```python
for indicator in indicators:
    print(indicator["indicator"] + " ; " + indicator["type"] + " ; " + indicator["title"] + " ; " + indicator["created"] + " ; ")

# Get everything OTX knows about google.com
otx.get_indicator_details_full(IndicatorTypes.DOMAIN, "google.com")
```
Для высчитывания оценки рейтинга индикатора потребуются следующие переменные: ``` базовая оценка, время, которое прошло с момента, когда индикатор был замечен последний раз, скорость затухания и скорость распада.

Базовую оценку пользователь вводит самостоятельно, самостоятельно:

```python
base_core = input("Введите значение от 0 до 100: ")
```
Высчитываем время, прошедшее с момента, когда индикатор был замечен в последний раз, и переводим в часы:

```python
now = datetime.datetime.now()
print("Текущая дата: ", now)

last_ind = datetime.datetime(2021, 5, 30, 10, 59, 2)
print("Дата последнего замеченного индикатора: ", last_ind)

delta = now - last_ind
print("Время, прошедшее с начала последнего замеченного индикатора: ", delta)

seconds = delta.total_seconds()
hours = round(seconds // 3600)
print("В часах: ", hours)
```
Далее высчитываем скорость затухания, и находим оценку рейтинга компрометации:


```python
v_rate = int(base_core)/int(hours)
print("Скорость затухания: ", round(v_rate, 2))

decay_rate = 7*24
score = float(base_core) * (1 - math.pow(float(hours)/float(decay_rate), 1/float(v_rate)))
score_s = round(score, 2)
print("Оценка рейтинга индикатора: ", score_s)
```

Чтобы изобразить график распада, будем переодически менять время:


```python
plt.axis([0,180,0,100])
plt.title('График распада', fontsize=18, fontname='Times New Roman')
plt.xlabel('Hours', color='gray')
plt.ylabel('Score',color='gray')
plt.plot([1, 20, 40, 60, 80, 100, 120, 140, 160, 170], [int(score_1), int(score_2), int(score_3), int(score_4), int(score_5), int(score_6), int(score_7), int(score_8), int(score_9), int(score_10)])
plt.grid(True)

plt.show()
```
Если все выполнено правильно, программа должна представить график распада.
