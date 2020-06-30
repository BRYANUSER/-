import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import datetime
import re


#回傳"下一頁"圖片(image/next.gif) 的網址
def Next_Image_link():
    t1 = soup1.find_all('td')
    for d in t1:
        if d.find('img'):        #再從div找img裡面的src  
            image = d.find('img')['src']
            if(image == 'image/next.gif'):
                return d.find('a')['href']

def Text_Clean(text):
    new_text = text.replace("\n","").replace("\r","").replace("\t","").replace(" ","").replace('\xa0', ' ')
    return new_text

def File_Name_Check(text):
    rstr = r"[\/\\\:\*\?\"\<\>\|]"  # '/ \ : * ? " < > |'
    new_text = re.sub(rstr, " ", text)
    new_text = new_text.replace('\xa0', ' ')
    return new_text

            
today = datetime.date.today()
directory = File_Name_Check('臺灣機械工業同業公會-會員名錄'+str(today))
os.makedirs(directory) #建立目錄
os.chdir(directory) #轉移工作目錄

Current = "http://www.tami.org.tw/category/product-new1.php"
Condition = True
while Condition :
    
    r1 = requests.get(Current) # 將此頁面的HTML GET下來
    soup1 = BeautifulSoup(r1.text,"html.parser") # 將網頁資料以html.parser
    
    
    product = soup1.find_all('a', { 'class': 'product-link'})
    for d in product:
        os.makedirs(File_Name_Check(d.text))
        os.chdir(File_Name_Check(d.text))
        product_url = 'http://www.tami.org.tw/category/'+d['href']
        r2 = requests.get(product_url) # 將此頁面的HTML GET下來
        soup2 = BeautifulSoup(r2.text,"html.parser") # 將網頁資料以html.parser
        t3 = soup2.find_all('a', { 'class': 'product-link'})
        for i in t3:
            
            type_url = 'http://www.tami.org.tw/category/'+i['href']
            r3 = requests.get(type_url) # 將此頁面的HTML GET下來
            soup3 = BeautifulSoup(r3.text,"html.parser")
            
            page_count = 0
            for z in soup3.find_all('span', { 'class': 'page'}):
                page_count += 1 ;
            
            name,company_phone,company_fax,company_address,factory_phone,factory_fax,factory_address,company_url,capital,email,employee,main_product=[],[],[],[],[],[],[],[],[],[],[],[]
            
            split = i['href'].split("?")

            for page in range(1,page_count+1):
                page_url = 'http://www.tami.org.tw/category/' + ('?on='+str(page)+'&').join(split)
                r3 = requests.get(page_url) # 將此頁面的HTML GET下來
                soup3 = BeautifulSoup(r3.text,"html.parser")
                
                
                
                for x in soup3.find_all('a', { 'class': 'company-word3'}):    # will give you all a tag
                    goal_url = "http://www.tami.org.tw/category/contact_2.php?ms=" + x['onclick'][-8:-3] + "&on=" +str(page)    # here you can do your stuff instead of print
                    r4 = requests.get(goal_url)
                    soup4 = BeautifulSoup(r4.text,"html.parser")
                    count = 1;
                    for y in soup4.find_all('td', { 'class': 'list_td'}):
                        if count==1:
                            name.append(Text_Clean(y.text))
                        elif count==2:
                            company_phone.append(Text_Clean(y.text))
                        elif count==3:
                            company_fax.append(Text_Clean(y.text))
                        elif count==4:
                            company_address.append(Text_Clean(y.text))
                        elif count==5:
                            factory_phone.append(Text_Clean(y.text))
                        elif count==6:
                            factory_fax.append(Text_Clean(y.text))
                        elif count==7:
                            factory_address.append(Text_Clean(y.text))
                        elif count==8:
                            company_url.append(Text_Clean(y.text))
                        elif count==9:
                            capital.append(Text_Clean(y.text))
                        elif count==10:
                            email.append(Text_Clean(y.text))
                        elif count==11:
                            employee.append(Text_Clean(y.text))
                        elif count==12:
                            main_product.append(Text_Clean(y.text))
                        count+=1
            
            excel = pd.DataFrame({"公司名稱":name,"公司電話":company_phone,"公司傳真":company_fax,"公司地址":company_address,"工廠電話":factory_phone,"工廠傳真":factory_fax,"工廠地址":factory_address,"公司網址":company_url,"資本額":capital,"電子郵件":email,"員工人數":employee,"主要產品":main_product})           
            excel.to_excel(File_Name_Check(i.text+'.xlsx'), engine='xlsxwriter',index=False)
        os.chdir('..')
        
        
    product = soup1.find_all('a', { 'class': 'product-link2'})
    for d in product:
        os.makedirs(d.text)
        os.chdir(d.text)
        product_url = 'http://www.tami.org.tw/category/'+d['href']
        r2 = requests.get(product_url) # 將此頁面的HTML GET下來
        soup2 = BeautifulSoup(r2.text,"html.parser") # 將網頁資料以html.parser
        t3 = soup2.find_all('a', { 'class': 'product-link'})
        for i in t3:
            
            type_url = 'http://www.tami.org.tw/category/'+i['href']
            r3 = requests.get(type_url) # 將此頁面的HTML GET下來
            soup3 = BeautifulSoup(r3.text,"html.parser")
            
            page_count = 0
            for z in soup3.find_all('span', { 'class': 'page'}):
                page_count += 1 ;
            
            name,company_phone,company_fax,company_address,factory_phone,factory_fax,factory_address,company_url,capital,email,employee,main_product=[],[],[],[],[],[],[],[],[],[],[],[]
            
            split = i['href'].split("?")

            for page in range(1,page_count+1):
                page_url = 'http://www.tami.org.tw/category/' + ('?on='+str(page)+'&').join(split)
                r3 = requests.get(page_url) # 將此頁面的HTML GET下來
                soup3 = BeautifulSoup(r3.text,"html.parser")
                
                
                
                for x in soup3.find_all('a', { 'class': 'company-word3'}):    # will give you all a tag
                    goal_url = "http://www.tami.org.tw/category/contact_2.php?ms=" + x['onclick'][-8:-3] + "&on=" +str(page)    # here you can do your stuff instead of print
                    r4 = requests.get(goal_url)
                    soup4 = BeautifulSoup(r4.text,"html.parser")
                    count = 1;
                    for y in soup4.find_all('td', { 'class': 'list_td'}):
                        if count==1:
                            name.append(Text_Clean(y.text))
                        elif count==2:
                            company_phone.append(Text_Clean(y.text))
                        elif count==3:
                            company_fax.append(Text_Clean(y.text))
                        elif count==4:
                            company_address.append(Text_Clean(y.text))
                        elif count==5:
                            factory_phone.append(Text_Clean(y.text))
                        elif count==6:
                            factory_fax.append(Text_Clean(y.text))
                        elif count==7:
                            factory_address.append(Text_Clean(y.text))
                        elif count==8:
                            company_url.append(Text_Clean(y.text))
                        elif count==9:
                            capital.append(Text_Clean(y.text))
                        elif count==10:
                            email.append(Text_Clean(y.text))
                        elif count==11:
                            employee.append(Text_Clean(y.text))
                        elif count==12:
                            main_product.append(Text_Clean(y.text))
                        count+=1
            
            excel = pd.DataFrame({"公司名稱":name,"公司電話":company_phone,"公司傳真":company_fax,"公司地址":company_address,"工廠電話":factory_phone,"工廠傳真":factory_fax,"工廠地址":factory_address,"公司網址":company_url,"資本額":capital,"電子郵件":email,"員工人數":employee,"主要產品":main_product})           
            excel.to_excel(File_Name_Check(i.text+'.xlsx'), engine='xlsxwriter')
        os.chdir('..')
    


    
    Next = 'http://www.tami.org.tw/category/' + Next_Image_link()
    if Current != Next:
        Current = Next
        Condition = True
    else:
        Condition = False
