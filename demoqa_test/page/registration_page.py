import os
from pathlib import Path
from selene.support.conditions.have import value
from demoqa_test import resource
import pytest
from selene import browser, have, Element
from demoqa_test.resource import upload_picture
from demoqa_test.user import user


class RegistrationPage:

    def __init__(self):
        self.first_name =browser.element('#firstName')
        self.last_name =browser.element('#lastName')
        self.email =browser.element('#userEmail')
        self.gender = browser.all('[name=gender]')
        self.date_of_birth_input = browser.element('#dateOfBirthInput')
        self.month_select = browser.element('.react-datepicker__month-select')
        self.year_select = browser.element('.react-datepicker__year-select')
        self.user_number =  browser.element('#userNumber')
        self.subjects = browser.element('#subjectsInput')
        self.submit_button = browser.element('#submit')
        self.registered_user_data = browser.all('tbody tr td:last-child')
        self.hobbies = browser.all('#hobbiesWrapper label')
        self.test_upload_file = browser.element('#uploadPicture')
        self.current_address = browser.element('#currentAddress')
        self.state = browser.element('#react-select-3-input')
        self.city = browser.element('#react-select-4-input')
        self.submit = browser.element('#submit')
        self.registered_user = browser.all('td')

    def register_user(self, user):
        self.first_name.type(user.first_name)
        self.last_name.type(user.last_name)
        self.email.type(user.email)
        self.gender.element_by(have.value(user.gender)).element('..').click()
        self.user_number.type(user.user_number)
        self.date_of_birth_input.click()
        self.month_select.type(user.month)
        self.year_select.type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        self.subjects.type(user.subjects).press_enter()
        self.hobbies.element_by(have.exact_text(user.hobbies)).click()
        self.test_upload_file.send_keys(os.path.abspath(user.test_upload_file))
        self.current_address.type(user.address)
        self.state.type(user.state).press_enter()
        self.city.type(user.city).press_enter()
        self.submit.click()

    def check_registered_user(self, user):
        self.registered_user.even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            user.email,
            user.gender,
            user.user_number,
            f'{user.day} {user.month},{user.year}',
            user.subjects,
            user.hobbies,
            user.test_upload_file,
            user.address,
            f'{user.state} {user.city}'
        )
        )






