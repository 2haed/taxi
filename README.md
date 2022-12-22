# Задание
## Реализовать простое веб-серверное приложение, которое позволяет пользователю по марке автомобиля узнать, в состав каких тарифов каких фирм такси он входит и во сколько обойдется поездка.
## Варианты тарифов с ценами и машинами, входящими в этот тариф.
### Гранд Такси
- Эконом (100p/км): Audi A4, Kia Rio, Hyundai Solaris
- Комфорт (300р/км): Hyundai Solaris, Toyota Camry, KIA
- Optima, Ford Mondeo
- Бизнес (500р/км): BMW 5, BMW 7, Audi A6
### Быстрая Поездка
- Эконом (100p/км): Audi A4, Kia Rio, Hyundai Solaris
- Комфорт (400р/км): Toyota Camry, KIA Optima
### Автодрайв
- Эконом (50р/км): Audi A4, Kia Rio
- Комфорт (250р/км): Hyundai Solaris, KIA Optima, Ford Mondeo
- Комфорт+ (300р/км): Toyota Camry, KIA Optima, Hyundai Elantra
- Бизнес (600р/км): BMW 5, Audi A6, Mercedes-Maybach S-class
# Требования
- Веб-серверное приложение должно быть
реализовано на Python на фреймворке Flask или
Django на выбор (что больше нравится/лучше
знаете)
- Перед началом разработки придумать схему
таблиц БД. Использовать реляционную БД (sql).
Схему приложить отдельно в любом виде
(картинкой, скриншотом, таблицей в документе,
вставить в README проекта)
- Использовать протокол REST, желательно
RESTful
- На странице приложения должен находиться
выпадающий список с марками всех возможных
машин и кнопка «Показать». При нажатии на
кнопку должен выводиться список фирм такси,
тариф, в который входит этот автомобиль, и цену
за км поездки.
  #### Пример 
  Пользователь выбирает в списке
  «Hyundai Solaris» и нажимает на кнопку
  «Показать». После этого выводится информация
  примерно следующего вида:
  ГрандТакси: эконом (100 руб/км), комфорт (300
  руб/км)
  Быстрая Поездка: эконом (100 руб/км)
  Автодрайв: комфорт (250 руб/км)
- Код проекта выложить на github
- Реализовать деплой на heroku или аналогичную
платформу
- Внешний вид оцениваться отдельно не будет
(можно не стараться делать красивые формы,
красивый вывод текста и т.п., главное, чтобы
информация отображалась корректно), но будет
оцениваться работа с данными (как разбили на
таблицы), обратите внимание на этот момент
- Выходные данные: ссылка на гитхаб с кодом
проекта, ссылка на heroku или аналогичную
платформу, схема таблиц БД в любом виде.