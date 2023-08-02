O Hyperledger Fabric é uma plataforma para soluções de contabilidade distribuída sustentadas por uma arquitetura modular que oferece altos graus de confidencialidade, resiliência, flexibilidade e escalabilidade. Ele foi projetado para oferecer suporte a implementações conectáveis ​​de diferentes componentes e acomodar a complexidade e os meandros existentes em todo o ecossistema econômico.

Este projeto se trata de um sistema que realiza um web scrape, recebendo os dados das estações em tempo real do website [Alerta Rio](http://alertario.rio.rj.gov.br/tabela-de-dados/), e os inserindo no blockchain


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
Entre na pasta do cliente

`` 
cd gateway/alertaRio
```

Agora, para iniciar o cliente que realiza o web scrape será necessário inserir um ID de estação disponível no [Alerta Rio](http://alertario.rio.rj.gov.br/tabela-de-dados/).


```
python3 
```



Para fazer a rede parar utilize os comandos abaixo:

```
cd .. 
cd blockchain
./network.sh down
```

