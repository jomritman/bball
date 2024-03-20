import numpy as np
from import_538 import import_538
from sim_games import sim_bracket

fn = 'fivethirtyeight_ncaa_forecasts_24.csv'

'''
Set upset preference: 
0 = All favorites win
50 = Normal odds
100 = All upsets win
Recommended setting: 40
'''
upset_preference = 50

men, women, norm_fit = import_538(fn)

cats_idx = np.where(men['team_name'].values == 'Vermont')[0][0]
while men.loc[cats_idx,'rd3_win'] < 1.0:

    men, women, norm_fit = import_538(fn)

    print('\n')
    print('=======================================')
    print("=            Men's bracket            =")
    print('=======================================')

    men_result = sim_bracket(men, norm_fit, upset_preference)

    print('\n')
    print('=======================================')
    print("=           Women's bracket           =")
    print('=======================================')

    women_result = sim_bracket(women, norm_fit, upset_preference)