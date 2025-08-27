# API メタデータ仕様

本プロジェクトで利用する API から取得できるメタデータのうち、重要な部分である data/segments の構造を以下に示す。

```json
[
  {
    "team1": "ONSIDE GAMING",       // チーム1の名前
    "team2": "Dplus Esports",       // チーム2の名前
    "score1": "2",                  // チーム1のスコア
    "score2": "1",                  // チーム2のスコア
    "flag1": "flag_kr",             // チーム1の国旗アイコン (コード)
    "flag2": "flag_kr",             // チーム2の国旗アイコン (コード)
    "time_completed": "4h 51m ago", // 試合終了からの経過時間
    "round_info": "Main Event-Lower Round 1", // 試合ラウンド情報
    "tournament_name": "Challengers 2025: Korea WDG Road to Ascension", // トーナメント名
    "match_page": "/528185/onside-gaming-vs-dplus-esports-challengers-2025-korea-wdg-road-to-ascension-lr1", // 試合詳細ページのパス
    "tournament_icon": "https://owcdn.net/img/6009f963577f4.png", // トーナメントのアイコンURL
    "page_number": 1                // ページ番号
  },
]
```