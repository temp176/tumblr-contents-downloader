# tumblr-contents-downloader
Tumblrの指定したブログのポスト，および自分がlikeしたポストの写真と動画を取得します．  

# 使用ライブラリ
* pytumblr
* requests
* beautifulsoup4
* tqdm

# 使い方
## 各種APIキーの取得
使用するにはAPIキーが必要になります．  
アプリケーション登録と https://api.tumblr.com/console/calls/user/info などから取得してください．  
### 参考
* Tumblr API和訳：http://kid0725.usamimi.info/api_v2_docs_ja.html
* PyTumblr：https://github.com/tumblr/pytumblr  

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
ブログのポストを取得したい場合は0，likeしたポストを取得したい場合は1を入力します．  

```
blog name :
```
ポストを取得したいブログの名前を入力します．  
前項で1を入力した場合は求められません．  

```
number of requests required : x
```
全てのポストを取得するのに必要なAPIのリクエスト数が表示されます．    

```
offset (request) :
```
リクエストの取得開始位置を入力します．  
1回のリクエストで最大50個のポストを取得します．  

```
number of requests :
```
前項で指定したリクエストから何回リクエストを取得するかを入力します．  

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
ブログのポストを取得した場合は「download」フォルダの中にブログ名のフォルダが作成され，その中にファイルが保存されます．  
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
ダウンロードされたファイルはポストのタイプごと(photo/video)にフォルダ分けされます．  
textタイプのポストには写真または動画が埋め込まれている場合があるので別のフォルダとしています．  

### 「error_log.txt」について
取得したポストがテキストのみだったり，写真や動画が削除されている場合など，なんらかの理由で写真か動画の取得が失敗した際に時刻とポストのタイプ，ポストのURLを記録します．

### 対応タイプ
photo，video，textタイプのポストのみに対応しており，audioなどその他のタイプのポストは無視されます．  

