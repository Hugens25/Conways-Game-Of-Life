My Python implementation of Conway's Game of Life.

Code Specifics:
  -In my implementation of this game, I am using smiley faces, ':)', to depict the cells. 
  -I give the user the option of selecting their own size for their orthoganal grid.
  -I give the user the option of having gridlines displayed on the grid.
  -Code detects if the user's generation is in a state that will endlessly loop, if so, the program ends.
  -Code detects if the user's generation has completely died off, if so, the program ends.


The rules to the game are listed below:

*************************************************** Rules ******************************************************

The universe of the Game of Life is an infinite two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are directly horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

Any live cell with fewer than two live neighbours dies (referred to as underpopulation or exposure[1]).
Any live cell with more than three live neighbours dies (referred to as overpopulation or overcrowding).
Any live cell with two or three live neighbours lives, unchanged, to the next generation.
Any dead cell with exactly three live neighbours will come to life.

The initial pattern constitutes the 'seed' of the system. The first generation is created by applying the above rules simultaneously to every cell in the seed — births and deaths happen simultaneously, and the discrete moment at which this happens is sometimes called a tick. (In other words, each generation is a pure function of the one before.) The rules continue to be applied repeatedly to create further generations.

****************************************************************************************************************


