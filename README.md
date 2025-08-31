# Six Degrees of Defeat: The Valorant Ouroboros
Valorantプロシーンの勝敗データに基づき，あるチームから別のチームへの間接的な勝利の連鎖（"A > B > C"のような関係）を見つけ出すツールです．
結果はREST APIを通じて提供されます．

This tool finds indirect victory paths between professional Valorant teams based on match data (e.g., "A > B > C"). The results are provided via a REST API.

## 機能 (Features)
- 指定された2チーム間の勝利経路を探索
- health check

## APIのエンドポイント
- 最短経路を取得する
    - /paths/shortest?from=A&to=B
- ヘルステェック
    - /health
