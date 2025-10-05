import socket
import random

host = ""
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))

print("Servidor UDP ligado...")

while True:
    data, addr = s.recvfrom(1024)
    msg = data.decode()
    print("Recebi:", msg)

    try:
        valor, moeda = msg.split()
        valor = float(valor)
        cotacao = round(random.uniform(4.5, 6.0), 2)
        convertido = round(valor / cotacao, 2)
        resposta = f"{valor} BRL = {convertido} {moeda.upper()} (cotação {cotacao})"
    except:
        resposta = "Erro no formato da mensagem."


    s.sendto(resposta.encode(), addr)
