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


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "ok"}
