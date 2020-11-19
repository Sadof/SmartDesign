# SmartDesign

Тестовое задание выполнено на фреймворке Django.

Создать директорию и перейти в нее.

Запустить виртуальное окружение:
1) virtualenv env
2) env\Scripts\activate.bat
3) cd env
4) git clone https://github.com/Sadof/SmartDesign
5) cd SmartDesign
6) pip install -r requirements.txt
7) Создать в mongoDB таблицу "Product", либо в SmartDesignTest\settings.py в строчке 15 заменить db="Product" на имеющуюся тестовую таблицу.
8) python manage.py runserver

Curl команды:
* Создание нового товара: 
  *<pre>curl --header "Content-Type: application/json" --request POST --data "{\"name\":\"Samsung A3\",\"description\":\"A3\", \"params\": {\"width\":13, \"height\":25}}" http://localhost:8000/api/product</pre>
* Получение товара по параметру:
  * curl "http://localhost:8000/api/product?name=Samsung%20A3" по имени.
  * curl "http://localhost:8000/api/product?param=height&value=25" по параметру.
  * curl "http://localhost:8000/api/product?name=Samsung%20A3&param=width&value=13" по имени и параметру.
* Получение товара по ID.
  * curl "http://localhost:8000/api/product/<id>"  id - можно скопировать из предыдущих запросов. 
