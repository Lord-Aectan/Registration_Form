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
        browser.all('[id^=react-select][id*=option]').element_by(have.text(value))

    def submit(self):
        browser.element('#submit').click()


def test_registration_form(browser_start):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Daniil')
    registration_page.fill_last_name('Moiseenko')
    registration_page.fill_email('test@test.test')
    registration_page.choose_gender('Male')
    registration_page.fill_mobile_number('78484884844')
    registration_page.choose_birth_date('07 Apr 1990')
    registration_page.choose_subject('Computer Science')
    registration_page.choose_hobbies('Reading')
    registration_page.upload_picture('Imp.jpg')
    registration_page.fill_adress('Test adress')
    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')
    registration_page.submit()


    # THEN
   # browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
   # browser.all('tbody tr').should(have.exact_texts(
   #     'Student Name Test Test2', 'Student Email test@test.test',
   #     'Gender Male', 'Mobile 7848488484',
   #     'Date of Birth 07 April,1990', 'Subjects Computer Science',
  #      'Hobbies Reading', 'Picture Imp.jpg',
  #      'Address Test adress', 'State and City NCR Delhi'
  #  ))
