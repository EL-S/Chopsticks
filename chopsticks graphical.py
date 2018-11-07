from random import *
import math
p1_name = "";
p2_name = "";
while (p1_name == ""):
    p1_name = input("Enter Player One's Name: ").title()
while (p2_name == ""):
    p2_name = input("Enter Player Two's Name: ").title();

user_data = [[p1_name,[[0],[0]]],[p2_name,[[0],[0]]]]

active = True;
c = 0;

hand = ('''
       _.-._
     _| | | |
    | | | | |
    | | | | |
    |  '-._ | ,-
    |`-.'-._;/ /
    |   '     /
     \.`   ` /
      |    |''','''
       _.-._
     _| | | |
    | | | | |
    | | | | |
    |  '-._ |.
    |`-.'-._\ \ 
    |   '     /
     \.`   ` /
      |    |''','''
       _.-._
      | | | |
      | | | |
     _| | | |
    | |'-._ |.
    | |-'-._\ \ 
    |-` '     /
     \.`   ` /
      |    |''','''
        .-._
        | | |
        | | |
     _.-| | |
    | | |._ |.
    | | '-._\ \ 
    |-`_'     /
     \.`   ` /
      |    |''','''
           _
          | |
          | |
     _.-.-| |
    | | |.| |.
    | | ' |_\ \ 
    |-`_'_'   /
     \.`   ` /
      |    |''','''
        
          
          
     _.-.-._
    | | |.| |.
    | | ' | \ \ 
    |-`_'_'-  /
     \.`   ` /
      |    |''');

hand_o = ('''
                                                       _.-._       
                                                      | | | |_     
                                                      | | | | |    
                                                      | | | | |    
                                                   -, | _.-'  |    
                                                   \ \;_.-'.-`|    
                                                    \     '   |    
                                                     \ `   `./     
                                                       |    |''','''
                                                       _.-._       
                                                      | | | |_     
                                                      | | | | |    
                                                      | | | | |    
                                                     .| _.-'  |    
                                                    / /_.-'.-`|    
                                                    \     '   |    
                                                     \ `   `./     
                                                       |    |''','''
                                                       _.-._       
                                                      | | | |     
                                                      | | | |    
                                                      | | | |_    
                                                     .| _.-'| |    
                                                    / /_.-'-| |    
                                                    \     ' `-|    
                                                     \ `   `./     
                                                       |    |''','''
                                                       _.-.       
                                                      | | |     
                                                      | | |    
                                                      | | |-._    
                                                     .| _.| | |    
                                                    / /_.-' | |    
                                                    \     '_`-|    
                                                     \ `   `./     
                                                       |    |''','''
                                                       _       
                                                      | |     
                                                      | |    
                                                      | |-.-._    
                                                     .| |.| | |    
                                                    / /_| ' | |    
                                                    \   '_'_`-|    
                                                     \ `   `./     
                                                       |    |''','''
                                                             
                                                           
                                                          
                                                       _-.-._    
                                                     .| |.| | |    
                                                    / / | ' | |    
                                                    \  -'_'_`-|    
                                                     \ `   `./     
                                                       |    |''');

hand_u = ('''

      |    |
     /.`   ` \ 
    |   '     \ 
    |`-.'-._.\ \  
    |  '-._ | `-
    | | | | |
    | | | | |
    '_| | | |
      '-|_|-`''','''

      |    |
     /.`   ` \ 
    |   '     \ 
    |`-.'-._/ / 
    |  '-._ |`
    | | | | |
    | | | | |
    '_| | | |
      '-|_|-`''','''

      |    |
     /.`   ` \ 
    |_  '     \ 
    |`'.'-._/ /  
    |'|'-._ |`
    '-| | | |
      | | | |
      | | | |
      '-|_|-`''','''

      |    |
     /.`   ` \ 
    |_  '     \ 
    |`'-'-._/ /  
    |'|'|._ |`
    '-|_| | |
        | | |
        | | |
        |_|-`''','''

      |    |
     /.`   ` \ 
    |_  '     \ 
    |`'-'-._/ /  
    |'|'|._ |`
    '-|_|_| |
          | |
          | |
          '-' ''','''

      |    |
     /.`   ` \ 
    |_  '     \ 
    |`'-'-._/ /  
    |'|'|._ |`
    '-|_|_|-'
             ''');

hand_u_o = ('''

                                                      |    |      
                                                     / `   `.\     
                                                    /     '   |    
                                                   / /;_.-'.-`|    
                                                   -' | _.-'  |    
                                                      | | | | |    
                                                      | | | | |    
                                                      | | | |_'
                                                      `-|_|-' ''','''

                                                       |    |      
                                                     / `   `.\     
                                                    /     '   |    
                                                    \ \_.-'.-`|    
                                                     `| _.-'  |    
                                                      | | | | |    
                                                      | | | | |    
                                                      | | | |_'
                                                      `-|_|-' ''','''

                                                       |    |      
                                                     / `   `.\     
                                                    /     '  _|    
                                                    \ \_.-'.'`|    
                                                     `| _.-'|'|    
                                                      | | | |-'    
                                                      | | | |     
                                                      | | | | 
                                                      `-|_|-' ''','''

                                                       |    |      
                                                     / `   `.\     
                                                    /     '  _|    
                                                    \ \_.-'-'`|    
                                                     `| _.|'|'|    
                                                      | | |_|-'    
                                                      | | |     
                                                      | | | 
                                                      `-|_| ''','''

                                                       |    |      
                                                     / `   `.\     
                                                    /     '  _|    
                                                    \ \_.-'-'`|    
                                                     `| _.|'|'|    
                                                      | |_|_|-'    
                                                      | |     
                                                      | | 
                                                      '-'   ''','''

                                                       |    |      
                                                     / `   `.\     
                                                    /     '  _|    
                                                    \ \_.-'-'`|    
                                                     `| _.|'|'|    
                                                      '-|_|_|-'    
                                                           
                                                      
                                                             ''');
#print(hand_5,hand_4,hand_3,hand_2,hand_1,hand_0,hand_5_o,hand_4_o,hand_3_o,hand_2_o,hand_1_o,hand_0_o,hand_5_u,hand_4_u,hand_3_u,hand_2_u,hand_1_u,hand_0_u,hand_5_u_o,hand_4_u_o,hand_3_u_o,hand_2_u_o,hand_1_u_o,hand_0_u_o);

def initiate():
    c = 0;
    message = "";
    first_player_id = randint(0,1);
    print(user_data[first_player_id][0], "is first")
    if first_player_id == 0:
        flag = 0;
    else:
        flag = 1;
    user_data[0][1][0] = 1;
    user_data[0][1][1] = 1;
    user_data[1][1][0] = 1;
    user_data[1][1][1] = 1;
    return [flag,message]

def info(flag2 = True):
    print("__________________________________________________________________");
    print("Turn:",c,"\n")
    if (c > 0):
        if (c%2 == 0):
            if var[0] == 1:
                prev_player = 1;
            else:
                prev_player = 0;
        else:
            if var[0] == 0:
                prev_player = 1;
            else:
                prev_player = 0;
    if (c%2 == 0):
        if var[0] == 1:
            player = 0;
        else:
            player = 1;
    else:
        if var[0] == 0:
            player = 0;
        else:
            player = 1;
    if (var[1] != "") & (c > 1) & (flag2 != False):
        print(user_data[prev_player][0],"used",var[1],"\n");
    elif (var[1] != "") & (c > 0):
        print(user_data[player][0],"used",var[1],"\n");
        
    if (user_data[0][1][0] >= 5):
        user_data[0][1][0] = 0;
    if (user_data[0][1][1] >= 5):
        user_data[0][1][1] = 0;
    if (user_data[1][1][0] >= 5):
        user_data[1][1][0] = 0;
    if (user_data[1][1][1] >= 5):
        user_data[1][1][1] = 0;
    print(user_data[0][0]+"'s Hands:\n  Left:",user_data[0][1][0],"\n  Right:",user_data[0][1][1],"\n")
    print(user_data[1][0]+"'s Hands:\n  Left:",user_data[1][1][0],"\n  Right:",user_data[1][1][1])
    print(hand_u[(len(hand_u) - 1) - user_data[prev_player][1][0]]);
    print(hand_u_o[(len(hand_u_o) - 1) - user_data[prev_player][1][1]]);
    print(hand[(len(hand) - 1) - user_data[player][1][0]]);
    print(hand_o[(len(hand_o) - 1) - user_data[player][1][1]]);
    return player

var = initiate();
while active:
    print("\n"*3);
    c += 1;
    player = info();
    hand_total = user_data[player][1][0] + user_data[player][1][1]
    if (hand_total <= 0):
        print("\n",user_data[player][0],"lost!");
        break
    while True:
        print("\nHand Total:",hand_total);
        if (player == 0):
            other_player = 1;
        else:
            other_player = 0;
        flag2 = True;
        action = list(input("\n"+user_data[player][0]+"'s move: ").split());
        if (action[0].lower() == "s"):
            if (len(action) > 1):
                if (action[1].lower().isdigit()):
                    if (int(action[1]) <= hand_total) & (int(action[1]) > 0) & (int(action[1]) < 5) & (hand_total - int(action[1]) < 5):
                        left = int(action[1]);
                        user_data[player][1][0] = left;
                        user_data[player][1][1] = hand_total - left;
                        var[1] = "a specific split value!";
                        break
                    else:
                        var[1] = "an invalid split value!";
                else:
                    var[1] = "a letter instead of a number, try again!";
            else:
                var[1] = "the default half split!";
                left = math.ceil(hand_total/2);
                user_data[player][1][0] = left;
                user_data[player][1][1] = hand_total - left;
                break
            flag2 = False;
        elif (action[0].lower() == "l"):
            if (user_data[player][1][0] > 0):
                if (len(action) > 1):
                    if (action[1].lower() == "l"):
                        if (user_data[other_player][1][0] > 0):
                            user_data[other_player][1][0] = user_data[other_player][1][0] + user_data[player][1][0]
                            var[1] = "left hand attacks left hand!";
                            break
                    elif (action[1].lower() == "r"):
                        if (user_data[other_player][1][1] > 0):
                            user_data[other_player][1][1] = user_data[other_player][1][1] + user_data[player][1][0]
                            var[1] = "left hand attacks right hand!";
                            break
                var[1] = "their left hand but on an invalid target!";
            else:
                var[1] = "their nonexistant left hand so it failed!";
            flag2 = False;
        elif (action[0].lower() == "r"):
            if (user_data[player][1][1] > 0):
                if (len(action) > 1):
                    if (action[1].lower() == "l"):
                        if (user_data[other_player][1][0] > 0):
                            user_data[other_player][1][0] = user_data[other_player][1][0] + user_data[player][1][1]
                            var[1] = "right hand attacks left hand!";
                            break
                    elif (action[1].lower() == "r"):
                        if (user_data[other_player][1][1] > 0 ):
                            user_data[other_player][1][1] = user_data[other_player][1][1] + user_data[player][1][1]
                            var[1] = "right hand attacks right hand!";
                            break
                var[1] = "their right hand but on an invalid target!";
            else:
                var[1] = "their nonexistant right hand so it failed!";
            flag2 = False;
            
        #actions
        #do a break when criteria
        print("\n"*3);
        if flag2:
            var[1] = "an invalid move, retry!";
        info(flag2);
        
            
    
