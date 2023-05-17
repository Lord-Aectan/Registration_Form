from selene import browser, have, command
from registration_form import resource

class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def register(self, student):
        # WHEN
        browser.element('#firstName').set(student.first_name)
        browser.element('#lastName').set(student.last_name)
        browser.element('#userEmail').set(student.email)
        browser.element(f'[name=gender][value={student.gender}]+label').click()
        browser.element('#userNumber').set(student.mobile_number)
        browser.element('#dateOfBirthInput').perform(command.select_all).type(student.birthday).press_enter()

        for subject in student.subjects:
            browser.element('#subjectsInput').send_keys(subject).press_tab()
        for hobby in student.hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(have.text(hobby)).click()

        browser.element('#uploadPicture').send_keys(resource.path(student.picture))

        browser.element('#currentAddress').send_keys(student.current_address)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(student.state)).click()

        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(have.text(student.city)).click()
        browser.element('#submit').click()

    def should_have_registered(self, student):
        full_name = f'{student.first_name} {student.last_name}'
        birthday = f'{student.birthday}'
        subjects = ', '.join(student.subjects)
        hobbies = ', '.join(student.hobbies)
        state_and_city = f'{student.state} {student.city}'

        browser.all('tbody tr').should(have.exact_texts(
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.mobile_number}',
            f'Date of Birth {birthday}',
            f'Subjects {subjects}',
            f'Hobbies {hobbies}',
            f'Picture {student.picture}',
            f'Address {student.current_address}',
            f'State and City {state_and_city}')
        )

