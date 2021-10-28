from flask import Blueprint, jsonify, request, abort
from sqlalchemy.sql.operators import endswith_op
import sqlalchemy
import datetime

from ..models import Person, blog_follow, Blog, db
import hashlib
import secrets

bp = Blueprint('person', __name__, url_prefix='/person')

######################################
# create person endpoint
# POST Create <baseURL>/person
# json format:
# {
# 	"username": "testing123",
# 	"password": "12345678",
# 	"first_name": "testing",
# 	"last_name": "123"
# }


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


@bp.route('', methods=['POST'])
def create():
    # conditions to stop creating Persons:
    # 1. This endpoint should require that both values are provided.
    # Abort with status code 400 if either is missing.
    if 'username' not in request.json or 'password'not in request.json or 'first_name' not in request.json or 'last_name' not in request.json:
        return abort(400)
    # 2. The username value must be at least 3 characters long => abort 400
    # 3. The password value must be at least 8 characters long.=>abort 400.
    # 4.  first and last name needs to be at least 2 chars
    if len(request.json['username']) < 3 or len(request.json['password']) < 8 or len(request.json['first_name']) < 1 or len(request.json['last_name']) < 1:
        return abort(400)
    # construct Person
    p = Person(
        username=request.json['username'],
        password=scramble(request.json['password']),
        first_name=request.json['first_name'],
        last_name=request.json['last_name']
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())

######################################
# show person index  endpoint
# GET Show <baseURL>/person


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    people = Person.query.all()  # ORM performs SELECT query
    result = []
    for p in people:
        result.append(p.serialize())  # build list of Blogs as dictionaries
    return jsonify(result)  # return JSON response

######################################
# show single person endpoints
# GET Show <baseURL>/person/<id>


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Person.query.get_or_404(id)
    return jsonify(p.serialize())


######################################
# update single person endpoints
# PUT update <baseURL>/person/<id>
@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    p = Person.query.get_or_404(id)
    print(f'=> {request.json}')
    if 'username' in request.json:
        p.username = request.json['username']
    if 'password' in request.json:
        p.password = scramble(request.json['password'])
    if 'first_name' in request.json:
        p.first_name = request.json['first_name']
    if 'last_name' in request.json:
        p.last_name = request.json['last_name']

    db.session.commit()
    return jsonify(p.serialize())

######################################
# delete single person endpoints
# DEL delete <baseURL>/person/<id>


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Person.query.get_or_404(id)
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

# below is after blog.py is implemented

######################################
# show single person has blogs endpoints
# get  <baseURL>/person/<id>/blog/


@bp.route('/<int:id>/blog', methods=['GET'])
def has_blog(id: int):
    person = Person.query.get_or_404(id)
    blogs = []
    for p in person.blogs:
        blogs.append(p.serialize())
    return jsonify(blogs)


######################################
# show single person follow endpoints
# get followed_blogs <baseURL>/person/<id>


@bp.route('/<int:id>/follows', methods=['POST'])
def follows(id: int):
    if 'blog_id' not in request.json:
        return abort(400)
    blog_id = request.json['blog_id']
    Person.query.get_or_404(id)
    Blog.query.get_or_404(blog_id)
    try:
        stmt = sqlalchemy.insert(blog_follow).values(
            person_id=id, blog_id=blog_id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

# how many blogs a person are following


@bp.route('/<int:id>/followed_blogs', methods=['GET'])
def followed_blogs(id: int):
    person = Person.query.get_or_404(id)
    print(person)
    blogs = []
    for b in person.blog_follow:
        print(b)
        blogs.append(b.serialize())
    return jsonify(blogs)


# unfollow a blog


@bp.route('/<int:person_id>/unfollows/<int:blog_id>', methods=['DELETE'])
def unfollows(person_id: int, blog_id: int):
    Person.query.get_or_404(person_id)
    Blog.query.get_or_404(blog_id)
    try:
        stmt = sqlalchemy.delete(blog_follow).where(
            blog_follow.c.person_id == person_id).where(blog_follow.c.blog_id == blog_id)
        # follows_table.Person_id == Person_id).where(follows_table.blog_id == blog_id)
        db.session.execute(stmt)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)

# below was implemented after comment was done
######################################
# show single person has blogs endpoints
# get  <baseURL>/person/<id>/comment/


@bp.route('/<int:id>/comment', methods=['GET'])
def has_comment(id: int):
    person = Person.query.get_or_404(id)
    comments = []
    for c in person.comments:
        comments.append(c.serialize())
    return jsonify(comments)
