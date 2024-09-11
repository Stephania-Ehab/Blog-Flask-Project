from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config_options
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap5
from flask_restful import Resource, Api
from flask_login import LoginManager
# from app.models import db, User

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app(config_name='prd'):
    app = Flask(__name__)

    current_config = config_options[config_name]
    app.config.from_object(current_config)

    db.init_app(app)
    migrate.init_app(app, db)
    bootstrap = Bootstrap5(app)
    api = Api(app)
    login_manager.init_app(app)
    # login_manager.login_view = 'auth.login'

    from app.posts import post_blueprint
    app.register_blueprint(post_blueprint)

    from app.creators import creator_blueprint
    app.register_blueprint(creator_blueprint)

    from app.auth import auth_blueprint
    app.register_blueprint(auth_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))


    from app.posts.api.views import  PostsList, PostResource
    api.add_resource(PostsList, '/api/posts')
    api.add_resource(PostResource, '/api/posts/<int:id>')

    return app

    



# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from app.config import config_options
# from app.models import db
# from flask_migrate import Migrate

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app(config_name='prd'):
#     app = Flask(__name__)

#     current_config = config_options[config_name]
#     # app.config.from_object(current_config)  
#     app.config['SQLALCHEMY_DATABASE_URI'] = current_config.SQLALCHEMY_DATABASE_URI
    
#     db.init_app(app)

#     migrate = Migrate (app, db)

#     from app.posts import post_blueprint
#     app.register_blueprint(post_blueprint)

#     from app.creators import creator_blueprint
#     app.register_blueprint(creator_blueprint)


#     # from app.posts.views import posts_landing
#     # app.add_url_rule("/posts", view_func=posts_landing , endpoint='posts_landing')
#     # @app.route('/')
#     # def index():
#     #     return "hi"

#     return app
