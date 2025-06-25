from itertools import product
import json
from pathlib import Path
import numpy as np


if __name__ == "__main__":
    hisp_props = np.linspace(0.15, 0.5, num=7)
    for hisp_prop in hisp_props:
        output_settings = {
            "bloc_voter_prop": {"hisp": hisp_prop, "non-hisp": 1-hisp_prop},
            "cohesion_parameters" : {
                "hisp": {"hisp": 0.8, "non-hisp": 0.2},
                "non-hisp": {"hisp": 0.6, "non-hisp": 0.4},
            },
            "alphas": {"hisp": {"hisp": 1, "non-hisp": 1},
                       "non-hisp": {"hisp": 1, "non-hisp": 1}},
            "slate_to_candidates" : {
                "hisp": ["D1", "D2", "D3", "D4", "D5"], 
                "non-hisp": ["R1", "R2", "R4", "R5"]},
        }

        output_dir = Path("./jefferson_run_settings")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = "." / Path(
            f"jefferson_run_settings/hisp_prop_{hisp_prop:.3g}_hisp_coh_0p8_non_hisp_coh_0p5".replace(
                ".", "p"
            )
            + ".json"
        )

        with open(output_path, "w") as f:
            json.dump(output_settings, f, indent=4)






'''
    wc_pairs = [
        (1.0, 0.0),
        (0.95, 0.05),
        (0.9, 0.1),
        (0.85, 0.15),
        (0.8, 0.2),
        (0.75, 0.25),
        (0.7, 0.3),
        (0.65, 0.35),
        (0.6, 0.4),
        (0.55, 0.45),
        (0.5, 0.5),
        (0.45, 0.55),
        (0.4, 0.6),
        (0.35, 0.65),
        (0.3, 0.7),
        (0.25, 0.75),
        (0.2, 0.8),
        (0.15, 0.85),
        (0.1, 0.9),
        (0.05, 0.95),
        (0.0, 1.0),
    ]

    coh_dict = {
        (0.9, 0.1, 0.9, 0.1),
        (0.8, 0.2, 0.8, 0.2),
        (0.7, 0.3, 0.7, 0.3),
        (0.6, 0.4, 0.6, 0.4),
        (0.5, 0.5, 0.5, 0.5),
        (0.4, 0.6, 0.4, 0.6),
    }

    for wc_pair, coh_tup in product(wc_pairs, coh_dict):
        output_settings = dict(
            bloc_voter_prop={"W": wc_pair[0], "C": wc_pair[1]},
            cohesion_parameters={
                "W": {"W": coh_tup[0], "C": coh_tup[1]},
                "C": {"W": coh_tup[2], "C": coh_tup[3]},
            },
            alphas={"W": {"W": 1, "C": 1}, "C": {"W": 1, "C": 1}},
            slate_to_candidates={"W": ["W1", "W2", "W3"], "C": ["C1", "C2"]},
        )

        output_dir = Path("../vk_run_settings")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = ".." / Path(
            f"vk_run_settings/wc_({wc_pair[0]}_{wc_pair[1]})_cohesion_({coh_tup[0]}_{coh_tup[1]}_{coh_tup[2]}_{coh_tup[3]})".replace(
                ".", "p"
            )
            + ".json"
        )

        with open(output_path, "w") as f:
            json.dump(output_settings, f, indent=4)

'''
