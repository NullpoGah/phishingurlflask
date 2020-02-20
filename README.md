# Phishing-URL-Detector
Лучше всего использовать окружение miniconda https://docs.conda.io/en/latest/miniconda.html
(На винде лучше использовать anaconda powershell)
создать новое окружение питону:
conda create --name env
активировать
conda activate env
conda install python
Установить все библиотеки:
pip install -r requirements.txt
Запуск сервера:
python server.py

GET ЗАПРОСЫ:
127.0.0.1:5000/result?name=URL
