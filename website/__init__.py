from flask import Flask
import sys
sys.path.append('/Users/sun/Desktop/WebOSTV/api')

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config['SECRET_KEY'] = 'qwertyuiop'

    from .views import views
    
    app.register_blueprint(views, url_prefix='/')

    return app
 
