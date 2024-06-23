import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou, erro: {}".format(e))
        sys.exit()

    print("Conexão com Exito!")

    host_alvo = input("Digite o host ou ip a ser conxtado: ")
    porta_alvo = input("Digite a porta que será usada: ")

    try:
        s.connect((host_alvo, int(porta_alvo)))
        print("Cliente TCP conectado com sucesso!")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou, erro: {}".format(e))
        sys.exit()


if __name__ == '__main__':
    main()
