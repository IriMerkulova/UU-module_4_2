def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()

test_function()

inner_function() # Вызовет ошибку, так как inner_function недоступна вне test_function