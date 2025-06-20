import votekit
import pandas as pd
#from gerrychain import Graph
import jsonlines as jl
import votekit.elections as elec
from votekit import PreferenceProfile
import votekit.ballot_generator as bg
from glob import glob
import json
from tqdm import tqdm

elec_df = pd.read_parquet("./JeffersonData/Jefferson_elections.parquet")
vap_df = pd.read_parquet("./JeffersonData/Jefferson_vap.parquet")

sum_elec_df = elec_df.sum()
print(sum_elec_df)
print(vap_df.head())
print(elec_df.columns)
dem_per = sum_elec_df["pres_20_dem"]
rep_per = sum_elec_df["pres_20_rep"]
total_votes = dem_per + rep_per
dem_per = dem_per/total_votes
rep_per = rep_per/total_votes
print(dem_per,rep_per)
"""
bloc_voter_prop = {
    "D": dem_per,
    "R": rep_per
}
cohesion_parameters = {
    "D": {
        "D": 0.9,
        "R": 0.1
    },
    "R": {
        "D": 0.9,
        "R": 0.1
    }
}
alphas = {
    "D": {
        "D": 1,
        "R": 1
    },
    "R": {
        "D": 1,
        "R": 1
    }
}
slate_to_candidates = {
    "D": [
        "D1",
        "D2",
        "D3",
        "D4",
        "D5"
    ],
    "R": [
        "R1",
        "R2",
        "R3",
        "R4",
        "R5"
    ]
}
"""

settings_files = glob("../vk_run_settings/*.json")
#settings_files = settings_files[:10]
print(settings_files)
with jl.open('partisan_election_results.jsonl','w') as writer:
    for setting_file in tqdm(settings_files):
        with open(setting_file, "r") as f:
            ballot_generator_kwargs = json.load(f)
            if ballot_generator_kwargs is None:
                ballot_generator_kwargs = {}

        for trials in tqdm(range(100),leave=False):
            profile = bg.slate_PlackettLuce.from_params(**ballot_generator_kwargs).generate_profile(number_of_ballots=10000)

            election = elec.STV(profile, m=3)
            writer.write({
                "winners": [winner for winner_set in election.get_elected() for winner in winner_set],
                "dem_percent": ballot_generator_kwargs["bloc_voter_prop"]["D"],
                "cohesion": ballot_generator_kwargs["cohesion_parameters"]["D"]["D"],
                "m":3
                })
            #print(election)

