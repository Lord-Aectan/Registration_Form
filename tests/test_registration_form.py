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


def test_registration_form(browser_start):
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Daniil')
    registration_page.fill_last_name('Moiseenko')

    browser.element('#userEmail').type('test@test.test')
    browser.element('[for = gender-radio-1]').click()
    browser.element('#userNumber').type('78484884844')
    browser.element('#dateOfBirthInput').perform(command.select_all).type('07 Apr 1990').press_enter()
    browser.element('#subjectsInput').type('Computer Science').press_enter()
    browser.element('[for = hobbies-checkbox-2]').click()
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
