# yearofthetiger
There are N towers build with 3 blocks of three possible colours.
Each colour is coded by a char.
The data structure reveived is like this:
T = ['aab','abc','acb', ...]
Each tower can swap the blocks 1 and 2 or the blocks 2 and 3 but only once at most.
The solution is the maximun number of same coloured towers after performing the best possible block swap for each tower (or left the tower as it is).
In the example above T, the solution is 
T = ['aab','abc','abc']
or 
T = ['aab','acb','acb']
