import sys
from playwright.sync_api import sync_playwright
n,w,out=sys.argv[1],int(sys.argv[2]),sys.argv[3]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":w,"height":900})
    errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file:///home/claude/fs/site/"+n);pg.wait_for_timeout(600)
    for y in range(0,12000,700): pg.evaluate("window.scrollTo(0,%d)"%y);pg.wait_for_timeout(120)
    pg.evaluate("window.scrollTo(0,0)");pg.wait_for_timeout(300)
    pg.screenshot(path=out,full_page=True);print(errs)
    b.close()
