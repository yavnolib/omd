# AAA Homeworks

# HW1
### About
This repository is about the free use of chatgpt technology using various telegram bots.  As an example of efficiency, we consider the option of adding a story about a poor duck that went to a bar to drink various drinks.  By answering interactive questions you can influence the course of the story that chatgpt comes up with.

### Run
To run this code on your computer, install pytelegrambotapi and telethon.  
```
pip install pyTelegramBotAPI
pip install telethon
```
Next, follow all the instructions that are specified in the head docstring of the omd.py file.
Good luck and have fun! 

# HW2
### About
There is a csv file with a report on the company's employees. It contains the following data:

Full name
Department
Team within the department
Position held
Quarterly assessment – review result
Current salary

### Structure
* Corp_Summary.csv - example of csv input file
* script.py - program file

### Program operating modes
1. Display the hierarchy of commands in an understandable form, i.e. department and all teams that are part of it
2. Display a summary report by department: name, number, salary range in the form of min – max, average salary
3. Save the summary report from the previous paragraph as a csv file. In this case, it is not necessary to first call the command from step 2

# HW3
### About
Implementation of the CountVectorizer class for text vectorization. Can be useful for natural language processing tasks.

# HW4
## ISSUE-01
 

В этой директории протестирована функция `encode()` с помощью `doctest`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-01

* Запустить файл `test_morse.py`, используя команду `python3 -m doctest -v -o ELLIPSIS test_morse.py` или просто запустить `test_morse.py`.
 

## ISSUE-02
 
В этой директории протестирована функция `decode()` с помощью `pytest.mark.parametrize`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-02

* Запустить pytest, используя команду `pytest -v`
 

 

## ISSUE-03
 
В этой директории протестирована функция `fit_transform()` с помощью `unittest`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-03

* Запустить `unittest`, используя команду `python3 -m unittest -v test_one_hot.py`
или просто запустить файл `test_one_hot.py`
 
 
## ISSUE-04
 
В этой директории протестирована функция `fit_transform()` с помощью `pytest`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-04

* Запустить `pytest`, используя команду `pytest -v`. 

## ISSUE-05
 
В этой директории протестирована функция `what_is_year_now()` с помощью `unittest.mock`, `pytest` и `pytest-cov`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-05
* Запустить `pytest`, используя команду `python3 -m pytest -v test_api.py`.
* Запустить `pytest-cov`, используя команду `python3 -m pytest -q test_api.py --cov . --cov-report html`.

 # HW-advanced-1
Описан класс, который наследуется от Mixin и динамически создает атрибуты экземпляра класса из атрибутов JSON-объекта. 

* К атрибутам любой вложенности можно обращаться через точку
* К названиям атрибутов, являющихся ключевыми словами python, в конце названия добавляется "_"
* Содержит текстовое представление объектов класса Advert, с использованием ColorizeMixin - цветного вывода в консоль
