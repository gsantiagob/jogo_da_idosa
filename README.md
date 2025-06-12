## Jogo da Idosa em Python

Esse é um jogo simples, aplicado em python, para dois jogadores. Eles alteram suas jogadas no tabuleiro até um dos dois completar uma coluna, linha ou diagonal com seus respectivos símbolos, ou, até ocorrer um empate, o famoso "Velha".

---

## Como Jogar?

1. O tabuleiro é uma matriz 3X3, inicialmente vazio.
2. Cada jogador possui um símbolo, sendo X ou O, após ser definido, eles alternam suas jogadas.
3. Em cada jogada, o jogador escolhe a linha e coluna correspondente, ao qual será inserido seu símbolo.
4. O sistema verifica a cada jogada se algum sdos dois jogadores venceu, caso contrário, a partida continua.
5. O primeiro jogador a formar uma linha, coluna ou diagonal com seu símbolo, ganha.
6. Se todas as células forem preenchidas sem vitória, o jogo é finalizado em empate: velha!

---

## Estrutura do código

⚪ Função mostrar_tabuleiro() - Mostra o estado atual das células da matriz.

⚪ Função verifica_vitoria() = Verifica a cada jogada se houve um vencedor.

# Variáveis

⚪ tabuleiro - Corresponde a matriz 3X3 que forma o tabuleiro do jogo.

⚪ jogador - Armazena o símbolo do jogador atual.

⚪ rodada - Controla e limita o número de jogadas, no caso, são possíveis no máximo 9.

---

## Requisitos

⚪ Python 3.x

## Como Rodar

Para rodar o código, basta seguir os seguintes passos:

1. Copie o código em um arquivo .py, jogo_da_idosa.py.
2. Abra seu terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo está localizado.
4. Execute o código com o seguinte comando:

```
bash

python jogo_da_idosa.py


