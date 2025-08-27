import networkx as nx
from src.models.utils import (
    parse_args,
    load_json_line,
    make_team_to_idx_dict,
    build_match_edges
) 

SAVE_MATCH_DATA="data/processed/match_data.jsonl"


def build_network(
        idx_to_team: dict, 
        team_edges: list[tuple[int, int]]
    ) -> None:

    team_node = []
    for team_id in range(len(idx_to_team)):
        team_node.append(team_id)
    
    DG = nx.DiGraph()
    DG.add_nodes_from(team_node)
    DG.add_edges_from(team_edges)
    return DG


def find_shortest_path(DG: nx.DiGraph, win_team: str, loss_team: str):
    try:
        return nx.shortest_path(DG, source=win_team, target=loss_team)
    except nx.exception.NetworkXNoPath:
        print(f"No path between {win_team} to {loss_team}")
        import sys
        sys.exit()


def main():
    args = parse_args()
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)
    




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

def debug_build_match_edges():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    team_edges = build_match_edges(match_data, team_to_idx)
    print(team_edges)

def debug_build_graph():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)
    
    print(f"list(DG.nodes): {list(DG.nodes)}")
    print(f"list(DG.edges): {list(DG.edges)}")
    print(f"list(DG.ad): {list(DG.adj[1])}")
    print(f"DG.degree[1]: {DG.degree[1]}")

def debug_find_shortest_path():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)

    win_team_id = 135
    loss_team_id = 111
    print(f"win_team: {idx_to_team.get(win_team_id)}")
    print(f"loss_team: {idx_to_team.get(loss_team_id)}")
    path = find_shortest_path(DG, win_team_id, loss_team_id)
    print(path)


def debug_search_team():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    print(team_to_idx.get("G2 Esports")) # 135
    print(team_to_idx.get("FNATIC")) # 111


if __name__ == "__main__":
    debug_find_shortest_path()
    # debug_search_team()