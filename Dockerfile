FROM python:3.6
MAINTAINER huangyifei <huangyifei0910@gmail.com>

COPY . /code
WORKDIR /code

RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
