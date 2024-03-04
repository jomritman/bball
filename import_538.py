import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.ion()
import scipy.stats as stats

#fn = 'fivethirtyeight_ncaa_forecasts.csv'

def import_538(fn, redo_fit=False, plot_flag=False):

    # Read dataframe               
    teams = pd.read_csv(fn)

    if redo_fit:

        # Back out opening round percentage correlation to rating differential
        rating_diffs = []
        win_pcts = []
        team_idxs = teams.index.values
        opp_playin = pd.Series(np.zeros(len(team_idxs)), index=team_idxs, name='opp_playin_flag')
        teams = teams.join(opp_playin)
        for team_idx in team_idxs:
            include_open_pct = True
            team = teams.loc[team_idx]
            gender = team['gender']
            team_slot = team['team_slot']
            if team['playin_flag']:
                win_pct = team['rd1_win']
                opponent_slot = team_slot+1 if team_slot%2 == 0 else team_slot - 1
                opponent_idx = teams.index.values[np.argwhere(np.logical_and((teams['team_slot'].values==opponent_slot),
                                                                            (teams['gender'].values==gender)))[0,0]]
            else:
                win_pct = team['rd2_win']
                opponent_slot = team_slot+2 if team_slot%4 == 0 else team_slot - 2
                opponent_idx = teams.index.values[np.argwhere(np.logical_and((teams['team_slot'].values==opponent_slot),
                                                                            (teams['gender'].values==gender)))[0,0]]
                # Check that 2nd round teams are not playing a play-in team,
                # this ruins their round 2 win percentage
                if teams.loc[opponent_idx,'playin_flag']:
                    teams.loc[team_idx,'opp_playin_flag'] = 1
                    include_open_pct = False
            if include_open_pct:
                win_pcts.append(win_pct)
                team_rating = team['team_rating']
                opponent_rating = teams.loc[opponent_idx,'team_rating']
                rating_diffs.append(team_rating-opponent_rating)
        data = np.vstack((rating_diffs,win_pcts))
        norm_fit = stats.norm.fit(data)

        if plot_flag:
            # Plot to check
            plt.plot(rating_diffs,win_pcts,'.')
            int = 0.1
            diff = np.arange(-50,50+int,int)
            plt.plot(diff,stats.norm(*norm_fit).cdf(diff))
            plt.show()

    else:
        norm_fit = (0.24999999999999997, 9.842497752546377)

    men_idxs = np.where(teams['gender'].values=='mens')[0]
    mens_teams = teams.loc[men_idxs]
    mens_teams.index = np.arange(0,mens_teams.shape[0])
    women_idxs = np.where(teams['gender'].values=='womens')[0]
    womens_teams = teams.loc[women_idxs]
    womens_teams.index = np.arange(0,womens_teams.shape[0])
    
    return mens_teams, womens_teams, norm_fit

if __name__ == '__main__':

    fn = 'fivethirtyeight_ncaa_forecasts.csv'
    
    mens_teams, womens_teams, norm_fit = import_538(fn, False, False)