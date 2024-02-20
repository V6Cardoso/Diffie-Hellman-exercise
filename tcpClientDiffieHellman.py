from socket import *

def encrypt(caesarKey, sentence):
    cryptographSentence = ""
    for char in sentence:
        cryptographSentence += chr(ord(char) + caesarKey)
    return cryptographSentence

def decrypt(caesarKey, sentence):
    return encrypt(-caesarKey, sentence)


serverName = "" # Put the server IP address here
serverPort = 1300
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

G = 15
N = 97
X = 5
R1 = (G ** X) % N

print("G: ", G)
print("N: ", N)
print("X: ", X)
print("R1: ", R1)

message = f"{G},{N},{R1}"
clientSocket.send(bytes(message, "utf-8"))

R2 = int(clientSocket.recv(1024))
print("R2: ", R2)

K = (R2 ** X) % N
print("K: ", K)

sentence = input("Input lowercase sentence: ")
sentence = sentence.lower()

CAESAR_KEY = K
cryptographSentence = encrypt(CAESAR_KEY, sentence)

clientSocket.send(bytes(cryptographSentence, "utf-8"))
modifiedSentence = clientSocket.recv(1024)
text = str(modifiedSentence,"utf-8")

decryptText = decrypt(CAESAR_KEY, text)

print ("Received from Make Upper Case Server: ", decryptText)
clientSocket.close()