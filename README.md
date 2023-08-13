# severstal

«Есть набор фотографий в папке, в количестве 100 единиц.
Необходимо в коде на Python в отдельном потоке забирать фотографии из папки и складывать их в очередь в Redis.
В другом потоке извлекать из очереди фотографии и записывать при извлечении в бд Postgres в таблицу,
где два поля: время записи и размер байт изображения.
Дополнительные инструменты и подходы к решению задачи на усмотрение кандидата.»

## реализация модуля сохранения в Redis
1. Файл конфигов
   1. Логин пароль к редис
   2. Логин пароль к постгре
   3. Путь до папки с фотографиями
2. Уметь считывать фотографии из папки
3. Уметь подключаться к редису
4. Нужно уметь писать в очередь редиса

## реадизация модуля сохранения данных в постгрю
1. Читать данные из редиса 
2. Писать данные в постгрес

Паралелить на потоках