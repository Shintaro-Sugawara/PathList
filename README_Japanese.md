![License: フリー版 MIT](https://img.shields.io/badge/License-Free%20MIT-green.svg)
![License: プロ版 Proprietary](https://img.shields.io/badge/License-Proprietary-red.svg)
![Platform: Windows](https://img.shields.io/badge/Platform-Windows-blue.svg)
![Language: Python 3.10+](https://img.shields.io/badge/Language-Python_3.10+-yellow.svg)  

---

このプロジェクトには2つの版があります：
- **フリー版**：MITライセンス、ソースコード公開  
- **プロ版**：非公開 / 商用ライセンス  

---

## ■ 他言語の README

-  [英語版（README_English.md）](README.md)
-  [ドイツ語版（README_German.md)](README_German.md)

---

## ■ アプリの入手先（Microsoft Store）

-  [Path List（フリー版）] ※公開後にリンク先を掲載予定（2025.11予定）
-  [Path List Pro（プロ版）](https://apps.microsoft.com/detail/9P3C6RXVNMSW)

---

# Path List / Path List Pro

フォルダ内のファイルやフォルダのフルパス（絶対パス）一覧を簡単に作成できるツールです。  
また、Pro版ではツリー構造での抽出と、Excel 等での出力も行えます。

Unicode に完全対応のため、使用言語以外の文字にも対応しています。  
アプリ自体も、日本語・英語・ドイツ語で表示可能です（他言語も拡張予定）。

本アプリは、Web アクセス・広告表示・レジストリ操作を一切行いません。  
また、外部サーバーとの通信や個人情報の収集・送信も行いませんので、安全でプライバシーにも配慮しています。

---

## ■ 使用方法（フリー版・プロ版共通）

![UsageAndUI_JP](docs/UsageAndUI/UsageAndUI_JP.png)
1. アプリを起動します。  
2. 表示されたダイアログ上に、フォルダ（またはそのショートカット）をドラッグ＆ドロップしてください。  
  ドラッグ＆ドロップ済か否かはダイアログ上の表示で識別できます。  
   - ファイル（またはそのショートカット）をドラッグ＆ドロップした場合は、そのファイルの親ディレクトリが抽出対象となります。  
   - 複数フォルダ・複数ファイルを同時にドラッグ＆ドロップしても動作します。（Treeモードは非対応）  
     なお、同じフォルダが重複して出力対象にはないらないよう、制御しあります。  
3. ダイアログ上の選択項目で希望の出力内容を選択し、 **[OK]** ボタン をクリックしてください。  
   - 初期設定のままでよければ **[Enter]** キー を押すだけです。  
4. 出力が完了すると、デスクトップに一覧ファイルが作成されます。

---

## ■ スクリーンショット（日本語）

アプリの表示言語は、Windows のロケール設定に応じて自動的に切り替わります。  
各言語での UI 表示例は、対応する言語版の README に掲載しています。
- [フリー版 UI](docs/Screenshot_02_Japanese/11_Dialog_List_Free_Before.png)
- [プロ版 UI（Listモード）](docs/Screenshot_02_Japanese/01_Dialog_List_Pro_Before.png)
- [プロ版 UI（Treeモード）](docs/Screenshot_02_Japanese/03_Dialog_Tree_Pro.png)

---

## ■ 出力サンプル（日本語）

アプリケーションが作成する出力ファイルの例です。  
実際の出力内容や書式を確認するための参考としてご利用ください。

- [フリー版の出力（Listモード）](docs/OutputSamples_02_Japanese/01_List_Free.txt)  
- [プロ版の出力（Listモード）](docs/OutputSamples_02_Japanese/02_List_Pro.xlsx)  
- [プロ版の出力（Treeモード）](docs/OutputSamples_02_Japanese/03_Tree_Pro.txt)

---

## ■ フリー版とプロ版について

フリー版も、開発者が常用する機能を詰め込んで作成した、完成されたアプリです。  
快適にご利用いただくため、使用の妨げとなる広告表示や使用期間の制限、プロ版への導入案内などは行っていません。

プロ版では以下の追加機能が利用できます。  
特に、ツリー構造での抽出と、Excel 出力が便利です。

### プロ版の追加機能

1. パスの一覧の抽出（Listモード）に加え、ツリー構造での抽出（Treeモード）が可能  
2. 検索ワードで、抽出対象のファイル名・フォルダ名（パスを含まないもの）を限定可能  
   - 使用例：「.xlsx」（後方一致）で検索すると、Excel ファイルを抽出  
3. 以下の情報を抽出可能  
   - ファイル名・フォルダ名（パスなし）  
   - サイズ  
   - タイムスタンプ（作成日時、更新日時、アクセス日時）  
4. 出力形式の選択肢  
   - `.txt`  
   - `.csv`  
   - `.csv`（各項目をダブルクォートで囲む形式）  
   - `.xlsx`

---

## ■ 機能一覧（Listモード）

- 一覧の作成対象：ファイル／フォルダ  
- サブフォルダ取得：する／しない  
- 検索ワード指定：プロ版のみ  
- サイズ取得：プロ版のみ  
- ファイル名・フォルダ名取得（パスなし）：プロ版のみ（拡張子あり／なし）  
- タイムスタンプ取得：プロ版のみ（作成日時／更新日時／アクセス日時）  
- 出力形式：プロ版のみ（テキスト／CSV／CSV引用符あり／Excel）  
  ※ Excel がインストールされていなくても Excel ファイルを出力可能  

**参考コマンド**
```
dir /b /s /a-d > %USERPROFILE%\desktop\FileList.txt
```
```
dir /b /s /ad  > %USERPROFILE%\desktop\FolderList.txt
```

※ コマンドプロンプトでは Unicode 文字（例：「Résumé」）が画面上では表示されますが、ファイル出力では文字化けします。  
　 Path List / Path List Pro は Unicode に完全対応済みで、外国語名も正しく出力されます。

---

## ■ 機能一覧（Treeモード）［プロ版のみ］

- ファイル情報取得：する／しない（`tree /f` の `/f` オプション相当）  
- 出力スタイル：通常／ASCII文字（`tree /a` の `/a` オプション相当）  

 **参考コマンド**
```
tree /f > %USERPROFILE%\desktop\FileTree.txt
```

英語・ドイツ語環境では、`/a` オプションの有無がコマンドプロンプト画面上には反映されますが、ファイル出力では常に `/a` 指定状態になります。  
Path List Pro では、画面と同様に `/a` なしで出力可能です。

---

## ■ その他の仕様

- 標準フォントより 1pt 大きい文字で UI を構成し視認性アップ  
- 高DPI対応済み。高解像度ディスプレイやスケール設定にも対応  

---

## ■ 対応言語

- 日本語、英語、ドイツ語  
- Windows のロケール（「言語と地域」）に従って自動切替  
- 日本語・ドイツ語以外は、英語表示  

---

## ■ 開発・動作確認環境

- **OS**：Windows 11 Pro 24H2（日本語）、Windows 11 Home 24H2（英語／ドイツ語）  
- **CPU**：AMD Ryzen 7 8845HS  
- **Memory**：32GB  
- 英語／ドイツ語環境は、Hyper-V （仮想環境）上で検証  
- Windows 10/11で動作する設計（SE、EducationなどすべてのEditionでの動作保証はなし）  

---

## ■ テスト・動作検証

- このアプリは、詳細かつ網羅的なテスト・動作検証を実施しています。  
テストケースや使用フォルダは下記を参照してください。
- [テストケース一覧（List_of_Test_Cases.xlsx）](docs/List_of_Test_Cases.xlsx)
- [簡易テスト用フォルダ_単一フォルダドロップ用（TestFolder_01）](docs/TestFolder_01)
- [簡易テスト用フォルダ_複数フォルダドロップ用（TestFolder_02）](docs/TestFolder_02)
---

## ■ 開発言語

1. **Python 3.10.11（CPython）**
2. **標準ライブラリ**
   - `locale`：ロケール（言語と地域）の取得  
   - `sys`：コマンドライン引数の取得  
   - `os`：パス操作、存在確認、リスト取得  
   - `ctypes`：Windows API（高DPI対応）  
   - `datetime`：日付・時刻取得  
   - `threading`：バックグラウンド処理（プロ版のみ）  
   - `gc`：COM解放時のGC制御（プロ版のみ）  
3. **外部ライブラリ**
   - `wxPython`：GUI作成  
   - `pywin32（win32com.client）`：.lnkリンク先取得、COM操作  
   - `openpyxl`：Excel出力用（プロ版のみ、遅延ロード）  

---

## ■ バージョン履歴

### フリー版

| バージョン  | 日付       | 内容                                                                 |
|------------|------------|----------------------------------------------------------------------|
| 1.00       | 2025-11-08 | 初期リリース                                                          |
| 1.10       | 2025-11-24 | Microsoft Store での配布に最適化（MSIX形式での動作を改善）              |

### プロ版

| バージョン  | 日付       | 内容                                                                 |
|------------|------------|----------------------------------------------------------------------|
| 1.00       | 2025-11-08 | 初期リリース                                                          |
| 1.10       | 2025-11-24 | Microsoft Store での配布に最適化（MSIX形式での動作を改善）              |

---

## ■ ご連絡先

- 📧 **s.sugawara.dev@gmail.com**  
- ご意見、ご要望、および、不具合報告は上記にお願いします。
- 本アプリは多言語 UI に対応していますが、日本語以外でのお問い合わせには AI 翻訳を利用して対応しております。  
 ご意見には真摯に対応するつもりですが、個人での開発・サポートのため、限りがございます。  
 AI 翻訳により内容に誤解が生じる可能性があること、および、対応にお時間をいただく場合があることにつきご了承ください。

---

## ■ コントリビューションについて

詳細は以下の日本語版ドキュメントをご参照ください。

-  [CONTRIBUTING_Japanese.md](CONTRIBUTING_Japanese.md)

---

## ■ 開発・サポートへのご支援のお願い

- 改善とサポート継続にご協力いただける方は、こちらからご支援をお願いいたします。  
[Stripe Payment Links](https://buy.stripe.com/dRmfZj8dt1BFeRX3BO9sk01)  
- プロ版を未購入の方は、寄付よりプロ版購入をご検討ください。

---

## ■ 著作権

- **Path List / Path List Pro** の著作権は、すべて開発者に帰属します。  
- プロ版のバイナリ・コードは非公開であり、無断での再配布、改変、逆コンパイル、リバースエンジニアリング等は禁止されています。  
- フリー版のソースコードは、**MIT ライセンス**に基づき公開しています。  
[PathList_1.10.py を GitHub で見る](https://github.com/Shintaro-Sugawara/PathList/blob/master/src/PathList_1.10.py)
- プロ版の Microsoft Store 支払いを除き、ライセンス料等は不要です。  

© 2025 **S. Sugawara** All rights reserved.
