# django-rest-framework-tutorial

Django REST framework框架

## 快速开始

|用户名|密码|
|:--|:--|
|ansheng|ansheng.me|

```bash
python manage.py runserver
```

使用`httpie`访问API

```bash
$ http -a ansheng:ansheng.me http://127.0.0.1:8000/quickstart/users/
HTTP/1.0 200 OK
Allow: GET, POST, OPTIONS
Content-Type: application/json
Date: Sun, 26 Feb 2017 12:39:22 GMT
Server: WSGIServer/0.2 CPython/3.5.2
Vary: Accept, Cookie
X-Frame-Options: SAMEORIGIN

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "email": "",
            "groups": [],
            "url": "http://127.0.0.1:8000/quickstart/users/1/",
            "username": "ansheng"
        }
    ]
}
```

获取浏览器打开`http://127.0.0.1:8000/quickstart/`

![quickstart](http://github.com/anshengme/django-rest-framework-tutorial/raw/master/images/quickstart.png))