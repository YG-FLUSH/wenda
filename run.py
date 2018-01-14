#!/usr/bin/env python
# -*- coding: utf-8 -*-
#   Author: Yoge
#   Time: 2018/01/14

import re
from orc import get_text_from_image_baidu
from config import config
from PIL import Image
from selenium import webdriver
import wda


def run():
    c = wda.Client()
    safari = webdriver.Safari()
    safari.set_window_size(1280, 800)
    while True:
        k = raw_input("题目出现后请输入 c 查找答案...")
        if k != "c":
            continue

        c.screenshot("1.png")
        img = "1.png"
        im = Image.open(img)
        w, h = im.size
        # 答题英雄
        region = im.crop((70,300, w-70,500))    #裁剪的区域
        crop_img = "1_crop.png"
        region.save(crop_img)
        with open(crop_img, 'r') as f:
            im_data = f.read()

        words = get_text_from_image_baidu(im_data, **config['baidu'])
        pattern = "\d{1,2}"
        search_text = ""
        for w in words:
            text = re.sub(pattern, "", w)
            search_text += text
        url = 'http://www.baidu.com/s?wd=%s' % search_text
        print url
        safari.get(url)


if __name__ == "__main__":
    run()
