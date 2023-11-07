# ch23_22.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
pObjTag = objSoup.select('p')
print("含<p>標籤的串列長度 = ", len(pObjTag))
for i in range(len(pObjTag)):
    print(str(pObjTag[i]))              # 內部有子標籤<strong>字串
    print(pObjTag[i].getText())         # 沒有子標籤
    print(pObjTag[i].text)              # 沒有子標籤




    
