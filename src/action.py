from bose import *
from .sign_up import Task as SignUpTask

class Task(SignUpTask):
    def get_data(self):
        return Profile.get_profiles()

    def run(self, driver, data):
        def perform_action():
            """
                Code to perform desired action using Bot
            """ 
            pass

        driver.organic_get("https://target-website.com/auth/sign-up/") 
        perform_action()