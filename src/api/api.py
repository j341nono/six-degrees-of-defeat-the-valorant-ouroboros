import argparse
import networkx as nx
from src.models.utils import (
    load_json_line,
    make_team_to_idx_dict,
    build_match_edges,
)
from src.models.network import (
    build_network,
    find_shortest_path,
    is_name_exist,
)
from fastapi import FastAPI

SAVE_MATCH_DATA="data/processed/match_data.jsonl"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/paths/shortest")
async def _find_shortest_path(from_team: str, to_team: str):
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, idx_to_team = make_team_to_idx_dict(match_data)

    missing_team_list = []
    if is_name_exist(from_team, team_to_idx):
        missing_team_list.append(from_team)

    if is_name_exist(to_team, team_to_idx):
        missing_team_list.append(to_team)
    
    if len(missing_team_list):
        return {
            "error": "Team not found",
            "missing_teams": missing_team_list,
        }

    from_team_idx = team_to_idx.get(from_team)
    to_team_idx = team_to_idx.get(to_team)

    team_edges = build_match_edges(match_data, team_to_idx)
    DG = build_network(idx_to_team, team_edges)

    team_idx_path_list = find_shortest_path(DG=DG, from_team=from_team_idx, to_team=to_team_idx)
    if isinstance(team_idx_path_list, int):
        return {
            "from": from_team,
            "to": to_team,
            "message": "No path found",
        }
    
    team_name_path_list = []
    for idx_team in team_idx_path_list:
        team_name_path_list.append(idx_to_team.get(idx_team))
    
    return {
        "from": from_team,
        "to": to_team,
        "path": [team_name_path_list],
    }


@app.get("/teams/exists")
async def _get_all_exist_team():
    match_data = load_json_line(SAVE_MATCH_DATA)
    


@app.get("/teams/{team_name}")
async def _is_team_exist(team_name: str):
    match_data = load_json_line(SAVE_MATCH_DATA)
    team_to_idx, _ = make_team_to_idx_dict(match_data)
    exist_flg = True
    if is_name_exist(team_name, team_to_idx):
        exist_flg = False
    return {
        "exist": exist_flg,
    }

