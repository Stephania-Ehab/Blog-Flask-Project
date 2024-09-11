from app.models import Post, db, Creator
from flask import render_template, request, redirect, url_for
from app.posts import  post_blueprint
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

@post_blueprint.route("", endpoint="landing") 
def landing():
    posts = Post.query.all()
    return render_template("landing.html", posts=posts)


@post_blueprint.route("<int:id>", endpoint="show")
def show(id):
    post = Post.query.get_or_404(id)
    return render_template("show.html", post=post)

from app.posts.forms import postForm

@post_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# @login_required
def posts_create():
    form = postForm()
    if request.method == "POST" and form.validate_on_submit():
        image_name=None
        if request.files.get('image'):
             image= form.image.data
             image_name =secure_filename(image.filename)
             image.save(os.path.join('app/static/images/', image_name))
        post = Post(title=request.form["title"], description=request.form["description"], 
          image=image_name)
        db.session.add(post)
        db.session.commit()
        return redirect(post.show_url)
    return render_template("create.html", form=form)


@post_blueprint.route("<int:id>/delete", endpoint="delete", methods=['POST'])
# @login_required
def posts_delete(id):
    post = Post.query.get_or_404(id)
    # if post.creator_id != current_user.id:
    #     return redirect(url_for('posts.landing'))
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('posts.landing'))

@post_blueprint.route("/<int:id>/edit", endpoint="edit", methods=["GET", "POST"])
# @login_required
def posts_edit(id):
    post = Post.query.get_or_404(id)
    # if post.creator_id != current_user.id:
    #     return redirect(url_for('posts.landing'))
    form = postForm(obj=post)
    if request.method == "POST" and form.validate_on_submit():
        post.title = form.title.data
        post.description = form.description.data
        post.creator_id = form.creator_id.data
        if request.files.get('image'):
            image= form.image.data
            image_name =secure_filename(image.filename)
            image.save(os.path.join('app/static/images/', image_name))
            post.image = image_name
        db.session.commit()
        return redirect(post.show_url)
    return render_template("edit.html", form=form, post=post)




# from flask import render_template, request, redirect, url_for, flash
# from app.models import Post, db, Creator
# from app.posts.forms import PostForm
# from app.posts import post_blueprint
# from werkzeug.utils import secure_filename
# import os


# @post_blueprint.route("", endpoint='landing')
# def posts_landing():
#     posts = Post.query.all()
#     return render_template('landing.html', posts=posts)

# ##################### Show post details #####################
# @post_blueprint.route("<int:id>/show", endpoint='show')
# def posts_show(id):
#     post = Post.query.get_or_404(id)
#     return render_template('show.html', post=post)

# ##################### Create or Edit Post #####################
# @post_blueprint.route("/form/create", methods=["POST", "GET"])
# @post_blueprint.route("/form/<int:id>/edit", methods=["POST", "GET"])
# def manage_post(id=None):
#     post = Post.query.get_or_404(id) if id else None
#     form = PostForm(obj=post)  # Prepopulate the form if post exists

#     if request.method == 'POST' and form.validate_on_submit():
#         image_name = post.image if post and form.image.data is None else None
#         if form.image.data:
#             image = form.image.data
#             image_name = secure_filename(image.filename)
#             image.save(os.path.join('static/images/', image_name))

#         data = {
#             "title": form.title.data,
#             "description": form.description.data,
#             "image": image_name,
#             "creator_id": form.creator_id.data
#         }

#         if post:
#             # Update existing post
#             post.title = data["title"]
#             post.description = data["description"]
#             post.image = data["image"]
#             post.creator_id = data["creator_id"]
#         else:
#             # Create new post
#             post = Post(**data)
#             db.session.add(post)

#         db.session.commit()
#         return redirect(url_for('posts.show', id=post.id))

#     return render_template("posts/forms/create.html", form=form, post=post)

# ##################### Delete a post #####################
# @post_blueprint.route('<int:id>/delete', endpoint='delete', methods=['GET', 'POST'])
# def posts_delete(id):
#     post = Post.query.get_or_404(id)
#     db.session.delete(post)
#     db.session.commit()
#     flash("Post deleted successfully!", 'success')
#     return redirect(url_for('posts.landing'))




# from flask import Flask, render_template, request, redirect, url_for
# from app.models import Post, db, Creator
# from app.posts import post_blueprint
# from werkzeug.utils import secure_filename
# import os


# @post_blueprint.route("", endpoint='landing')
# def posts_landing():
#     posts = Post.query.all()
#     return render_template('landing.html', posts=posts)

# ##################### Show post details #####################
# @post_blueprint.route("<int:id>/show", endpoint='show')
# def posts_show(id):
#     post = db.get_or_404(Post, id)
#     return render_template('show.html', post=post)

# ##################### Create a new post #####################
# @post_blueprint.route("create", endpoint="create", methods=["GET", "POST"])
# def posts_create():
#     creators = Creator.query.all()
#     if request.method == 'POST':
#         new_post = Post(
#             title=request.form['title'],
#             description=request.form['description'],
#             image=request.form['image'],
#             creator_id=request.form["creator_id"]
#         )
#         db.session.add(new_post)
#         db.session.commit()
#         return redirect(url_for('posts.landing'))
#     return render_template('create.html', creators=creators)

# ##################### Edit post details #####################
# @post_blueprint.route('<int:id>/edit', endpoint='edit', methods=['GET', 'POST'])
# def posts_edit(id):
#     post = db.get_or_404(Post, id)
#     if request.method == 'POST':
#         post.title = request.form['title']
#         post.description = request.form['description']
#         post.image = request.form['image']
#         db.session.commit()
#         return redirect(url_for('posts.show', id=post.id))
#     return render_template('edit.html', post=post)

# ##################### Delete a post #####################
# @post_blueprint.route('<int:id>/delete', endpoint='delete', methods=['GET', 'POST'])
# def posts_delete(id):
#     post = db.get_or_404(Post, id)
#     db.session.delete(post)
#     db.session.commit()
#     return redirect(url_for('posts.landing'))






# @post_blueprint.route("/form/create", endpoint="form_create", methods=["POST", "GET"])
# @post_blueprint.route("/form/<int:id>/edit", endpoint="form_edit", methods=["POST", "GET"])
# def manage_post(id=None):
#     form = PostForm()
    
#     if id:
#         post = Post.query.get_or_404(id)
#         if request.method == 'GET':
#             form.title.data = post.title
#             form.description.data = post.description
#             form.image.data = post.image
#             form.creator_id.data = post.creator_id
#     else:
#         post = None

#     if request.method == 'POST':
#         if form.validate_on_submit():
#             image_name = None
#             if form.image.data:
#                 image = form.image.data
#                 image_name = secure_filename(image.filename)
#                 image_path = os.path.join('static/images/', image_name)
#                 image.save(image_path)
#             else:
#                 # Retain existing image if not updating
#                 image_name = post.image if post else None

#             data = {
#                 "title": form.title.data,
#                 "description": form.description.data,
#                 "image": image_name,
#                 "creator_id": form.creator_id.data
#             }

#             if post:
#                 # Update existing post
#                 post.title = data["title"]
#                 post.description = data["description"]
#                 post.image = data["image"]
#                 post.creator_id = data["creator_id"]
#             else:
#                 # Create new post
#                 post = Post(**data)
#                 db.session.add(post)

#             db.session.commit()
#             return redirect(url_for('posts.show', id=post.id))

#     return render_template("posts/forms/create.html", form=form, post=post)







#     # from app.posts.forms import PostForm

# # @post_blueprint.route("/form/create", endpoint="form_create", methods=["POST", "GET"])
# # def create_post():
# #     form  = PostForm()
# #     if request.method=='POST':
# #         if form.validate_on_submit():
# #             image_name=None
# #             if request.files.get('image'):
# #                 image= form.image.data
# #                 image_name =secure_filename(image.filename)
# #                 # save image to server
# #                 image.save(os.path.join('static/images/', image_name))
# #                 # then --> save image name in db ??
# #             data= dict(request.form)
# #             del data['csrf_token']
# #             del data['submit']
# #             # save only image name
# #             data["image"]= image_name
# #             print(request.form)
# #             post= Post(**data)
# #             db.session.add(Post)
# #             db.session.commit()
# #             return redirect(post.show_url)
# #     return  render_template("posts/forms/create.html", form=form)
