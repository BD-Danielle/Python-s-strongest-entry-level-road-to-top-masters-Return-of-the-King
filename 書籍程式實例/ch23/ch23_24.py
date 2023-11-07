# ch23_24.py
import bs4

htmlFile = open('myhtml.html', encoding='utf-8')
objSoup = bs4.BeautifulSoup(htmlFile, 'lxml')
imgTag = objSoup.select('img')
print("含<img>標籤的串列長度 = ", len(imgTag))
for i in range(len(imgTag)):              
    print("列印標籤串列 = ", imgTag[i])
    print("列印圖檔     = ", imgTag[i].get('src'))



    




    
