import argparse
import json
import networkx as nx

SAVE_MATCH_DATA="data/processed/match_data.jsonl"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", action="store_true")
    parser.add_argument("--min", action="store_true")
    return parser.parse_args()


def load_json_line(path: str) -> list:
    match_list = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            match_list.append(json.loads(line))
    return match_list
            

def make_team_to_idx_dict(match_data: list) -> tuple[dict[str, int], dict[int, str]]:
    all_team = set()
    for one_match in match_data:
        all_team.add(one_match.get("team1"))
        all_team.add(one_match.get("team2"))

    team_to_idx = {}
    idx_to_team = {}
    for i, team in enumerate(sorted(list(all_team))):
        team_to_idx[team] = i
        idx_to_team[i] = team
    return team_to_idx, idx_to_team


def add_winner(match_data: list) -> None:
    for one_match in match_data:
        if one_match.get("score1") > one_match.get("score2"):
            one_match["winner"] = one_match.get("team1")
        else:
            one_match["winner"] = one_match.get("team2")
            

def network(match_data: list, idx_to_team: dict):
    for one_match in match_data:
        one_match.get("winner")


    G = nx.DiGrapsh()




def main():
    args = parse_args()
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    print(len(team_to_idx))



def debug_load_json():
    match_data = load_json_line(SAVE_MATCH_DATA)
    print(match_data[:2])
    print(f"data num: {len(match_data)}")

def debug_make_dict():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_id = {}
    for one_match in match_data:
        team1 = one_match.get("team1")
        team2 = one_match.get("team2")
        print(team1)
        import sys
        sys.exit()

def debug_make_team_to_idx():
    match_data = load_json_line(SAVE_MATCH_DATA)
    all_team = set()
    for one_match in match_data:
        all_team.add(one_match.get("team1"))
        all_team.add(one_match.get("team2"))
    team_to_idx = {}
    idx_to_team = {}
    for i, team in enumerate(sorted(list(all_team))):
        team_to_idx[team] = i
        idx_to_team[i] = team
    # print(team_to_idx)
    print(idx_to_team)

def debug_win_func():
    match_data = load_json_line(SAVE_MATCH_DATA)
    add_winner(match_data)
    print(match_data[:2])


if __name__ == "__main__":
    debug_win_func()