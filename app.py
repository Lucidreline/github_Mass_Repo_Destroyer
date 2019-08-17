import config
from selenium import webdriver

# makes an array of every line of the Repos.txt
with open("Repos.txt") as f:
    repos = f.readlines()
# removes whitespace characters like `\n` at the end of each line
repos = [x.strip() for x in repos] 

#Opens up a chrome browser
browser = webdriver.Chrome()

# opens the login screen for github
browser.get("https://github.com/login")

#put in email
browser.find_elements_by_xpath("//*[@id='login_field']")[0].send_keys(config.GITHUB_USERNAME)

#put in password
browser.find_elements_by_xpath("//*[@id='password']")[0].send_keys(config.GITHUB_PASSWORD)

#hit signin
browser.find_elements_by_xpath("//*[@id='login']/form/div[3]/input[7]")[0].click()

# Loops through each repo
for repo in repos:
    browser = webdriver.Chrome()
    browser.get("https://github.com/Lucidreline/" + str(repo) + "/settings")

    #Checks to see if the settings page got pulled up
    # if it hasn't, then the repo does not exist
    if(len(browser.find_elements_by_xpath("//*[@id='options_bucket']/div[1]/h2"))>0):
        # confirms the delete
        browser.find_element_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[4]/details/summary").click()
        browser.find_element_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[4]/details/details-dialog/div[3]/form/p/input").send_keys(repo)
        browser.find_element_by_xpath("//*[@id='options_bucket']/div[8]/ul/li[4]/details/details-dialog/div[3]/form/button").click()
    else:
        #if the settings page was not found
        print("The repo: " + repo + " does not exist!")

    # Closes the browser
    browser.close()
    
    




