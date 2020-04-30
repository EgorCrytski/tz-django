# tz-django
## API
### api root path:
* 'host:port/api/v1/library'

### api paths:
* '/user/detail/<int>'
  > Удаление, изменение юзера
* '/user/all'
  > Список всех юзеров
* '/user/add'
  > Добавляет нового юзера
* '/book/detail/<int>'
  > Удаление, изменение книги
* '/book/all'
  > Список всех книг
* '/book/add'
  > Добавляет новую книгу
## library app
### library app root path:
* 'host:port/library'

### library app paths:
* ' '
  > Выводит список юзеров
* 'user/<user id>'
  > Выводит список книг конкретного юзера
* 'user/add'
  > Добавляет нового юзера
* 'book/<book id>'
  > Выводит информацию о книге
* 'book/add'
  > Добавляет новую книгу текущему пользователю
* 'book/change/<book id>'
  > Изменяет информацию о книге
* 'book/delete/<book id>'
  > Удаляет книгу