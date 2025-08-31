import networkx as nx
from src.models.utils import (
    load_json_line,
    make_team_to_idx_dict,
    build_match_edges,
    parse_args
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


def find_shortest_path(DG: nx.DiGraph, from_team: str, to_team: str):
    try:
        return nx.shortest_path(DG, source=from_team, target=to_team)
    except nx.exception.NetworkXNoPath:
        # print(f"No path between {from_team} to {to_team}")
        # import sys
        # sys.exit()
        return -1


def is_name_exist(name: str, team_to_idx: list) -> int:
    # match_data = load_json_line(SAVE_MATCH_DATA)
    # team_to_idx, _ = make_team_to_idx_dict(match_data)
    try:
        team_to_idx[name]
        return 0
    except KeyError:
        return -1


def main():
    args = parse_args()
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)

    from_team_id = 135
    to_team_id = 111
    if args.find_shortest_path:
        path = find_shortest_path(DG, from_team_id, to_team_id)
        print(path)




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

    from_team_id = 1
    to_team_id = 111
    # print(f"from_team: {idx_to_team.get(from_team_id)}")
    # print(f"to_team: {idx_to_team.get(to_team_id)}")
    path = find_shortest_path(DG, from_team_id, to_team_id)
    if isinstance(path, int):
        return -1
    print(path)


def debug_search_team():
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)
    print(team_to_idx.get("G2 Esports")) # 135
    print(team_to_idx.get("FNATIC")) # 111


def debug_api():
    from_team = "Fnatic"
    to_team = "T1"

    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)

    print(is_name_exist(from_team, idx_to_team))
    print(type(is_name_exist(from_team, idx_to_team)))
    print(is_name_exist(to_team, idx_to_team))
    print(type(is_name_exist(to_team, idx_to_team)))

    missing_team_list = []
    if is_name_exist(from_team, idx_to_team):
        print("missing 1")
        missing_team_list.append(from_team)

    if is_name_exist(to_team, idx_to_team):
        print("missing 2")
        missing_team_list.append(to_team)
    
    if len(missing_team_list):
        # return {
        #     "error": "Team not found",
        #     "missing_teams": missing_team_list,
        # }
        print("0")
    # print("1")

def debug_api_internal_error():
    from_team = "T1"
    to_team = "DRX"

    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)

    missing_team_list = []
    if is_name_exist(from_team, team_to_idx):
        print("missing 1")
        missing_team_list.append(from_team)

    if is_name_exist(to_team, team_to_idx):
        print("missing 2")
        missing_team_list.append(to_team)
    
    if len(missing_team_list):
        print( {
            "error": "Team not found",
            "missing_teams": missing_team_list,
        } )
        import sys; sys.exit()

    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)

    from_team_idx = team_to_idx.get(from_team)
    to_team_idx = team_to_idx.get(to_team)

    team_idx_path_list = find_shortest_path(DG=DG, from_team=from_team_idx, to_team=to_team_idx)
    print(team_idx_path_list)
    if isinstance(team_idx_path_list, int):
        print( {
            "from": from_team,
            "to": to_team,
            "message": "No path found",
        } )
        import sys; sys.exit()
    
    team_name_path_list = []
    for idx_team in team_idx_path_list:
        team_name_path_list.append(idx_to_team.get(idx_team))
    
    print( {
        "from": from_team,
        "to": to_team,
        "path": [team_name_path_list],
    } )


if __name__ == "__main__":
    # debug_find_shortest_path()
    # is_name_exist("aaaaaa")
    debug_api_internal_error()