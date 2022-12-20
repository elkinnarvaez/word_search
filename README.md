# Word Search

## Dependencies

- Python 3.x. Instructions for installation can be found [here](https://www.python.org/downloads/).

## Run program

In order to run this program please follow the steps bellow.

1. Clone the repository in your local machine.

   ```
   git clone https://github.com/elkinnarvaez/word_search.git
   ```

2. Go to the project folder.

   ```
   cd word_search
   ```

3. Run the following command in your terminal:

   ```
   python word_search.py < input.txt
   ```

   Refer to the next section for further reference about the _input.txt_ file.

## Input description

The _input.txt_ file contains the input data used in the program. It can have several test cases, where each case consists of two integers representing the dimensions of the word search board: number of rows (N) and number of cloumns (M); followed by N lines, where each line contains M letters separated by an space character; and a single line with with the words to find in the board separated by an space character.

A test case where N = 0 or M = 0 finishes the execution of the program.

### Input example

```
3 5
S O L A F
U N S U N
N U T C J
SUN SOL LOT ONU RAY
0 0
```

## Output description

For each test case, the program prints a line with the case numer followed by the occurences found for each word in the board. If a word has no ocurrences, the program must indicate so.

### Output example

```
Case #1
Searching 'SUN'
S - (1, 2)
U - (1, 3)
N - (1, 4)
-------------
S - (0, 0)
U - (1, 0)
N - (2, 0)
Searching 'SOL'
S - (0, 0)
O - (0, 1)
L - (0, 2)
Searching 'LOT'
'LOT' not found
Searching 'ONU'
O - (0, 1)
N - (1, 1)
U - (2, 1)
Searching 'RAY'
'RAY' not found
```
