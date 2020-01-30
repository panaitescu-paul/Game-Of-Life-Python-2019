# Game of Life (Evolution of Life Forms)
Alive cells interact with their neighbours to evolve to the next state, based on different rules.

## Preview:
<p align="center">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/04.png">
</p>

## Technologies:
- Python

## Features:
1. Separate configuration from implementation 
2. GUI
3. Grid 100 x 100
4. Multiple rule sets
5. Random & Clear
6. User defined initial state
7. Configurable speed
8. Step-by-step progression 
9. Unit tests

### 1. Separate configuration from implementation
- **Write** the rules in json format
- **Read** the rules from json
- **Use** the rules to process the next state
 
### 2. GUI
- Canvas 
- Buttons 
- Slider
 
### 3. Grid 100 x 100
Two representations:
- In the **Model**
- In the **View**

### 4. Multiple rule sets
- Json file with **multiple rule sets**
- **Dropdown menu** to switch rules
  
### 5. Random & Clear
- **Random** - creates the initial cells randomly
- **Clear** - all cells are dead

### 6. User defined initial state
- Bind a method to **click event**
- Based on click, change values to either 1 or 0, in the matrix
- **Draw next frame**
 
### 7. Configurable speed
- Move the slider from 1 to 1000
- **Process and draw the next frame** based on selected speed (every 1 to 1000
milliseconds)
 
### 8. Step-by-step progression
- Calculate the **next state** based on the current state
- Determine the number of neighbours of every cell
 
### 9. Unit tests
- Test for **equal and not equal cases** applied on multiple rules

## Screenshots:
<p align="center">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/00.png">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/01.png">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/02.png">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/03.png">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/04.png">
  <img width="45%" height="45%" src="https://github.com/panaitescu-paul/GameOfLife-2019/blob/master/screenshots/05.png">
</p>
 

 
