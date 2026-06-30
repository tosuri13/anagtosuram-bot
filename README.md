# anagtosuram-bot

## Overview

Twitterなどでよく見る文字列を並べ替えてキャッキャするDiscord BotをAWSで構築できるテンプレートです。

uv + AWS CDK構成で作成されています。

## Build & Deploy

Discord Developer Portalから新しいApplicationsを作成し、下記を参考に`.env`ファイルを作成してください。

```
DISCORD_BOT_TOKEN=<Discord Botのトークン>
DISCORD_CHANNEL_ID=<メッセージを投稿したいチャンネルのID>
SOURCE_TEXT=<並べ替えたい文字列>
```

以下のコマンドを入力して、自身のAWS環境にデプロイします。

```bash
$ make deploy
```
