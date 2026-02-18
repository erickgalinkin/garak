# SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Provide feedback, recommendations, and qualitative feedback on scan results.
"""

import pandas as pd
from pathlib import Path

from garak.analyze.deep_analysis.analytics import *
from garak.analyze.deep_analysis.probe_groups import TIER_1_PROBE_GROUPS


@lru_cache
def load_scores(filepath: Path) -> pd.DataFrame:
    df = pd.read_csv(filepath)
    return df


def get_position(probe_name: str, score: float, filepath: Path) -> int:
    """
    Get the position of a target's probe score in relation to other models in the bag

    Parameters
    ----------
    probe_name: str: Name of the probe
    score: float: Value of the score
    filepath: Path: Path to file containing the values of models in the bag

    Returns
    -------
    position: int: The position of the model in the set of sorted scores.
    """
    scores = load_scores(filepath)
    probe_scores = np.sort(scores[probe_name].to_numpy())
    position = int(np.where(probe_scores <= score)[0])
    return position


def tier_1(analysis_dict: dict) -> dict:
    # Could make this multithreaded for efficiency. - EG
    # Probably a better way to manage this whole process
    tier_1_analyses = dict()
    if analysis_dict["jailbreak"]:
        tier_1_analyses["jailbreak"] = jailbreak(analysis_dict["jailbreak"])
    if analysis_dict["system"]:
        tier_1_analyses["system"] = system(analysis_dict["system"])
    if analysis_dict["code"]:
        tier_1_analyses["code"] = code(analysis_dict["code"])
    if analysis_dict["harm"]:
        tier_1_analyses["harm"] = harm(analysis_dict["harm"])
    if analysis_dict["training_data"]:
        tier_1_analyses["training_data"] = training_data(analysis_dict["training_data"])
    if analysis_dict["bypass"]:
        tier_1_analyses["bypass"] = bypass(analysis_dict["bypass"])
    return tier_1_analyses


def tier_2(analysis_dict: dict) -> str:
    # Save tier 2 analysis for next iteration
    raise NotImplementedError


def deep_analysis(report_path) -> dict:
    """
    Take garak report jsonl file and perform qualitative analysis on the probe results for the target.

    Parameters
    ----------
    report_path: Path: Path to garak report file

    Returns
    -------
    Dictionary of Tier 1 analysis results by probe group.

    """
    evals = dict()
    with open(report_path, "r", encoding="utf-8") as reportfile:
        for line in reportfile:
            record = json.loads(line.strip())
            if record["entry_type"] == "eval":
                probe = record["probe"].replace("probes.", "")
                detector = record["detector"].replace("detector.", "")
                score = record["passed"] / record["total"] if record["total"] else 0
                instances = record["total"]
                if probe not in evals.keys():
                    evals[probe] = {
                        "detector": detector,
                        "score": score,
                        "instances": instances,
                    }

    # Tier 1 analysis
    tier_1_results = dict()
    for k, v in TIER_1_PROBE_GROUPS.items():
        tier_1_results[k] = dict()
        for probe_name in v:
            if probe_name in evals:
                overall_score = evals[probe_name]["score"]
                instances = evals[probe_name]["instances"]
                tier_1_results[k][probe_name] = {
                    "score": overall_score,
                    "instances": instances,
                }
    tier_1_analysis = tier_1(tier_1_results)

    # Tier 2 analysis

    return tier_1_analysis
