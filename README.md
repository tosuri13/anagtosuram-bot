# anagtosuram-bot

## 🌟 Overview

Twitterなどでよく見る文字列を並べ替えてキャッキャするDiscord BotをAWSで構築できるテンプレートです。

Poetry(Poethepoet) + AWS SAM構成で作成されています。

## 🛠️ Build & Deploy

Discord Developer Portalから新しいApplicationsを作成し、以下のSSMパラメータを事前に作成してください。

- `/ANAGTOSURAM_BOT/DISCORD/BOT_TOKEN`

  - Discord Botのトークンを入力します

- `/ANAGTOSURAM_BOT/DISCORD/CHANNEL_ID`

  - メッセージを投稿したいチャンネルのIDを入力します

- `/ANAGTOSURAM_BOT/SOURCE_TEXT`

  - 並べ替えたい文字列を入力します

以下のコマンドを入力して、自身のAWS環境にデプロイします。

```bash
$ poe build && poe deploy
```
