
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
from wxpy import *


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
    for q_num in [5, 7, 8, 15, 17, 19, 21, 22, 23, 25, 30]:
        driver.find_element_by_xpath(f'//*[@id="divquestion{q_num}"]/ul/li[2]/a').click()

    # check the result page
    driver.save_screenshot('填写结果.png')

    # submit this page and close
    submit = driver.find_element_by_id('submit_button')
    time.sleep(60)
    submit.click()
    time.sleep(10)
    driver.quit()

def is_questionary_msg(text):
    return str(text).find('每日一报链接和健康卡通知') != -1

def url_processer(text):
    if not is_questionary_msg(text):
        return

    website_re = r'(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([a-zA-Z0-9\-\.,@?^=%&amp;:/~\+#]*[a-zA-Z0-9\-\@?^=%&amp;/~\+#])?'
    url = re.search(website_re, text).group()
    return url

# In[ ]:
if __name__ == '__main__':
    answer_dict = {}

    with open('./answer-sheet.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            q_num = int(line.split()[0])
            answer = line.split()[-1]
            answer_dict[q_num] = answer

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', type=str, action='store', dest="url",
                        default='./chromedriver',
                        help="if use url, the fill the questionary of the url; else watch the wechat")
    parser.add_argument('-d', '--driver-path', action='store', dest="driver",
                        default='./chromedriver', help="the driver path")
    args = parser.parse_args()
    url = args.url
    driver_path = args.driver

    if not url:
        parse_questionnaire(driver_path, url, answer_dict)
    else:
        def wjx_answer(text, driver_path='./chromedriver'):
            text = str(text)
            print(text)
            url = url_processer(text)
            print(url)

            if url is not None:
                parse_questionnaire(driver_path, url, answer_dict)

        bot = Bot()
        bot.groups(update=True, contact_only=False)

        # watch all groups' messages and process it
        @bot.register(except_self=False)
        def watch_all_group_msg(msg):
            wjx_answer(msg)

        embed()