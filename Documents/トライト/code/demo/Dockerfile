# python:3.8の公式 image をベースの image として設定
FROM python:3.10.7

#Pythonの環境変数を指定
ENV PYTHONUNBUFFERED 1

# 作業ディレクトリの作成
RUN mkdir /code

# 作業ディレクトリの設定
WORKDIR /code

# ホストPCにあるrequirements.txtをコンテナ内のcodeディレクトリにコピー
COPY requirements.txt /code/

# カレントディレクトリにある資産をコンテナ上の指定のディレクトリにコピーする
ADD . /code

# pipでrequirements.txtに指定されているパッケージを追加する
RUN pip install -r requirements.txt

# 起動（コンテナのポート8000番で受け付けるように起動する）
CMD python3 manage.py runserver 0.0.0.0:8000

# ポートを公開する
EXPOSE 8000