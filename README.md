# app_spider
[![Build Status](https://travis-ci.org/Chyroc/WechatSogou.svg?branch=master)](https://github.com/Chyroc/WechatSogou)
[![PyPI version](https://badge.fury.io/py/wechatsogou.svg)](https://github.com/Chyroc/WechatSogou)
[![PyPI](https://img.shields.io/pypi/wheel/wechatsogou.svg)](https://github.com/Chyroc/WechatSogou)
[![py27,py35,py36](https://img.shields.io/pypi/pyversions/wechatsogou.svg)](https://github.com/Chyroc/WechatSogou)
[![PyPI](https://img.shields.io/pypi/l/wechatsogou.svg)](https://github.com/Chyroc/WechatSogou)

------

## Description
- Spider the video source address in the Vibrato sharing link

------

## Build
```
jackdan@jackdan-ThinkPad-T430:~$ git clone
jackdan@jackdan-ThinkPad-T430:~$ cd app_spider

### install virtualenv
jackdan@jackdan-ThinkPad-T430:~/app_spider$ pip install virtualenv
jackdan@jackdan-ThinkPad-T430:~/app_spider$ virtualenv --no-site-packages .venv
jackdan@jackdan-ThinkPad-T430:~/app_spider$ source .venv/bin/activate

### install python library
(.venv) jackdan@jackdan-ThinkPad-T430:~/app_spider/app_spider$ pip install -r requirements.txt

### run scrapy
(.venv) jackdan@jackdan-ThinkPad-T430:~/app_spider/app_spider$ scrapy crawl app

### result
###### Source Uri Address ######
https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f980000bk3o48r2esi7j2hhj8r0&ratio=720p&line=0
###### Source Uri Address ######
```

------

## Thanks
- If you like the program, please give me a star. Thanks!
- If you have some suggestions of the program, please chat with me.
```
QQ: 1835812864
```