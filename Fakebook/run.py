##followed class videos and online resources to try and figure this out. 

from app import createApp, db

app = createApp()

from app.blueprints.blog.models import Post, User

@app.shell_context_processor
def makeContext():
    return {
        'db': db,
        'User': User,
        'Post': Post
    }

    