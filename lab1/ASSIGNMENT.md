# Лабораторная № 1. Поиск по каталогу

Напишите консольную программу для поиска по каталогу. Программа запускается командой `python main.py`, принимает команды и завершается командой `exit`.

## Вариант

Параметры программы задаются назначенным вариантом:

```text
данные | поля | обработка | поиск | выдача | подсветка | рейтинг
```


| Параметр  | Значения                                                                                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Данные    | `books-json` — книги; `artworks-csv` — искусство; `airports-csv` — аэропорты; `earthquakes-jsonl` — землетрясения; `chess-json` — дебюты; `exoplanets-csv` — экзопланеты; `papers-jsonl` — статьи |
| Поля      | `title` — заголовок; `all` — все возможные текстовые поля                                                                                                                                         |
| Обработка | `raw` — без изменений; `fold` — без учёта регистра; `clean` — своя очистка                                                                                                                        |
| Поиск     | `substr` — подстрока; `words-all` — все слова; `words-any` — любое слово; `fuzzy-words` — все слова с опечатками; `fuzzy-text` — сходство с текстом поля целиком с опечатками                     |
| Выдача    | `ranked` — все совпадения по релевантности; `top10` — до десяти лучших; `best` — одно лучшее                                                                                                      |
| Подсветка | `plain` — без подсветки; `mark` — выделять совпадения любым заметным способом                                                                                                                     |
| Рейтинг   | `none` — без оценок; `stars` — оценки записей от 1 до 5; `boost` — оценки также влияют на порядок выдачи                                                                                          |


Для `clean` самостоятельно выберите правила очистки. Запрос и текст записей обрабатывайте одинаково.

## Вывод

`show` выводит все загруженные записи со всеми полями, без фильтров и ограничения количества записей. Формат вывода произвольный, можно как в виде таблицы, так и в виде карточек

`search` выводит такой же результат, что и `show`, но только для записей, подходящих под запрос и фильтры. Дополнительно показываются релевантность, оценка пользователя в режимах `stars` и `boost`, итоговые баллы в режиме `boost`. Указываются число найденных и показанных записей и время поиска. В режиме `mark` совпадения выделяются в соответствующих полях карточки.

## Релевантность и оценки

Релевантность вычисляется по запросу и тексту записи. В режимах `none` и `stars` записи сортируются по убыванию релевантности. Формулу выберите самостоятельно и опишите в отчёте.

Для приближённого поиска выберите меру сходства строк от 0 до 1, где 1 означает полное совпадение. `threshold` задаёт минимальное допустимое сходство. Релевантность и сходство могут вычисляться по разным формулам.

Оценку от 1 до 5 ставит пользователь командой `rate`. В режиме `stars` она сохраняется и выводится. В режиме `boost` она даёт прибавку к релевантности при сортировке; формулу прибавки также опишите в отчёте. Релевантность, оценка и итоговые баллы выводятся отдельно. Оценка не может добавить в выдачу запись, не подходящую под запрос или фильтры.

## Команды


| Команда                                   | Действие                                                                |
| ----------------------------------------- | ----------------------------------------------------------------------- |
| `help`                                    | Список команд                                                           |
| `load <файл>`                             | Загрузить данные; сбросить фильтры, порог, последнюю выдачу и оценки    |
| `show`                                    | Вывести все записи карточками                                           |
| `fields`                                  | Показать поля, типы и допустимые фильтры                                |
| `filter add <поле> <оператор> <значение>` | Добавить условие                                                        |
| `filter list`                             | Показать условия с номерами от 1                                        |
| `filter remove <номер>`                   | Удалить условие и перенумеровать остальные                              |
| `filter clear`                            | Удалить все условия                                                     |
| `threshold <число>`                       | Установить порог в интервале (0, 1]; только для приближённого поиска    |
| `search "<запрос>"`                       | Вывести результаты поиска; пустой запрос применяет только фильтры       |
| `save <файл>`                             | Сохранить последнюю показанную выдачу в текстовый файл                  |
| `rate <id> <1..5>`                        | Оценить запись из последней показанной выдачи; только `stars` и `boost` |
| `ratings`                                 | Показать оценки; только `stars` и `boost`                               |
| `exit`                                    | Завершить программу                                                     |




## Фильтры


| Оператор   | Значение       |
| ---------- | -------------- |
| `eq`       | Равно          |
| `ne`       | Не равно       |
| `lt`       | Меньше         |
| `le`       | Не больше      |
| `gt`       | Больше         |
| `ge`       | Не меньше      |
| `contains` | Содержит текст |


- Числовые поля поддерживают `eq`, `ne`, `lt`, `le`, `gt`, `ge`.
- Строковые поля поддерживают `eq`, `ne`, `contains`.
- Логические поля поддерживают `eq`, `ne`; значения — `true` и `false`.
- Все фильтры применяются одновременно, до ограничения количества результатов. Пустое поле не проходит фильтр.
- Изменение настроек действует при следующем `search`.



## Общие требования

- До загрузки данных доступны только `help`, `load`, `exit`.
- Аргументы с пробелами заключаются в кавычки.
- Ошибка команды выводит понятное сообщение и не завершает программу.
- Оценки хранятся в памяти до выхода или новой загрузки, привязаны к ID и сохраняются при смене запроса. Повторная оценка заменяет предыдущую.



## Пример работы

Вариант: `airports-csv | all | fold | words-all | top10 | mark | boost`. В файле `airports.csv` четыре записи; команда `show` показывает их целиком.

```text
$ python main.py
Поиск по каталогу. Команды: help. Выход: exit.


# Загрузка: каждая запись — отдельная карточка со всеми полями.

search> load airports.csv
Загружено записей: 4

search> fields
Поиск по полям: title, city, keywords

Поле          Тип    Фильтры
------------  -----  -----------------
id            str    -
title         str    -
city          str    -
keywords      str    -
country       str    eq ne contains
kind          str    eq ne contains
elevation_ft  float  eq ne lt le gt ge
latitude      float  eq ne lt le gt ge
longitude     float  eq ne lt le gt ge
scheduled     bool   eq ne
url           str    -

eq = равно; ne = не равно; contains = содержит текст.
lt <; le <=; gt >; ge >=. true = да; false = нет.

search> show
Записей: 4

[KBOS] Boston Logan International Airport
  city: Boston
  keywords: General Edward Lawrence Logan International Airport
  country: US
  kind: large_airport
  elevation_ft: 20.0
  latitude: 42.36197
  longitude: -71.0079
  scheduled: true
  url: https://ourairports.com/airports/KBOS/

[NH60] Huff Memorial Airport
  city: New Boston
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/

[US-0960] Tufts Medical Center Heliport
  city: Boston
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/

[EGTE] Exeter International Airport
  city: Exeter, Devon
  keywords: —
  country: GB
  kind: medium_airport
  elevation_ft: 102.0
  latitude: 50.734261
  longitude: -3.413984
  scheduled: true
  url: https://ourairports.com/airports/EGTE/


# Поиск без учёта регистра; совпадения выделены [[так]].

search> search "bOsToN"
Найдено: 3; показано: 3

[KBOS] [[Boston]] Logan International Airport
  city: [[Boston]]
  keywords: General Edward Lawrence Logan International Airport
  country: US
  kind: large_airport
  elevation_ft: 20.0
  latitude: 42.36197
  longitude: -71.0079
  scheduled: true
  url: https://ourairports.com/airports/KBOS/
  Релевантность: 4.00
  Оценка: нет
  Баллы: 4.00

[NH60] Huff Memorial Airport
  city: New [[Boston]]
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/
  Релевантность: 1.00
  Оценка: нет
  Баллы: 1.00

[US-0960] Tufts Medical Center Heliport
  city: [[Boston]]
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/
  Релевантность: 1.00
  Оценка: нет
  Баллы: 1.00

Время поиска: 0.04 мс


# Оставим аэропорты США без регулярных рейсов.

search> filter add country eq US
Добавлен фильтр 1: country = US

search> filter add scheduled eq false
Добавлен фильтр 2: scheduled = false

search> filter list
1. country = US
2. scheduled = false

search> search "Boston"
Найдено: 2; показано: 2

[NH60] Huff Memorial Airport
  city: New [[Boston]]
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/
  Релевантность: 1.00
  Оценка: нет
  Баллы: 1.00

[US-0960] Tufts Medical Center Heliport
  city: [[Boston]]
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/
  Релевантность: 1.00
  Оценка: нет
  Баллы: 1.00

Время поиска: 0.02 мс


# Ошибка не завершает программу. Оценка меняет порядок, но не релевантность.

search> rate US-0960 6
Ошибка: Оценка должна быть целым числом от 1 до 5

search> rate US-0960 5
Оценка: US-0960 — 5/5

search> ratings
US-0960: 5/5

search> search "Boston"
Найдено: 2; показано: 2

[US-0960] Tufts Medical Center Heliport
  city: [[Boston]]
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/
  Релевантность: 1.00
  Оценка: 5/5
  Баллы: 3.50

[NH60] Huff Memorial Airport
  city: New [[Boston]]
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/
  Релевантность: 1.00
  Оценка: нет
  Баллы: 1.00

Время поиска: 0.01 мс

search> save result.txt
Сохранено: result.txt


# show по-прежнему выводит весь файл, даже при активных фильтрах.

search> show
Записей: 4

[KBOS] Boston Logan International Airport
  city: Boston
  keywords: General Edward Lawrence Logan International Airport
  country: US
  kind: large_airport
  elevation_ft: 20.0
  latitude: 42.36197
  longitude: -71.0079
  scheduled: true
  url: https://ourairports.com/airports/KBOS/

[NH60] Huff Memorial Airport
  city: New Boston
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/

[US-0960] Tufts Medical Center Heliport
  city: Boston
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/

[EGTE] Exeter International Airport
  city: Exeter, Devon
  keywords: —
  country: GB
  kind: medium_airport
  elevation_ft: 102.0
  latitude: 50.734261
  longitude: -3.413984
  scheduled: true
  url: https://ourairports.com/airports/EGTE/


# Удалим второй фильтр. Пустой запрос оставляет только фильтрацию.

search> filter remove 2
Фильтр удалён

search> filter list
1. country = US

search> search ""
Найдено: 3; показано: 3

[US-0960] Tufts Medical Center Heliport
  city: Boston
  keywords: —
  country: US
  kind: heliport
  elevation_ft: 230.0
  latitude: 42.349037
  longitude: -71.063223
  scheduled: false
  url: https://ourairports.com/airports/US-0960/
  Релевантность: 0.00
  Оценка: 5/5
  Баллы: 2.50

[KBOS] Boston Logan International Airport
  city: Boston
  keywords: General Edward Lawrence Logan International Airport
  country: US
  kind: large_airport
  elevation_ft: 20.0
  latitude: 42.36197
  longitude: -71.0079
  scheduled: true
  url: https://ourairports.com/airports/KBOS/
  Релевантность: 0.00
  Оценка: нет
  Баллы: 0.00

[NH60] Huff Memorial Airport
  city: New Boston
  keywords: —
  country: US
  kind: small_airport
  elevation_ft: 840.0
  latitude: 42.958877
  longitude: -71.653126
  scheduled: false
  url: https://ourairports.com/airports/NH60/
  Релевантность: 0.00
  Оценка: нет
  Баллы: 0.00

Время поиска: 0.01 мс


# Очистим фильтры и выполним запрос без совпадений.

search> filter clear
Фильтры удалены

search> search "Atlantis"
Найдено: 0; показано: 0

Время поиска: 0.01 мс


# Новая загрузка сбрасывает оценки и настройки.

search> load airports.csv
Загружено записей: 4

search> ratings
Оценок нет

search> filter list
Фильтров нет

search> exit
```



## Отчёт

Загрузите отчёт по лабораторной работе (`README.md` и файлы работы) **обязательно в директорию** `lab1` **вашего собственного репозитория с домашними заданиями, рядом с 01_Basic, 02_Data_Structures, ... (student-xxx)**.