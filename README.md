# Troca de Chaves Secretas com Diffie-Hellman

Este é um exemplo simples de como dois sistemas podem concordar em uma chave secreta, mesmo que comuniquem através de um canal inseguro.

## O que é Diffie-Hellman?

O Diffie-Hellman é um protocolo criptográfico que permite a dois sistemas calcular uma chave secreta compartilhada sobre um canal inseguro. Este algoritmo é fundamental para a segurança de muitos sistemas de comunicação, como HTTPS e VPNs.

## Como usar este projeto?

Este projeto é composto por dois scripts em Python: um cliente e um servidor. Siga os passos abaixo para iniciar a troca de chaves secretas:

1. Clone este repositório em sua máquina local:

   ```git clone https://github.com/V6Cardoso/Diffie-Hellman-exercise.git```

2. Acesse o código do Cliente (tcpClientDiffieHellman.py) e adicione o IP do servidor

   ```serverName = "" # Put the server IP address here```

3. Execute o servidor:

   ```python tcpServerDiffieHellman.py```

4. Em outro terminal, execute o cliente:

   ```python tcpClientDiffieHellman.py```

 
5. Siga as instruções apresentadas no terminal do cliente e do servidor para completar a troca de chaves.

## Recursos Adicionais

Para mais informações sobre o algoritmo de Diffie-Hellman, confira os seguintes recursos:

- [Wikipedia - Diffie-Hellman key exchange](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)
- [Secret Key Exchange (Diffie-Hellman) - Computerphile](https://www.youtube.com/watch?v=NmM9HA2MQGI)
- [Diffie Hellman -the Mathematics bit- Computerphile](https://www.youtube.com/watch?v=Yjrfm_oRO0w)

## Contribuindo

Se você gostaria de contribuir para este projeto, sinta-se à vontade para abrir um pull request! Todas as contribuições são bem-vindas.

## Autores

- Victor Cardoso
- Vitor de Barros
- Leonardo Matias
- João Victor

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE).
