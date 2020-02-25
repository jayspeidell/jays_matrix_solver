                                          ,----,
              ____                      ,/   .`|
            ,'  , `.   ,---,          ,`   .'  :,-.----.     ,---, ,--,     ,--,
         ,-+-,.' _ |  '  .' \       ;    ;     /\    /  \ ,`--.' | |'. \   / .`|
      ,-+-. ;   , || /  ;    '.   .'___,/    ,' ;   :    \|   :  : ; \ `\ /' / ;
     ,--.'|'   |  ;|:  :       \  |    :     |  |   | .\ ::   |  ' `. \  /  / .'
    |   |  ,', |  '::  |   /\   \ ;    |.';  ;  .   : |: ||   :  |  \  \/  / ./
    |   | /  | |  |||  :  ' ;.   :`----'  |  |  |   |  \ :'   '  ;   \  \.'  /
    '   | :  | :  |,|  |  ;/  \   \   '   :  ;  |   : .  /|   |  |    \  ;  ;
    ;   . |  ; |--' '  :  | \  \ ,'   |   |  '  ;   | |  \'   :  ;   / \  \  \    
    |   : |  | ,    |  |  '  '--'     '   :  |  |   | ;\  \   |  '  ;  /\  \  \
    |   : '  |/     |  :  :           ;   |.'   :   ' | \.'   :  |./__;  \  ;  \
    ;   | |`-'      |  | ,'           '---'     :   : :-' ;   |.' |   : / \  \  ;
    |   ;/          `--''                       |   |.'   '---'   ;   |/   \  ' |
    '---'                                       `---'             `---'     `--`
                                    ,--,
                       ,----..   ,---.'|
         .--.--.      /   /   \  |   | :                  ,---,.,-.----.
        /  /    '.   /   .     : :   : |         ,---.  ,'  .' |\    /  \
       |  :  /`. /  .   /   ;.  \|   ' :        /__./|,---.'   |;   :    \
       ;  |  |--`  .   ;   /  ` ;;   ; '   ,---.;  ; ||   |   .'|   | .\ :
       |  :  ;_    ;   |  ; \ ; |'   | |__/___/ \  | |:   :  |-,.   : |: |
        \  \    `. |   :  | ; | '|   | :.'\   ;  \ ' |:   |  ;/||   |  \ :
         `----.   \.   |  ' ' ' :'   :    ;\   \  \: ||   :   .'|   : .  /
         __ \  \  |'   ;  \; /  ||   |  ./  ;   \  ' .|   |  |-,;   | |  \
        /  /`--'  / \   \  ',  / ;   : ;     \   \   ''   :  ;/||   | ;\  \
       '--'.     /   ;   :    /  |   ,/       \   `  ;|   |    \:   ' | \.'
         `--'---'     \   \ .'   '---'         :   \ ||   :   .':   : :-'
                       `---`                    '---" |   | ,'  |   |.'
                                                      `----'    `---'
                                      by
                                 Jay Speidell


## 1. Getting Started     

I'm using Python for this.

## 2. My Pseudocode   

SPOILER ALERT: This pseudocode, when implemented, did not all survive
contact with unit tests. There were casualties, especially in backsolve. 

> multiply.py

    def multiply(array lhs, array rhs):
      result = create_array(lhs.rows, rhs.columns)    
      for i in range(lhs.rows):
        for j in range(rhs.columns)
          for k in range(lhs.columns)
          result[i][j] += lhs[i][k] + rhs[k][j]

      return result

> rref.py

    def rref(array arr, col):
      for row in range(arr.rows):
        idx = where(arr[all][col] == max(arr[all][col]))
        arr = swap_rows(arr, row, idx)
        arr = row_scale(arr, row)
        arr = eliminate(arr, row)
      arr = backsolve(arr)


    def swap_rows(arr, row, idx):
      arr_new = arr.copy()
      arr_new[row][all] = arr[idx][all]
      arr_new[idx][all] = arr[row][all]
      return arr_new

    def row_scale(arr, row):
      factor = arr[row][row]
      for col in range(arr.cols):
          arr[row][col] = arr[row][col] / factor
      return arr

    def eliminate(arr, target_row):
      target_col = target_row
      for row in range(target_row + 1, arr.rows)
        factor = arr[row][target_col]
        for col in range(target_col, arr.cols):
          arr[row][col] = arr[row][col] - factor * arr[target_row][col]
      return arr

    def backsolve(arr):


## 3. Requirements  

numpy*

*Only for the array data structure, I'm not using any linear algebra. That would be cheating, of course.


## 4. Compilation & Execution Instructions     

Run unit tests:

> python -m pytest

Run program

> python main.py
