#!/bin/bash
cd /home/claude/fs/build
python3 build.py >/tmp/build.log 2>&1 || { echo "build.py FEIL"; tail -5 /tmp/build.log; exit 1; }
python3 static.py >/dev/null && python3 designmanual.py >/dev/null && cp ../site/tjenester.html /tmp/_fresh_tjenester.html && cp ../site/bransjer.html /tmp/_fresh_bransjer.html && cp /home/claude/rescue/tjenester.html /home/claude/rescue/bransjer.html ../site/ && python3 inject_hero.py && python3 menu_patch.py && python3 sync_rescue_header.py && python3 runde1.py && python3 shot_dm.py && python3 optimize.py
