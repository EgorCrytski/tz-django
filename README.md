# tz-django
## API
### api root path:
* 'host:port/api/v1/library'

### api paths:
* '/user/\<int\>/'
  > Просмотр юзера
* '/user/\me/'
  > Просмотр информации о себе
* '/user/\<int\>/edit/'
  > Изменение юзера
* '/user/\<int\>/delete/'
  > Удаление юзера
* '/user/all'
  > Список всех юзеров
* '/user/add'
  > Добавляет нового юзера
* '/user/\<int\>/book/\<int\>/detail'
  > Просмотр книги пользователя
* '/user/\<int\>/book/\<int\>/edit'
  > Изменение книги пользователя
* '/user/\<int\>/book/\<int\>/delete'
  > Удаление книги пользователя
* '/book/all'
  > Список всех книг
* '/book/add'
  > Добавляет новую книгу
* '/book/add/myself'
  > Добавить новую книгу себе
* '/token/'
  > Получить токен
* '/toke/refresh/'
  > Обновить токен
* 'token/verify/'
  

## library app
### library app root path:
* 'host:port/library'

### library app paths:
* ' '
  > Выводит список юзеров
* 'user/\<user id\>'
  > Выводит список книг конкретного юзера
* 'user/add'
  > Добавляет нового юзера
* 'book/\<int\>'
  > Выводит информацию о книге
* 'book/add'
  > Добавляет новую книгу текущему пользователю
* 'book/\<int\>/change/'
  > Изменяет информацию о книге
* 'book/\<int\>/delete\'
  > Удаляет книгу
