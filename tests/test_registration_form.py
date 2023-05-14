from selene import browser, have, command
from registration_form import resource
from tests import conftest


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

    def birth_date_choose(self, value):
        browser.element('#dateOfBirthInput').perform(command.select_all).type(value).press_enter()

    def subject_choose(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def hobbies_choose(self, value):
        browser.all('[for^=hobbies-checkbox]').element_by(have.text(value)).click()


def test_registration_form(browser_start):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Daniil')
    registration_page.fill_last_name('Moiseenko')
    registration_page.fill_email('test@test.test')
    registration_page.choose_gender('Male')
    registration_page.fill_mobile_number('78484884844')
    registration_page.birth_date_choose('07 Apr 1990')
    registration_page.subject_choose('Computer Science')
    registration_page.hobbies_choose('Reading')


    browser.element('#uploadPicture').set_value(resource.path('Imp.jpg'))


    browser.element('#currentAddress').type('Test adress')
    browser.element('#state').click().with_().element('#react-select-3-option-0').click()
    browser.element('#city').click().with_().element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Test Test2', 'Student Email test@test.test',
        'Gender Male', 'Mobile 7848488484',
        'Date of Birth 07 April,1990', 'Subjects Computer Science',
        'Hobbies Reading', 'Picture Imp.jpg',
        'Address Test adress', 'State and City NCR Delhi'
    ))
