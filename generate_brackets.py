from import_538 import import_538
from sim_games import sim_playin

fn = 'fivethirtyeight_ncaa_forecasts.csv'

men, women, norm_fit = import_538(fn)

sim_playin(men, norm_fit)