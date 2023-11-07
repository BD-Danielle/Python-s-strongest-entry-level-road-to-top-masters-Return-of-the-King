# ch24_7.py
from selenium import webdriver

driverPath = 'D:\geckodriver\geckodriver.exe'
browser = webdriver.Firefox(executable_path=driverPath)
url = 'http://aaa.24ht.com.tw'
browser.get(url)                # 網頁下載至瀏覽器

tag1 = browser.find_element_by_tag_name('title')        # 傳回<title>
print("標籤名稱 = %s, 內容是 = %s " % (tag1.tag_name, tag1.text))

tag2 = browser.find_element_by_id('author')             # 傳回<h1>
print("\n標籤名稱 = %s, 內容是 = %s " % (tag2.tag_name, tag2.text))

print()
tag3 = browser.find_elements_by_id('content')           # 傳回<h1>
for i in range(len(tag3)):
    print("標籤名稱 = %s, 內容是 = %s " % (tag3[i].tag_name, tag3[i].text))

print()
tag4 = browser.find_elements_by_tag_name('p')           # 傳回<p>
for i in range(len(tag4)):
    print("標籤名稱 = %s, 內容是 = %s " % (tag4[i].tag_name, tag4[i].text))

print()
tag5 = browser.find_elements_by_tag_name('img')         # 傳回<img>
for i in range(len(tag5)):
    print("標籤名稱 = %s, 內容是 = %s " % (tag5[i].tag_name, tag5[i].get_attribute('src')))
