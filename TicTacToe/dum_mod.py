
def win_check(ind):

    to_win = [[1,5,9],[3,5,7],[1,4,7],[2,5,8],[3,6,9],[1,2,3],[4,5,6],[7,8,9]]

    o_ind,x_ind = ind
    count_x = 0 
    count_o = 0 

    for i in range(len(to_win)):

        for j in range(3):
            if to_win[i][j] in x_ind:
                count_x +=1
            
            elif to_win[i][j] in o_ind:
                count_o += 1

        if count_o == 3 or count_x == 3:
            break
        else:
            count_x = 0
            count_o = 0

    if count_o == 3:
        return 'o'

    elif count_x == 3:
        return 'x'
    
    else:
        return 0
