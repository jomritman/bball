from import_538 import import_538
from sim_games import sim_bracket

fn = 'fivethirtyeight_ncaa_forecasts_24.csv'

'''
Set upset preference: 
0 = All favorites win
50 = Normal odds
100 = All upsets win

Recommended setting: 40
(Only teams with at least 10% chance
will ever actually win a game)
'''
upset_preference = 40

men, women, norm_fit = import_538(fn)

print('\n')
print('=======================================')
print("=            Men's bracket            =")
print('=======================================')

men = sim_bracket(men, norm_fit, upset_preference)

print('\n')
print('=======================================')
print("=           Women's bracket           =")
print('=======================================')

women = sim_bracket(women, norm_fit, upset_preference)