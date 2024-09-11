from app.creators import  creator_blueprint
from app.models import  db, Creator
from flask import  render_template, request, redirect, url_for

@creator_blueprint.route('', endpoint='landing')
def landing():
    creators = Creator.query.all()
    return render_template("creators/landing.html", creators=creators)


@creator_blueprint.route('/create', endpoint='create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        creator = Creator(name=request.form['name'])
        db.session.add(creator)
        db.session.commit()
        return redirect(url_for('creators.landing'))

    return render_template("creators/create.html")

@creator_blueprint.route('/<int:id>', endpoint='show', methods=['GET'])
def show(id):
    creator = db.get_or_404(Creator, id)
    return render_template("creators/show.html", creator=creator)