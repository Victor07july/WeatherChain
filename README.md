O Hyperledger Fabric é uma plataforma para soluções de contabilidade distribuída sustentadas por uma arquitetura modular que oferece altos graus de confidencialidade, resiliência, flexibilidade e escalabilidade. Ele foi projetado para oferecer suporte a implementações conectáveis ​​de diferentes componentes e acomodar a complexidade e os meandros existentes em todo o ecossistema econômico.

Este projeto blockchain possui dois clientes:

- Um cliente realiza um web scrape, recebendo os dados das estações em tempo real do website [Alerta Rio](http://alertario.rio.rj.gov.br/tabela-de-dados/), e os inserindo no blockchain

- Outro cliente recebe dados da API do FieldClimate os insere no blockchain



Caso a plataforma não esteja instalada na maquina, existem alguns requisitos minimos necessarios para utilizar a rede, que podem ser encontrados no seguinte repósitório
<link>https://github.com/malkai/Inmetrochain-Vehicle</link>

Para mais detalhes a documentação será um otimo guia com tutoriais de como a rede funciona -  <link>https://hyperledger-fabric.readthedocs.io/en/latest/</link>

Para começar, abra o terminal e acesse a pasta do projeto.
A seguir abra a pasta "blockchain"

```
cd blockchain
```
Crie o canal com o comando:

```
./network.sh up createChannel -ca
```

Implemente o chaincode com o comando:

```
./network.sh deployCC -ccn fabpki -ccp contrato/fabpki -ccl go
```
Entre na pasta gateway

```
cd gateway
```

E execute o seguinte comando para atualizar o arquivo json (necessário apenas 1 vez a cada inicialização da rede blockchain)

```
python3 findKey.py
```

Começando com o cliente do Alerta Rio, para inicia-lo é necessário inserir um ID de estação disponível no [Alerta Rio](http://alertario.rio.rj.gov.br/tabela-de-dados/). Caso você insira um ID não disponível, o cliente irá retornar uma mensagem de erro e listar os IDs disponíveis para cada tabela no site.

Para executar o cliente, insira o comando:

```
python3 client_insert.py <ID da Estação>

Exemplo:

python3 client_insert.py 16
```

E pronto! O cliente irá buscar os dados e os inserir no ledger. Para retornar os últimos dados inseridos, use o comando

```
python3 client_get.py <ID da Estação>

Exemplo:

python3 client_get.py 16
```

Os dados são inseridos com um timestamp em Unix com base na última atualização realizada no [Alerta Rio](http://alertario.rio.rj.gov.br/tabela-de-dados/), e é possível retornar os dados inseridos no ledger de uma estação um horário específico. Para fazer isso, execute o seguinte comando:

```
python3 client_query.py <Horário em unix>

Exemplo:

python3 client_query.py 1690991400
```

Agora, para executar o cliente do FieldClimate, retorne para a pasta gateway e entre na pasta fieldclimate

```
cd ..
cd fieldclimate
```

E insira o seguinte comando

```
python3 client.py
```


Para fazer a rede parar utilize os comandos abaixo:

```
cd .. 
cd blockchain
./network.sh down
```

