# -*- coding: utf-8 -*-

import socket

target_host = "www.google.com"
target_port = 80

#ソケットオブジェクトを作成
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#サーバに接続
client.connect((target_host, target_port))

#データ送信
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#データ受信
response = client.recv(4096)

print response

