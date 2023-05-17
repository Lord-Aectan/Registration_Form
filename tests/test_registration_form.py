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
        subjects=[Subject.computer_science.value],
        hobbies=[Hobbies.reading.value],
        picture='Imp.jpg',
        current_address='Test address',
        state='Haryana',
        city='Panipat'
    )

    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.should_have_registered(student)


# browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
# browser.all('tbody tr').should(have.exact_texts(
#     'Student Name Test Test2', 'Student Email test@test.test',
#     'Gender Male', 'Mobile 7848488484',
#     'Date of Birth 07 April,1990', 'Subjects Computer Science',
#      'Hobbies Reading', 'Picture Imp.jpg',
#      'Address Test adress', 'State and City NCR Delhi'
#  ))