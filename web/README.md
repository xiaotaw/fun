# Fun web 应用

## 1. 开发环境搭建

```bash
# 准备本地开发环境变量
cp .env.example .env

# 安装pipenv
sudo apt install pipenv

# 设置PIPENV_VENV_IN_PROJECT, 以便将 .venv 安装到当前目录
export PIPENV_VENV_IN_PROJECT=$PWD

# 安装依赖包
pipenv install

# 激活虚拟环境
pipenv shell
```

## 2. 运行应用

```bash
python manager.py runserver
```