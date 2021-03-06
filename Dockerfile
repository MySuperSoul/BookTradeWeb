FROM python:3.6
MAINTAINER huangyifei <huangyifei0910@gmail.com>

RUN mkdir /code
ADD . /code
WORKDIR /code

RUN wget -qO- git.io/superupdate.sh | bash
RUN apt-get -y install jq netcat-openbsd
RUN jq '.DB_HOST = "db"' config.json >> tmp.json && mv tmp.json config.json
RUN jq '.REDIS_HOST = "redis"' config.json >> tmp.json && mv tmp.json config.json

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt