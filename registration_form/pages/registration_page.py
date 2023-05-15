from selene import browser, have, command

from registration_form import resource


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, value):
        browser.element('#userEmail').type(value)

    def choose_gender(self, value):
        browser.all('[name = gender]').element_by(have.value(value)).element('..').click()

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)

    def choose_birth_date(self, value):
        browser.element('#dateOfBirthInput').perform(command.select_all).type(value).press_enter()

    def choose_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def choose_hobbies(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).click()

    def upload_picture(self, value):
        browser.element('#uploadPicture').set_value(resource.path(value))

    def fill_adress(self, value):
        browser.element('#currentAddress').type(value)

    def choose_state(self, value):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    def choose_city(self, value):
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value)).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_registered(self, full_name, email, gender, mobile_phone, birth_date,
                               subjects, hobbies, picture, current_address, state_and_city_address):
        browser.element('.table').all('td').even.should(have.exact_texts(
            full_name,
            email,
            gender,
            mobile_phone,
            birth_date,
            subjects,
            hobbies,
            picture,
            current_address,
            state_and_city_address,
        )
        )
