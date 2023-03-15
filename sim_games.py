import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from random import random

# Each region offsets slots by known amount
region_offset = {'South':0,
                'Greenville 1':0,
                'East':32,
                'Seattle 4':32,
                'West':64,
                'Seattle 3':64,
                'Midwest':96,
                'Greenville 2':96}
    

def sim_game(bracket, round, region, slot, norm_fit):

    team_idxs = bracket.index.values
    round_idx = 'rd'+str(round)+'_win'

    # Make list of possible slots to find remaining opponent
    if round == 1:
        opp_slot = slot+1 if slot%2 == 0 else slot-1
        slot += region_offset[region]
        opp_slot += region_offset[region]
        possible_slots = [slot, opp_slot]
    elif round < 6:
        slot_divisor = 2**round
        slot_remainder = slot%slot_divisor
        base_slot = slot-slot_remainder
        base_slot += region_offset[region]
        possible_slots = np.arange(base_slot,base_slot+slot_divisor)
    
    # Find team1 and team2
    team1idx = None
    team2idx = None
    team_idx = 0
    while team1idx == None and team_idx <= max(team_idxs):
        team = bracket.loc[team_idx]
        if (team['team_slot'] in possible_slots) and (team[round_idx] > 0) and (team[round_idx] < 1):
            team1idx = team_idx
        team_idx += 1
    while team2idx == None and team_idx <= max(team_idxs):
        team = bracket.loc[team_idx]
        if (team['team_slot'] in possible_slots) and (team[round_idx] > 0) and (team[round_idx] < 1):
            team2idx = team_idx
        team_idx += 1
    if team2idx == None:
        raise ValueError('Could not find 2 remaining teams in this slot!')
    teams = []
    for i in [team1idx, team2idx]:
        teams.append(bracket.loc[i])

    # Simulate game
    ratings = [team['team_rating'] for team in teams]
    rating_diff = ratings[0] - ratings[1]
    result = stats.norm(*norm_fit).cdf(rating_diff) > random()
    if result:
        winner_idx = team1idx
        loser_idx = team2idx
    else:
        winner_idx = team2idx
        loser_idx = team1idx
    bracket.loc[winner_idx,round_idx] = 1.0
    if round == 1:
        bracket.loc[loser_idx,'playin_flag'] = 0
    for future_round in np.arange(round,8):
        future_round_idx = 'rd'+str(future_round)+'_win'
        bracket.loc[loser_idx,future_round_idx] = 0.0
    print('#{} {} defeats #{} {}'.format(bracket.loc[winner_idx,'team_seed'],
                                         bracket.loc[winner_idx,'team_name'],
                                         bracket.loc[loser_idx,'team_seed'],
                                         bracket.loc[loser_idx,'team_name']),end='')
    if round < 6:
        print(' in the {} region'.format(region))
    else: print('')

    return bracket


def sim_playin(bracket, norm_fit):

    print ('Round #1 (First Four)\n')

    team_idxs = bracket.index.values

    for team_idx in team_idxs:
        team = bracket.loc[team_idx]
        if team['playin_flag'] and team['rd1_win'] < 1.0:
            slot = team['team_slot']
            region = team['team_region']
            slot -= region_offset[region]
            bracket = sim_game(bracket, 1, region, slot, norm_fit)
