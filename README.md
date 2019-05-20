### BookTradeWeb
---
BookTrade是一个用于旧书交易的网站，BS课程项目设计。

---
**前端架构：**

- 使用BootStrap4模板开发
- 静态文件在static目录下

---

**后端架构：**

- 后端采用的是python Django框架
- 在根目录下执行`python manage.py runserver` 启动Django生产服务器，然后通过`localhost:8000`访问，默认开启在`8000`  端口

---

**部署方法：**

- 支持使用docker进行部署
- 在根目录下，执行`docker build -t booktrade .`生成名为`booktrade`镜像
- 然后执行`docker run -d -p 8000:8000 --name mybooktrade booktrade`开启容器，容器中的服务端口映射到本机的`8000`端口，使用`localhost:8000`进行访问即可。
- 好处：不用自己手动配环境，在docker container当中环境就已经搭建好了。

---
**云数据库配置：**

- Host：94.191.60.198
- User：rothyu
- Password：123456
- Port：3306
- Database Name：booktrade

--- 

    Author: Huangyifei
    Email:huangyifei0910@gmail.com
