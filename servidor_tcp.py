import socket
import random

host = ""
port = 5006

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

print("Servidor TCP ligado...")

while True:
    conn, addr = s.accept()
    print("Conexão de", addr)
    data = conn.recv(1024).decode()
    try:
        valor, moeda = data.split()
        valor = float(valor)
        cotacao = round(random.uniform(4.5, 6.0), 2)
        convertido = round(valor / cotacao, 2)
        resposta = f"{valor} BRL = {convertido} {moeda.upper()} (cotação {cotacao})"
    except:
        resposta = "Erro no formato da mensagem."
    conn.send(resposta.encode())

    conn.close()
