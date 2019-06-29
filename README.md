[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)

### BookTradeWeb

BookTrade是一个用于旧书交易的网站，BS课程项目设计。

<br>

**前端架构：**

- 使用Bootstrap4模板开发
- 静态文件在static目录下

<br>

**后端架构：**

- 后端采用的是python Django框架
- 首先安装redis，可以通过`docker run -d -p 6379:6379 redis:latest`开启redis服务，并监听在6379端口
- clone项目, `git clone https://github.com/MySuperSoul/BookTradeWeb.git && cd BookTradeWeb`
- 安装项目依赖packages：`pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt`
- 修改`config.json`当中配置选项
- 迁移数据库，数据库导出脚本在`sqldata/booktrade.sql`.
- 在根目录下执行`python manage.py runserver 8000` 启动Django生产服务器，然后通过`localhost:8000`访问，默认开启在`8000`  端口

<br>

**部署方法：**

- 支持使用docker进行部署
- clone项目, `git clone https://github.com/MySuperSoul/BookTradeWeb.git && cd BookTradeWeb`
- 需要先安装`docker-compose`, 安装步骤为：
```shell
    sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    `docker-compose -v` 检查是否安装成功
```

- 部署方法: `./scripts/start_docker.sh`.可能需要等待20-30秒等待container中的MySQL和server开启。
- 访问: `Your-IP : 8000`,需要保证`8000`、`3000`、`6379`这几个端口不被占用，因为这是docker containers映射到本机的端口
- 移除container: `./scripts/stop_docker.sh`.

<br>

**服务端口配置**

<div align="center">

| Port | Service|
| :--: | :----: |
| 3000 | MySQL |
| 6379 | Redis |
| 8000 | Website |

</div>

<br>

**版权©️**
> Copyright©️ 2019 <br>
> Author: huangyifei <br>
> Email: [huangyifei0910@gmail.com](mailto:huangyifei0910@gmail.com) <br>
> website: [Old-books](http://94.191.60.198:8000)