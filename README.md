# zzgl_platform


### 介绍
本项目为组织关联平台多媒体流程框架


#### 软件架构
软件架构说明
软件架构说明
```
.
├── libs                    # 主要库封装
├── logs                    # 日志目录（非项目跟踪目录，可在config文件中配置）
├── server                  # server后端服务
│   ├── apps                    # 模块接口逻辑
│   ├── base.py                 # 接口handle基类
│   ├── urls.py                 # 接口路由
│   ├── start.py                # server服务启动文件
├── settings                # 配置目录
│   ├── config.py               # 通用配置
├── utils                   # 工具目录
│   ├── db.py                   # 数据库封装函数
├── README.en.md
├── README.md               # README
├── requirements.txt        # python依赖库
```