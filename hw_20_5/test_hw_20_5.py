import os
import pytest
from selene import browser, command, have

def test_hw():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Testovich')
    browser.element('#userEmail').type('testemeil@test.com')
    browser.element(f"//label[text()='Male']").click()
    browser.element('#userNumber').type('79998884455')
    browser.element('#dateOfBirthInput').click()
    browser.element(".react-datepicker__year-select").type('1993').click()
    browser.element(".react-datepicker__month-select").element('[value="6"]').click()
    browser.element(".react-datepicker__day--013").click()
    browser.element('#subjectsInput').type('English').press_enter()
    browser.element(f"//label[(text()='Sports')]").click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('test.jpg'))
    browser.element('#currentAddress').type('Earth, Eurasia 4.8.15.22.43')
    # Совершенно не понял как искать данные элементы .element('#react-select-3-option-2')
    browser.element('#state').click().element('#react-select-3-option-2').click()
    browser.element('#city').click().element('#react-select-4-option-0').click()
    #Проверка
    browser.element('#submit').perform(command.js.scroll_into_view).click()
    browser.element('.table-responsive').all('td').even.should(have.exact_texts(f'Test Testovich', 'testemeil@test.com', 'Male', '7999888445', '13 July,1993', 'English', 'Sports', 'test.jpg', 'Earth, Eurasia 4.8.15.22.43', 'Haryana Karnal'))
