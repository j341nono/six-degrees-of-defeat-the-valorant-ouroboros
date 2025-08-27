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
    

def network(match_data: list, idx_to_team: dict, team_to_idx: dict):
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

    print(team_edges)


    team_node = []
    # for team_id in len(idx_to_team):
    #     team_node.append(team_id)
    
    # G = nx.DiGrapsh()
    # G.add_node_from(team_node)




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

def debug_network():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    network(match_data, idx_to_team, team_to_idx)


if __name__ == "__main__":
    debug_network()