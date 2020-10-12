# chp04

## 日本語データの前処理
- HTMLタグやJavaScriptのコードの除去 -> beautifulSoup
- 単語分割 -> janome
- 単語の正規化
  - 文字種の統一
  - 数字の置き換え
  - 辞書を用いた単語の統一
- ストップワードの除去
- 単語のID化
- パディング

## データセット
- https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_multilingual_JP_v1_00.tsv.gz
  - アクセスでダウンロードが始まるので注意