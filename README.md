# BookDataQuery

书籍信息查询网站（Django + Gunicorn + SQLite）。

## 功能

- 支持按 ISBN、书名、作者三种方式搜索。
- 书名/作者搜索忽略字母大小写。
- 支持按出版时间范围筛选（如 2016-2019、2019-至今）。
- 搜索结果以列表展示，点击进入书籍详情页。
- 详情页展示：书名、ISBN、出版时间、出版社、简介、目录。

## 目录结构

- `bookquery/`：Django 项目配置
- `books/`：书籍查询应用
  - `models.py`：Book 数据模型
  - `views.py`：搜索与详情视图
  - `templates/books/`：HTML 模板
  - `fixtures/sample_books.json`：示例书籍数据
- `manage.py`：Django 管理脚本
- `requirements.txt`：依赖
- `start.bat`：Windows 启动脚本（使用 Django 开发服务器）
- `start.sh`：Linux/macOS 启动脚本（使用 Gunicorn）

## 运行方式

### 1. 激活虚拟环境

```bash
# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

### 2. 初始化数据库与示例数据

```bash
python manage.py migrate
python manage.py loaddata sample_books.json
```

### 3. 启动服务

**Windows（Gunicorn 不支持 Windows，使用 Django 开发服务器）：**

```bash
python manage.py runserver 0.0.0.0:8000
# 或直接双击 start.bat
```

**Linux/macOS（使用 Gunicorn）：**

```bash
bash start.sh
```

### 4. 访问

打开浏览器访问：<http://127.0.0.1:8000>

## 管理后台

后台地址：<http://127.0.0.1:8000/admin>

可创建超级用户后登录管理书籍：

```bash
python manage.py createsuperuser
```
