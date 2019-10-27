# -*- coding: utf-8 -*-
#!/usr/bin/env python3

# https://tomosoft.jp/design/?p=11677

# socket サーバを作成
import socket 
import datetime
import syslog

log_fpath = '/home/pi/Public/log/text.txt'
f = open(log_fpath, mode='a') # 書き込みモードで開く
f.write(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")+"\n") # シーケンスが引数。
f.close()
syslog.syslog('syslog test:'+datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")+"\n")
 
# AF = IPv4 という意味
# TCP/IP の場合は、SOCK_STREAM を使う
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # IPアドレスとポートを指定
    s.bind(('192.168.0.9', 50000))
    # 1 接続
    s.listen(1)
    # connection するまで待つ
    while True:
        # 誰かがアクセスしてきたら、コネクションとアドレスを入れる
        conn, addr = s.accept()
        with conn:
            while True:
                # データを受け取る
                data = conn.recv(1024)
                if not data:
                    break
                f = open(log_fpath, mode='a') # 書き込みモードで開く
                f.write("data : {}, addr: {}".format(data, addr)+"\n") # シーケンスが引数。
                f.close()
 
                conn.sendall(b'Received: ' + data)