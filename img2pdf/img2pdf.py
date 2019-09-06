#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import glob
import fitz

def img2pdf(img_folder,pdf_file,img_type):
    '''
    存img的文件夹里，找到所有符合img_type扩展名的图片，转为pdf。
    '''
    # 如果输入的是.png,把前面的点去掉，得到png
    if len(img_type):
        if img_type[0]==".":
            img_type=img_type[1:]
    # 读取文件夹中的所有指定扩展名的图片
    imgs=glob.glob(os.path.join(img_folder,"*."+img_type))
    #print(imgs)
    doc=fitz.open()
    for img in imgs:
        print(img)
        # 打开图片
        img=fitz.open(img)
        # 图片转换为单页pdf
        single_pdf=img.convertToPDF()
        # 将当前页插入文档
        doc.insertPDF(fitz.open("tmp.pdf",single_pdf))
    # 保存pdf文件
    doc.save(pdf_file)
    doc.close()

if __name__=="__main__":
    img2pdf(r"./files","img.pdf","png")
