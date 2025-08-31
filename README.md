# Six Degrees of Defeat: The Valorant Ouroboros

Valorantプロシーンの勝敗データに基づき、あるチームから別のチームへの間接的な勝利の連鎖（"A > B > C"のような関係）を見つけ出すツールです。  
結果はFastAPIを使用したREST APIを通じて提供されます。

This tool finds indirect victory paths between professional Valorant teams based on match data (e.g., "A > B > C").  
The results are provided via a REST API built with FastAPI.

## 機能 (Features)

- 指定された2チーム間の勝利経路を探索 (Find victory paths between two specified teams)
- 存在する全チームを返す (Return all existing teams)
- ユーザーが指定したチームが存在するかどうかを確認 (Check if a specified team exists)
- ヘルスチェック (Health check)

## 前提条件 (Prerequisites)

- [uv](https://github.com/astral-sh/uv) が利用可能であること
- Python 3.8+

## セットアップ (Setup)

1. リポジトリをクローン
```bash
git clone <repository-url>
cd six-degrees-of-defeat
```

2. 試合データをダウンロード
```bash
./data_processor.sh
```

3. APIを起動
```bash
./run_api.sh
```

APIサーバーは `http://127.0.0.1:8000` で起動します。

## APIエンドポイント (API Endpoints)

### 最短経路を取得
```
GET /paths/shortest?from={team_a}&to={team_b}
```
指定された2チーム間の最短勝利経路を返します。

### 存在する全チーム一覧
```
GET /teams/exists
```
データベースに存在するすべてのチーム名を返します。

### チーム存在確認
```
GET /teams/{team_name}
```
指定されたチームが存在するかどうかを確認します。

### ヘルスチェック
```
GET /health
```
APIサーバーの稼働状況を確認します。

## 技術スタック (Tech Stack)

- **FastAPI**: REST APIフレームワーク
- **Python**: バックエンド言語
- **uv**: パッケージ管理・実行環境

## APIドキュメント (API Documentation)

FastAPIの自動生成ドキュメントは以下のURLで確認できます：
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## ライセンス (License)

このプロジェクトは[MIT License](LICENSE)の下で公開されています。
