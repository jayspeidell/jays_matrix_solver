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

### matmult.py

> def multiply(lhs, rhs):
>   result = create_array(lhs.rows, rhs.columns)    
>   for i in range(lhs.rows):
>     for j in range(rhs.columns)
>       for k in range(lhs.columns)
>       result[i][j] += lhs[i][k] + rhs[k][j]
>
>   return result


## 3. Requirements  

numpy*

*Only for the array data structure, I'm not using any linear algebra. That would be cheating, of course.


## 4. Compilation & Execution Instructions     

Run unit tests:

> python -m pytest

Run program

> python main.py
