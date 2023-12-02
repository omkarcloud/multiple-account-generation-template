
from botasaurus import *

@browser(
    data = lambda: bt.generate_user(3, country=bt.Country.IN),
    block_images=True,
    profile= lambda account: account['username'],
    tiny_profile= True,
    output=None,
)
def create_accounts(driver: AntiDetectDriver, account):
    name = account['name']
    email = account['email']
    username = account['username']
    password = account['password']

    def sign_up():
        """
        Sample Code to sign up in a typical sign up form. Adjust as Necessary to make it work. 
        """
        name_input = driver.get_element_or_none_by_selector(
        'form input[name="name"]', bt.Wait   .VERY_LONG)

        email_input = driver.get_element_or_none_by_selector(
        'form input[type="email"]', bt.Wait   .VERY_LONG)

        password_input = driver.get_element_or_none_by_selector(
        'form input[type="password"]', bt.Wait   .VERY_LONG)

        sign_up_button = driver.get_element_or_none_by_selector(
        'form *[type="submit"]', bt.Wait   .VERY_LONG)

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
        link = bt.TempMail.get_email_link_and_delete_mailbox(email)
        driver.get(link)

    def input_on_board_details():
        # Write Code here to enter onboarding details if they are asked by the target website.
        pass
    
    def assert_account_created():
        """
        This function asserts account creation by checking that the success text is displayed or that the current page url is the desired one. 

        To check for success text use code like below:
        driver.get_element_or_none_by_text_contains("Success", bt.Wait   =None)

        To check for arrival in success page use code like below:
        driver.is_in_page('target-website.com/auth/success/', bt.Wait   =bt.Wait   .LONG, raise_exception=True)
        
        
        If you don't want to check for success page, leave it blank.
        """
        pass

    driver.organic_get("https://target-website.com/auth/sign-up/") 
    
    sign_up()

    confirm_email()
    
    input_on_board_details()

    assert_account_created()

    bt.Profile.set_profile(account)