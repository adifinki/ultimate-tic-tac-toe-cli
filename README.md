# Ultimate tic-tac-toe CLI
## Installation

<code>poetry install</code>

## Activation

<code>poetry run start-game</code>

## Rules of the game:

 - The first player can place their designated shape at any of the 81 squares provided.
 - Whichever square that the first player places in a small tic tac toe, determines which square of the large tic tac toe the next player gets to place their shape at.
 - Wining the game requires to win the big board (wining a row, column or diagonal of boards)

```
  X       X            O O            X       X       
    X   X           O       O           X   X
      X             O       O             X
    X   X           O       O           X   X
  X       X            O O            X       X


     O O           O ##   ## O         ## X ##        
  O       O       #############     #############     
  O       O        O ## X ##           ##   ## X      
  O       O       #############     #############     
     O O           X ## X ##         O ## O ## X      


   ##   ##             O O           X ## X ##
#############       O       O       #############
 X ## O ## O        O       O          ##   ## O
#############       O       O       #############
 X ## O ## X           O O           O ## X ##
```