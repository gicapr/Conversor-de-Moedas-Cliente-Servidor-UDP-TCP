import socket

host = "192.168.30.130"
port = 5006

while True:
    valor = input("Digite o valor em reais (ou sair): ")
    if valor.lower() == "sair":
        break
    moeda = input("Digite a moeda (ex: usd, eur): ")
    msg = f"{valor} {moeda}"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(msg.encode())
    data = s.recv(1024).decode()
    print("Servidor:", data)

    s.close()
