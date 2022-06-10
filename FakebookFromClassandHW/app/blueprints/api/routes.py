from .import bp as api
from flask import jsonify
from app.blueprints.blog.models import Post
from flask_login import current_user

@api.route('/blog')
def get_posts():
    """
    [GET] /api/blog
    """
    # posts = Post.query.all()
    return jsonify([p.to_dict() for p in Post.query.all()])

@api.route('/blog/user')
def get_user_posts():
    """
    [GET] /api/blog/user
    """
    # posts = Post.query.all()
    return jsonify([p.to_dict() for p in current_user.posts.all()])

