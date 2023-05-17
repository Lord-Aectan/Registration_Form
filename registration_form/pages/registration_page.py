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
        browser.element('#dateOfBirthInput').perform(command.select_all).type(student.birth_day).press_enter()


        for subject in student.subjects:
            browser.element('#subjectsInput').send_keys(subject).press_tab()
        for hobby in student.hobbies:
            browser.all('#hobbiesWrapper .custom-checkbox').element_by(
                have.exact_text(hobby)
            ).click()

        browser.element('#uploadPicture').send_keys(
            resource.path(student.picture)
        )

        browser.element('#currentAddress').send_keys(student.current_address)
        browser.element('#state').perform(command.js.scroll_into_view)
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.state)
        ).click()
        browser.element('#city').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(student.city)
        ).click()
        browser.element('#submit').press_enter()

    def should_have_registered(self, student):
        full_name = f'{student.first_name} {student.last_name}'
        birth_day = f'{student.birth_day}'
        subjects = ', '.join(student.subjects)
        hobbies = ', '.join(student.hobbies)
        state_and_city = f'{student.state} {student.city}'

        browser.all('tbody tr').even.should(have.exact_texts(
            full_name,
            f'{student.email}',
            f'{student.gender}',
            f'{student.mobile_number}',
            f'{birth_day}',
            f'{subjects}',
            f'{hobbies}',
            f'{student.picture}',
            f'{student.current_address}',
            f'{state_and_city}'
        )
        )

   # def should_have_registered(self, full_name, email, gender, mobile_phone, birth_date,
   #                            subjects, hobbies, picture, current_address, state_and_city_address):
   #     browser.element('.table').all('td').even.should(have.exact_texts(
   #         f'{full_name}',
   #         f'{email}',
   #         f'{gender}',
   #         f'{mobile_phone}',
   #         f'{birth_date}',
   #         f'{subjects}',
   #         f'{hobbies}',
   #         f'{picture}',
   #         f'{current_address}',
   #         f'{state_and_city_address}',
   #     )
   #     )
