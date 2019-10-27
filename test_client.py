# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 07:44:28 2019

@author: hfuji
"""

# https://tomosoft.jp/design/?p=11677

# クライアントを作成
import socket
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('192.168.0.9', 50000))
    # サーバにメッセージを送る
    s.sendall(b'hello')
    # ネットワークのバッファサイズは1024。サーバからの文字列を取得する
    data = s.recv(1024)
    #
    print(repr(data))