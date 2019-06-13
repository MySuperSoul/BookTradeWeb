### BookTradeWeb

BookTrade是一个用于旧书交易的网站，BS课程项目设计。


**前端架构：**

- 使用BootStrap4模板开发
- 静态文件在static目录下



**后端架构：**

- 后端采用的是python Django框架
- 在根目录下执行`python manage.py runserver` 启动Django生产服务器，然后通过`localhost:8000`访问，默认开启在`8000`  端口



**部署方法：**

- 支持使用docker进行部署
- clone项目, `git clone https://github.com/MySuperSoul/BookTradeWeb && cd BookTradeWeb`
- 需要先安装`docker-compose`, 安装步骤为：

    - sudo curl -L "https://github.com/docker/compose/releases/download/1.24.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    - chmod +x /usr/local/bin/docker-compose
    - `docker-compose -v` 检查是否安装成功

- 如果使用docker-compose部署的话，需要将`config.json`当中的`DB_HOST`一项改为`db`，如果本地测试还是使用`localhost`.
- 部署方法: `./start_docker.sh`
- 访问: `Your IP : 8000`,需要保证`8000`和`3305`两个端口不被占用，因为这是两个docker container映射到本机的端口
- 移除container: `docker-compose down`.

**云数据库配置：**

- Host：94.191.60.198
- User：rothyu
- Password：123456
- Port：3306
- Database Name：booktrade



    Author: Huangyifei
    Email:huangyifei0910@gmail.com
