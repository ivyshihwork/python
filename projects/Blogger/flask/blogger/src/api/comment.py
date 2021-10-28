from flask import Blueprint, jsonify, request, abort
from ..models import Blog, Post, Person, Comment, db
import datetime

bp = Blueprint('comment', __name__, url_prefix='/comment')

# create comment endpoint


@bp.route('', methods=['POST'])
def create():
    # req body must contain Person_id and content
    if 'person_id' not in request.json or 'content' not in request.json or 'post_id' not in request.json:
        return abort(400)
    # Post with id of POST_ID must exist
    Post.query.get_or_404(request.json['post_id'])
    # construct comment
    c = Comment(
        content=request.json['content'],
        last_action='Created',
        last_updated=datetime.datetime.utcnow(),
        post_id=request.json['post_id'],
        person_id=request.json['person_id']
    )
    db.session.add(c)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(c.serialize())

# show comments index endpoints


@ bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    comments = Comment.query.all()  # ORM performs SELECT query
    result = []
    for c in comments:
        result.append(c.serialize())  # build list of comments as dictionaries
    return jsonify(result)  # return JSON response

# show comments endpoints


@ bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    c = Comment.query.get_or_404(id)
    return jsonify(c.serialize())

######################################
# update single comment endpoints
# PUT update <baseURL>/comment/<id>


@bp.route('/<int:id>', methods=['PUT', 'PATCH'])
def update(id: int):
    c = Comment.query.get_or_404(id)
    if 'content' in request.json:
        c.content = request.json['content']
    c.last_action = 'Updated'
    c.last_updated = datetime.datetime.utcnow()

    db.session.commit()
    return jsonify(c.serialize())

# delete comment endpoint


@ bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    c = Comment.query.get_or_404(id)
    try:
        db.session.delete(c)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        return jsonify(False)
