# Remove-AI-Watermarks - AI画像透かし除去ツール

## 概要
AI生成画像に埋め込まれた可視・不可視の透かしを無料で除去できるオープンソースツール「Remove-AI-Watermarks」が公開された。

## 主な機能
- 可視透かし（Geminiのスパークルロゴなど）の除去
- 不可視透かし（GoogleのSynthID、C2PAなど）の除去
- メタデータ（EXIF、XMPなど）の削除
- 一括処理や解析機能も搭載

## 使い方
- GitHubで公開されており、Python経由でインストール可能。
- Web版（https://raiw.cc/）もあるようです。

## 背景と議論
- AI画像の透かしは、偽情報対策やコンテンツの出所管理のためにGoogleなどが導入している。
- このツールはそれをまとめて除去できる。
- Hacker Newsでは「プライバシーの観点で肯定的」という声がある一方、「AI画像を本物と偽りやすくなる」という懸念も指摘されている（ツールのREADMEにも「合法的な使用のみ」と明記されています）。

## ソース
- 記事: https://gigazine.net/news/20260531-remove-ai-watermarks/
- Web版: https://raiw.cc/
