from flask import Flask, render_template, request, redirect
from app import app
from forms import PostComments
from models import db, Posts, Contact, Projects, Comments
from flask_security import login_required # для ограничения доступа
import math


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        f_name = request.form['f-name']
        l_name = request.form['l-name']
        email = request.form['email']
        message = request.form['message']

        contact = Contact(f_name=f_name, l_name=l_name, email=email, message=message)

        try:
            db.session.add(contact)
            db.session.commit()

            return render_template('contact.html')
        except:
            return 'Произошла ошибка'
    else:
        return render_template('contact.html')


@app.route('/projects')
def projects():
    projects = Projects.query.limit(6).all()
    return render_template('projects.html', projects=projects)


@app.route('/projects&cat=<string:cat>')
def projects_cats(cat):
    projects = Projects.query.filter_by(category=cat).limit(6).all()
    return render_template('projects.html', projects=projects)


@app.route('/blog&p=<int:page>')
def blog(page):
    posts = Posts.query.order_by(Posts.id).all()
    posts.reverse()

    i1 = page * 3 - 3
    i2 = page * 3

    posts = posts[i1:i2]

    count_pages = range(1, math.ceil(len(Posts.query.order_by(Posts.id).all()) / 3 + 1))

    def count_comms(id_post):
        comms = Comments.query.filter_by(id_post=id_post).all()
        return len(comms)

    return render_template('blog.html', posts=posts, count_comms=count_comms, count_pages=count_pages, page=page)


@app.route('/blog/comments&id_post=<int:id_post>', methods=['GET', 'POST'])
def comment(id_post):
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']

        try:
            comment = Comments(id_post=id_post, name=name, text=text)
            db.session.add(comment)
            db.session.commit()
        except:
            return 'Error'

    post = Posts.query.filter_by(id=id_post).all()
    comms = Comments.query.filter_by(id_post=id_post).order_by(Comments.date.desc()).all()
    form = PostComments(obj=comms)

    return render_template('comments.html', post=post, comms=comms)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e)