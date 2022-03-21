from flask import Flask,render_template,url_for
from os import path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
db=SQLAlchemy()
DB_NAME="database.db"
def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='yeuryudhbfjmndfjj'
    
    app.config['SQLALCHEMY_DATABASE_URL']=f'sqlite://{DB_NAME}'
    db.init_app(app)
  
    
    from .views import views
    from.auth import auth
    
    
    app.register_blueprint(views,urls_prefix='/')
    app.register_blueprint(auth,url_prefix='/')
    
    from .models import User,Note
    
    create_database(app)
    
      
    login_manger=LoginManager()
    login_manger.login_view='auth.login'
    login_manger.init_app(app)
    @login_manger.user_loader
    def load_user(id):
            return User.query.get(int(id))
     
    
    return app
def create_database(app):
    if not path.exists('wesite/'+DB_NAME):
        db.create_all(app=app)
        print("created Database")
                       
    