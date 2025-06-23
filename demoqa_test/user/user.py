import dataclasses

@dataclasses.dataclass()
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    user_number: str
    fill_date_of_birth: str
    subjects: str
    hobbies: str
    test_uplod




    def hobbies(self, value):
        browser.element(f"//label[contains(text(), '{value}')]").click()

    def upload_file(self, value):
        upload_picture(value)

    def current_address(self, value):
        browser.element('#currentAddress').type('Earth, Eurasia 4.8.15.22.43')

    def state(self, value):
        browser.element('#state').click().element('#react-select-3-option-2').click()

    def city(self, value):
        browser.element('#city').click().element('#react-select-4-option-0').click()