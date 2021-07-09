from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#driver= webdriver.Chrome(executable_path=r"C:\Users\trupt\OneDrive\Desktop\practice\MadLib")
driver= webdriver.Chrome()

driver.get("https://stackoverflow.com/users/signup?ssrc=head&returnurl=/users/story/current%27")
sleep(3)
driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()
driver.find_element_by_xpath('//input[@type="email"]').send_keys("jasmin.jupiter.jam@gmail.com")
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
sleep(4)
driver.find_element_by_xpath('//input[@type="password"]').send_keys("jackrabbit20")
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
sleep(3)
driver.get("https://mail.google.com")
sleep(3)
for i in range(5 ):
    driver.get("https://mail.google.com/mail/u/0/#inbox?compose=new")
    sleep(3)
    driver.find_element_by_class_name("vO").send_keys("sender email")
    driver.find_element_by_class_name("aoT").send_keys("hi :)")
    driver.find_element_by_css_selector("div[aria-label='Message Body']").send_keys("i automated these messages :)")
    driver.find_element_by_xpath("//div[text()='Send']").click()
    sleep(3)
