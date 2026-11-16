from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox"])
    pg=b.new_page(viewport={"width":1440,"height":900});errs=[];pg.on("pageerror",lambda e:errs.append(str(e)))
    pg.goto("file:///home/claude/fs/site/kunnskap.html");pg.wait_for_timeout(500)
    print([pg.evaluate("document.querySelectorAll('.ksent select')[%d].offsetWidth"%i) for i in (0,1)])
    pg.select_option("select[data-g=o]","salg");pg.click(".ktab[data-v=art]");print(pg.inner_text(".kcount"),errs)
    pg.screenshot(path="/tmp/k3.png",clip={"x":100,"y":1050,"width":1240,"height":300})
    b.close()
