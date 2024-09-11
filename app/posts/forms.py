from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
from wtforms.validators import DataRequired, Length
from app.models import Creator, db


class postForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(2, 40)])
    description = StringField("Description")
    image= FileField("Image") 
    creator_id = SelectField("Creator", validators=[DataRequired()], choices=[])
    submit = SubmitField("submit")

    def __init__(self, *args, **kwargs):
        super(postForm, self).__init__(*args, **kwargs)
        self.creator_id.choices = [(c.id, c.name) for c in Creator.query.all()]
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField, SelectField, FileField, TextAreaField
# from wtforms.validators import DataRequired, Length
# from app.models import Post, Creator

# class PostForm(FlaskForm):
#     title = StringField("Title", validators=[DataRequired(), Length(2, 40)])
#     image = FileField("Image", validators=[DataRequired()])
#     description = TextAreaField("Description", validators=[Length(max=500)])

#     creator_id = SelectField("Creator", validators=[DataRequired()], choices=[])
#     submit = SubmitField("Save Post")

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         # Populate creator choices dynamically
#         self.creator_id.choices = [(c.id, c.name) for c in Creator.query.all()]


# from flask import Flask, render_template, redirect, url_for
# from flask_bootstrap import Bootstrap

# from flask_wtf import FlaskForm, CSRFProtect
# from wtforms import StringField, SubmitField, IntegerField, SelectField, FileField
# from wtforms.validators import DataRequired, Length
# from app.models import Post, db



# class PostForm(FlaskForm):
#     title = StringField("Name", validators=[DataRequired(), Length(2, 40)])
#     image= FileField("Image", validators=[DataRequired()])
#     description = StringField("Description")
#     # grade = IntegerField("Grade")


#     post_id = SelectField("Post", validators=[DataRequired()], choices=[])
#     submit = SubmitField("Save new Student")

#     def __init__(self, *args, **kwargs):
#         super(PostForm, self).__init__(*args, **kwargs)
#         # while creating object from form --> please give me the posts
#         self.post_id.choices = [(p.id, p.title) for p in Post.query.all()]