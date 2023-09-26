import numpy as np

def find_cumm_return(red_cards,black_cards):
    cumm_return = [[0 for _ in range(black_cards+1)] for _ in range(red_cards+1)]
    for i in range(red_cards+1):
        for j in range(black_cards+1):
            cumm_return[black_cards-j][red_cards-i] = max(j-i,0)
    return(cumm_return)
cumm_return_df = find_cumm_return(26,26)

def find_exp_return(red_cards, black_cards):
    exp_return = [[0 for _ in range(black_cards + 1)] for _ in range(red_cards + 1)]

    # Initialize the base cases
    for i_drawn in reversed(range(0,black_cards)):
        exp_return[26][i_drawn] = 0
    for j_drawn in reversed(range(0,black_cards)):
        exp_return[j_drawn][26] = black_cards - j_drawn
    #for i in range(0,red_cards + 1):
        #dp[i][0] = -1

    # Fill in the DP table iteratively
    for i_draws in reversed(range(0, red_cards)):
        for j_draws in reversed(range(0, black_cards)):
            red_prob = (black_cards-i_draws) / ((black_cards-i_draws) + (red_cards-j_draws))
            black_prob = (red_cards- j_draws) / ((black_cards-i_draws) + (red_cards-j_draws))
            exp_return_tp = red_prob * exp_return[i_draws + 1][j_draws] + black_prob * (exp_return[i_draws][j_draws+1])
            exp_return[i_draws][j_draws] = max(exp_return_tp, cumm_return_df[i_draws][j_draws])
    return exp_return

exp_return = find_exp_return(26,26)
np_cumm_return = np.array(cumm_return_df)
np_exp_return = np.array(exp_return)
np_exp_return_rounded = list(np.around(np.array(exp_return),2))
print(np_exp_return_rounded[0][0])




