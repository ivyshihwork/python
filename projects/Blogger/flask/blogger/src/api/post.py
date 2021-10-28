from flask import Blueprint, jsonify, request, abort
from ..models import Blog, Post, Person, db
import datetime

bp = Blueprint('post', __name__, url_prefix='/post')

# create post endpoint


@bp.route('', methods=['POST'])
def create():
    # req body must contain Person_id and content
    if 'blog_id' not in request.json or 'title' not in request.json or 'content' not in request.json:
        return abort(400)
    # Blog with id of Blog_id must exist
    Blog.query.get_or_404(request.json['blog_id'])
    # construct post
    p = Post(
        blog_id=request.json['blog_id'],
        title=request.json['title'],
        content=request.json['content'],
        last_action='Created',
        last_updated=datetime.datetime.utcnow()
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())

# show posts index endpoints


@ bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    posts = Post.query.all()  # ORM performs SELECT query
    result = []
    for p in posts:
        result.append(p.serialize())  # build list of posts as dictionaries
    return jsonify(result)  # return JSON response

# show posts endpoints


@ bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    p = Post.query.get_or_404(id)
    return jsonify(p.serialize())

######################################
# update single post endpoints
# PUT update <baseURL>/post/<id>


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    p = Post.query.get_or_404(id)
    if 'title' in request.json:
        p.title = request.json['title']
    if 'content' in request.json:
        p.content = request.json['content']
    p.last_action = 'Updated'
    p.last_updated = datetime.datetime.utcnow()

    db.session.commit()
    return jsonify(p.serialize())

# delete post endpoint


@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Post.query.get_or_404(id)
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


# implement after commment is done
# show how many have commented on posts

@bp.route('/<int:id>/comment', methods=['GET'])
def has_comments(id: int):
    post = Post.query.get_or_404(id)
    comments = []
    for c in post.comments:
        comments.append(c.serialize())
    return jsonify(comments)
