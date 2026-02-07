# Simple Web App (Python)

## 📖 概要
Python + Flask で作成したシンプルなWeb APIアプリです。
環境変数管理やAPI設計の練習を目的としています。

## 🛠 技術スタック
- Python
- Flask
- python-dotenv
- REST API

## 📂 機能
- `/` : Welcomeページ
- `/health` : ヘルスチェックAPI
- `/api/info` : アプリ情報取得API

## 🚀 実行方法

```bash
pip install -r requirements.txt
cp .env.example .env
python app.py
```

## ブラウザで：
http://localhost:5000

## 📌 学習内容
- FlaskによるAPI開発
- 環境変数管理
- GitHubでのプロジェクト管理

## 👤 作者
- etenix

## Features

- Flaskを使用したRESTful API
- 環境変数による設定管理（.env対応）
- JSON形式のリクエスト／レスポンス
- 基本的なエラーハンドリング

## Tech Stack

- Python 3.x
- Flask
- python-dotenv
- REST API

## Setup

1. リポジトリをクローン

```bash
git clone https://github.com/你的ID/simple-web-app-python.git
cd simple-web-app-python

2.	仮想環境を作成

python -m venv venv
source venv/bin/activate

3.	ライブラリをインストール

pip install -r requirements.txt

4.	環境変数ファイルを作成

cp .env.example .env

5.	アプリ起動

python app.py

```
## 📌 Future Improvements（今後の改善予定）

- Docker対応
- データベース連携
- 認証機能の実装
- AWSへのデプロイ