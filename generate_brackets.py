'''
Set upset preference: 
0 = All favorites win ("chalk" bracket)
50 = Normal odds
100 = Completely random ("coin flip" bracket - 16 seeds could win)

Recommended setting: 40
'''
upset_preference = 40
num_brackets = 1

from import_538 import import_538
from sim_games import sim_bracket
import numpy as np

fn = 'fivethirtyeight_ncaa_forecasts_24.csv' # As of 2024: Using RPI regressed to 538 models, 538 no longer does sports

for i in range(num_brackets):
    
    men, women, norm_fit = import_538(fn)
    
    upset_preference = 40-np.floor(i/5)*10
    
    print('\n')
    print('=======================================')
    print("=          Men's bracket #{:00}          =".format(i))
    print("=           Randomness: {:00}%           =".format(int(upset_preference)))
    print('=======================================')

    men = sim_bracket(men, norm_fit, upset_preference)

    print('\n')
    print('=======================================')
    print("=         Women's bracket #{:00}         =".format(i))
    print("=           Randomness: {:00}%           =".format(int(upset_preference)))
    print('=======================================')

    women = sim_bracket(women, norm_fit, upset_preference)