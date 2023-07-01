from bose.account_generator import AccountGenerator, Country
from bose.temp_mail import TempMail
from bose import *

class Task(BaseTask):
    task_config = TaskConfig(
            # prompt_to_close_browser=True,
            # change_ip=True,
        )

    def get_browser_config(self, data):
        return BrowserConfig(
                profile=data['username'], 
                is_tiny_profile=True,
            )

    def get_data(self):
        accounts = AccountGenerator.generate_accounts(3, country=Country.IN)
        return accounts

    def run(self, driver, account):
        name = account['name']
        email = account['email']
        username = account['username']
        password = account['password']

        def sign_up():
            """
            Sample Code to sign up in a typical sign up form. Adjust as Necessary to make it work. 
            """
            name_input = driver.get_element_or_none_by_selector(
                'form input[name="name"]', Wait.VERY_LONG)

            email_input = driver.get_element_or_none_by_selector(
                'form input[type="email"]', Wait.VERY_LONG)

            password_input = driver.get_element_or_none_by_selector(
                'form input[type="password"]', Wait.VERY_LONG)

            sign_up_button = driver.get_element_or_none_by_selector(
                'form *[type="submit"]', Wait.VERY_LONG)

            name_input.send_keys(name)
            driver.short_random_sleep()

            email_input.send_keys(email)
            driver.short_random_sleep()

            password_input.send_keys(password)
            driver.short_random_sleep()
            
            sign_up_button.click()

        def confirm_email():
            """
            Sample Code to confirm email in a typical email verification email. Adjust as Necessary to make it work. 
            """
            link = TempMail.get_email_link_and_delete_mailbox(email)
            driver.get(link)

        def input_on_board_details():
            # Write Code here to enter onboarding details if they are asked by the target website.
            pass
        
        def assert_account_created():
            """
            This function asserts account creation by checking that the success text is displayed or that the current page url is the desired one. 

            To check for success text use code like below:
                driver.get_element_or_none_by_text_contains("Success", wait=None)

            To check for arrival in success page use code like below:
                driver.is_in_page('target-website.com/auth/success/', wait=Wait.LONG, raise_exception=True)
            
                
            If you don't want to check for success page, leave it blank.
            """
            pass

        driver.organic_get("https://target-website.com/auth/sign-up/") 
        
        sign_up()

        confirm_email()
        
        input_on_board_details()

        assert_account_created()

        Profile.set_profile(account)