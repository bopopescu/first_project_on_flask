from flask import Flask, render_template, url_for, request, redirect
import os
from models import app
from models import db
from models import Literat
from models import Video
from models import Scrum
from models import Article
from werkzeug.utils import secure_filename

POST_IMAGE_PATH = r'C:\Users\Vertigo\Desktop\python\blog\My_blog\static\image\post_image\\'
ALLOWED_EXTENSIONS_image = set( ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'] )


@app.route('/') # отслеживание страницы
@app.route('/home')
def index():
    # обращение к базе через куэри к первой записи first(), all к всем
    articles = Article.query.order_by(Article.date.desc()).all() # order_by - для сортировки по убыванию по дате например
    return render_template("index.html", articles=articles) # articles(шаблон в бд) в шаблон передаем список articles


@app.route('/scrum')
def scrum():
    scrum = Scrum.query.order_by( Scrum.date ).all()
    return render_template("scrum.html", scrum=scrum)


@app.route('/update_scrum', methods=['POST', 'GET'])
def update_scrum():
    if request.method == "POST":  # если видим пост запрос, то
        text_scrum = request.form['scrum']  # создаем переменные и туда добавляем все из html, где поля title, intro, ...
        # в класс бд передаем в title значение title из html и тд...
        scrum1 = Scrum( scrum=text_scrum )
        try:
            db.session.add( scrum1 )  # добавляем из переменной артикл все в бд
            db.session.commit()  # делаем commit
            return redirect( '/scrum' )  # если статья успешно добавлено, то редирект на главную
        except:
            return "При добавлении информации произошла ошибка."
    else:
        return render_template( "update_scrum.html" )


@app.route('/update_scrum/<int:id>/update', methods=['POST', 'GET']) # method для обработки пост запроса, чтоб не было ошибки сайта
def reupdate_scrum(id):
    scrum = Scrum.query.get( id )  # получаем статью
    if request.method == "POST": # если видимо пост запрос, то
        scrum.scrum = request.form['scrum'] # создаем переменные и туда добавляем все из article, где поля title, intro, ...
        # scrum.scrum бред согласен, из за того, что вначале функции получаем статью и пишем в scrum в html

        try:
            db.session.commit() # делаем commit в бд
            return redirect('/scrum') # если статья успешно добавлено, то редирект на главную
        except:
            return "При редактировании статьи произошла ошибка."
    else:

        return render_template("reupdate_scrum.html", scrum=scrum)


@app.route('/literature')
def literature():
    literature = Literat.query.order_by(Literat.date ).all()  # order_by - для сортировки по убыванию по дате например
    return render_template( "literature.html", literature=literature )


@app.route('/add-literature', methods=['POST', 'GET'])
def add_literature():
    if request.method == "POST": # если видим пост запрос, то
        name = request.form['name'] # создаем переменные и туда добавляем все из html, где поля title, intro, ...
        author = request.form['author']
        # в класс бд передаем в title значение title из html и тд...
        literature = Literat(name=name, author=author)
        try:
            db.session.add(literature) # добавляем из переменной артикл все в бд
            db.session.commit() # делаем commit
            return redirect('/literature') # если статья успешно добавлено, то редирект на главную
        except:
            return "При добавлении книги произошла ошибка."
    else:
        return render_template("add-literature.html")


@app.route('/literature/<int:id>/delete') #
def literature_delete(id):
    literature = Literat.query.get_or_404(id) #
    try:
        db.session.delete(literature) #delete запись из бд
        db.session.commit()
        return redirect('/literature')
    except:
        return "При удалении книги произошла ошибка."


@app.route('/literature/<int:id>/update', methods=['POST', 'GET']) # method для обработки пост запроса, чтоб не было ошибки сайта
def literature_update(id):
    literature = Literat.query.get( id )  # получаем статью
    if request.method == "POST": # если видимо пост запрос, то
        literature.name = request.form['name'] # создаем переменные и туда добавляем все из article, где поля title, intro, ...
        literature.author = request.form['author']

        try:
            db.session.commit() # делаем commit в бд
            return redirect('/literature') # если статья успешно добавлено, то редирект на главную
        except:
            return "При редактировании книги произошла ошибка."
    else:

        return render_template("literature_update.html", literature=literature)


@app.route('/video-link')
def video_link():
    video = Video.query.order_by( Video.date.desc() ).all()
    return render_template("video-link.html", video=video)


@app.route('/add-video', methods=['POST', 'GET'])
def add_video():
    if request.method == "POST":  # если видим пост запрос, то
        name = request.form['name']  # создаем переменные и туда добавляем все из html, где поля title, intro, ...
        link = request.form['link']
        # в класс бд передаем в title значение title из html и тд...
        video = Video( name=name, link=link )
        try:
            db.session.add( video )  # добавляем из переменной артикл все в бд
            db.session.commit()  # делаем commit
            return redirect( '/video-link' )  # если статья успешно добавлено, то редирект на главную
        except:
            return "При добавлении видео произошла ошибка."
    else:
        return render_template( "add-video.html" )


@app.route('/video-link/<int:id>/delete') #
def video_delete(id):
    video = Video.query.get_or_404(id) #

    try:
        db.session.delete(video) #delete запись из бд
        db.session.commit()
        return redirect('/video-link')
    except:
        return "При удалении видео произошла ошибка."


@app.route('/video-link/<int:id>/update', methods=['POST', 'GET']) # method для обработки пост запроса, чтоб не было ошибки сайта
def video_update(id):
    video = Video.query.get( id )  # получаем статью
    if request.method == "POST": # если видимо пост запрос, то
        video.name = request.form['name'] # создаем переменные и туда добавляем все из article, где поля title, intro, ...
        video.link = request.form['link']

        try:
            db.session.commit() # делаем commit в бд
            return redirect('/video-link') # если статья успешно добавлено, то редирект на главную
        except:
            return "При редактировании видео произошла ошибка."
    else:

        return render_template("video_update.html", video=video) #video передаем в html


@app.route('/posts')
def posts():
    # обращение к базе через куэри к первой записи first(), all к всем
    articles = Article.query.order_by(Article.date.desc()).all() # order_by - для сортировки по убыванию по дате например
    return render_template("posts.html", articles=articles) # articles(шаблон в бд) в шаблон передаем список articles


@app.route('/posts/<int:id>') # <> для обработки айдишника
def post_detail(id):
    article = Article.query.get(id) # гет для получения полной инфы по статьи по id
    return render_template("post_detail.html", article=article) # articles(шаблон в бд) в шаблон передаем список articles


@app.route('/posts/<int:id>/delete') #
def post_delete(id):
    article = Article.query.get_or_404(id) #

    try:
        db.session.delete(article) #delete запись из бд
        db.session.commit()
        return redirect('/posts')
    except:
        return "При удалении статьи произошла ошибка."


@app.route('/posts/<int:id>/update', methods=['POST', 'GET']) # method для обработки пост запроса, чтоб не было ошибки сайта
def post_update(id):
    article = Article.query.get( id )  # получаем статью
    if request.method == "POST": # если видимо пост запрос, то
        article.title = request.form['title'] # создаем переменные и туда добавляем все из article, где поля title, intro, ...
        article.intro = request.form['intro']
        article.text = request.form['text']
        article.marker = request.form['marker']
        file = request.files['file']
        if file and allowed_file( file.filename ):  # не трогай это)
            filename = secure_filename( file.filename )  # проверка файла на секьюрность
            file.save( POST_IMAGE_PATH + filename )  # путь файла + имя файла и сохранить
            article.image = filename # это для того, чтоб при редактировании файла менялось и название файла на новое.
        try:
            db.session.commit() # делаем commit в бд
            return redirect('/posts') # если статья успешно добавлено, то редирект на главную
        except:
            return "При редактировании статьи произошла ошибка."
    else:

        return render_template("post_update.html", article=article) #article передаем в html


def allowed_file(filename): # для проверки файла
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS_image


@app.route('/create-article', methods=['POST', 'GET']) # method для обработки пост запроса, чтоб не было ошибки сайта
def create_article():
    if request.method == "POST": # если видим пост запрос, то
        title = request.form['title'] # создаем переменные и туда добавляем все из html, где поля title, intro, ...
        intro = request.form['intro']
        text = request.form['text']
        image = request.form['image']
        marker = request.form['marker']
        file = request.files['file']
        if file and allowed_file(file.filename): # не трогай это)
            filename = secure_filename(file.filename) #проверка файла на секьюрность
            file.save(POST_IMAGE_PATH + filename)  # путь файла + имя файла и сохранить
        # в класс бд передаем в title значение title из html и тд...
        article = Article(title=title, marker=marker, intro=intro, text=text, image=filename)
        try:
            db.session.add(article) # добавляем из переменной артикл все в бд
            db.session.commit() # делаем commit
            return redirect('/posts') # если статья успешно добавлено, то редирект на главную
        except:
            return "При добавлении статьи произошла ошибка."
    else:
        return render_template("create-article.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__": #main это сам файл app.py
    app.run(debug=True) #debug нужен для ошибок в консольке