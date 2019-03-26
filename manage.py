from app.main import views
from app import *


if __name__ == '__main__':
    db.create_all()
    app.run(
        host = "localhost",
        port = 8000,
        debug = True
    )