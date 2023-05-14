from selene import browser, have, command
import os


def test_registration_form():
    browser.config.window_width = 1500
    browser.config.window_height = 1200
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Test')
    browser.element('#lastName').type('Test2')
    browser.element('#userEmail').type('test@test.test')
    browser.element('[for = gender-radio-1]').click()
    browser.element('#userNumber').type('78484884844')
    browser.element('#dateOfBirthInput').perform(command.select_all).type('07 Apr 1990').press_enter()
    browser.element('#subjectsInput').type('te').press_enter()
    browser.element('[for = hobbies-checkbox-2]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + '/Imp.jpg')
    browser.element('#currentAddress').type('Test adress')
    browser.element('#state').click().with_().element('#react-select-3-option-0').click()
    browser.element('#city').click().with_().element('#react-select-4-option-0').click()
    browser.element('#submit').click()

    # Проверяем корректность заполненных полей
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Test Test2', 'Student Email test@test.test',
        'Gender Male', 'Mobile 7848488484',
        'Date of Birth 07 April,1990', 'Subjects Computer Science',
        'Hobbies Reading', 'Picture Imp.jpg',
        'Address Test adress', 'State and City NCR Delhi'
    ))
