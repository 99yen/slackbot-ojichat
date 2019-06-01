# Slackbot-ojichat
ojichat( https://github.com/greymd/ojichat )をSlack bot化します。
Python 3.5以降が必要です。

## インストール

1. ojichatのバイナリを適当な位置に配置してください。
2. https://my.slack.com/services/new/bot へアクセスしてbotを作成し、API Tokenを取得します。
2. `git clone https://github.com/99yen/slackbot-ojichat.git`
3. `pip install -r requirements.txt`
4. `cp slackbot_settings_sample.py slackbot_settings.py`
5. slackbot_settings.pyのうち、API_TOKENとOJICHAT_PATHを最低限編集してください。
6. `python run.py`

## 開発環境
- Python 3.7.2
- Ojichat 0.1.0

## ライセンス
MIT License
