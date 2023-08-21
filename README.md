# 珊瑚礁服务端
Coral Hub （寓意科技部落）是一个综合了科技交流社区,在线学习平台,频道实时通信,在线协同IDE,硬件在线仿真,硬件开发工具链,云软件/硬件工程托管的综合性开源社区,为科技爱好者、学生、工程师和创业者提供了一个全方位的科技交流与合作的平台。

无论你是想展示自己的创意、寻找合作伙伴、学习新技术还是进行项目开发，Coral Hub都能满足你的需求。

星星之火可以燎原，我们将携手无数“技术疯子”们共同打造一个开放、包容、友好的科技社区。



## 采用的技术栈
```

Python 3.11+
uvicorn --> ASGI 服务端框架
FastAPI --> 全异步非阻塞服务端接口框架
SQLAlchemy --> ORM
MySQL 8.0 / MariaDB --> SQL数据库
Anyio --> 异步框架
asyncfiles --> 异步文件操作
asyncmy --> 异步MYSQL数据库驱动
motor --> 异步MongoDB驱动
Elastic Search --> ElasticSearch索引数据库
Redis --> 缓存数据库
Emqx --> 消息队列
HTTPX --> HTTP客户端
阿里云OSS --> 对象存储
Docker --> 容器化
k8s --> 容器集群
```

## 服务端系统采用模块化架构

### 模块划分

```
接口服务模块 （该模块将会创建两个FastApi实例）

    app_sys -> 系统接口（管理层）
        api_router -> 系统接口路由
        
    app -> 社区主页接口 （用户层）

```

