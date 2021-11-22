import socket
import os

while True:
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(('localhost', 7172))
  print('AGUARDANDO O CLIENTE SE CONECTAR...\n.\n.\n.\n.\n')
  server.listen(1)
  connection, address =server.accept()
  print("ESTAMOS CONECTADOS")

  condi = connection.recv(1024).decode()
#enviar arquivo para o client
  if (condi=='1'):
    namefile = connection.recv(1024).decode()

    with open(namefile, 'rb') as file:
      for data in file.readlines():
        connection.send(data)
  
      print("O ARQUIVO FOI ENVIADO COM EXITO")

 #enviar arquivo para o servidor     
  if (condi=='2'):
    namefile = connection.recv(1024).decode()
    with open(namefile, 'wb') as file:
      
      data = connection.recv(1000000)
      if not data:
        quit
      file.write(data)
    print("ARQUIVO FOI RECEBIDO COM EXITO")
  


 #exibir lista de arquivos no diretorio  
  if (condi=='3'):
    raiz = './'
    aux1=0
    for diretorio, subpastas, arquivos in os.walk(raiz):
      print("EXIBINDO LISTA PARA O CLIENTE\n")
      for arquivo in arquivos:
        aux=os.path.join(diretorio, arquivo)
        connection.send(str.encode(aux) )
        aux1+=1
        arquivo = open('diretoriolist.txt', 'a')
        arquivo.write(aux + "\n")
        arquivo.close()
    print(aux1)
    namefile = connection.recv(1024).decode()
    with open(namefile, 'rb') as file:
      for data in file.readlines():
        connection.send(data)

#encerrando conexão
  if (condi=='0'):
    print('ENCERRANDO CONEXÃO COM O CLIENTE....\n\n\n\n\n')
    connection.close()
    break