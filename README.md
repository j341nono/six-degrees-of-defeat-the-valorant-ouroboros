# Six Degrees of Defeat: The Valorant Ouroboros
Valorantプロシーンの勝敗データに基づき、あるチームから別のチームへの間接的な勝利の連鎖（"A > B > C"のような関係）を見つけ出すツールです。結果はREST APIを通じて提供されます。

This tool finds indirect victory paths between professional Valorant teams based on match data (e.g., "A > B > C"). The results are provided via a REST API.

## 機能 (Features)
- 指定された2チーム間の勝利経路を探索
- なんらかの勝利経路を提示（最短，最長，...）
- 最新の試合結果を自動で取得
- 結果をJSON形式で返すREST API
