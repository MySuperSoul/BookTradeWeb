FROM python:3.6
MAINTAINER huangyifei <huangyifei0910@gmail.com>

RUN mkdir /code
ADD . /code
WORKDIR /code

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
