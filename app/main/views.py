import datetime
from app import *
from flask import request,render_template


from app.models import Article
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about/")
def about():
    return render_template('about.html')

@app.route("/orderlist/")
def orderlist():
    order = Article.query.all()
    return render_template('orderlist.html',**locals())

@app.route("/orderadd/",methods= ["POST","GET"])
def orderadd():
    if request.method == "POST":
        data = request.form
        title= data.get("title")
        author = data.get("author")
        types = data.get("types")
        description = data.get("description")
        content = data.get("content")
        time = datetime.datetime.now()
        file = request.files
        img = file.get("picture")
        path = os.path.join(
            basedir,'static\\imgs',img.filename
        )
        art = Article(
            title = title,
            author = author,
            types = types,
            time = time,
            description = description,
            content = content,
            picture = '/static/imgs/'+img.filename
        )
        img.save(path)
        session.add(art)

    return render_template('orderadd.html')