#!/usr/bin/env python3
"""
Hermes Agentの会話セッションをGitHubリポジトリに保存するスクリプト
"""
import os
import sys
import json
import subprocess
from datetime import datetime

REPO_PATH = "/workspace/hermes-conversations"
SESSIONS_DIR = os.path.join(REPO_PATH, "sessions")

def get_session_info():
    """現在のセッション情報を取得（環境変数から）"""
    session_id = os.environ.get("HERMES_SESSION_ID", "unknown")
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return session_id, timestamp

def save_conversation(session_id, timestamp, content):
    """会話内容をファイルに保存"""
    os.makedirs(SESSIONS_DIR, exist_ok=True)
    
    filename = f"session_{timestamp}_{session_id[:8]}.md"
    filepath = os.path.join(SESSIONS_DIR, filename)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(f"# Session {session_id}\n\n")
        f.write(f"**保存日時**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write("---\n\n")
        f.write(content)
    
    return filepath

def git_commit_push(filepath, session_id):
    """Gitにコミットしてプッシュ"""
    os.chdir(REPO_PATH)
    
    # Git設定確認
    subprocess.run(['git', 'config', 'user.email', 'yosshi33@github.com'], check=True)
    subprocess.run(['git', 'config', 'user.name', 'yosshi33'], check=True)
    
    # リモートURLをトークン付きに更新
    token = os.environ.get('GITHUB_TOKEN', '')
    remote_url = f"https://yosshi33:{token}@github.com/yosshi33/hermes-conversations.git"
    subprocess.run(['git', 'remote', 'set-url', 'origin', remote_url], check=True)
    
    # 追加・コミット・プッシュ
    subprocess.run(['git', 'add', filepath], check=True)
    commit_msg = f"Save session {session_id[:8]} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
    subprocess.run(['git', 'push', 'origin', 'main'], check=True)
    
    print(f"✓ セッションを保存しました: {filepath}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python save-session.py '<会話内容>'")
        sys.exit(1)
    
    content = sys.argv[1]
    session_id, timestamp = get_session_info()
    
    try:
        filepath = save_conversation(session_id, timestamp, content)
        git_commit_push(filepath, session_id)
    except Exception as e:
        print(f"エラー: {e}")
        sys.exit(1)
