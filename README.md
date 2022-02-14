# 关于django学习中的一些记录

## python虚拟环境

https://www.jianshu.com/p/d37662e6ef34

https://juejin.cn/post/6844903896742117389

1.移动到你要创建虚拟环境的目录，创建虚拟环境目录文件夹

```
virtualenv env
```

2.激活虚拟环境

```
source env/bin/activate
```

3.安装所需要的库

```
python3 -m pip install mysql
python3 -m pip install pymysql
python3 -m pip install django
```

4.退出虚拟环境

```
deactivate
```

## 第一个Django项目

### 数据库连接（terminal）

配置环境变量

```
open ~/.bash_profile
```

添加

```
PATH=$PATH:/usr/local/mysql/bin
```

生效

```
source ~/.bash_profile
```

登录mysql

```
mysql -uroot -p
password:password
quit
```

### MySQL基本语法

https://www.runoob.com/mysql/mysql-tutorial.html

### 一些错误的解决方案

- django连接mysql出现"django.db.utils.OperationalError: (2059, "Authentication plugin 'caching_sha"错误的解决方法https://blog.csdn.net/weixin_43996007/article/details/104065678

## 步骤记录

https://blog.csdn.net/weixin_43499626/article/details/84351572

1.建立Django文件

```
django-admin startproject orthancDjango

cd orthancDjango 
virtualenv env
source env/bin/activate
python3 -m pip install mysql
python3 -m pip install pymysql
python3 -m pip install django
```

2.修改settings

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}

TIME_ZONE = 'Asia/Shanghai'
```

\_\_init\_\_.py

```python
import pymysql
pymysql.install_as_MySQLdb()
```

3.创建应用notification

```
python manage.py startapp notification
```

4.创建Notification model

https://www.cnblogs.com/allan-king/p/5807659.html

```python
class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    from_hospital_id = models.CharField('from_hospital_id', max_length=255, null=True)
    target_hospital_id = models.CharField('target_hospital_id', max_length=255, null=True)
    # from_hospital_id = models.ForeignKey('Hospitals', related_name='hospital_id', on_delete=models.RESTRICT, \
    # name='hospital_from')
    # target_hospital_id = models.ForeignKey('Hospitals', related_name='hospital_id', on_delete=models.RESTRICT, \
    # name='hospital_target')
    created_time = models.DateTimeField('created_time', null=True)
    title = models.CharField('title', max_length=255, null=True)
    description = models.TextField('description', null=True)
    status = models.IntegerField('status', null=True, default=0)
    type = models.CharField('type', max_length=255, null=True)

    class Meta:
        db_table = 'Notifications'
        indexes = [
            models.Index(fields=['from_hospital_id'], name='hospital_from'),
            models.Index(fields=['target_hospital_id'], name='hospital_target')
        ]
```

6.激活模型

settings.py

```python
INSTALLED_APPS = [
    'notification.apps.NotificationConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

7.手动创建数据库

```
mysql> create database django_mysql;
```

8.迁移

```
python manage.py makemigrations
python manage.py migrate
```

9.terminal操作mysql

```
mysql> use django_mysql
mysql> show tables;
```