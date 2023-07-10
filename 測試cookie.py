# 抓取ptt八卦版的原始碼(HTML)
import urllib.request as req
def getData(url):
    # 建立一個Requests物件，附加Requests Headers 的資訊
    request=req.Request(url, headers={
        "cookie":"over18=1",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    # 解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data, "html.parser")# 讓Beautifulsoup協助我們解析html文件
    titles=root.find_all("div", class_="title")# 尋找所有 class_="title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤(沒有被刪除)，印出來
            print(title.a.string)
    # 抓取下一頁的連結
    nextLink=root.find("a", string="‹ 上頁")# 找到內文是 ‹ 上頁 的 a 標籤
    return nextLink["href"]
# 主程序:抓取多個頁面的標題
pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<100:    
    pageURL="https://www.ptt.cc"+getData(pageURL)
    count+=1