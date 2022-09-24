#!/usr/bin/env python
# coding: utf-8

# In[28]:

import os
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
os.chdir(r'C:\CAU_COVID19')

ID_num = 'B2022123456'
password = '123456789'

# # 自动申请当天进出校

# ### 出校申请

# In[175]:


driver = webdriver.Edge('edgedriver_win64_105.0.1343.42/msedgedriver.exe')
# 打开网页
# url="https://service.cau.edu.cn/v2/matter/detail?id=366"
url='http://onecas.cau.edu.cn/tpass/login?service=http%3A%2F%2Fservice.cau.edu.cn%2Fsite%2Flogin%2Fcas-login%3Fredirect_url%3Dhttps%25253A%25252F%25252Fservice.cau.edu.cn%25252Fv2%25252Fmatter%25252Fdetail%25253Fid%25253D366'
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")
# 最大化浏览器窗体
driver.maximize_window()
time.sleep(0.3)

#学号
elem = driver.find_element_by_id("un")
elem.send_keys(ID_num)
#密码
elem = driver.find_element_by_id("pd")
elem.send_keys(password)

#登录
driver.find_element_by_xpath('//*[@id="index_login_btn"]').click()
time.sleep(2)

#点击立即申请
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[1]/div/div[2]/div/button').click()
time.sleep(4)

#选择宿舍楼
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/div/div[1]'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

xpath='/html/body/div[4]/div[1]/div[1]/ul/li[20]'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

#填写宿舍号
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/table/tbody/tr[4]/td[4]/div/div[1]/div/span/span/div[2]/input'
driver.find_element_by_xpath(xpath).send_keys('东校区家属区')
time.sleep(0.3)


#填写体温
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/table/tbody/tr[5]/td[2]/div/div[1]/div/span/span/div[2]/input'
driver.find_element_by_xpath(xpath).send_keys('36.5')
time.sleep(0.3)

#选择校区
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[3]/div/table/tbody/tr[5]/td[4]/div/div[1]/div/div/div'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

xpath='/html/body/div[5]/div[1]/div[1]/ul/li[3]'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

#选择外出时间
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div/table/tbody/tr[1]/td[2]/div/div[1]'
driver.find_element_by_xpath(xpath).click()
time.sleep(4)

#此刻
css_selector='button.el-picker-panel__link-btn:nth-child(1)'
driver.find_element_by_css_selector(css_selector).click()
time.sleep(0.3)


# xpath='/html/body/div[16]/div[1]/div/div[1]/span[1]/div/input'
# '/html/body/div[27]/div[1]/div/div[1]/span[1]/div/input'
# time.sleep(1)
# driver.find_element_by_xpath(xpath).send_keys('2022-09-21')
# time.sleep(0.3)

# xpath='/html/body/div[18]/div[1]/div/div[1]/span[2]/div[1]/input'
# driver.find_element_by_xpath(xpath).send_keys('00:00')
# time.sleep(0.3)


# #返回时间
# xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div/table/tbody/tr[1]/td[4]/div/div[1]/div/div/input'
# driver.find_element_by_xpath(xpath).click()
# time.sleep(10)
# for i in range(10):
#     xpath='/html/body/div[8]/div[1]/div/div[1]/div[1]/ul/li[2]'
#     driver.find_element_by_xpath(xpath).click()
# # css_selector='li.active:nth-child(2)'
# # driver.find_element_by_css_selector(css_selector).click()
# time.sleep(1)

# 外出去向
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/span/div[2]/textarea'
driver.find_element_by_xpath(xpath).send_keys('东校区家属区')
time.sleep(0.3)

# 外出事由
xpath='/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/div[1]/div[4]/div/table/tbody/tr[4]/td[2]/div/div[1]/div/span/div[2]/textarea'
driver.find_element_by_xpath(xpath).send_keys('走读出入校')
time.sleep(0.3)

# 提交
xpath='/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/button[2]'
driver.find_element_by_xpath(xpath).click()
time.sleep(4)

#二次确认
xpath='/html/body/div[1]/div[2]/div[2]/div/div[2]/div/button[2]'
driver.find_element_by_xpath(xpath).click()
time.sleep(10)

#关闭浏览器
driver.close() 


# ### 返校登记

# In[174]:


driver = webdriver.Edge('edgedriver_win64_105.0.1343.42/msedgedriver.exe')
# 打开网页
url="https://service.cau.edu.cn/v2/matter/todo"
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")
# 最大化浏览器窗体
driver.maximize_window()
time.sleep(0.3)

#学号
elem = driver.find_element_by_xpath('//*[@id="un"]')
elem.send_keys(ID_num)
#密码
elem = driver.find_element_by_xpath('//*[@id="pd"]')
elem.send_keys(password)
#登录
driver.find_element_by_xpath('//*[@id="index_login_btn"]/input').click()
time.sleep(4)

#处理事项
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/section/div[1]/ul/li/section/a/div[2]/div[2]/a[1]'
driver.find_element_by_xpath(xpath).click()
time.sleep(4)

#切换到新窗口
handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
        
#提交勾选
xpath='/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/table/tr[1]/td[2]/label/span[1]'
driver.find_element_by_xpath(xpath).click()
time.sleep(2)

# 外出时间
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[5]/div/table/tbody/tr[2]/td[2]/div/div[1]/div/div/input'
driver.find_element_by_xpath(xpath).send_keys(' ')
time.sleep(4)

# xpath='/html/body/div[4]/div[2]/button[1]/span'
xpath='/html/body/div[3]/div[2]/button[1]/span'
xpath='/html/body/*/div[2]/button[1]/span'

driver.find_element_by_xpath(xpath).click()
time.sleep(4)

# 外出地点
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[6]/div/table/tbody/tr[3]/td[1]/div/div[1]/div/span/span/div[2]/input'
driver.find_element_by_xpath(xpath).send_keys('东校区家属区')
time.sleep(2)

# 乘坐交通工具
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[6]/div/table/tbody/tr[3]/td[2]/div/div[1]/div/div/div/input'
driver.find_element_by_xpath(xpath).send_keys('步行')
time.sleep(2)

# xpath='/html/body/div[6]/div[1]/div[1]/ul/li/span'
xpath='/html/body/*/div[1]/div[1]/ul/li[1]/span'
driver.find_element_by_xpath(xpath).click()
time.sleep(2)

# 班次
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[6]/div/table/tbody/tr[3]/td[3]/div/div[1]/div/span/span/div[2]/input'
driver.find_element_by_xpath(xpath).send_keys('步行')
time.sleep(3)

# 到达时间
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[6]/div/table/tbody/tr[3]/td[4]/div/div[1]/div/div/input'
driver.find_element_by_xpath(xpath).send_keys(' ')
time.sleep(5)

xpath='/html/body/div[6]/div[2]/button[1]/span'
# xpath='/html/body/*/div[2]/button[1]/span'
driver.find_element_by_xpath(xpath).click()
time.sleep(3)

#停留时长
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[6]/div/table/tbody/tr[3]/td[5]/div/div[1]/div/span/span/div[2]/input'
driver.find_element_by_xpath(xpath).send_keys('1')
time.sleep(3)

# 返回时间(为了和外出时间错开一分钟)
time.sleep(34)
xpath='/html/body/div[1]/div[2]/div[1]/div[3]/div[2]/div/div/div[1]/div[1]/div[5]/div/table/tbody/tr[2]/td[4]/div/div[1]/div/div/input'
driver.find_element_by_xpath(xpath).send_keys(' ')
time.sleep(4)

try:
    xpath='/html/body/div[5]/div[2]/button[1]/span'
    driver.find_element_by_xpath(xpath).click()
except:
    xpath='/html/body/div[7]/div[2]/button[1]/span'
    driver.find_element_by_xpath(xpath).click()
time.sleep(3)

driver.execute_script("document.body.style.transform='scale(0.5)'")

#正式提交
xpath='/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[2]/button'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)
time.sleep(10)

# 关闭浏览器
driver.close() 


# # 自动疫情上报

# In[88]:


driver = webdriver.Edge('edgedriver_win64_105.0.1343.42/msedgedriver.exe')
# 打开网页
url='https://wep.cau.edu.cn/cauncovxs/wap/default/index'
driver.get(url) # 打开url网页 比如 driver.get("http://www.baidu.com")
# # 最大化浏览器窗体
# driver.maximize_window()
time.sleep(0.3)

#学号
elem = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[1]/input')
elem.send_keys(ID_num)
#密码
elem = driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/input')
elem.send_keys(password)
#登录
driver.find_element_by_xpath('/html/body/div[1]/div[3]').click()
time.sleep(2)

# 获取定位
xpath='/html/body/div[1]/div/div/section/div[4]/ul/li[9]/div/input'
driver.find_element_by_xpath(xpath).click()
time.sleep(5)

#昨日是否核酸
t=time.localtime(time.time())
if t.tm_yday%2==1:
    xpath='/html/body/div[1]/div/div/section/div[4]/ul/li[27]/div/div/div[1]/span[1]/i'  #是
else:
    xpath='/html/body/div[1]/div/div/section/div[4]/ul/li[27]/div/div/div[2]/span[1]/i'  #否

driver.find_element_by_xpath(xpath).click()
time.sleep(0.3)

# 提交信息
xpath='/html/body/div[1]/div/div/section/div[5]/div'
driver.find_element_by_xpath(xpath).click()
time.sleep(1)

#确认
xpath='/html/body/div[4]/div/div[2]/div[2]'
driver.find_element_by_xpath(xpath).click()
time.sleep(10)

#关闭浏览器
driver.close() 



