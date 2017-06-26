# -*- coding: utf-8 -*-
__author__ = 'bobby'

import time
import sys
import os

reload(sys)
sys.setdefaultencoding('utf-8')

from selenium import webdriver
from scrapy.selector import Selector
import requests


def pre_login(name, password):
    if not (name and password):
        print "login name or password cannot be empty!"
        exit()
    if '@' not in name:
        print "please use email as login name!"
        exit()
        
    browser.get('https://auth.udacity.com/sign-in?next=https%3A%2F%2Fclassroom.udacity.com%2Fauthenticated')
    time.sleep(1)
    browser.find_element_by_css_selector("input[type='email']").send_keys(name)
    time.sleep(1)
    browser.find_element_by_css_selector("input[type='password']").send_keys(password)
    time.sleep(1)
    browser.find_element_by_css_selector("input[type='password']").click()
    print "点击登陆按钮！"
    time.sleep(20)
    #browser.find_element_by_css_selector("form button[type='button']").click()


def get_all_titles(selector):
    x = selector.css('div > ol > li a')
    lessons = []
    for i in x:
        try:
            url = 'https://classroom.udacity.com' + i.css('::attr(href)').extract_first()
            name = i.css('::attr(title)').extract_first().replace('.', ' -')
        except:
            continue
        lessons.append((url, name))
    return lessons



            

def get_all_vtt_urls(url):
    
    def get_vtt_urls(lessons, filename):
        for i in lessons:
            url = i[0]
            name = i[1]
            browser.get(url)
            time.sleep(3)
            selector = Selector(text=browser.page_source)
            eng_cn = selector.css('track[label=Eng-Cn]::attr(src)').extract_first() # 中英双语字幕的url
            cn = selector.css('track[label=Chinese]::attr(src)').extract_first() # 中文字幕的URL
            print eng_cn, cn
            with open(filename, 'a') as f:
                f.write('{}++{}\n'.format(name + 'eng-cn.vtt', eng_cn))
                f.write('{}++{}\n'.format(name + 'cn.vtt', cn))    
    
    browser.get(url)
    time.sleep(5)
    #print 'wait for login'
    selector = Selector(response=None, text=browser.page_source)
    s =selector.re(u'<span>课程(.+?)</span>')
    if s :
        filename = s[0].replace(':', '') + '.txt'
    else:
        filename = 'xxxxx.txt'
    print filename
    lessons = get_all_titles(selector)
    get_vtt_urls(lessons, filename)    
 

def get_lessions_url(course_url='https://classroom.udacity.com/courses/ud201'):
    browser.get(course_url)
    time.sleep(3)
    y = browser.find_elements_by_css_selector('ol li div a[href="#"]')
    for i in y:
        i.click()
        time.sleep(0.5)
    s = Selector(text=browser.page_source)
    aa = s.css('ol >li > div > a::attr(href)')
    urls = ['https://classroom.udacity.com' + x.extract() for x in aa if x.extract() != '#']
    return urls


if __name__ == '__main__':
    
    browser = webdriver.Chrome(executable_path="./chromedriver.exe")
    login_name = "xx@qq.com"
    login_password = "你的密码"
    c_url = 'https://classroom.udacity.com/courses/ud827'  #课堂地址， udxxx
    
    pre_login(login_name, login_password)
    lesson_urls = get_lessions_url(course_url=c_url)
    for lesson_url in lesson_urls:
        get_all_vtt_urls(lesson_url)
      
    browser.quit()
    print 'Done!'