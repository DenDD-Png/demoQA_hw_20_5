import os
from pathlib import Path

from demoqa_test import resource
import pytest
from selene import browser, have, Element

from demoqa_test.resource import upload_picture


class RegistrationPage:

    def __init__(self):
        self.submit_button = browser.element('#submit')
        self.registered_user_data = browser.all('tbody tr td:last-child')

    def first_name(self, value):
        browser.element('#firstName').type(value)

    def last_name(self, value):
        browser.element('#lastName').type(value)

    def email(self, value):
        browser.element('#userEmail').type(value)

    def gender(self, value):
        browser.element(f"//label[text()='Male']").click()

    def user_number(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month).click()
        browser.element('.react-datepicker__year-select').type(year).click()
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def subjects(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def hobbies(self, value):
        browser.element(f"//label[contains(text(), '{value}')]").click()

    def test_upload_file(self, value):
        upload_picture(value)

    def current_address(self, value):
        browser.element('#currentAddress').type('Earth, Eurasia 4.8.15.22.43')

    def state(self, value):
        browser.element('#state').click().element('#react-select-3-option-2').click()

    def city(self, value):
        browser.element('#city').click().element('#react-select-4-option-0').click()

    def submit(self):
        self.submit_button.click()

    def should_have_registered_user_with(
            self,
            full_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            state_and_city
    ):
        self.registered_user_data.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile,
            date_of_birth,
            subjects,
            hobbies,
            picture,
            address,
            state_and_city
        ))
















