from botasaurus import *

@browser(
    data = lambda: bt.Profile.get_profiles(random=True),
    block_images=True,
    profile= lambda account: account['username'],
    tiny_profile= True,
)
def perform_action(driver: AntiDetectDriver, account):
    def perform():
        """
            Code to perform desired action using Bot
        """ 
        pass

    driver.organic_get("https://target-website.com/auth/sign-up/") 
    perform()
