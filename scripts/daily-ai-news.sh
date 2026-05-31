#!/bin/bash
# 毎朝7時のAIニュース収集・LINE送信スクリプト

set -e

# 設定
REPO_PATH="/workspace/hermes-conversations"
NEWS_DIR="$REPO_PATH/news"
TODAY=$(date +%Y-%m-%d)
NEWS_FILE="$NEWS_DIR/${TODAY}.md"
GITHUB_TOKEN="${GITHUB_TOKEN}"
LINE_TOKEN="${LINE_CHANNEL_ACCESS_TOKEN}"
LINE_USER_ID="${LINE_USER_ID:-}"  # デフォルトの送信先（設定されていれば）

mkdir -p "$NEWS_DIR"

echo "📰 AIニュース収集開始: $TODAY"

# ニュース収集（Web検索を模擬・実際はHermes Agentのタスクで実行）
# このスクリプトはCronジョブのプロンプトから呼び出される

# プレースホルダー（実際の収集はPythonで行う）
cat > "$NEWS_FILE" << EOF
# AIニュース要約 - ${TODAY}

## 収集対象
- ChatGPT
- Claude (Anthropic)
- Gemini (Google)

## ニュース一覧

（ここに収集したニュースが入ります）

EOF

echo "✓ ニュースファイル作成: $NEWS_FILE"

# Git操作
cd "$REPO_PATH"
git config user.email "yosshi33@github.com"
git config user.name "yosshi33"
git remote set-url origin "https://yosshi33:${GITHUB_TOKEN}@github.com/yosshi33/hermes-conversations.git"
git add "$NEWS_FILE"
git commit -m "Daily AI news: ${TODAY}" || echo "No changes to commit"
git push origin main

echo "✓ GitHubプッシュ完了"

# LINE送信（プレースホルダー）
if [ -n "$LINE_TOKEN" ]; then
    echo "📱 LINE送信準備..."
    # 実際の送信はPythonスクリプトで行う
fi

echo "完了！"
