# [Python教學]Request和BeautifulSoup爬蟲教學

實作對象為: [臺灣機械工業同業公會-會員名錄](http://www.tami.org.tw/category/product-new1.php)

針對本次爬蟲，需要有以下套件:

## Python套件介紹

### request
建立各種 HTTP 請求，從網頁伺服器上取得想要的資料。

[request參考資料](https://blog.gtwang.org/programming/python-requests-module-tutorial/)

### BeautifulSoup
可以快速解析網頁 HTML 碼，從中翠取出使用者有興趣的資料。

[BeautifulSoup參考資料](https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/)

### io
負責開啟檔案、關閉檔案的套件
### time
負責處理時間上的運算。而且短時間內大量抓取資料會消耗網站資源，影響網站運行，請設定睡眠時間，避免造成對方主機的負擔。
### pandas
Python 中常用的資料前處理套件，提供高效能、簡易使用的資料格式(DataFrame)讓使用者可以快速操作及分析資料。

[pandas參考資料](https://oranwind.org/python-pandas-ji-chu-jiao-xue/)

***

正式Coding

### 大致流程
爬蟲最重要的是要流程。
使用者如何操作，我們就如何爬蟲。

基本流程如下:
  1. 開啟會員名錄頁面
  2. 點開第一層產品分類
  3. 點開第二層產品分類
  4. 點開公司名稱
  5. 擷取公司資料
重複上述步驟
