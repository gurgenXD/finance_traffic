# Поликлиника "УЗИ 4Д"

### Команды запуска компонент

1. Запустить инфраструктуру для локальной разрабоки
    ```
    docker-compose -f cicd/docker-compose.local.yml up -d
    ```
1. Создать миграцию базы данных
    ```
    python manage.py migrations make "Migration message."
    ```
1. Накатить миграции
    ```
    python manage.py migrations up
    ```
1. Откатить последнюю миграцию
    ```
    python manage.py migrations down
    ```
1. Запусть API
    ```
    python manage.py start api
    ```
1. Отсортировать импорты
    ```
    isort .
    ```
1. Отрефакторить код
    ```
    black .
    ```