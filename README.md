# Прогноз погоды с сайта https://m3o.com/
Описана скрипт для обращения к API сайта, предоставляющего прогноз погоды

## Первичная настройка 
#### Требования:
- интерпретатор python 3.8
- установка (при их отсутствии) модулей `typing`, `requests` (пример в командной строке: `pip install typing`)
#### Дополнительно:
- при наличии необходимости визуализировать результат работы скрипта - раскомментировать стр. 151 в исполняемом файле WEATHER.py
- при отсутствии необходимости визуализации - продолжить работу (по факту завершения работы обсуждаемого скрипта) с переменной weather_forecast (стр.148), в котоую будет возвращена структура DTO со схемой:
тип `dict`, пример: 
`{'response_location': 'location_name', 'list_dates': {'YYYY-MM-DD HH:MM': any_int}}`
- при наличии необходимости завести аккаунт на сайте https://m3o.com/ и получить токен (лимит 1000 запросов к API) для того, чтобы вставить его после строки `Bearer` (стр. 8 в исполняемом файле) или пользоваться существующим кодом (токен там уже имеется; остаток по лимиту ~900 запросов к API)

## Запуск скрипта
- В командной строке, перейдя в директорию с исполняемым файлом, выполнить команду:  `python WEATHER.py`
- Средствами сторонних IDE: открыть файл `WEATHER.py`, нажать на кнопку Run или аналогичную по функционалу

## Выполнение
В ходе выполнения скрипта в терминале будут воспроизведены несколько диалогов с заранее предусмотренными вариантами ответов. Необходимо, следуя инструкции:
- выбрать один из двух режимов, нажатием на кнопку 1 или 2  (`Текущая погода` или `Прогноз погоды (до 10 дней)`)
- указать город определения прогноза погоды (название города необходимо ввести латиницей; можно вводить заглавными или строчными буквами - это не важно)
- на 3-м шаге, в случае, если в 1-м диалоговом вопросе был выбран режим `2`, а именно `Прогноз погоды (до 10 дней)`, потребуется ввести кол-во дней, на которые необходимо получить прогноз (ввести число от 1 до 10)
