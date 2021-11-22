import socket
import time

while True:
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  client.connect(('localhost', 7172))
  print('CONEXÃO ESTABELECIDA\n\n')


  option=str(input("DIGITE 1 PARA REALIZAR DOWNLOAD\nDIGITE 2 PARA REALIZAR UPLOAD\nDIGITE 3 PARA LISTAR OS ARQUIVOS EXISTENTES\nDIGITE 0 PARA DESCONECTAR\n\n"))
  opt = option
  client.send(opt.encode())

  
  if (option=='1'):
    namefile = str(input('QUAL O NOME DO ARQUIVO?\n '))
    client.send(namefile.encode())

    with open(namefile, 'wb') as file:
      data = client.recv(1000000)
      if not data:
        quit
      file.write(data)
      

    print("ARQUIVO RECEBIDO COM EXITO\n")
    time.sleep(1.0)

  if (option=='2'):
    namefile = str(input('QUAL O NOME DO ARQUIVO?\n '))
    client.send(namefile.encode())
    with open(namefile, 'rb') as file:
      for data in file.readlines():
        client.send(data)
      print("ARQUIVO ENVIADO COM EXITO.\n")
    time.sleep(1.0)

  if (option=='3'):
    namefile = 'diretoriolist.txt'
    client.sendall(namefile.encode())
    oi=[]
    with open(namefile, 'wb') as file:
        for i in range(4):
          data = client.recv(1024)  
          oi=(data.decode())
          print(oi)
          quit
          if not data:      
            quit
            file.write(data)
    

    time.sleep(0.5)

  if (option=='0'):
    print('ENCERRANDO CONEXÃO COM O SERVIDOR\n\n\n\n\n')
    client.close()
    break