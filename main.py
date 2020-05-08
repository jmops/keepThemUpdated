from selenium import webdriver                                  # Imports the webdriver API
from selenium.webdriver.common.keys import Keys                 # Keyboard keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException   # Exceptions
import getpass
from time import sleep                                          # sleep function
from setup import *

######################################################################################################
# A simple python messenger bot 
######################################################################################################
###
# TODO Check if the login was successful, quiting the program, the bot breaks easily
###


# Get the login credentials
def login(driver):
    username = input("Username: ")  #
    password = getpass.getpass()    #
    try:
        WebDriverWait(driver, 20).until(expected_conditions.presence_of_element_located((By.ID, "email")) ) # Waits until the id="email" is present, or 20 seconds. Passing a tuple as a single argument
    except TimeoutException:
        print("ERROR loading the URL")
        driver.quit()
    
    usr = getElementById(driver, "email")
    usr.clear()                                 # Removes anything that has been automatically filled in
    usr.send_keys(username)                     # Enters the username/email
    psw = getElementById(driver, "pass")
    psw.clear()
    psw.send_keys(password, Keys.RETURN)        # Enters the password and presses ENTER
    username = ""
    password = ""


# Keep sending messages in the chat
def keepThemUpdated(driver):
    numberOfLoops = 0
    sleep(15) # Let the chat load

        
    action = ActionChains(driver) # Create an action chain
    action.send_keys(message)
    action.send_keys('.')   #Adds a '.' to hopefully avoid autocompleting names
    action.send_keys(Keys.ENTER)
    
    while True:
        action.perform() # writes the message
        numberOfLoops +=1
        print("Number of messages: ", numberOfLoops, "Message: ", message)
        sleep(intervalInSeconds)   # Intervals


# Get an element with the given ID and return it.
def getElementById(driver, id):
    try:
        element = driver.find_element_by_id(id)
    except NoSuchElementException:                  # If the element could not be found
        print("ERROR, cannot find the id: " + id)
        driver.quit()
    
    return element
################################################################################################## 

driver = webdriver.Firefox()    # Use the firefox webdriver (GeckoDriver)
driver.get(url)                 # Go to the URL

login(driver)
keepThemUpdated(driver)


