from registration_form.data.users import User, Gender, Subject, Hobbies
from registration_form.pages.registration_page import RegistrationPage


def test_registration_form(browser_start):
    student = User(
        first_name ='Daniil',
        last_name='Moiseenko',
        email='test@test.test',
        gender=Gender.male.value,
        mobile_number='78484884844',
        birth_day='07 Apr 1990',
        subjects=Subject.computer_science.value,
        hobbies=Hobbies.reading.value,
        picture='Imp.jpg',
        current_address='Test address',
        state='Haryana',
        city='Panipat'
    )

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
    registration_page.fill_adress('Test address')
    registration_page.choose_state('Haryana')
    registration_page.choose_city('Panipat')
    registration_page.submit()

    # THEN
    registration_page.should_have_registered(
        'Daniil Moiseenko',
        'test@test.test',
        'Male',
        '7848488484',
        '07 April,1990',
        'Computer Science',
        'Reading',
        'Imp.jpg',
        'Test address',
        'Haryana Panipat'
    )

# browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
# browser.all('tbody tr').should(have.exact_texts(
#     'Student Name Test Test2', 'Student Email test@test.test',
#     'Gender Male', 'Mobile 7848488484',
#     'Date of Birth 07 April,1990', 'Subjects Computer Science',
#      'Hobbies Reading', 'Picture Imp.jpg',
#      'Address Test adress', 'State and City NCR Delhi'
#  ))
