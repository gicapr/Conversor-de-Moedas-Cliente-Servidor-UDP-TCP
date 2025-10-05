import socket

host = "192.168.30.130"
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    valor = input("Digite o valor em reais (ou sair): ")
    if valor.lower() == "sair":
        break
    moeda = input("Digite a moeda (ex: usd, eur): ")
    msg = f"{valor} {moeda}"
    s.sendto(msg.encode(), (host, port))
    data, _ = s.recvfrom(1024)

    print("Servidor:", data.decode())
