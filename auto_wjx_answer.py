
# coding: utf-8

# In[1]:
# get_ipython().system('pip install selenium')


# In[2]:


import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import re
from datetime import datetime


# In[3]:


# fill the first 4 questions
def answer_personal_questions(driver, grade, stunum, name, dormitory):
    grade_choice = driver.find_element_by_xpath('//*[@id="divquestion1"]/ul/li[{}]/a'.format(grade))
    grade_choice.click()

    stunum_input = driver.find_element_by_id('q2')
    stunum_input.clear()
    stunum_input.send_keys(stunum)

    name_input = driver.find_element_by_id('q3')
    name_input.clear()
    name_input.send_keys(name)

    dormitory_input = driver.find_element_by_id('q4')
    dormitory_input.clear()
    dormitory_input.send_keys(dormitory)


# In[4]:


def parse_questionnaire(driver_path, url, asnwer_dict):
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)

    # checked if this questionnaire is finished
    try:
        driver.execute_script('window.parent.PDF_close()')
    except:
        pass

    answer_personal_questions(driver, answer_dict[1], answer_dict[2], answer_dict[3], answer_dict[4])

    ## fill the last questions for people have no connnection with hubei
    for q_num in [5, 7, 8, 15, 17, 19, 21, 22, 23, 28]:
        driver.find_element_by_xpath(f'//*[@id="divquestion{q_num}"]/ul/li[2]/a').click()

    # check the result page
    driver.save_screenshot('填写结果.png')

    # submit this page and close
    submit = driver.find_element_by_id('submit_button')
    submit.click()
    # driver.quit()


# In[ ]:


if __name__ == '__main__':
    answer_dict = {}

    with open('./answer-sheet.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            q_num = int(line.split()[0])
            answer = line.split()[-1]
            answer_dict[q_num] = answer

    parser = argparse.ArgumentParser()
    parser.add_argument('url', type=str,
                        help="the questionary website")
    parser.add_argument('-d', '--driver-path', action='store', dest="driver",
                        default='./chromedriver', help="the driver path")
    args = parser.parse_args()
    url = args.url
    driver_path = args.driver

    parse_questionnaire(driver_path, url, answer_dict)
