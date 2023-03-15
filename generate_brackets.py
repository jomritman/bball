from import_538 import import_538
from sim_games import sim_bracket

fn = 'fivethirtyeight_ncaa_forecasts.csv'

men, women, norm_fit = import_538(fn)

print('\n')
print('=======================================')
print("=            Men's bracket            =")
print('=======================================')

men = sim_bracket(men, norm_fit)

print('\n')
print('=======================================')
print("=           Women's bracket           =")
print('=======================================')

women = sim_bracket(women, norm_fit)