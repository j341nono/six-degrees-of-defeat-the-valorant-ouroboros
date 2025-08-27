import argparse
import json

SAVE_MATCH_DATA="data/processed/match_data.jsonl"


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max", action="store_true")
    parser.add_argument("--min", action="store_true")
    return parser.parse_args()


def load_json(path: str) -> list:
    match_list = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            match_list.append(json.loads(line))
    return match_list
            

def main():
    args = parse_args()



def debug():
    match_data = load_json(SAVE_MATCH_DATA)
    print(match_data[:2])
    print(f"data num: {len(match_data)}")


if __name__ == "__main__":
    debug()