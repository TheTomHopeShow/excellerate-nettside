from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1440,"height":900})
    pg.goto("file:///home/claude/fs/site/index.html");pg.wait_for_timeout(800)
    pg.screenshot(path="/home/claude/fs/site/img/dm-forside.jpg",type="jpeg",quality=85)
    b.close()
