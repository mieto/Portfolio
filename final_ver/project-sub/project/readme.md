<div id="top"></div>

## 使用技術一覧


<p style="display: inline">
  
  <!-- バックエンドのフレームワーク一覧 -->
  <img src="https://img.shields.io/badge/-Django-092E20.svg?logo=django&style=for-the-badge">
  <!-- バックエンドの言語一覧 -->
  <img src="https://img.shields.io/badge/-Python-F2C63C.svg?logo=python&style=for-the-badge">
</p>

## 目次

1. [給料計算アプリ](#給料計算アプリ)
2. [環境](#環境)
3. [開発環境構築](#開発環境構築)


<br />


## 給料計算アプリ





### 給料計算アプリ概要

私のバイト先はシフトをエクセルで管理しています。そのため給料を計算するには、既存のアプリを使っても手入力する必要があります。
<br />
それなりに時間・労力がかかるため、シフトのファイル(CSVファイル)をアップロードすることで計算するアプリをつくってみました。


使用方法とポートフォリオの説明は<a href="https://docs.google.com/document/d/1Hk1wOa4RMHZh6bIXULUTw47FEaOhVV3WWGxHGync9JM/edit?usp=sharing" target="_blank">こちら</a>をご確認ください。
  <p align="left">
    

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境



| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.10.5     |
| Django                | 4.2.5      |




<p align="right">(<a href="#top">トップへ</a>)</p>


## 開発環境構築


pythonのバージョンは最新バージョンで問題なし。ただしpython3以降を推奨。
djangoは pip install django というコマンドをターミナル上で行ってください。
venvの仮想環境をセットアップしてからdjangoをインストールすることもできます。



### 動作確認

http://127.0.0.1:8000 にアクセスできるか確認
アクセスできたら成功


### コマンド一覧

| Make                | 実行する処理                                                            | 元のコマンド                                                                               |
| ------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| make project        | プロジェクトフォルダを作成　　　　　　　　　　　　　　　　　　　　　　　　　 | django-admin startproject [プロジェクト名]
| make app            | アプリケーションフォルダの作成                                           | python manage.py startapp [アプリ名]
| make migrations     | マイグレーションファイルの作成                                           | python manage.py make migrations
| make migrate        | マイグレーションを行う                                                  | python manage.py migrate                                |
| make superuser      | 管理者の設定(名前とメールアドレスとパスワードを設定する)→admin サイトでデータベースの設定・削除ができる。| python manage.py createsuperuser 
| run server          | アプリをローカル環境で立ち上げることができる                              | python manage.py runserver 

※基本的にはターミナル上でコマンドを入力してください。 

<p align="right">(<a href="#top">トップへ</a>)</p>
