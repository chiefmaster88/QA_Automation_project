from modules.ui.page_objects.sign_in_page import SingInPage
import pytest

@pytest.mark.ui
def test_check_incorrect_page_obj():
    #створення об'єкту сторінки
    sing_in_page = SingInPage()

    #відкриваємо сторінку
    sing_in_page.go_to()

    #виконуємо спробу увійти в систему гітхаб
    sing_in_page.try_login('page_object@gmail.com', 'wrond password')

    #перевіряємо що назва сторінки така, яку ми очікуємо
    assert sing_in_page.check_title('Sign in to GitHub · GitHub')

    sing_in_page.close()

