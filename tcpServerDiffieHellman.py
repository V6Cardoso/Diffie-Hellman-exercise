from socket import *

def encrypt(caesarKey, sentence):
    cryptographSentence = ""
    for char in sentence:
        cryptographSentence += chr(ord(char) + caesarKey)
    return cryptographSentence

def decrypt(caesarKey, sentence):
    return encrypt(-caesarKey, sentence)

serverPort = 1300
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()
print ("Server ready to receive\n")
received_message = connectionSocket.recv(1024)
G, N, R1 = map(int, received_message.decode("utf-8").split(","))
Y = 123
print("Y: ", Y)

R2 = (G ** Y) % N
print("R2: ", R2)

K = (R1 ** Y) % N
print("K: ", K)

connectionSocket.send(bytes(str(R2), "utf-8"))

sentence = connectionSocket.recv(65000)

received = str(sentence,"utf-8")
print ("Received From Client: ", received)

CAESAR_KEY = K
decriptedSentence = decrypt(CAESAR_KEY, received)

capitalizedSentence = decriptedSentence.upper() # processamento

encriptedSentence = encrypt(CAESAR_KEY, capitalizedSentence)
print ("Sent back to Client: ", encriptedSentence)
connectionSocket.send(bytes(encriptedSentence, "utf-8"))

connectionSocket.close()
    
