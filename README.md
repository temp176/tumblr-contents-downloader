# tumblr-contents-downloader
Tumblrの指定したブログの投稿，および自分がlikeした投稿の写真および動画を取得します．  

# 使用ライブラリ
* pytumblr
* requests
* beautifulsoup4
* tqdm

# 使い方
## 各種APIキーの取得
使用するにはAPIキーが必要になります．  
アプリケーション登録と https://api.tumblr.com/console/calls/user/info などから取得してください．  
参考：https://github.com/tumblr/pytumblr  

## APIキーの入力
取得したAPIキーを[config.py](https://github.com/temp176/tumblr-contents-downloader/blob/master/config.py)に入力してください．  

## 実行
```
python download.py
```

## 各種設定
```
select mode (0:get post / 1:get my likes) :
```
ブログの投稿を取得したい場合は0，likeした投稿を取得したい場合は1を入力します．  

```
blog name :
```
投稿を取得したいブログの名前を入力します．  
前項で1を入力した場合は求められません．  

```
number of requests required : x
```
全ての投稿を取得するのに必要なAPIのリクエスト数が表示されます．    

```
offset (request) :
```
いくつめのリクエストから開始するかを入力します．  

```
number of requests :
```
いくつリクエストを取得するかを入力します．  
一度のリクエストで最大50個の投稿を取得します．  

```
interval of download [s] :
```
1ファイルごとのダウンロード間隔を指定します．  

```
start downloading? (y/n) :
```
yを入力すると開始し，nを入力するとプログラムを終了します．

## 実行後
ディレクトリに「download」フォルダが作られます．    
ブログの投稿を取得した場合は「download」フォルダの中にブログ名のフォルダが作成され，その中にファイルが保存されます．  
likeの取得をした場合は「download」フォルダの中に「my_likes」フォルダが作成され，その中にファイルが保存されます．  

## ディレクトリ構成例
```
.  
├── README.md  
├── config.py  
├── download  
│   ├── blog_name1  
│   │   ├── video  
│   │   ├── photo  
│   │   └── text_type  
│   ├── blog_name2  
│   │   ├── video  
│   │   ├── photo  
│   │   └── text_type  
│   └── my_likes  
│       ├── video  
│       ├── photo  
│       └── text_type  
├── download.py  
└── error_log.txt  
```

## その他
### ファイルのフォルダ分けについて
ダウンロードされたファイルは投稿のタイプごと(photo/video)にフォルダ分けされます．  
textタイプの投稿には写真または動画が埋め込まれている場合があるので別のフォルダとしています．  

### 「error_log.txt」について
取得した投稿がテキストのみだったり，写真や動画が削除されている場合など，なんらかの理由で写真か動画の取得が失敗した時に時刻と投稿のタイプ，投稿のURLを記録します．

### 対応タイプ
photo，video，textタイプの投稿のみに対応しており，audioなどその他の投稿は無視されます．  

