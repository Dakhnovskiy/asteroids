# asteroids
Catalog of asteroids(API)

## TODO
* tests
* readme

## Заупуск приложения
`docker-compose up --build`


## Исходное задание:
Реализовать сервис (API) для работы с каталогом астероидов.

* Пользователи могут загружать фотографии астероидов
    * Для каждой фотографии пользователи указывают:
        * дату и время, когда сделана фотография
        * название одного или нескольких астероидов, которые попали на фотографию
    * Сервис должен валидировать названия астероидов (по каталогу NASA)

* Сервис должен отдавать информацию об астероиде по его имени. В информации об астероиде должны присутствовать список URL фотографий, если они были загружены для этого астероида. 

    * Информацию об астероидах можно взять из API  https://api.nasa.gov/

* Реализовать возможность регистрации в сервисе (получение токена)
* Реализовать возможность добавления астероидов в закладки
