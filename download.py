# coding:utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re

import requests


headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36', 
    
}


for i in range(1, 40):
    txt = './{}.txt'.format(i)
    if not os.path.isfile(txt):
        continue
    else:
        with open(txt) as f:
            t = f.readlines()
            for s in t:
                ss = s.split('++')
                if len(ss) == 2:
                    name = re.sub(r'[/\\\?\>\<\>\"]', '_', ss[0])
                    url = ss[1].replace('\n', '')
                    if 'http' not in url:
                        continue
                    fname = "{}-{}".format(i, name)
                    print fname
                    
                    with open(fname.decode('utf-8'), 'w') as y:
                        y.write(requests.get(url, headers=headers).content)
                        print fname