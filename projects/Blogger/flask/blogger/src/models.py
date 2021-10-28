from flask_sqlalchemy import SQLAlchemy
import datetime


db = SQLAlchemy()

# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    # Relationships
    blogs = db.relationship('Blog', backref='person', cascade="all,delete")
    comments = db.relationship(
        'Comment', backref='person', cascade="all,delete")

    def __init__(self, username: str, password: str, first_name: str, last_name: str) -> None:
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name
        }


blog_follow = db.Table(
    'blog_follow',
    db.Column(
        'person_id', db.Integer,
        db.ForeignKey('person.id'),
        primary_key=True
    ),

    db.Column(
        'blog_id', db.Integer,
        db.ForeignKey('blog.id'),
        primary_key=True
    ),

)


class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    summary = db.Column(db.String(2000), nullable=False)
    last_action = db.Column(db.String(10), nullable=False)
    last_updated = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    person_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), nullable=False)

    # relantionships
    posts = db.relationship('Post', backref='blog', cascade="all,delete")

    blog_follow = db.relationship(
        'Person', secondary=blog_follow,
        lazy='subquery',
        backref=db.backref('blog_follow', lazy=True)
    )

    def __init__(self, title: str, summary: str, last_action: str, last_updated: datetime, person_id):
        self.title = title,
        self.summary = summary,
        self.last_action = last_action,
        self.last_updated = last_updated,
        self.person_id = person_id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'summary': self.summary,
            'last_action': self.last_action,
            'last_updated': self.last_updated.isoformat(),
            'person_id': self.person_id
        }


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(500), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    last_action = db.Column(db.String(10), nullable=False)
    last_updated = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow(),
        nullable=False
    )
    # view_count = db.Column(db.Integer, nullable=False, default=0)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)

    # Relationships
    comments = db.relationship(
        'Comment', backref='comment', cascade="all,delete")

    def __init__(self, title: str, content: str, last_action: str, last_updated: datetime, blog_id: int) -> None:
        self.title = title,
        self.content = content,
        self.last_action = last_action,
        self.last_updated = last_updated,
        self.blog_id = blog_id

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'last_action': self.last_action,
            'last_updated': self.last_updated.isoformat(),
            'blog_id': self.blog_id
        }


# Maybe remove person id later
# writes = db.Table(
#     'likes',
#     db.Column(
#         'person_id', db.Integer,
#         db.ForeignKey('person.id'),
#         primary_key=True
#     ),

#     db.Column(
#         'comment_id', db.Integer,
#         db.ForeignKey('comment.id'),
#         primary_key=True
#     ),

#     db.Column(
#         'created_at', db.DateTime,
#         default=datetime.datetime.utcnow,
#         nullable=False
#     )
# )


class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    content = db.Column(db.String(2000), nullable=False)
    last_action = db.Column(db.String(10), nullable=False)
    last_updated = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey(
        'person.id'), nullable=False)

    # belongs = db.relationship(
    #     'Post', secondary=belong_in,
    #     lazy='subquery',
    #     backref=db.backref('belonged_to', lazy=True)
    # )
    # writes = db.relationship(
    #     'Person', secondary=write,
    #     lazy='subquery',
    #     backref=db.backref('written_by', lazy=True)
    # )

    def __init__(self, content: str, last_action: str, last_updated: datetime, post_id: int, person_id: int) -> None:
        self.content = content,
        self.last_action = last_action,
        self.last_updated = last_updated,
        self.post_id = post_id,
        self.person_id = person_id

    def serialize(self):
        return {
            'id': self.id,
            'content': self.content,
            'last_action': self.last_action,
            'last_updated': self.last_updated.isoformat(),
            'post_id': self.post_id,
            'person_id': self.person.id
        }
