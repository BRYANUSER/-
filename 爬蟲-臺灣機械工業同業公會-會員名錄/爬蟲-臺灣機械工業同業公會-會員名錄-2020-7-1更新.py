import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re

tStart = time.time()#計時開始

def Next_Image_link(Current):
    request = requests.get(Current) # 將此頁面的GET下來
    soup = BeautifulSoup(request.text,"html.parser") # 將網頁字串資料以html.parser解析
    reg = soup.find_all('a')
    for tag in reg :
        if tag.find('img'):       #再從標籤<a>找標籤<img>
            image = tag.find('img')['src']
            if(image == 'image/next.gif'):    #利用標籤<img>的屬性src，確認是否是我們要找的圖
                return 'http://www.tami.org.tw/category/'+tag['href']   #確認後，回傳該標籤<a>的屬性href(網頁連結)
    return None    

def Text_Clean(text):
    new_text = text.replace("\n","").replace("\r","").replace("\t","").replace(" ","").replace('\xa0', ' ')
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_text = re.sub(rstr, " ", new_text)
    return new_text

def sleeptime(hour,min,sec):
    return hour*3600 + min*60 + sec;

layer_1_list,layer_2_list,name,company_phone,company_fax,company_address,factory_phone,factory_fax,factory_address,company_url,capital,email,employee,main_product=[],[],[],[],[],[],[],[],[],[],[],[],[],[]


Current_1 = "http://www.tami.org.tw/category/product-new1.php"

while True :
    request_1 = requests.get(Current_1) # 將此頁面的GET下來
    soup_1 = BeautifulSoup(request_1.text,"html.parser")  # 將網頁字串資料以html.parser解析
    
    layer_1 = soup_1.find_all('a', { 'class': ['product-link','product-link2']})
    
    
    
    for tag_1 in layer_1:
        
        layer_1_name = Text_Clean(tag_1.text)   #別忘了記錄第一層產品分類名稱
        
        Current_2 = 'http://www.tami.org.tw/category/'+tag_1['href']
        request_2 = requests.get(Current_2)
        soup_2 = BeautifulSoup(request_2.text,"html.parser")
        
        layer_2 = soup_2.find_all('a', { 'class': 'product-link'})
        
        for tag_2 in layer_2:
            
            layer_2_name = Text_Clean(tag_2.text)
            
            Current_3 = 'http://www.tami.org.tw/category/'+tag_2['href']
            request_3 = requests.get(Current_3)
            soup_3 = BeautifulSoup(request_3.text,"html.parser")
            
            page_count = 0
            for tag_3 in soup_3.find_all('span', { 'class': 'page'}):
                page_count += 1 ;
                            
            split = tag_2['href'].split("?")
            
            for page in range(1,page_count+1):
                
                page_url = 'http://www.tami.org.tw/category/' + ('?on='+str(page)+'&').join(split)
                request_4 = requests.get(page_url)
                soup_4 = BeautifulSoup(request_4.text,"html.parser")
                
                for tag_4 in soup_4.find_all('a', { 'class': 'company-word3'}):
                    
                    goal_url = "http://www.tami.org.tw/category/contact_2.php?ms=" + tag_4['onclick'][-8:-3] + "&on=" + str(page)    # here you can do your stuff instead of print
                    request_5 = requests.get(goal_url)
                    soup_5 = BeautifulSoup(request_5.text,"html.parser")
                    
                    count = 1;
                    layer_1_list.append(layer_1_name)
                    layer_2_list.append(layer_2_name)
                    for tag_5 in soup_5.find_all('td', { 'class': 'list_td'}):
                        if count==1:
                            name.append(Text_Clean(tag_5.text))
                        elif count==2:
                            company_phone.append(Text_Clean(tag_5.text))
                        elif count==3:
                            company_fax.append(Text_Clean(tag_5.text))
                        elif count==4:
                            company_address.append(Text_Clean(tag_5.text))
                        elif count==5:
                            factory_phone.append(Text_Clean(tag_5.text))
                        elif count==6:
                            factory_fax.append(Text_Clean(tag_5.text))
                        elif count==7:
                            factory_address.append(Text_Clean(tag_5.text))
                        elif count==8:
                            company_url.append(Text_Clean(tag_5.text))
                        elif count==9:
                            capital.append(Text_Clean(tag_5.text))
                        elif count==10:
                            email.append(Text_Clean(tag_5.text))
                        elif count==11:
                            employee.append(Text_Clean(tag_5.text))
                        elif count==12:
                            main_product.append(Text_Clean(tag_5.text))
                        count+=1
                    
                    
                
            
    print ("test")
    time.sleep(sleeptime(0,0,10))
    
    if Next_Image_link(Current_1) == Current_1 :
        break
    
    Current_1 = Next_Image_link(Current_1)

excel = pd.DataFrame({"產品分類1":layer_1_list,"產品分類2":layer_2_list,"公司名稱":name,"公司電話":company_phone,"公司傳真":company_fax,"公司地址":company_address,"工廠電話":factory_phone,"工廠傳真":factory_fax,"工廠地址":factory_address,"公司網址":company_url,"資本額":capital,"電子郵件":email,"員工人數":employee,"主要產品":main_product})           
excel.to_excel('臺灣機械工業同業公會-會員名錄.xlsx', engine='xlsxwriter') 
excel.to_csv('臺灣機械工業同業公會-會員名錄.csv', index=False) 

tEnd = time.time()#計時結束
print ("It cost %f sec" % (tEnd - tStart))#會自動做近位