import json
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--find_shortest_path", action="store_true")
    parser.add_argument("--min", action="store_true")
    return parser.parse_args()

def load_json_line(path: str) -> list:
    match_list = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            match_list.append(json.loads(line))
    return match_list
            

def get_set_all_team(match_data: list) -> set:
    all_team = set()
    for one_match in match_data:
        all_team.add(one_match.get("team1"))
        all_team.add(one_match.get("team2"))
    return all_team    


def make_team_to_idx_dict(match_data: list) -> tuple[dict[str, int], dict[int, str]]:
    all_team = get_set_all_team(match_data)

    team_to_idx = {}
    idx_to_team = {}
    for i, team in enumerate(sorted(list(all_team))):
        team_to_idx[team] = i
        idx_to_team[i] = team
    return team_to_idx, idx_to_team
    

def build_match_edges(match_data: list, team_to_idx: dict) -> list[tuple[int, int]]:
    team_edges = []
    for one_match in match_data:
        team1_name = one_match.get("team1")
        team2_name = one_match.get("team2")
        team1_id = team_to_idx.get(team1_name)
        team2_id = team_to_idx.get(team2_name)

        if one_match.get("score1") > one_match.get("score2"):            
            team_edges.append((team1_id, team2_id))
        else:
            team_edges.append((team2_id, team1_id))
    return team_edges


# def get_all_exist_team(match_data: list):
#     all_team = get_set_all_team(match_data)

    
