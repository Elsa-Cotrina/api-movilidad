from app import create_app
from utils import db,migrate,jwt

app = create_app()

with app.app_context():
    print("a.................")
    db.init_app(app)
    print("b.................")
    migrate.init_app(app,db)
    print("c.................")
    jwt.init_app(app)

