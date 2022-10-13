запуск тестов: docker run -v {your_dir_for_allure_reports}:/tmp/allure_results oxtiotaz/wise_tests wisebits_tests


докер: https://hub.docker.com/r/oxtiotaz/wise_tests  
тесты: https://pypi.org/project/wisebits-qa-automation-task/


Используя любой язык программирования необходимо написать следующие автотесты для сайта https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_all
1. Вывести все строки таблицы Customers и убедиться, что запись с ContactName равной 'Giovanni Rovelli' имеет Address = 'Via Ludovico il Moro 22'.
2. Вывести только те строки таблицы Customers, где city='London'. Проверить, что в таблице ровно 6 записей.
3. Добавить новую запись в таблицу Customers и проверить, что эта запись добавилась.
4. Обновить все поля (кроме CustomerID) в любой записи таблицы Customersи проверить, что изменения записались в базу.
5. Придумать собственный автотест и реализовать (тут все ограничивается только вашей фантазией).
Заполнить поле ввода можно с помощью js кода, используя объект window.editor.
Требования:
- Для реализации обязательно использовать Selenium WebDriver
- Код автотестов нужно выложить в любой git-репозиторий
- Тесты должны запускаться в docker контейнере