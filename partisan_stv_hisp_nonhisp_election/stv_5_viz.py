import pandas as pd
from typing import Optional
import numpy as np
from matplotlib.axes import Axes
import matplotlib.pyplot as plt

jsonl_file = "./partisan_election_results_5.jsonl"

def get_cohesions():
    election_df = pd.read_json(jsonl_file,lines = True)
    return election_df['cohesion'].tolist()

def get_percents():
    election_df = pd.read_json(jsonl_file,lines = True)
    return election_df['dem_percent'].tolist()

def filter_df(election_df, m,dem_per,cohesion):
    return election_df[(election_df.m == m) & (abs(election_df.dem_percent - dem_per) <.001)& (abs(election_df.cohesion - cohesion) < .001)]


def get_all_simulations():
    return pd.read_json(jsonl_file,lines = True)


def get_num_reps(winner_list):
    return len(list(filter(lambda x: 'R' in x, winner_list)))

def get_num_rep_win(election_df):
    winners_list = election_df['winners'].tolist()
    num_winners = [0,0,0,0,0,0] #0th element is 0 rep wins, 1st ele is 1 rep win, etc

    each_winner = []
    for trial in winners_list:
        num_reps = get_num_reps(trial)
        num_winners[num_reps] +=1
        each_winner.append(num_reps)
    return num_winners,each_winner





def bubble_plot_integer(
    data: list[list[int]],
    colors: list[str],
    ax: Optional[Axes] = None,
    marker: str =".",
    size: int = 1000,
):
    # create figure

    if ax is None:
        fig, ax = plt.subplots()

    x_max = int(max(max(vector) for vector in data))
    bin_min = 0
    bin_max = x_max
    bins = np.arange(bin_min-.5, bin_max+1.5, 1)

    for j, vector in enumerate(data):
        x = [i for i in range(x_max+1)] # x=0,...,x_max
        y = [j+1]*len(x) # put each vector at a different height

        bin_heights, _ = np.histogram(vector, bins = bins,density=True)
        circle_areas = [size*bin_heights[i] for i in range(x_max+1)]
        ax.scatter(x, y, s=circle_areas, alpha=1, color = colors[j], label = None, edgecolors='black', marker=marker)

    return ax


cohesions = sorted(list(set(get_cohesions())))
percents = sorted(list(set(get_percents())))
election_df = get_all_simulations()
cohesion = .9

each_winners = []
percent = percents[9]
cohesion = 1
for i in cohesions:
    filtered_df = filter_df(election_df, 5,percent,i)
    rep_wins,each_winner = get_num_rep_win(filtered_df)
    print(rep_wins)
    each_winners.append(each_winner)



ax = bubble_plot_integer(data = each_winners, colors = ['#deadbeef' for x in range(len(each_winners))])
ax.set_yticks(ticks = [i+1 for i in range(len(cohesions))],labels= [float(int(i*10))/10 for i in cohesions])
ax.set_xticks([i for i in range(6)])
ax.set_ylabel("Cohesion Parameter of a Group")
ax.set_xlabel("Number of Seats Won by Republicans")
plt.savefig("STV_Five_Winners.png")
plt.show()
print(rep_wins)
