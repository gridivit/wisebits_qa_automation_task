from allure_commons._allure import story, feature, title

from wisebits_qa_automation_task.pages.w3schools.try_sql_page import TrySqlPage

@feature("w3school")
@story("try_sql_page")
@title("select all customers where Giovanni Rovelli is Via Ludovico il Moro 22")
def test_giovanni_rovelli(get_webdriver):
    try_sql_page = TrySqlPage(webdriver=get_webdriver)
    try_sql_page.press_button_run_sql()
    results = try_sql_page.get_result()

    giovanni_rovelli = [x for x in results if x['ContactName'] == "Giovanni Rovelli"]

    assert len(giovanni_rovelli) is 1, "Giovanni Rovelli don't found"
    assert giovanni_rovelli[0]['Address'] == 'Via Ludovico il Moro 22', "address is not 'Via Ludovico il Moro 22'"


@feature("w3school")
@story("try_sql_page")
@title("select all customers from london where total customers amound is 6")
def test_london(get_webdriver):
    try_sql_page = TrySqlPage(webdriver=get_webdriver)
    try_sql_page.set_sql_statement("Select * from Customers where city = 'London'")
    try_sql_page.press_button_run_sql()
    results = try_sql_page.get_result()

    assert len(results) == 6, f"result amount customers is {len(results)}"


@feature("w3school")
@story("try_sql_page")
@title("Insert new customer and success select it.")
def test_add_new_line(get_webdriver):
    try_sql_page = TrySqlPage(webdriver=get_webdriver)
    request = "INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country) " \
              "VALUES ('Cardinal', 'Tom B. Erichsen', 'Skagen 21', 'Stavanger', '4006', 'Norway');"
    try_sql_page.set_sql_statement(request)
    try_sql_page.press_button_run_sql()

    try_sql_page.set_sql_statement("Select * from Customers where ContactName = 'Tom B. Erichsen'")
    try_sql_page.press_button_run_sql()

    results = try_sql_page.get_result()

    assert len(results) == 1, f"result amount Tom B. Erichsen is {len(results)}"


@feature("w3school")
@story("try_sql_page")
@title("Update some customer and select check it.")
def test_update_line(get_webdriver):
    try_sql_page = TrySqlPage(webdriver=get_webdriver)
    customer_name = 'customer_name'
    contact_name = 'contact_name'
    address = 'address'
    city = 'city'
    postal_code = 'postal_code'
    country = 'country'

    request = f"""
        UPDATE Customers
        SET 
        CustomerName = '{customer_name}',
        ContactName = '{contact_name}', 
        Address = '{address}',
        City = '{city}',
        PostalCode = '{postal_code}',
        Country = '{country}'
        WHERE CustomerID = 1;
    
    """
    try_sql_page.set_sql_statement(request)
    try_sql_page.press_button_run_sql()

    try_sql_page.set_sql_statement(f"Select * from Customers where ContactName = '{contact_name}'")
    try_sql_page.press_button_run_sql()

    results = try_sql_page.get_result()

    assert len(results) == 1, f"result amount Tom B. Erichsen is {len(results)}"
    assert results[0]['CustomerName'] == customer_name
    assert results[0]['ContactName'] == contact_name
    assert results[0]['Address'] == address
    assert results[0]['City'] == city
    assert results[0]['PostalCode'] == postal_code
    assert results[0]['Country'] == country


@feature("w3school")
@story("try_sql_page")
@title("select Giovanni Rovelli with help like in request.")
def test_like(get_webdriver):
    try_sql_page = TrySqlPage(webdriver=get_webdriver)
    try_sql_page.set_sql_statement("SELECT * FROM Customers WHERE ContactName LIKE 'Giov%';")
    try_sql_page.press_button_run_sql()
    results = try_sql_page.get_result()

    assert len(results) is 1, "Giovanni Rovelli don't found"
    assert results[0]['Address'] == 'Via Ludovico il Moro 22', "address is not 'Via Ludovico il Moro 22'"
