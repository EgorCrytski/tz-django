# tz-django
## API
### api root path:
* 'host:port/api/v1/library'

### api paths:
* '/user/<int>/detail/'
  > Просмотр юзера
* '/user/<int>/edit/'
  > Изменение юзера
* '/user/<int>/delete/'
  > Удаление юзера
* '/user/all'
  > Список всех юзеров
* '/user/add'
  > Добавляет нового юзера
* '/book/<int>/detail'
  > Просомтр книги
* '/book/<int>/edit'
  > Изменение книги
* '/book/<int>/delete'
  > Удаление книги
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
