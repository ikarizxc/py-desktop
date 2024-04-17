
### Файлы с данными:

###### competitors2.json - спортсмены с указанием нагрудного номера, имени и фамилии
###### results_RUN.txt - результаты первой попытки




Время приходит в формате «нагрудный_номер start ЧЧ:ММ:СС,дст» и «нагрудный_номер finish ЧЧ:ММ:СС,дст».


### Задание:
Написать программу с графическим интерфейсом, используя библиотеку PySide6 и язык разметки QML.
В интерфейсе должны быть следующие элементы:
1. Кнопки для загрузки файлов, которые открывают диалоговые окна выбора файла. (Для загрузки competitors2.json и results_RUN.txt)
2. Кнопка которая запускает вычисления (считает результаты спортсменов)
3. Кнопка для сохранения Json файла с результатами
4. Таблица, которая заполняется результатами спортсменов.


Что нужно вывести в таблицу:

| Занятое место | Нагрудный номер | Имя | Фамилия | Результат |
| --- | --- | --- | --- | --- |
| 1 | 132 | Иван | Иванов | 01:02,32 |
| 2 | 222 | Петр | Иванов | 01:03,00 |
| 3 | 331 | Клим | Петров | 01:04,10 |
| 4 | 2	| Андрей | Сидоров | 01:05,98 |

Пример того как должен выглядеть Json, который сохраняется по нажатию кнопки.
```json
{
    "1": {
        "Нагрудный номер": "132",
        "Имя": "Иван",
        "Фамилия": "Иванов",
        "Результат": "01:02,32"
    },
    "2": {
        "Нагрудный номер": "222",
        "Имя": "Петр",
        "Фамилия": "Иванов",
        "Результат": "01:03,00"
    },
    "3": {
        "Нагрудный номер": "331",
        "Имя": "Клим",
        "Фамилия": "Петров",
        "Результат": "01:04,10"
    },
    "4": {
        "Нагрудный номер": "2",
        "Имя": "Андрей",
        "Фамилия": "Сидоров",
        "Результат": "01:05,98"
    }
}
```

Задание выполнять в этом же репозитории в ветке "dev". 
Ответ на задание присылать в пулреквест в ветку main. В реквесте указать ваши контактные данные данные.
Язык программирования Python, версия 3.9 - 3.11. Файл из которого происходит запуск программы должен называться main.py

Крайний срок выполнения задания воскресенье 23:59 по Новосибирскому времени. Если вы не успели и доступа на запись в репозиторий нет - не надо делать в своем репозитории и присылать PR, перезапросите ссылку на новый у HR.

Для решения задачи необходимо использовать только встроенные средства/модули языка программирования и библиотеку PySide6.
