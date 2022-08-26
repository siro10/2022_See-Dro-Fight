import socket
# ホスト名を取得して表示
host = socket.gethostname()
print (host)


# IPアドレスを取得して表示
ip = socket.gethostbyname(host)
print(ip) # 192.168.○○○.○○○