from playwright.sync_api import sync_playwright
import sys
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("file:///home/claude/fs/site/index.html"); pg.wait_for_timeout(1500)
    pg.screenshot(path="/home/claude/fs/site/img/dm-forside.jpg",type="jpeg",quality=82,clip={"x":0,"y":0,"width":1440,"height":900})
    pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("file:///home/claude/fs/site/designmanual.html"); pg.wait_for_timeout(2000)
    n=pg.evaluate("document.querySelectorAll('[id^=s]').length")
    for i in range(15):
        pg.evaluate("document.getElementById('s%d').scrollIntoView()"%i); pg.wait_for_timeout(300)
        pg.screenshot(path="/tmp/dm%02d.png"%i)
    b.close()
