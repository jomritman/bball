from import_538 import import_538
from sim_games import sim_game

fn = 'fivethirtyeight_ncaa_forecasts.csv'

men, women, norm_fit = import_538(fn)

sim_game(men, 3, 'Midwest', 1, norm_fit)