import pytest
from future.backports.http.cookiejar import month
from selene import browser, command, have
from demoqa_test import resource
from demoqa_test.page import registration_page
from demoqa_test.page.registration_page import RegistrationPage
from demoqa_test.model.conftest import open_browser
from demoqa_test.user.user import User


def test_registration(open_browser):
    registration_page = RegistrationPage()
    user = User(
        first_name='John',
        last_name='Doe',
        email='john.die@gmail.com',
        gender='Male',
        user_number='8999888777',
        year = '1990',
        month = 'January',
        day = '01',
        subjects='English',
        hobbies='Sports',
        test_upload_file='test.jpg',
        address='Earth, Moscow',
        state='Haryana',
        city='Karnal'
    )

    #Заполнение формы
    registration_page.register_user(user)

    # Проверка данных в таблице
    registration_page.check_registered_user(user)