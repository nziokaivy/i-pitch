import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from . import main
from .. import db, mail
from .forms import UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from ..models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
# from .email import mail_message

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
   
    return render_template('index.html')

@main.route('/home')
def home():

    '''
    View root page function that returns the index page and its data
    '''
    posts = None
    # page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc())
    title = 'Home'
    return render_template('home.html', title=title, posts=posts)    


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', picture_fn)
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    
    return picture_fn


@main.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file

        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pictures/' + current_user.image_file)
    
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@main.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post(): 
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))

    return render_template('create_post.html', title='New Post', form=form, legend="New Post")

@main.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@main.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend="Update Post")

@main.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required    
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)   
    db.session.delete()
    db.session.commit()    
    flash('Your post has been deleted')
    return redirect(url_for('home'))

@main.route('/user/<string:username>')
def user_posts(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(author=user)
    title = 'User'
    return render_template('user_posts.html', title=title, posts=posts, user=user)    

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', sender='nziokaivy@gmail.com', recipients=[user.email])
    msg.body = f'''
    To reset your password, visit the following link: {url_for('rest_token', token=token, _external=True)}
    '''
    mail.send(msg)

@main.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        form = RequestResetForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email=form.email.data.first())
            send_reset_email(user)
            flash('An email has been sent to reset your password')
            return redirect(url_for('login'))
        return render_template('reset_request.html', title='Reset Password', form=form)

@main.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        user = User.verufy_rest_token(token)
        if user is None:
            flash('That is an invalid or expired token', 'warning')
            return redirect(url_for('reset_request'))
        form = ResetPasswordForm()
        if form.validate_on_submit():
            user = User( username=form.username.data, email=form.email.data, password=form.password.data)
            user.password = form.email.data
            db.session.commit()
            flash(f'Your password has been updated! You can now log in')
            return redirect(url_for('login'))
   
    return render_template('reset_token.html', title='Reset Password', form=form)    


@main.route('/post/<post_id>/add/comment', methods = ['GET','POST'])
@login_required
def comment(uname,post_id):
    user = User.query.filter_by(username = uname).first()
    post = Post.query.filter_by(id = post_id).first()
    form = CommentForm()

    if form.validate_on_submit():
        body = form.comment.data
        name = form.name.data
        new_comment = Comment(body=body)
        new_comment.save_comment()
        
        return redirect(url_for("main.show_comments",id = id))
    return render_template("comments.html", form = form, post = post)

@main.route('/<post_id>/comments')
@login_required
def show_comments(post_id):
    
    comments = None
    post = Post.query.filter_by(id = post_id).first()
    comments = post.get_post_comments()

    return render_template('show_comments.html',comments= comments,post= post)

@main.route('/post/<category>')
def post_category(category):
    
    posts= None
    if category == 'all':
        posts = Post.query.order_by(Post.date.desc())
    else :
        posts = Post.query.filter_by(category = category).order_by(Post.date.desc()).all()

    return render_template('home.html', posts = posts ,title = category.upper())

@main.route('/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
    '''
    Function that returns a list of comments for the particular pitch
    '''
    form = CommentForm()
    pitches = Pitches.query.filter_by(id=id).first()

    if pitches is None:
        abort(404)

    if form.validate_on_submit():
        comment_id = form.comment_id.data
        new_comment = Comments(comment_id=comment_id,
                               user_id=current_user.id, pitches_id=pitches.id)
        new_comment.save_comment()
        return redirect(url_for('main.post_category', id=pitches.category_id))

    return render_template('comments.html', form=form)

