## ISSUE-01
 
В этой директории протестирована функция $\textit{encode()}$ с помощью doctest.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-01
* Запустить файл `test_morse.py`, используя команду `python3 -m doctest -v -o ELLIPSIS test_morse.py` или просто запустить `test_morse.py`.
 

## ISSUE-02
 
В этой директории протестирована функция $\textit{decode()}$ с помощью `pytest.mark.parametrize`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-02
* Запустить pytest, используя команду `pytest -v`
 

## ISSUE-03
 
В этой директории протестирована функция $\textit{fit_transform()}$ с помощью `unittest`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-03
* Запустить `unittest`, используя команду $\newline$ $\textbf{python3 -m unittest -v test_one_hot.py } \newline$
или просто запустить файл `test_one_hot.py`
 
## ISSUE-04
 
В этой директории протестирована функция $\textit{fit_transform()}$ с помощью `pytest`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-04
* Запустить `pytest`, используя команду $\newline$ $\textbf{pytest -v}. \newline$ 

## ISSUE-05
 
В этой директории протестирована функция $\textit{what_is_year_now()}$ с помощью `unittest.mock`, `pytest` и `pytest-cov`.
 
#### Run
 
Для запуска необходимо:
* Склонировать проект
* Зайти в директорию issue-05
* Запустить `pytest`, используя команду $\newline$ $\textbf{python3 -m pytest -v test_api.py } \newline$
* Запустить `pytest-cov`, используя команду $\newline$ $\textbf{python3 -m pytest -q test_api.py --cov . --cov-report html} \newline$ 

 
