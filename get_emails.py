from selenium import webdriver
import sys, time

browser = webdriver.Chrome()
browser.get('https://mail.qq.com/')

time.sleep(1)
browser_text = browser.find_elements_by_link_text('text')
emailElem = browser.find_element_by_id('u')
emailElem.send_keys('1398998373@qq.com')
passWordElem = browser.find_element_by_id('password')
passWordElem.send_keys('yao52088qingshe')
passWordElem.submit()
login_elem = browser.find_elements_by_id('submit')
login_elem.click()

time.sleep(1)
write_elem = browser.find_elements_by_xpath('/html/body/div[0]')
write_elem.click()

time.sleep(1)
recipent_elem = browser.find_element_by_id('addr')
recipent_elem.send_keys('yao1398998373@qq.com')

time.sleep(1)
frame_elem =browser.find_element_by_xpath('//iframe[@class="qmEditorIfrmEditArea"]')
browser.switch_to.frame(frame_elem)
content_elem =browser.find_element_by_xpath('/html/body')
content_elem.send_keys(browser_text)

browser.switch_to.default_content()
send_elem = browser.find_element_by_xpath('//div[contains(@id,"toolbar")]')
send_elem.click()

browser.find_element_by_xpath('//div[contains(@id,"QMconfirm_QMDialog_confirm")]').click()

time.sleep(1)
browser.close()






