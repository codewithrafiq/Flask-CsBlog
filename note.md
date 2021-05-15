```
 db.create_all()
>>> from main import User,Post
>>> u = User(username="testuser1",email="testuser1@gmail.com",password="password1")
>>> db.session.add(u)


s=User.query.filter_by(id=1).first()
```

```
Python 3.6.9 (default, Jan 26 2021, 15:33:00)
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import db
/home/mdrafiqulislm/codewithrafiq/flask_learn/csFlask/env/lib/python3.6/site-packages/flask_sqlalchemy/__init__.py:873: FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.
  'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
>>> db.create_all()
>>> from main import User,Post
>>> u = User(username="testuser1",email="testuser1@gmail.com",password="password1")
>>> db.session.add(u)
>>> u2 = User(username="testuser2",email="testuser2@gmail.com",password="password2")
>>> db.session.commit(u2)Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: commit() takes 1 positional argument but 2 were given
>>> db.session.commit()
>>> db.session.add(u2)>>> db.session.commit()
>>> User.query.all()
[User('testuser1', 'testuser1@gmail.com', 'default.jpg'), User('testuser2', 'testuser2@gmail.com', 'default.jpg')]
>>> User.query.filter(id=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: filter() got an unexpected keyword argument 'id'
>>> User.query.filter_by(id=1)
<flask_sqlalchemy.BaseQuery object at 0x7fcb5a52ff98>
>>> User.query.filter_by(id=1).first()
User('testuser1', 'testuser1@gmail.com', 'default.jpg')
>>> s=User.query.filter_by(id=1).first()
>>> s.username
'testuser1'
>>> s.email
'testuser1@gmail.com'
>>> s.password
'password1'
>>> s.image_file
'default.jpg'
>>> s.posts
[]
>>> s.id
1
>>> post1 = Post(title="title-1",content="Content-1",user_id=s.id)
>>> db.session.add(post1)
>>> post1.id
>>> post2 = Post(title="title-2",content="Content-2",user_id=s.id)
>>> db.session.add(post2)
>>> db.session.commit()
>>> s.posts
[Post('title-1', '2021-05-15 07:13:14.808379'), Post('title-2', '2021-05-15 07:13:14.809343')]
>>> for post in s.posts:
... print(post.title)
  File "<stdin>", line 2
    print(post.title)
        ^
IndentationError: expected an indented block
>>> for post in s.posts:
...     print(post.title)
...
title-1
title-2
>>> post.query.first()
Post('title-1', '2021-05-15 07:13:14.808379')
>>> post = post.query.first()
>>> post
Post('title-1', '2021-05-15 07:13:14.808379')
>>> post.user_id
1
>>> post.author
User('testuser1', 'testuser1@gmail.com', 'default.jpg')
>>> db.drop_all()
>>> db.create_all()
>>> User.query.all()
[]
>>> Post.query.all()
[]
>>>
```
