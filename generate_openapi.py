#!/usr/bin/env python3
"""
OpenAPI仕様を生成してJSONファイルとして保存するスクリプト
"""

import json
import os
import sys
from pathlib import Path

try:
    sys.path.append('src')
    from src.api.api import app
except ImportError as e:
    print(f"FastAPIアプリのインポートに失敗しました: {e}")
    print("src/main.py にあなたのFastAPIアプリがあることを確認してください")
    sys.exit(1)

def generate_openapi_spec():
    docs_dir = Path("docs")
    docs_dir.mkdir(exist_ok=True)
    
    try:
        openapi_spec = app.openapi()
        
        openapi_spec["info"]["title"] = "Six Degrees of Defeat: Valorant API"
        openapi_spec["info"]["description"] = "Valorantプロチーム間の勝利経路を探索するAPI"
        openapi_spec["info"]["version"] = "1.0.0"
        
        output_file = docs_dir / "openapi.json"
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(openapi_spec, f, ensure_ascii=False, indent=2)
        
        print(f"✅ OpenAPI仕様を {output_file} に生成しました")
        return True
        
    except Exception as e:
        print(f"❌ OpenAPI仕様の生成に失敗しました: {e}")
        return False

if __name__ == "__main__":
    success = generate_openapi_spec()
    sys.exit(0 if success else 1)