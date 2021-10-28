from flask import Blueprint, jsonify, request, abort
from ..models import Blog, Person, db
import datetime

bp = Blueprint('blog', __name__, url_prefix='/blog')

# create Blog endpoint


@bp.route('', methods=['POST'])
def create():
    # req body must contain Person_id and content
    if 'person_id' not in request.json or 'title' not in request.json or 'summary' not in request.json:
        return abort(400)
    # Person with id of Person_id must exist
    Person.query.get_or_404(request.json['person_id'])
    # construct Blog
    bt = Blog(
        person_id=request.json['person_id'],
        title=request.json['title'],
        summary=request.json['summary'],
        last_action='Created',
        last_updated=datetime.datetime.utcnow()
    )
    db.session.add(bt)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(bt.serialize())

# show Blogs index endpoints


@ bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    Blogs = Blog.query.all()  # ORM performs SELECT query
    result = []
    for b in Blogs:
        result.append(b.serialize())  # build list of Blogs as dictionaries
    return jsonify(result)  # return JSON response

# show Blogs endpoints


@ bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    b = Blog.query.get_or_404(id)
    return jsonify(b.serialize())

######################################
# update single blog endpoints
# PUT update <baseURL>/person/<id>


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    b = Blog.query.get_or_404(id)
    print(f'=> {request.json}')
    if 'title' in request.json:
        b.title = request.json['title']
    if 'summary' in request.json:
        b.summary = request.json['summary']
    b.last_action = 'Updated'
    b.last_updated = datetime.datetime.utcnow()

    db.session.commit()
    return jsonify(b.serialize())


# delete Blog endpoint


@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    b = Blog.query.get_or_404(id)
    try:
        db.session.delete(b)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)

# show how many are following a blog


@bp.route('/<int:id>/followed_by', methods=['GET'])
def followed_by(id: int):
    blog = Blog.query.get_or_404(id)
    people = []
    for p in blog.blog_follow:
        people.append(p.serialize())
    return jsonify(people)

# show how posts are on a blog


@bp.route('/<int:id>/posts', methods=['GET'])
def has_posts(id: int):
    blog = Blog.query.get_or_404(id)
    posts = []
    for p in blog.posts:
        posts.append(p.serialize())
    return jsonify(posts)
