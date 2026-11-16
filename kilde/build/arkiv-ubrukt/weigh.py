import sys
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    for name in sys.argv[1:]:
        pg=b.new_page(viewport={"width":390,"height":800});r=[];bad=[]
        pg.on("response",lambda x:(r.append((x.url.split('/')[-1],len(x.body()) if x.ok else 0)),bad.append(x.url) if not x.ok else 0))
        pg.goto("file:///home/claude/fs/site/"+name);pg.wait_for_timeout(1200)
        pg.evaluate("window.scrollTo(0,document.body.scrollHeight)");pg.wait_for_timeout(1500)
        print(name,len(r),"filer",sum(x[1] for x in r)//1024,"KB","feil:",bad[:3],"høyde",pg.evaluate("document.body.scrollHeight"),"overflow",pg.evaluate("document.documentElement.scrollWidth"))
    b.close()
