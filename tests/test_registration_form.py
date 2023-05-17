from registration_form.data.users import User, Gender, Subject, Hobbies
from registration_form.pages.registration_page import RegistrationPage


def test_registration_form(browser_start):
    student = User(
        first_name ='Daniil',
        last_name='Moiseenko',
        email='test@test.test',
        gender=Gender.male.value,
        mobile_number='7848488484',
        birthday='07 April,1990',
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
