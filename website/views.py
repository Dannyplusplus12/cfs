from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Wish
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        content = request.form['content']
        author = request.form['author']

        current_wish = Wish(content=content, author=author)
        db.session.add(current_wish)
        db.session.commit()
        return redirect('/')

    wishes = Wish.query.all()

    return render_template('view.html', wishes=wishes)