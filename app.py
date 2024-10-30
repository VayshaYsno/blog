import os
from flask import Flask, render_template, current_app, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from datetime import datetime


db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = "article"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    intro = db.Column(db.String(500), nullable=False)
    text = db.Column(db.Text, nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id
    

def create_app():
    site = Flask(__name__)    

    site.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@mydatabase:3306/dbfile"      
    site.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(site)

    with site.app_context():
        db.create_all()

    @site.route('/')           
    @site.route('/home')
    def index():
        count = db.session.query(Article).all()
        return render_template('index.html', count=len(count))


    @site.route('/posts')
    def posts():
        post = Article.query.order_by(Article.data.desc()).all()
        return render_template('posts.html', post=post)


    @site.route('/posts/<int:id>/edit', methods=['POST', 'GET'])
    def post_edit(id):
        article = Article.query.get(id)
        if request.method == "POST":
            article.title = request.form['title']
            article.intro = request.form['intro']
            article.text = request.form['text']

            try:
                db.session.commit()
                return redirect('/posts')
            except:
                return "Error while editing"
        else:
        
            return render_template("postedit.html", article=article)



    @site.route('/posts/<int:id>/delete')
    def post_del(id):
        article = Article.query.get_or_404(id)

        try:
            db.session.delete(article)
            db.session.commit()
            return redirect("/posts")
        except:
            return "При удалении произошла ошибка"


    @site.route('/posts/<int:id>')
    def post_details(id):
        posted = Article.query.get(id)
        return render_template('post_details.html', posted=posted)


    @site.route('/create_article', methods=['POST', 'GET'])
    def create_article():
        if request.method == "POST":
            title = request.form['title']
            intro = request.form['intro']
            text = request.form['text']
            article = Article(title=title, intro=intro, text=text)

            try:
                db.session.add(article)
                db.session.commit()
                return redirect('/posts')
            except:
                return "Error while creating"
        else:
            return render_template("create_article.html")
    return site


if __name__ == "__main__":
    site = create_app()
    site.run(host='0.0.0.0', debug=True)