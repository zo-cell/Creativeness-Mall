from flask import Flask, render_template, redirect, session, url_for, flash, g, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError, DataRequired, Email, EqualTo, NumberRange
from flask_bcrypt import Bcrypt
from datetime import datetime
from werkzeug.utils import secure_filename
import pandas as pd
from dotenv import load_dotenv
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os

db = SQLAlchemy()
app = Flask(__name__)
app.app_context().push()
# app.app_context()
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY']=os.urandom(32)
db.init_app(app)



class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

class UserInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    apartment_no = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(80), nullable=False)
    cash = db.Column(db.Float, default=0)
    remember = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class UserProducts(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    Name = db.Column(db.String(300), nullable=False)
    Brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    old_price = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    size = db.Column(db.String(1000), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    img1 = db.Column(db.String(100), nullable=False)
    img2 = db.Column(db.String(100), nullable=False)
    section = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class DeleteMode(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    del_mode = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Transactions(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(300), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    img = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sub_total_ = db.Column(db.Integer, nullable=False)
    shipping_ = db.Column(db.Integer, nullable=False)
    taxes_ = db.Column(db.Integer, nullable=False)
    discount_ = db.Column(db.Integer, nullable=False)
    grand_total_ = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))



class OwnerTransactions(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    product_name = db.Column(db.String(300), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img1 = db.Column(db.String(100), nullable=False)
    img2 = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    old_price = db.Column(db.Integer, nullable=False)
    new_price = db.Column(db.Integer, nullable=False)
    date_time = db.Column(db.DateTime)
    purchases = db.Column(db.Integer, nullable=False)
    section = db.Column(db.String(100), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Products(db.Model):

    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    old_price = db.Column(db.Integer, nullable=False)
    new_price = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.String(500))
    img1 =db.Column(db.String(80), nullable=False)
    img2 = db.Column(db.String(80), nullable=False)
    img3 = db.Column(db.String(80), nullable=False)
    img4 = db.Column(db.String(80), nullable=False)
    img5 = db.Column(db.String(80), nullable=False)
    section = db.Column(db.String(100), nullable=False)

class Colors(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    color1 = db.Column(db.String(100))
    color2 = db.Column(db.String(100))
    color3 = db.Column(db.String(100))
    color4 = db.Column(db.String(100))
    color5 = db.Column(db.String(100))

class FastCheckout(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    size = db.Column(db.String(80), nullable=False)
    color = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class registrationForm(FlaskForm):
    username = StringField(validators=[InputRequired("please insert a Username"), Length(min=3, max=80)], render_kw={"placeholder": "username",'autofocus':True})
    email = StringField("Email addr ess", validators=[DataRequired(), Email()], render_kw={"placeholder": "Email"})
    password = PasswordField(validators=[InputRequired("Please insert a Password"), EqualTo('confirm', message='Passwords must match'),Length(min=8, max=50)], render_kw={"placeholder": "password"})
    # password2 = PasswordField(validators=[InputRequired("Please insert a Password"), Length(min=8, max=50)], render_kw={"placeholder": "password"})
    confirm  = PasswordField(validators=[InputRequired("Please repeat your Password"), EqualTo('password', message='Passwords must match'),Length(min=8, max=50)], render_kw={"placeholder": "repeat password"})
    submit = SubmitField("Register")

    def validate_useraname(self, username):
       existed_username = User.query.filter_by(
            username=username.data).first()

       if existed_username:
            raise ValidationError("this username is already existed blease choose another one")


class LoginForm(FlaskForm):
    username = StringField(validators=[ InputRequired(), Length(min=3, max=80)], render_kw={"placeholder":"username",'autofocus':True})
    password = PasswordField(validators=[ InputRequired(), Length(min=8, max=50)], render_kw={"placeholder":"password"})
    submit = SubmitField("Login")



@app.route("/register", methods=["GET", "POST"])
def register():

    # Declaring registrationForm:
    form=registrationForm()

    if form.validate_on_submit():
        # Hashing the users password:
        hashed_password = bcrypt.generate_password_hash(form.password.data)

        # Insert the new user data in the database:
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        # Putting the new user's username and id in a sessions:
        user_id = User.query.filter_by(email=form.email.data).first().id
        session["user"] = form.username.data
        session["id"] = user_id

        # Make a new row for the new user in UserInformation table:
        user_info = UserInformation.query.filter_by(user_id=session["id"]).first()
        if user_info:
            first_name = UserInformation.query.filter_by(user_id=session["id"]).first().first_name
            last_name = UserInformation.query.filter_by(user_id=session["id"]).first().last_name
            country = UserInformation.query.filter_by(user_id=session["id"]).first().country
            city  = UserInformation.query.filter_by(user_id=session["id"]).first().city
            address = UserInformation.query.filter_by(user_id=session["id"]).first().address
            apartment_no = UserInformation.query.filter_by(user_id=session["id"]).first().apartment_no
            phone = UserInformation.query.filter_by(user_id=session["id"]).first().phone
            cash = UserInformation.query.filter_by(user_id=session["id"]).first().cash

        if user_info:
            new_user_info = UserInformation(username=form.username.data, email=form.email.data, first_name=first_name, last_name=last_name, country=country, city=city, address=address, aprtment_no=apartment_no, phone=phone, cash=cash, remember=0, user_id=user_id)
            db.session.add(new_user_info)
            db.session.commit()
        else:
            new_user_infoo = UserInformation(username=form.username.data, email=form.email.data, first_name="---", last_name="---", country="---", city="---", address="---", apartment_no="---", phone="---", cash=0, remember=0, user_id=user_id)
            db.session.add(new_user_infoo)
            db.session.commit()

        return redirect("/")
    else:
        return render_template("register.html", form=form)




@app.route("/login", methods=["GET", "POST"])
def login():
    # declaring the LoginForm:
    form=LoginForm()
    if request.method=="POST":
        if form.validate_on_submit():

            # dropping any sessions on submitting the form:
            session.pop("user", None)

            # getting username of the user who is signing in from database:
            user = User.query.filter_by(username=form.username.data).first()

            # if the username and the password is correct:
            if user:

                # making a special account for the owner:
                if user.password == "admin@aDmin111" and user.username == "owner":

                    # if the password is correct set a session the owner id and password:
                    if form.password.data == user.password:
                        session["user"] = "admin@aDmin111"
                        session["id"] = user.id

                        return redirect('/')
                    else:
                        flash("invalid username or Password, try again...!")
                        return redirect("/login")


                # check if that user's password is correct:
                if bcrypt.check_password_hash(user.password, form.password.data):

                    # if it correct set a session for the id and Username:

                    session["user"] = form.username.data
                    session["id"] = user.id

                    return redirect('/')

                else:
                    flash("invalid username or Password, try again...!")
                    return redirect("/login")
            else:
                flash("invalid username, try again...!")
                return redirect(url_for('login'))
    return render_template("login.html", form=form, flash=flash)



@app.route("/", methods=["GET", "POST"])
def home():

        # declaring the del_mode_row variable:
        del_mode_row = 0

        # declaring some variables to get the products of new arrivals and best sellers sections:
        newarrivals_women_product = Products.query.order_by(Products.id.desc()).filter_by(section="newarrival-women").all()
        newarrivals_men_product = Products.query.order_by(Products.id.desc()).filter_by(section="newarrival-Men").all()
        newarrivals_kids_product = Products.query.order_by(Products.id.desc()).filter_by(section="newarrival-kids").all()
        best_sellers_women_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).filter_by(section="bestsellers-women").paginate(per_page=4)
        best_sellers_men_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).filter_by(section="bestsellers-Men").all()

        if request.method == "POST":

            # in case the user is logged in:
            if g.user:
                if g.id:

                    # getting the del_mode_row where user id equal to the user who is logged in id:
                    del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()

                    # getting the del_take value from the form in the frontend:
                    del_take = request.form.get('del_take')

                    # getting the products of the user who is logged in from database:
                    user_car = UserProducts.query.filter_by(user_id=session['id']).all()

                    # getting the length of the users' products:
                    L = len(user_car)

                    # if we have a del_take value comming from the frontend make the value of del_mode = 0:
                    if del_take:
                        del_mode_row.del_mode = 0
                        db.session.commit()
                        return render_template("index.html", title="Home", css="main.css", user=session["user"], flash=flash, user_car=user_car, L=L, del_mode_row=del_mode_row, newarrivals_women_product=newarrivals_women_product, best_sellers_women_products=best_sellers_women_products, best_sellers_men_products=best_sellers_men_products, newarrivals_men_product=newarrivals_men_product, newarrivals_kids_product=newarrivals_kids_product)
                    else:
                        return render_template("index.html", title="Home", css="main.css", user=session["user"], flash=flash, user_car=user_car, L=L, del_mode_row=del_mode_row, newarrivals_women_product=newarrivals_women_product, best_sellers_women_products=best_sellers_women_products, best_sellers_men_products=best_sellers_men_products, newarrivals_men_product=newarrivals_men_product, newarrivals_kids_product=newarrivals_kids_product)
        else:
            if g.user:
                if g.id:
                    user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                    L = len(user_car)
                    del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                    return render_template("index.html", title="Home", css="main.css", user=session["user"], flash=flash, user_car=user_car, L=L, del_mode_row=del_mode_row, newarrivals_women_product=newarrivals_women_product, best_sellers_women_products=best_sellers_women_products, best_sellers_men_products=best_sellers_men_products, newarrivals_men_product=newarrivals_men_product, newarrivals_kids_product=newarrivals_kids_product)
        return render_template("index.html", title="Home", css="main.css", del_mode_row=del_mode_row, newarrivals_women_product=newarrivals_women_product, best_sellers_women_products=best_sellers_women_products, best_sellers_men_products=best_sellers_men_products, newarrivals_men_product=newarrivals_men_product, newarrivals_kids_product=newarrivals_kids_product)

@app.before_request
def before_request():
    g.user = None
    g.id = None
    g.img1 = None

    if "user" in session and "id" in session:
        g.user = session["user"]
        g.id = session["id"]
        
    if "img1" in session:
        g.img1 = session["img1"]


@app.route("/search", methods=["GET", "POST"])
def Search():
    del_mode_row = 0
    if request.method == "POST":
        if g.user:
            if g.id:

                #shopping car things:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')

                # getting the searched product from the search input:
                searched = request.form.get('searched')

                # returning the search results to the frontend:
                search_results = Products.query.filter(Products.section.like('%'+ searched +'%')).all()

                #shopping car things:
                if del_take:
                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("search.html", title="Search", css="newarrivals.css", user=session["user"], user_car=user_car, L=L, del_mode_row=del_mode_row, searched=searched, search_results=search_results)
                else:
                    return render_template("search.html", title="Search", css="newarrivals.css", user=session["user"], user_car=user_car, L=L, del_mode_row=del_mode_row, searched=searched, search_results=search_results)


        else:
            searched = request.form.get('searched')
            search_results = Products.query.filter(Products.section.like('%'+ searched +'%')).all()
            return render_template("search.html", title="Search", css="newarrivals.css", searched=searched, search_results=search_results, del_mode_row=del_mode_row)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("search.html", title="Search", css="newarrivals.css", user=session["user"], user_car=user_car, L=L, del_mode_row=del_mode_row)
    return render_template("search.html", title="Search", css="newarrivals.css", del_mode_row=del_mode_row)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    session.clear()
    flash("you have logged out successfully!")
    return redirect("/login")





@app.route("/dashboard_back")
def dashboard_back():
    return redirect("/dashboard")


# upload_folder = os.path.join('static','uploads')
# app.config["IMAGE_UPLOADS"] = os.getcwd()
app.config["IMAGE_UPLOADS"] = "/opt/render/project/src/"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "WEBP", "AVIF", "GIF"]

def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

@app.route("/creation_form-<string:sec>", methods=["GET", "POST"])
def creation_form(sec):
    # app.logger.info('in creation_form-<string:sec> route')
    cloudinary.config(
        cloud_name="drnoxkesy,
        api_key="828688123921376", 
        api_secret="i0reEJH3AzbvkqP119DjXEzvKa8,
    )
    path = None
    # getting products from database and getting ots length:
    products = Products.query.order_by(Products.id).all()
    LP = len(products)

    if request.method == "POST":
        if g.user:

            # getting the section name from the form in frontend:
            section_take = request.form.get('section_take')

            # passes section name to itself:
            if section_take:
                return redirect(url_for('creation_form', sec=sec))
            else:
                # then it use it in posting into the database process:
                name = request.form.get('name')
                brand= request.form.get('brand')
                description = request.form.get('description')

                # getting colors from colors input and filtering it befor posting in the database:
                color1 = request.form.get('color1')
                if color1 == '----':
                    color1 = ""
                else:
                    color1 = request.form.get('color1')
                color2 = request.form.get('color2')
                if color2 == '----':
                    color2 = ""
                else:
                    color2 = request.form.get('color2')
                color3 = request.form.get('color3')
                if color3 == '----':
                    color3 = ""
                else:
                    color3 = request.form.get('color3')
                color4 = request.form.get('color4')
                if color4 == '----':
                    color4 = ""
                else:
                    color4 = request.form.get('color4')
                color5 = request.form.get('color5')
                if color5 == '----':
                    color5 = ""
                else:
                    color5 = request.form.get('color5')
                colors = f"{color1} {color2}\n{color3} {color4}\n{color5}"
                old_price = request.form.get('old_price')
                new_price = request.form.get('new_price')

                # getting the images from its form inputs at the frontend:
                if request.files['img1']:
                    img1 = request.files['img1']
                    # app.logger.info('%s img1', img1)
                else:
                    img1 = None
                if request.files['img2']:
                    img2 = request.files['img2']
                else:
                    img2 = None

                if request.files['img3']:
                    img3 = request.files['img3']
                else:
                    img3 = None

                if request.files['img4']:
                    img4 = request.files['img4']
                else:
                    img4 = None

                if request.files['img5']:
                    img5 = request.files['img5']
                else:
                    img5 = None

                # securing filenames before saving it on the server:
                if img1 != None:
                    image1 = secure_filename(img1.filename)
                else:
                    image1 = "no_photo.jpg"

                if img2 != None:
                    image2 = secure_filename(img2.filename)
                else:
                    image2 = "no_photo.jpg"
                if img3 != None:
                    image3 = secure_filename(img3.filename)
                else:
                    image3 = "no_photo.jpg"
                if img4 != None:
                    image4 = secure_filename(img4.filename)
                else:
                    image4 = "no_photo.jpg"
                if img5 != None:
                    image5 = secure_filename(img5.filename)
                else:
                    image5 = "no_photo.jpg"

                # saving images on the server:
                if img1 != None:
                    # img1.save(os.path.join(app.config["IMAGE_UPLOADS"], image1))
                    # path = os.path.join(app.config["IMAGE_UPLOADS"], image1)
                    # flash(path)
                    session["img1"] = image1
                    # secured_image = os.path.join(app.config["IMAGE_UPLOADS"], image1)
                    
                    cloudinary.config(
                        cloud_name="drnoxkesy,
                        api_key="828688123921376", 
                        api_secret="i0reEJH3AzbvkqP119DjXEzvKa8,
                    )
                    
                    upload_result = cloudinary.uploader.upload(img1)
                    image_info = cloudinary.api.resource
                    # app.logger.info(upload_result)
                    # return jsonify(upload_result)
                if img2 != None:
                    img2.save(os.path.join(app.config["IMAGE_UPLOADS"], img2.filename))
                if img3 != None:
                    img3.save(os.path.join(app.config["IMAGE_UPLOADS"], img3.filename))
                if img4 != None:
                    img4.save(os.path.join(app.config["IMAGE_UPLOADS"], img4.filename))
                if img5 != None:
                    img5.save(os.path.join(app.config["IMAGE_UPLOADS"], img5.filename))


                if not allowed_image(image1) or not allowed_image(image2) or not allowed_image(image3) or not allowed_image(image4) or not allowed_image(image5):
                    return redirect(request.url)
                ST = sec

                # posting in the database tables the new product:
                NewProduct = Products(name=name, brand=brand, description=description, colors=colors, old_price=old_price, new_price=new_price, img1=image1, img2=image2, img3=image3, img4=image4, img5=image5, section=ST)
                db.session.add(NewProduct)
                NewColor = Colors(color1=color1, color2=color2, color3=color3, color4=color4, color5=color5)
                db.session.add(NewColor)
                db.session.commit()


                return redirect('/dashboard')
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                return render_template("creation_form.html", title="creating a new product", css="creation_form.css", user=session["user"], sec=sec, L=L, user_car=user_car)
    return render_template("creation_form.html", title="creating a new product", css="creation_form.css", sec=sec)






@app.route("/dashboard")
def dashboard():

    # getting all products from database for product table in the dashboard:
    products = Products.query.order_by(Products.id).all()

    # getting all transactions from database for transactions table in the dashboard:
    transactions = Transactions.query.order_by(Transactions.id).all()

    # getting all the best sellers products from database for best sellers table in the dashboard:
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()

    # getting all users from database for users table in the dashboard:
    users = User.query.order_by(User.id).all()

    # getting all user informations from database for user inforamtion table in the dashboard:
    users_info = UserInformation.query.order_by(UserInformation.id).all()

    # getting the length of transactions:
    TL = len(transactions)

    # getting the length of best sellers:
    BL = len(best_sellers_products)

    # getting the length of the users:
    UL = len(users)

    # getting the length of products:
    LP = len(products)

    if g.user:
        if g.id:
            user_car = UserProducts.query.filter_by(user_id=session['id']).all()
            L = len(user_car)
            return render_template("dashboard.html", title="Controll pad", css="dashboard.css", user=session["user"], products=products, user_car=user_car, L=L, LP=LP, TL=TL, BL=BL, UL=UL, users=users, users_info=users_info, transactions=transactions, best_sellers_products=best_sellers_products)
    if g.user:
        if g.id:
            if g.img1:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                return render_template("dashboard.html", title="Controll pad", css="dashboard.css", user=session["user"], products=products, user_car=user_car, L=L, LP=LP, TL=TL, BL=BL, UL=UL, users=users, users_info=users_info, transactions=transactions, best_sellers_products=best_sellers_products, img1=session["img1"])
    return render_template("dashboard.html", title="Controll pad", css="dashboard.css", LP=LP, TL=TL, BL=BL, UL=UL, users=users, users_info=users_info, transactions=transactions, best_sellers_products=best_sellers_products)









@app.route("/update<int:id>", methods=["GET", "POST"])
def update(id):
    product_to_update = Products.query.get_or_404(id)
    color_to_update = Colors.query.get_or_404(id)
    if request.method == "POST":
        if g.user:
            product_to_update.name = request.form.get('name')
            product_to_update.brand = request.form.get('brand')
            product_to_update.description = request.form.get('description')

            color1 = request.form.get('color1')
            if color1 == '----':
                color1 = ""
            else:
                color1 = request.form.get('color1')
            color2 = request.form.get('color2')
            if color2 == '----':
                color2 = ""
            else:
                color2 = request.form.get('color2')
            color3 = request.form.get('color3')
            if color3 == '----':
                color3 = ""
            else:
                color3 = request.form.get('color3')
            color4 = request.form.get('color4')
            if color4 == '----':
                color4 = ""
            else:
                color4 = request.form.get('color4')
            color5 = request.form.get('color5')
            if color5 == '----':
                color5 = ""
            else:
                color5 = request.form.get('color5')
            colors = f"{color1} {color2}\n{color3} {color4}\n{color5}"

            color_to_update.color1 = color1
            color_to_update.color2 = color2
            color_to_update.color3 = color3
            color_to_update.color4 = color4
            color_to_update.color5 = color5
            product_to_update.colors = colors
            product_to_update.old_price = request.form.get('old_price')
            product_to_update.new_price = request.form.get('new_price')

            if request.files['img1']:
                    img1 = request.files['img1']
            else:
                img1 = None

            if request.files['img2']:
                img2 = request.files['img2']
            else:
                img2 = None

            if request.files['img3']:
                img3 = request.files['img3']
            else:
                img3 = None

            if request.files['img4']:
                img4 = request.files['img4']
            else:
                img4 = None

            if request.files['img5']:
                img5 = request.files['img5']
            else:
                img5 = None


            if img1 != None:
                image1 = secure_filename(img1.filename)
            else:
                image1 = "no_photo.jpg"

            if img2 != None:
                image2 = secure_filename(img2.filename)
            else:
                image2 = "no_photo.jpg"
            if img3 != None:
                image3 = secure_filename(img3.filename)
            else:
                image3 = "no_photo.jpg"
            if img4 != None:
                image4 = secure_filename(img4.filename)
            else:
                image4 = "no_photo.jpg"
            if img5 != None:
                image5 = secure_filename(img5.filename)
            else:
                image5 = "no_photo.jpg"

            if img1 != None:
                img1.save(os.path.join(app.config["IMAGE_UPLOADS"], img1.filename))
            if img2 != None:
                img2.save(os.path.join(app.config["IMAGE_UPLOADS"], img2.filename))
            if img3 != None:
                img3.save(os.path.join(app.config["IMAGE_UPLOADS"], img3.filename))
            if img4 != None:
                img4.save(os.path.join(app.config["IMAGE_UPLOADS"], img4.filename))
            if img5 != None:
                img5.save(os.path.join(app.config["IMAGE_UPLOADS"], img5.filename))


            if not allowed_image(image1) or not allowed_image(image2) or not allowed_image(image3) or not allowed_image(image4) or not allowed_image(image5):
                return redirect(request.url)

            product_to_update.img1  = image1
            product_to_update.img2 = image2
            product_to_update.img3 = image3
            product_to_update.img4 = image4
            product_to_update.img5 = image5
            try:
                db.session.commit()
                return redirect("/dashboard")
            except:
                flash("oops something went wrong while updating!!")
            return render_template("update.html",title="update" , css="update.css", user=session["user"], product_to_update=product_to_update)
    if g.user:
        if g.id:
            user_car = UserProducts.query.filter_by(user_id=session['id']).all()
            L = len(user_car)
            return render_template("update.html",title="update" , css="update.css", user=session["user"], product_to_update=product_to_update, flash=flash, user_car=user_car, L=L)
    return render_template("update.html",title="update" , css="update.css", product_to_update=product_to_update)


@app.route("/delete/<int:id>")
def delete(id):
    product_to_delete = Products.query.get_or_404(id)
    color_to_delete = Colors.query.get_or_404(id)
    try:
        db.session.delete(product_to_delete)
        db.session.delete(color_to_delete)
        db.session.commit()
        return redirect("/dashboard")
    except:
        flash("somthing went wrong while deleting")
    return render_template("dashboard.html", flash=flash)


@app.route("/product<int:id>", methods=["GET", "POST"])
def productss(id):

    # getting the chosen Product to display it on the page:
    product_to_show = Products.query.get_or_404(id)

    # getting the chosen product colors from database:
    color_to_show = Colors.query.get_or_404(id)

    # taking the size, color and quantity from the user:
    size = request.form.get('size')
    color = request.form.get('color_take')
    quantity = request.form.get('quantity')

    del_mode_row = 0
    if request.method == 'POST':
        if g.user:
            if g.id:

                # declaring all the chosen product in a variable:
                name = product_to_show.name
                brand = product_to_show.brand
                description = product_to_show.description
                old_price = product_to_show.old_price
                price = product_to_show.new_price
                size = request.form.get('size')
                color = request.form.get('color_take')
                quantity = request.form.get('quantity')
                img1 = product_to_show.img1
                img2 = product_to_show.img2
                section = product_to_show.section
                user_id = session['id']
                product_id = product_to_show.id
                color_take2 = request.form.get('color_take2')

                # getting the fast checkout transactions from database:
                all_user_fast_check = FastCheckout.query.filter_by(user_id=session["id"]).all()
                user_fast_check = FastCheckout.query.filter_by(user_id=session["id"]).first()

                # shopping car things:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                del_take = request.form.get('del_take')

                del_mode_rows = DeleteMode.query.filter_by(user_id=session["id"]).all()
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()

                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)

                if del_take:
                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("product.html", title="product", css="product.css", user=session["user"], product_to_show=product_to_show, color_to_show=color_to_show, user_car=user_car, L=L, size=size, color=color, quantity=quantity, del_mode_row=del_mode_row)
                else:

                    if size and color and quantity:

                        # posting the new user product in the database:
                        New_User_Product = UserProducts(Name=name, Brand=brand, description=description,
                                                        old_price=old_price, price=price, size=size,
                                                        color=color, quantity=quantity, img1=img1,
                                                        img2=img2, section=section, product_id=product_id,
                                                        user_id=user_id)

                        db.session.add(New_User_Product)
                        db.session.commit()
                    else:
                        flash("Choose a size, color and  quantity!")

                    # shopping car things:
                    if len(del_mode_rows) == 1:
                        db.session.delete(del_mode_row)
                        db.session.commit()
                        New_Delete_Mode = DeleteMode(del_mode=0, user_id=session["id"])
                        db.session.add(New_Delete_Mode)
                        db.session.commit()
                    else:
                        New_Delete_Mode = DeleteMode(del_mode=0, user_id=session["id"])
                        db.session.add(New_Delete_Mode)
                        db.session.commit()

                    i = product_to_show.id

                    # posting and updating the fast checkout table:
                    if color_take2:
                        if len(all_user_fast_check) == 1:
                            try:
                                db.session.delete(user_fast_check)
                                db.session.commit()
                            except:
                                flash("something went wrong!")
                            New_User_FastCheckout = FastCheckout(size=size, color=color, quantity=quantity, user_id=session["id"])
                            try:
                                db.session.add(New_User_FastCheckout)
                                db.session.commit()
                            except:
                                flash("something went wrong!")
                        else:
                            New_User_FastCheckout = FastCheckout(size=size, color=color, quantity=quantity, user_id=session["id"])
                            try:
                                db.session.add(New_User_FastCheckout)
                                db.session.commit()
                            except:
                                flash("something went wrong!")

                        return redirect(url_for('fast_checkout', id=i))
                    else:
                        return redirect(url_for('product_back', id=i))


        else:
            if size and color and quantity:

                flash("You have to log in first!")

            else:
                flash("Choose a size, color and  quantity!")


    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()

                return render_template("product.html", title="product", css="product.css", user=session["user"], product_to_show=product_to_show, color_to_show=color_to_show, user_car=user_car, L=L, size=size, color=color, quantity=quantity, del_mode_row=del_mode_row)
    return render_template("product.html", title="product", css="product.css", product_to_show=product_to_show, color_to_show=color_to_show, size=size, color=color, quantity=quantity, del_mode_row=del_mode_row)


@app.route("/product_back/<int:id>")
def product_back(id):
    product_to_show = Products.query.get_or_404(id)
    d = product_to_show.id

    return redirect(url_for('productss', id=d))




@app.route('/cart_delete/<int:id>')
def cart_delete(id):
    if g.user:
        if g.id:
            cart_product_to_delete = UserProducts.query.get_or_404(id)
            back = request.referrer
            del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()

            try:
                del_mode_row.del_mode = 1
                db.session.delete(cart_product_to_delete)
                db.session.commit()
                return redirect(back)
            except:
                flash("somthing went wrong, the product is not deleted!")

    return render_template("product.html", title="product", css="product.css")


@app.route('/cart_update/<int:id>/<int:id2>')
def cart_update(id, id2):
    product_to_show = Products.query.get_or_404(id2)
    o = product_to_show.id
    color_to_show = Colors.query.get_or_404(id2)
    if g.user:
        if g.id:
            cart_product_to_delete = UserProducts.query.get_or_404(id)

            try:
                db.session.delete(cart_product_to_delete)
                db.session.commit()
                return redirect(url_for('productss', id=o))

            except:
                flash("somthing went wrong, the product in not deleted!")
    return render_template("product.html", title="product", css="product.css", product_to_show=product_to_show, color_to_show=color_to_show)







#purchase process:
@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    del_mode_row=0
    if g.user:
        if g.id:

           # getting user's email from the database:
            user_email = User.query.filter_by(id=session["id"]).first().email

            # shopping car things:
            user_car = UserProducts.query.filter_by(user_id=session['id']).all()
            L = len(user_car)

            # getting user's informations from the database:
            rem = UserInformation.query.filter_by(user_id=session["id"]).first()

            # decalring user's id session in a variable:
            user_id = session['id']

            # getting user's product from the database and getting its length:
            products = UserProducts.query.filter_by(user_id=session["id"]).all()
            LP = len(products)

            # setting date and time:
            date_time = datetime.now()

            # getting user's information from database to make sure that he has just a one row:
            user_information_validation = UserInformation.query.filter_by(user_id=session["id"]).all()

            # shopping car things:
            del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()

            if request.method == "POST":

                # declaring user informations in a variable:
                username = User.query.filter_by(id=session["id"]).first().username

                email = User.query.filter_by(id=session["id"]).first().email

                fname = request.form.get('fname')

                lname = request.form.get('lname')

                country = request.form.get('country')

                city = request.form.get('city')

                address = request.form.get('address')

                apartment_no = request.form.get('apartment_no')

                phone = request.form.get('phone')

                # setting and declaring the remember inputs to save user's informations at the checkout form:
                remember1 = request.form.get('remember')
                if remember1 == None:
                    remember1 = 0
                remember2 = request.form.get('remember2')
                remember3 = request.form.get('remember3')
                if remember3 == None:
                    remember3 = 0
                cash = request.form.get('cash')

                # counting the purchase total:
                subtotal=0
                for car in user_car:
                    subtotal += float(car.price * car.quantity)

                shipping = float(subtotal * 5/100)
                taxes = float(subtotal * 15/100)
                discount = float(subtotal * 10/100)
                grand_total = subtotal + shipping + taxes - discount

                current_user_info = UserInformation.query.filter_by(user_id=session["id"]).all()
                current_user_cash = 0

                # shopping car things:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')

                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row, user_information_validation=user_information_validation)
                else:


                    if len(current_user_info) == 1:

                        # getting the current user cash from the database:
                        current_user_cash = UserInformation.query.filter_by(user_id=session["id"]).first().cash

                    info_row = UserInformation.query.filter_by(user_id=session["id"]).first()

                    # setting remember process to save user informations in the checkout form:
                    if len(current_user_info) == 1 and remember1 != 1 and remember3 == None:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!")
                        # counting the new user cash after purchasing:
                        new_user_cash= current_user_cash - grand_total

                        # adding the new user informations at the database:
                        NewInfo = UserInformation(username=username, email=email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember2, user_id=user_id)
                        try:
                            db.session.add(NewInfo)
                            db.session.commit()
                            NewTrans=0
                            for t in range(LP):

                                # counting the invoice total for each product:
                                sub_total = products[t].price * products[t].quantity
                                _shipping_ = float(sub_total * 5/100)
                                _taxes_ = float(sub_total * 15/100)
                                _discount_ = float(sub_total * 10/100)
                                _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)

                                # adding the new purchasing process in the Transactions table at the database:
                                NewTrans = Transactions(product_name=products[t].Name, brand=products[t].Brand,img=products[t].img1, color=products[t].color, size=products[t].size ,price=products[t].price, quantity=products[t].quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=products[t].product_id, user_id=user_id)

                                # adding the new purchasing process in the OwnerTransactions table at the database to sum the number of burchases of each product:
                                existed_product_name = OwnerTransactions.query.filter_by(product_name=products[t].Name).first()
                                if "women" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "Men" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "kids" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                else:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)

                                if existed_product_name:
                                    times = existed_product_name.purchases
                                    try:
                                        db.session.delete(existed_product_name)
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")

                                    if "women" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "Men" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "kids" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    else:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)


                                    try:
                                        db.session.add_all([NeWTrAnS2])
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")
                                else:
                                    db.session.add_all([NewTrans2])
                                    db.session.commit()

                                db.session.add_all([NewTrans])
                                db.session.delete(products[t])
                                db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong !!")

                        return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row, user_information_validation=user_information_validation)
                    elif len(current_user_info) == 1 and rem.remember != 1:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!, check your information")
                        new_user_cash= current_user_cash - grand_total
                        NewInfoo = UserInformation(username=username, email=email,first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember3, user_id=user_id)
                        try:
                            db.session.add(NewInfoo)
                            db.session.commit()
                            NewTrans=0
                            for t in range(LP):
                                sub_total = products[t].price * products[t].quantity
                                _shipping_ = float(sub_total * 5/100)
                                _taxes_ = float(sub_total * 15/100)
                                _discount_ = float(sub_total * 10/100)
                                _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                                NewTrans = Transactions(product_name=products[t].Name, brand=products[t].Brand,img=products[t].img1, color=products[t].color, size=products[t].size ,price=products[t].price, quantity=products[t].quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=products[t].product_id, user_id=user_id)

                                existed_product_name = OwnerTransactions.query.filter_by(product_name=products[t].Name).first()
                                if "women" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "Men" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "kids" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                else:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)

                                if existed_product_name:
                                    times = existed_product_name.purchases
                                    try:
                                        db.session.delete(existed_product_name)
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")

                                    if "women" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "Men" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "kids" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    else:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)

                                    try:
                                        db.session.add_all([NeWTrAnS2])
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")
                                else:
                                    db.session.add_all([NewTrans2])
                                    db.session.commit()


                                db.session.add_all([NewTrans])
                                db.session.delete(products[t])
                                db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!, check your information")

                        return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row, user_information_validation=user_information_validation)

                    elif len(current_user_info) == 1 and rem.remember == 1:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!, check your information")
                        new_user_cash= current_user_cash - grand_total
                        NewInfoo = UserInformation(username=username, email=email,first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember1, user_id=user_id)
                        try:
                            db.session.add(NewInfoo)
                            db.session.commit()
                            NewTrans=0
                            for t in range(LP):
                                sub_total = products[t].price * products[t].quantity
                                _shipping_ = float(sub_total * 5/100)
                                _taxes_ = float(sub_total * 15/100)
                                _discount_ = float(sub_total * 10/100)
                                _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                                NewTrans = Transactions(product_name=products[t].Name, brand=products[t].Brand,img=products[t].img1, color=products[t].color, size=products[t].size ,price=products[t].price, quantity=products[t].quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=products[t].product_id, user_id=user_id)

                                existed_product_name = OwnerTransactions.query.filter_by(product_name=products[t].Name).first()
                                if "women" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "Men" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "kids" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                else:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)

                                if existed_product_name:
                                    times = existed_product_name.purchases
                                    try:
                                        db.session.delete(existed_product_name)
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")

                                    if "women" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "Men" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "kids" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    else:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)


                                    try:
                                        db.session.add_all([NeWTrAnS2])
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")
                                else:
                                    db.session.add_all([NewTrans2])
                                    db.session.commit()



                                db.session.add_all([NewTrans])
                                db.session.delete(products[t])
                                db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!, check your information")

                        return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row, user_information_validation=user_information_validation)

                    else:
                        new_user_cash = current_user_cash - grand_total
                        NewInfo = UserInformation(username=username, email=email,first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=cash, remember=remember3, user_id=user_id)
                        try:
                            db.session.add(NewInfo)
                            db.session.commit()
                            NewTrans=0
                            for t in range(LP):
                                sub_total = products[t].price * products[t].quantity
                                _shipping_ = float(sub_total * 5/100)
                                _taxes_ = float(sub_total * 15/100)
                                _discount_ = float(sub_total * 10/100)
                                _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                                NewTrans = Transactions(product_name=products[t].Name, brand=products[t].Brand,img=products[t].img1, color=products[t].color, size=products[t].size ,price=products[t].price, quantity=products[t].quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=products[t].product_id, user_id=user_id)

                                existed_product_name = OwnerTransactions.query.filter_by(product_name=products[t].Name).first()
                                if "women" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "Men" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                elif "kids" in products[t].section:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)
                                else:
                                    NewTrans2 = OwnerTransactions(product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=1, product_id=products[t].product_id, user_id=user_id)

                                if existed_product_name:
                                    times = existed_product_name.purchases
                                    try:
                                        db.session.delete(existed_product_name)
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")

                                    if "women" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-women", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "Men" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-Men", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    elif "kids" in products[t].section:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section="bestsellers-kids", color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)
                                    else:
                                        NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=products[t].Name, brand=products[t].Brand, description=products[t].description, img1=products[t].img1, img2=products[t].img2, section=products[t].section, color=products[t].color, old_price=products[t].old_price, new_price=products[t].price, date_time=date_time, purchases=times+1, product_id=products[t].product_id, user_id=user_id)


                                    try:
                                        db.session.add_all([NeWTrAnS2])
                                        db.session.commit()
                                    except:
                                        flash("Something went wrong!")
                                else:
                                    db.session.add_all([NewTrans2])
                                    db.session.commit()



                                db.session.add_all([NewTrans])
                                db.session.delete(products[t])
                                db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!, check your information")

                        return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row, user_information_validation=user_information_validation)
            else:
                subtotal=0
                for car in user_car:
                    subtotal += float(car.price * car.quantity)

                shipping = float(subtotal * 5/100)
                taxes = float(subtotal * 15/100)
                discount = float(subtotal * 10/100)
                grand_total = subtotal + shipping + taxes - discount
                info_row = UserInformation.query.filter_by(user_id=session["id"]).first()
                current_user_info = UserInformation.query.filter_by(user_id=session["id"]).all()
                current_user_cash = 0
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                if len(current_user_info) == 1:
                    current_user_cash = UserInformation.query.filter_by(user_id=session["id"]).first().cash
                return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, del_mode_row=del_mode_row, user_information_validation=user_information_validation)
    return render_template("checkout.html", title="checkout", css="checkout.css", del_mode_row=del_mode_row, user_information_validation=user_information_validation)




@app.route("/fast_checkout<int:id>", methods=["GET", "POST"])
def fast_checkout(id):
    product_to_show = Products.query.get_or_404(id)
    color_to_show = Colors.query.get_or_404(id)
    del_mode_row=0
    if g.user:
        if g.id:

            user_email = User.query.filter_by(id=session["id"]).first().email
            user_car = UserProducts.query.filter_by(user_id=session['id']).all()
            L = len(user_car)
            rem = UserInformation.query.filter_by(user_id=session["id"]).first()
            user_id = session['id']
            products = UserProducts.query.filter_by(user_id=session["id"]).all()
            LP = len(products)
            date_time = datetime.now()
            product_to_show = Products.query.get_or_404(id)
            color_to_show = Colors.query.get_or_404(id)


            user_fast_check = FastCheckout.query.filter_by(user_id=session["id"]).first()

            pro_del = UserProducts.query.filter_by(product_id=id).first()

            if request.method == "POST":

                username = User.query.filter_by(id=session["id"]).first().username

                user_email = User.query.filter_by(id=session["id"]).first().email

                fname = request.form.get('fname')

                lname = request.form.get('lname')

                country = request.form.get('country')

                city = request.form.get('city')

                address = request.form.get('address')

                apartment_no = request.form.get('apartment_no')

                phone = request.form.get('phone')


                remember1 = request.form.get('remember')
                if remember1 == None:
                    remember1 = 0
                remember2 = request.form.get('remember2')
                remember3 = request.form.get('remember3')
                if remember3 == None:
                    remember3 = 0





                subtotal = float(product_to_show.new_price * user_fast_check.quantity)

                shipping = float(subtotal * 5/100)
                taxes = float(subtotal * 15/100)
                discount = float(subtotal * 10/100)
                grand_total = subtotal + shipping + taxes - discount

                current_user_info = UserInformation.query.filter_by(user_id=session["id"]).all()
                current_user_cash = 0

                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')

                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("checkout.html", title="checkout", css="checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, del_mode_row=del_mode_row)
                else:

                    if len(current_user_info) == 1:

                        current_user_cash = UserInformation.query.filter_by(user_id=session["id"]).first().cash

                    info_row = UserInformation.query.filter_by(user_id=session["id"]).first()


                    if len(current_user_info) == 1 and remember1 != 1 and remember3 == None:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!")
                        new_user_cash= current_user_cash - grand_total
                        NewInfo = UserInformation(username=username, user_email=user_email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember2, user_id=user_id)
                        try:
                            db.session.add(NewInfo)
                            db.session.commit()

                            sub_total = product_to_show.new_price * user_fast_check.quantity
                            _shipping_ = float(sub_total * 5/100)
                            _taxes_ = float(sub_total * 15/100)
                            _discount_ = float(sub_total * 10/100)
                            _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                            NewTrans = Transactions(product_name=product_to_show.name, brand=product_to_show.brand,img=product_to_show.img1, color=user_fast_check.color, size=user_fast_check.size, price=product_to_show.new_price, quantity=user_fast_check.quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=product_to_show.id, user_id=user_id)

                            existed_product_name = OwnerTransactions.query.filter_by(product_name=product_to_show.name).first()
                            if "women" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "Men" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "kids" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            else:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)





                            if existed_product_name:
                                times = existed_product_name.purchases
                                try:
                                    db.session.delete(existed_product_name)
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")


                                if "women" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "Men" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "kids" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                else:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)



                                try:
                                    db.session.add_all([NeWTrAnS2])
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")
                            else:
                                db.session.add_all([NewTrans2])
                                db.session.commit()

                            db.session.add(NewTrans)
                            db.session.delete(pro_del)
                            db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong !!")

                        return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, product_to_show=product_to_show, color_to_show=color_to_show, user_fast_check=user_fast_check, del_mode_row=del_mode_row)
                    elif len(current_user_info) == 1 and rem.remember != 1:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!, check your information")
                        new_user_cash= current_user_cash - grand_total
                        NewInfoo = UserInformation(username=username, email=user_email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember3, user_id=user_id)
                        try:
                            db.session.add(NewInfoo)
                            db.session.commit()

                            sub_total = product_to_show.new_price * user_fast_check.quantity
                            _shipping_ = float(sub_total * 5/100)
                            _taxes_ = float(sub_total * 15/100)
                            _discount_ = float(sub_total * 10/100)
                            _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                            NewTrans = Transactions(product_name=product_to_show.name, brand=product_to_show.brand,img=product_to_show.img1, color=user_fast_check.color, size=user_fast_check.size ,price=product_to_show.new_price, quantity=user_fast_check.quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=product_to_show.id, user_id=user_id)

                            existed_product_name = OwnerTransactions.query.filter_by(product_name=product_to_show.name).first()
                            if "women" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "Men" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "kids" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            else:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)





                            if existed_product_name:
                                times = existed_product_name.purchases
                                try:
                                    db.session.delete(existed_product_name)
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")


                                if "women" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "Men" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "kids" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                else:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)



                                try:
                                    db.session.add_all([NeWTrAnS2])
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")
                            else:
                                db.session.add_all([NewTrans2])
                                db.session.commit()

                            db.session.add(NewTrans)
                            db.session.delete(pro_del)
                            db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!!, check your information")

                        return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, product_to_show=product_to_show, color_to_show=color_to_show, user_fast_check=user_fast_check, del_mode_row=del_mode_row)

                    elif len(current_user_info) == 1 and rem.remember == 1:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!, check your information")
                        new_user_cash= current_user_cash - grand_total
                        NewInfoo = UserInformation(username=username, email=user_email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember1, user_id=user_id)
                        try:
                            db.session.add(NewInfoo)
                            db.session.commit()

                            sub_total = product_to_show.new_price * user_fast_check.quantity
                            _shipping_ = float(sub_total * 5/100)
                            _taxes_ = float(sub_total * 15/100)
                            _discount_ = float(sub_total * 10/100)
                            _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                            NewTrans = Transactions(product_name=product_to_show.name, brand=product_to_show.brand,img=product_to_show.img1, color=user_fast_check.color, size=user_fast_check.size ,price=product_to_show.new_price, quantity=user_fast_check.quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=product_to_show.id, user_id=user_id)

                            existed_product_name = OwnerTransactions.query.filter_by(product_name=product_to_show.name).first()
                            if "women" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "Men" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "kids" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            else:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)





                            if existed_product_name:
                                times = existed_product_name.purchases
                                try:
                                    db.session.delete(existed_product_name)
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")


                                if "women" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "Men" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "kids" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                else:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)



                                try:
                                    db.session.add_all([NeWTrAnS2])
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")
                            else:
                                db.session.add_all([NewTrans2])
                                db.session.commit()

                            db.session.add(NewTrans)
                            db.session.delete(pro_del)
                            db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!!, check your information")

                        return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, product_to_show=product_to_show, color_to_show=color_to_show, user_fast_check=user_fast_check, del_mode_row=del_mode_row)

                    else:
                        new_user_cash = current_user_cash - grand_total
                        NewInfo = UserInformation(username=username, email=user_email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=new_user_cash, remember=remember3, user_id=user_id)


                        try:
                            db.session.add(NewInfo)
                            db.session.commit()


                            sub_total = product_to_show.new_price * user_fast_check.quantity
                            _shipping_ = float(sub_total * 5/100)
                            _taxes_ = float(sub_total * 15/100)
                            _discount_ = float(sub_total * 10/100)
                            _grand_total_ = float(sub_total + _shipping_ + _taxes_ - _discount_)
                            NewTrans = Transactions(product_name=product_to_show.name, brand=product_to_show.brand,img=product_to_show.img1, color=user_fast_check.color, size=user_fast_check.size ,price=product_to_show.new_price, quantity=user_fast_check.quantity, sub_total_=sub_total ,shipping_=_shipping_, taxes_=_taxes_, discount_=_discount_, grand_total_=_grand_total_, date_time=date_time, product_id=product_to_show.id, user_id=user_id)

                            existed_product_name = OwnerTransactions.query.filter_by(product_name=product_to_show.name).first()
                            if "women" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "Men" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            elif "kids" in product_to_show.section:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)
                            else:
                                NewTrans2 = OwnerTransactions(product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description , img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=1, product_id=product_to_show.id, user_id=user_id)





                            if existed_product_name:
                                times = existed_product_name.purchases
                                try:
                                    db.session.delete(existed_product_name)
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")


                                if "women" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-women", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "Men" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-Men", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                elif "kids" in product_to_show.section:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section="bestsellers-kids", color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)
                                else:
                                    NeWTrAnS2 = OwnerTransactions(id=existed_product_name.id, product_name=product_to_show.name, brand=product_to_show.brand, description=product_to_show.description, img1=product_to_show.img1, img2=product_to_show.img2, section=product_to_show.section, color=user_fast_check.color, old_price=product_to_show.old_price, new_price=product_to_show.new_price, date_time=date_time, purchases=times+1, product_id=product_to_show.id, user_id=user_id)



                                try:
                                    db.session.add_all([NeWTrAnS2])
                                    db.session.commit()
                                except:
                                    flash("Something went wrong!")
                            else:
                                db.session.add_all([NewTrans2])
                                db.session.commit()

                            db.session.add(NewTrans)
                            db.session.delete(pro_del)
                            db.session.commit()
                            flash("Your purchase process is done Successfully!")
                            return redirect("/order_history")
                        except:
                            flash("something went wrong!!!, check your information")

                        return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", user=session["user"], user_car=user_car, L=L,user_id=user_id, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, flash=flash, product_to_show=product_to_show, color_to_show=color_to_show, user_fast_check=user_fast_check, del_mode_row=del_mode_row)
            else:
                subtotal=0
                for car in user_car:
                    subtotal += float(car.price * car.quantity)

                shipping = float(subtotal * 5/100)
                taxes = float(subtotal * 15/100)
                discount = float(subtotal * 10/100)
                grand_total = subtotal + shipping + taxes - discount
                info_row = UserInformation.query.filter_by(user_id=session["id"]).first()
                current_user_info = UserInformation.query.filter_by(user_id=session["id"]).all()
                current_user_cash = 0
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                if len(current_user_info) == 1:
                    current_user_cash = UserInformation.query.filter_by(user_id=session["id"]).first().cash
                return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", user=session["user"], user_car=user_car, L=L, rem=rem, current_user_cash=current_user_cash, grand_total=grand_total, user_email=user_email, product_to_show=product_to_show, color_to_show=color_to_show, user_fast_check=user_fast_check, del_mode_row=del_mode_row)
    return render_template("fast_checkout.html", title="checkout", css="fast_checkout.css", product_to_show=product_to_show, color_to_show=color_to_show, del_mode_row=del_mode_row)


# user profile page:
@app.route("/user_profile", methods=["GET", "POST"])
def user_profile():
    user_email = User.query.filter_by(id=session["id"]).first().email
    user_car = UserProducts.query.filter_by(user_id=session['id']).all()
    info_row = UserInformation.query.filter_by(user_id=session["id"]).first()
    form=registrationForm()
    current_user = User.query.filter_by(id=session["id"]).first()
    old_password = current_user.password
    L = len(user_car)
    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("profile.html", title="Your account", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, del_mode_row=del_mode_row)
                else:

                    return render_template("profile.html", title="Your account", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, del_mode_row=del_mode_row)
    else:
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("profile.html", title="Your account", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, del_mode_row=del_mode_row)
    return render_template("profile.html", title="Your account", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, del_mode_row=del_mode_row)

# order history page:
@app.route("/order_history", methods=["GET", "POST"])
def order_history():
    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                transactions = Transactions.query.filter_by(user_id=session["id"]).all()

                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:
                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("order_history.html", title="Order History", css="order_history.css", user=session["user"], user_car=user_car, L=L, transactions=transactions, del_mode_row=del_mode_row)
                else:
                    return render_template("order_history.html", title="Order History", css="order_history.css", user=session["user"], user_car=user_car, L=L, transactions=transactions, del_mode_row=del_mode_row)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                transactions = Transactions.query.filter_by(user_id=session["id"]).all()

                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("order_history.html", title="Order History", css="order_history.css", user=session["user"], user_car=user_car, L=L, transactions=transactions, del_mode_row=del_mode_row)
    return render_template("order_history.html", title="Order History", css="order_history.css", del_mode_row=del_mode_row)


@app.route("/clear_transactions")
def clear_transactions():
    transactions = Transactions.query.filter_by(user_id=session["id"]).all()
    for tr in range(len(transactions)):
        db.session.delete(transactions[tr])
        db.session.commit()
    return redirect("/order_history")

# upadate and change yor username, email and password:
@app.route("/account_update", methods=["GET", "POST"])
def account_update():
    user_email = User.query.filter_by(id=session["id"]).first().email
    user_car = UserProducts.query.filter_by(user_id=session['id']).all()
    info_row = UserInformation.query.filter_by(user_id=session["id"]).first()
    form=registrationForm()
    current_user = User.query.filter_by(id=session["id"]).first()
    old_password = current_user.password
    L = len(user_car)
    del_mode_row = 0
    if request.method == "POST":

        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:
                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("account_update.html", title="account update", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, old_password=old_password, del_mode_row=del_mode_row)
                else:
                    if form.validate_on_submit():
                        hashed_password = bcrypt.generate_password_hash(form.password.data)
                        current_user.username = request.form.get('username')
                        current_user.email = request.form.get('email')
                        current_user.password = hashed_password
                        if bcrypt.check_password_hash(old_password, request.form.get('old_password')):
                            db.session.commit()
                            flash("your data is changed successfully!")
                        else:
                            flash("wrong password !")
                        session["user"] = form.username.data
                    return render_template("account_update.html", title="account update", css="profile.css", user=session["user"], user_email=user_email, L=L, user_car=user_car, info_row=info_row, form=form, old_password=old_password, flash=flash, del_mode_row=del_mode_row)
    if g.user:
        if g.id:
            user_car = UserProducts.query.filter_by(user_id=session['id']).all()
            L = len(user_car)
            del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
            return render_template("account_update.html", title="account update", css="profile.css", user=session["user"], user_email=user_email, user_car=user_car, L=L, form=form, del_mode_row=del_mode_row)
    return render_template("account_update.html", title="account update", css="profile.css", user_car=user_car, L=L, form=form, del_mode_row=del_mode_row)

# update and change the user's personal informations:
@app.route("/customer_information", methods=["GET", "POST"])
def customer_information():
    info_row = UserInformation.query.filter_by(user_id=session["id"]).first()
    username = User.query.filter_by(id=session["id"]).first().username
    email = User.query.filter_by(id=session["id"]).first().email
    if info_row:
        current_user_cash = info_row.cash
    user_car = UserProducts.query.filter_by(user_id=session['id']).all()
    L = len(user_car)
    del_mode_row = 0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:
                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("customer_information.html", title="customer information", css="customer_information.css", user=session["user"], user_car=user_car, L=L, info_row=info_row, del_mode_row=del_mode_row)
                else:
                    if info_row:
                        try:
                            db.session.delete(info_row)
                            db.session.commit()
                        except:
                            flash("something went wrong!")
                        if info_row.remember == 1:
                            first_name = request.form.get('fname')
                            last_name = request.form.get('lname')
                            countryy = request.form.get('country')
                            cityy = request.form.get('city')
                            addresss = request.form.get('address')
                            apartmentt_no = request.form.get('apartment_no')
                            phonee = request.form.get('phone')
                            current_user_cash += float(request.form.get('cash'))
                            new_infoo = UserInformation(username=username, email=email, first_name=first_name, last_name=last_name, country=countryy, city=cityy, address=addresss, apartment_no=apartmentt_no, phone=phonee, cash=current_user_cash, remember=1, user_id=session["id"])
                            try:
                                db.session.add(new_infoo)
                                db.session.commit()
                                flash("Your information is updated successfully!")
                            except:
                                flash("Something went wrong!")
                        else:
                            first_name = request.form.get('fname')
                            last_name = request.form.get('lname')
                            countryy = request.form.get('country')
                            cityy = request.form.get('city')
                            addresss = request.form.get('address')
                            apartmentt_no = request.form.get('apartment_no')
                            phonee = request.form.get('phone')
                            current_user_cash += float(request.form.get('cash'))
                            new_infooo = UserInformation(username=username, email=email, first_name=first_name, last_name=last_name, country=countryy, city=cityy, address=addresss, apartment_no=apartmentt_no, phone=phonee, cash=current_user_cash, remember=0, user_id=session["id"])
                            try:
                                db.session.add(new_infooo)
                                db.session.commit()
                                flash("Your information is updated successfully!")
                            except:
                                flash("Something went wrong!")
                        return render_template("customer_information.html", title="customer information", css="customer_information.css", user=session["user"], user_car=user_car, L=L, info_row=info_row, flash=flash, del_mode_row=del_mode_row)
                    else:
                        fname = request.form.get('fname')
                        lname = request.form.get('lname')
                        country = request.form.get('country')
                        city = request.form.get('city')
                        address = request.form.get('address')
                        apartment_no = request.form.get('apartment_no')
                        phone = request.form.get('phone')
                        cash = request.form.get('cash')
                        new_info = UserInformation(username=username, email=email, first_name=fname, last_name=lname, country=country, city=city, address=address, apartment_no=apartment_no, phone=phone, cash=cash, remember=0, user_id=session["id"])
                        try:
                            db.session.add(new_info)
                            db.session.commit()
                            flash("Your Information is Added Successfully !")
                        except:
                            flash("something went wrong, check your inputs validations !")
                        return render_template("customer_information.html", title="customer information", css="customer_information.css", user=session["user"], user_car=user_car, L=L, info_row=info_row, flash=flash, del_mode_row=del_mode_row)


    if g.user:
        if g.id:
            del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
            return render_template("customer_information.html", title="customer information", css="customer_information.css", user=session["user"], user_car=user_car, L=L, info_row=info_row, del_mode_row=del_mode_row)
    return render_template("customer_information.html", title="customer information", css="customer_information.css", info_row=info_row, del_mode_row=del_mode_row)




@app.route("/women", methods=["GET","POST"])
def women():
    products = Products.query.order_by(Products.id.desc()).all()
    # women_products = 0
    WL = 0
    for i in products:
        if "women" in i.section:
            WL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women.html", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, WL=WL)
                else:

                    return render_template("women.html", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, WL=WL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women.html", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, WL=WL)
    return render_template("women.html", css="women.css", products=products, del_mode_row=del_mode_row, WL=WL)


@app.route("/women-dresses", methods=["GET","POST"])
def dresses():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0

    women_dresses_products = len(Products.query.filter_by(section="women-dresses").all())


    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_dresses.html", css="women.css", title="Women Dresses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_dresses_products=women_dresses_products)
                else:
                    return render_template("women_dresses.html", css="women.css", title="Women Dresses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_dresses_products=women_dresses_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_dresses.html", css="women.css", title="Women Dresses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_dresses_products=women_dresses_products)
    return render_template("women_dresses.html", css="women.css", title="Women Dresses", products=products, del_mode_row=del_mode_row, women_dresses_products=women_dresses_products)
#ok

@app.route("/women-tops", methods=["GET","POST"])
def tops():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_tops_products = len(Products.query.filter_by(section="women-tops").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_tops.html", css="women.css", title="Women Tops", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_tops_products=women_tops_products)
                else:
                    return render_template("women_tops.html", css="women.css", title="Women Tops", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_tops_products=women_tops_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_tops.html", css="women.css", title="Women Tops", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_tops_products=women_tops_products)
    return render_template("women_tops.html", css="women.css", title="Women Tops", del_mode_row=del_mode_row, products=products, women_tops_products=women_tops_products)
#ok


@app.route("/women-Jackets&Coats", methods=["GET","POST"])
def jackets_coats():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_Jackets_products = len(Products.query.filter_by(section="women-jacket&coats").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_jackets_coats.html", css="women.css", title="Women Jackets & Coats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Jackets_products=women_Jackets_products)
                else:
                    return render_template("women_jackets_coats.html", css="women.css", title="Women Jackets & Coats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Jackets_products=women_Jackets_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_jackets_coats.html", css="women.css", title="Women Jackets & Coats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Jackets_products=women_Jackets_products)
    return render_template("women_jackets_coats.html", css="women.css", title="Women Jackets & Coats", del_mode_row=del_mode_row, products=products, women_Jackets_products=women_Jackets_products)
#ok


@app.route("/women-Blazers", methods=["GET","POST"])
def Blazers():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_blazers_products = len(Products.query.filter_by(section="women-blazers").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_Blazers.html", css="women.css", title="Women Blazers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_blazers_products=women_blazers_products)
                else:
                    return render_template("women_Blazers.html", css="women.css", title="Women Blazers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_blazers_products=women_blazers_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_Blazers.html", css="women.css", title="Women Blazers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_blazers_products=women_blazers_products)
    return render_template("women_Blazers.html", css="women.css", title="Women Blazers", del_mode_row=del_mode_row, products=products, women_blazers_products=women_blazers_products)
#ok


@app.route("/women-Pants_Jeans", methods=["GET","POST"])
def Pants_Jeans():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_Pants_products = len(Products.query.filter_by(section="women-pants&jeans").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_pants&jeans.html", css="women.css", title="Women Pants & Jeans", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Pants_products=women_Pants_products)
                else:
                    return render_template("women_pants&jeans.html", css="women.css", title="Women Pants & Jeans", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Pants_products=women_Pants_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_pants&jeans.html", css="women.css", title="Women Pants & Jeans", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Pants_products=women_Pants_products)
    return render_template("women_pants&jeans.html", css="women.css", title="Women Pants & Jeans", del_mode_row=del_mode_row, products=products, women_Pants_products=women_Pants_products)
#ok



@app.route("/women-Shirts_Blouses", methods=["GET","POST"])
def Shirts_Blouses():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_shirts_products = len(Products.query.filter_by(section="women-shirts&blouses").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_Shirts&Blouses.html", css="women.css", title="Women Shirts & Blouses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_shirts_products=women_shirts_products)
                else:
                    return render_template("women_Shirts&Blouses.html", css="women.css", title="Women Shirts & Blouses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_shirts_products=women_shirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_Shirts&Blouses.html", css="women.css", title="Women Shirts & Blouses", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_shirts_products=women_shirts_products)
    return render_template("women_Shirts&Blouses.html", css="women.css", title="Women Shirts & Blouses", del_mode_row=del_mode_row, products=products, women_shirts_products=women_shirts_products)
#ok


@app.route("/women-Sweetshirts_Hoodies", methods=["GET","POST"])
def Sweetshirts_Hoodies():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_sweetshirts_products = len(Products.query.filter_by(section="women-sweetshirts&hoodies").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_Sweetshirts.html", css="women.css", title="Women Sweetshirts & Hoodies", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sweetshirts_products=women_sweetshirts_products)
                else:
                    return render_template("women_Sweetshirts.html", css="women.css", title="Women Sweetshirts & Hoodies", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sweetshirts_products=women_sweetshirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_Sweetshirts.html", css="women.css", title="Women Sweetshirts & Hoodies", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sweetshirts_products=women_sweetshirts_products)
    return render_template("women_Sweetshirts.html", css="women.css", title="Women Sweetshirts & Hoodies", del_mode_row=del_mode_row, products=products, women_sweetshirts_products=women_sweetshirts_products)
#ok


@app.route("/women-Skirts", methods=["GET","POST"])
def Skirts():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_skirts_products = len(Products.query.filter_by(section="women-skirts").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_skirts.html", css="women.css", title="Women Skirts", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skirts_products=women_skirts_products)
                else:
                    return render_template("women_skirts.html", css="women.css", title="Women Skirts", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skirts_products=women_skirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_skirts.html", css="women.css", title="Women Skirts", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skirts_products=women_skirts_products)
    return render_template("women_skirts.html", css="women.css", title="Women Skirts", del_mode_row=del_mode_row, products=products, women_skirts_products=women_skirts_products)
#ok


@app.route("/women-SportWear", methods=["GET","POST"])
def sportwear():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_sportwear_products = len(Products.query.filter_by(section="women-sportwear").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_sportwear.html", css="women.css", title="Women SportWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sportwear_products=women_sportwear_products)
                else:
                    return render_template("women_sportwear.html", css="women.css", title="Women SportWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sportwear_products=women_sportwear_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_sportwear.html", css="women.css", title="Women SportWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sportwear_products=women_sportwear_products)
    return render_template("women_sportwear.html", css="women.css", title="Women SportWear", del_mode_row=del_mode_row, products=products, women_sportwear_products=women_sportwear_products)
#ok


@app.route("/Women-SleepWear", methods=["GET","POST"])
def SleepWear():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_sleepwear_products = len(Products.query.filter_by(section="women-sleepwear").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_sleepwear.html", css="women.css", title="Women SleepWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sleepwear_products=women_sleepwear_products)
                else:
                    return render_template("women_sleepwear.html", css="women.css", title="Women SleepWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sleepwear_products=women_sleepwear_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_sleepwear.html", css="women.css", title="Women SleepWear", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sleepwear_products=women_sleepwear_products)
    return render_template("women_sleepwear.html", css="women.css", title="Women SleepWear", del_mode_row=del_mode_row, products=products, women_sleepwear_products=women_sleepwear_products)
#ok
#==============================================================================================================================
#women footwears:
#flats:
@app.route("/women_flats", methods=["GET", "POST"])
def women_flats():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_flats_products = len(Products.query.filter_by(section="women-flats").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_flats.html", css="women.css", title="Women Flats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_flats_products=women_flats_products)
                else:
                    return render_template("women_flats.html", css="women.css", title="Women Flats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_flats_products=women_flats_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_flats.html", css="women.css", title="Women Flats", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_flats_products=women_flats_products)
    return render_template("women_flats.html", title="Women Flats", css="women.css", del_mode_row=del_mode_row, products=products, women_flats_products=women_flats_products)
#ok


#women sneakers:
@app.route("/women_sneakers", methods=["GET", "POST"])
def women_sneakers():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_sneakers_products = len(Products.query.filter_by(section="women-sneakers").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_sneakers.html", css="women.css", title="Women Sneakers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sneakers_products=women_sneakers_products)
                else:
                    return render_template("women_sneakers.html", css="women.css", title="Women Sneakers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sneakers_products=women_sneakers_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_sneakers.html", css="women.css", title="Women Sneakers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sneakers_products=women_sneakers_products)
    return render_template("women_sneakers.html", title="Women Sneakers", css="women.css", del_mode_row=del_mode_row, products=products, women_sneakers_products=women_sneakers_products)
#ok


# women heals:
@app.route("/women_heals", methods=["GET", "POST"])
def women_heals():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_heals_products = len(Products.query.filter_by(section="women-heals").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_heals.html", css="women.css", title="Women Heals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_heals_products=women_heals_products)
                else:
                    return render_template("women_heals.html", css="women.css", title="Women Heals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_heals_products=women_heals_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_heals.html", css="women.css", title="Women Heals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_heals_products=women_heals_products)
    return render_template("women_heals.html", title="Women Heals", css="women.css", del_mode_row=del_mode_row, products=products, women_heals_products=women_heals_products)
#ok



# women boots:
@app.route("/women_boots", methods=["GET", "POST"])
def women_boots():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_boots_products = len(Products.query.filter_by(section="women-boots").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_boots.html", css="women.css", title="Women Boots", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_boots_products=women_boots_products)
                else:
                    return render_template("women_boots.html", css="women.css", title="Women Boots", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_boots_products=women_boots_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_boots.html", css="women.css", title="Women Boots", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_boots_products=women_boots_products)
    return render_template("women_boots.html", title="Women Boots", css="women.css", del_mode_row=del_mode_row, products=products, women_boots_products=women_boots_products)
#ok


# Women Sandals & Mules:
@app.route("/women_sandals_mules", methods=["GET", "POST"])
def women_sandals_mules():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_sandals_products = len(Products.query.filter_by(section="women-sandals&mules").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_sandals&mules.html", css="women.css", title="Women Sandals & Mules", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sandals_products=women_sandals_products)
                else:
                    return render_template("women_sandals&mules.html", css="women.css", title="Women Sandals & Mules", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sandals_products=women_sandals_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_sandals&mules.html", css="women.css", title="Women Sandals & Mules", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_sandals_products=women_sandals_products)
    return render_template("women_sandals&mules.html", title="Women Sandals & Mules", css="women.css", del_mode_row=del_mode_row, products=products, women_sandals_products=women_sandals_products)
#ok




# Women Slippers:
@app.route("/women_slippers", methods=["GET", "POST"])
def women_slippers():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_slippers_products = len(Products.query.filter_by(section="women-slippers").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_slippers.html", css="women.css", title="Women Slippers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_slippers_products=women_slippers_products)
                else:
                    return render_template("women_slippers.html", css="women.css", title="Women Slippers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_slippers_products=women_slippers_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_slippers.html", css="women.css", title="Women Slippers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_slippers_products=women_slippers_products)
    return render_template("women_slippers.html", title="Women Slippers", css="women.css", del_mode_row=del_mode_row, products=products, women_slippers_products=women_slippers_products)
#ok


#==============================================================================================================================
#women bags:
#Shoulder Bags:
@app.route("/women_ShoulderBags", methods=["GET", "POST"])
def women_ShoulderBags():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_ShoulderBags_products = len(Products.query.filter_by(section="women-shoulder_bags").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_shoulderbags.html", title="Women Shoulder Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_ShoulderBags_products=women_ShoulderBags_products)
                else:
                    return render_template("women_shoulderbags.html", title="Women Shoulder Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_ShoulderBags_products=women_ShoulderBags_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_shoulderbags.html", title="Women Shoulder Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_ShoulderBags_products=women_ShoulderBags_products)
    return render_template("women_shoulderbags.html", title="Women Shoulder Bags", css="women.css", del_mode_row=del_mode_row, products=products, women_ShoulderBags_products=women_ShoulderBags_products)


# Women Clutch & Mini Bags:
@app.route("/women_Clutch_MiniBags", methods=["GET", "POST"])
def women_Clutch_MiniBags():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_Clutch_MiniBags_products = len(Products.query.filter_by(section="women-clutch&mini_bags").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_clutch&mini_bags.html", title="Women Clutch & Mini Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Clutch_MiniBags_products=women_Clutch_MiniBags_products)
                else:
                    return render_template("women_clutch&mini_bags.html", title="Women Clutch & Mini Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Clutch_MiniBags_products=women_Clutch_MiniBags_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_clutch&mini_bags.html", title="Women Clutch & Mini Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_Clutch_MiniBags_products=women_Clutch_MiniBags_products)
    return render_template("women_clutch&mini_bags.html", title="Women Clutch & Mini Bags", css="women.css", del_mode_row=del_mode_row, products=products, women_Clutch_MiniBags_products=women_Clutch_MiniBags_products)



# Women Tute Bags:
@app.route("/women_TuteBags", methods=["GET", "POST"])
def women_TuteBags():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_TuteBags_products = len(Products.query.filter_by(section="women-tute_bags").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_tutebags.html", title="Women Tute Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_TuteBags_products=women_TuteBags_products)
                else:
                    return render_template("women_tutebags.html", title="Women Tute Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_TuteBags_products=women_TuteBags_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_tutebags.html", title="Women Tute Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_TuteBags_products=women_TuteBags_products)
    return render_template("women_tutebags.html", title="Women Tute Bags", css="women.css", del_mode_row=del_mode_row, products=products, women_TuteBags_products=women_TuteBags_products)


# Women Backpacks:
@app.route("/women_BackPacks", methods=["GET", "POST"])
def women_BackPacks():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_BackPacks_products = len(Products.query.filter_by(section="women-back_packs").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_backpacks.html", title="Women Backbacks", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BackPacks_products=women_BackPacks_products)
                else:
                    return render_template("women_backpacks.html", title="Women Backbacks", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BackPacks_products=women_BackPacks_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_backpacks.html", title="Women Backbacks", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BackPacks_products=women_BackPacks_products)
    return render_template("women_backpacks.html", title="Women Backbacks", css="women.css", del_mode_row=del_mode_row, products=products, women_BackPacks_products=women_BackPacks_products)



# Women Laptop Bags:
@app.route("/women_LaptopBags", methods=["GET", "POST"])
def women_LaptopBags():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_LaptopBags_products = len(Products.query.filter_by(section="women-laptop_bags").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_laptopbags.html", title="Women Laptop Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_LaptopBags_products=women_LaptopBags_products)
                else:
                    return render_template("women_laptopbags.html", title="Women Laptop Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_LaptopBags_products=women_LaptopBags_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_laptopbags.html", title="Women Laptop Bags", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_LaptopBags_products=women_LaptopBags_products)
    return render_template("women_laptopbags.html", title="Women Laptop Bags", css="women.css", del_mode_row=del_mode_row, products=products, women_LaptopBags_products=women_LaptopBags_products)


#===================================================================================================================================================================================================================================================================
# Women Jewelry & Accessories:
# Women earrings:
@app.route("/women_earrings", methods=["GET", "POST"])
def women_earrings():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_earrings_products = len(Products.query.filter_by(section="women-earrings").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_earrings.html", title="Women Earrings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_earrings_products=women_earrings_products)
                else:
                    return render_template("women_earrings.html", title="Women Earrings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_earrings_products=women_earrings_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_earrings.html", title="Women Earrings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_earrings_products=women_earrings_products)
    return render_template("women_earrings.html", title="Women Earrings", css="women.css", del_mode_row=del_mode_row, products=products, women_earrings_products=women_earrings_products)
#ok



# Women Necklaces:
@app.route("/women_necklaces", methods=["GET", "POST"])
def women_necklaces():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_necklaces_products = len(Products.query.filter_by(section="women-necklaces").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_necklaces.html", title="Women Necklaces", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_necklaces_products=women_necklaces_products)
                else:
                    return render_template("women_necklaces.html", title="Women Necklaces", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_necklaces_products=women_necklaces_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_necklaces.html", title="Women Necklaces", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_necklaces_products=women_necklaces_products)
    return render_template("women_necklaces.html", title="Women Necklaces", css="women.css", del_mode_row=del_mode_row, products=products, women_necklaces_products=women_necklaces_products)
#ok


# Women Rings:
@app.route("/women_rings", methods=["GET", "POST"])
def women_rings():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_rings_products = len(Products.query.filter_by(section="women-rings").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_rings.html", title="Women Rings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_rings_products=women_rings_products)
                else:
                    return render_template("women_rings.html", title="Women Rings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_rings_products=women_rings_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_rings.html", title="Women Rings", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_rings_products=women_rings_products)
    return render_template("women_rings.html", title="Women Rings", css="women.css", del_mode_row=del_mode_row, products=products, women_rings_products=women_rings_products)
#ok


# Women Hair Accessories:
@app.route("/women_HairAccessories", methods=["GET", "POST"])
def women_HairAccessories():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_HairAccessories_products = len(Products.query.filter_by(section="women-hair_accessories").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_HairAccessories.html", title="Women Hair Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_HairAccessories_products=women_HairAccessories_products)
                else:
                    return render_template("women_HairAccessories.html", title="Women Hair Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_HairAccessories_products=women_HairAccessories_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_HairAccessories.html", title="Women Hair Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_HairAccessories_products=women_HairAccessories_products)
    return render_template("women_HairAccessories.html", title="Women Hair Accessories", css="women.css", del_mode_row=del_mode_row, products=products, women_HairAccessories_products=women_HairAccessories_products)
#ok



# Women Phone Accessories:
@app.route("/women_PhoneAccessories", methods=["GET", "POST"])
def women_PhoneAccessories():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_PhoneAccessories_products = len(Products.query.filter_by(section="women-phone_accessories").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_PhoneAccessories.html", title="Women Phone Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_PhoneAccessories_products=women_PhoneAccessories_products)
                else:
                    return render_template("women_PhoneAccessories.html", title="Women Phone Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_PhoneAccessories_products=women_PhoneAccessories_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_PhoneAccessories.html", title="Women Phone Accessories", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_PhoneAccessories_products=women_PhoneAccessories_products)
    return render_template("women_PhoneAccessories.html", title="Women Phone Accessories", css="women.css", del_mode_row=del_mode_row, products=products, women_PhoneAccessories_products=women_PhoneAccessories_products)
#ok

#======================================================================================================================================================================================================
# Women Beauty:
# Women Bath & Body:
@app.route("/women_Bath&Body", methods=["GET", "POST"])
def women_BathBody():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_BathBody_products = len(Products.query.filter_by(section="women-bath&body").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_bath&body.html", title="Women Bath & Body", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BathBody_products=women_BathBody_products)
                else:
                    return render_template("women_bath&body.html", title="Women Bath & Body", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BathBody_products=women_BathBody_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_bath&body.html", title="Women Bath & Body", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_BathBody_products=women_BathBody_products)
    return render_template("women_bath&body.html", title="Women Bath & Body", css="women.css", del_mode_row=del_mode_row, products=products, women_BathBody_products=women_BathBody_products)
#ok


# Women Skincare:
@app.route("/women_skincare", methods=["GET", "POST"])
def women_skincare():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_skincare_products = len(Products.query.filter_by(section="women-skincare").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_skincare.html", title="Women Skincare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skincare_products=women_skincare_products)
                else:
                    return render_template("women_skincare.html", title="Women Skincare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skincare_products=women_skincare_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_skincare.html", title="Women Skincare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_skincare_products=women_skincare_products)
    return render_template("women_skincare.html", title="Women Skincare", css="women.css", del_mode_row=del_mode_row, products=products, women_skincare_products=women_skincare_products)
#ok


# Women Haircare:
@app.route("/women_haircare", methods=["GET", "POST"])
def women_haircare():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    women_haircare_products = len(Products.query.filter_by(section="women-haircare").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("women_haircare.html", title="Women Haircare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_haircare_products=women_haircare_products)
                else:
                    return render_template("women_haircare.html", title="Women Haircare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_haircare_products=women_haircare_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("women_haircare.html", title="Women Haircare", css="women.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, women_haircare_products=women_haircare_products)
    return render_template("women_haircare.html", title="Women Haircare", css="women.css", del_mode_row=del_mode_row, products=products, women_haircare_products=women_haircare_products)


#====================================================================================================================================
#====================================================================================================================================
#====================================================================================================================================
#                           ===> MEN <===:
@app.route("/men", methods=["GET","POST"])
def men():
    products = Products.query.order_by(Products.id.desc()).all()
    # women_products = 0
    ML = 0
    for i in products:
        if "Men" in i.section:
            ML += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men.html", css="men.css", title="Men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, ML=ML)
                else:

                    return render_template("men.html", css="men.css", title="Men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, ML=ML)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men.html", css="men.css", title="Men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, ML=ML)
    return render_template("men.html", css="men.css", title="Men", products=products, del_mode_row=del_mode_row, ML=ML)
#ok



# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                       ===> MEN CLOTHING <===:
# Men Sweetshirts & Hoodies:
@app.route("/men_sweetshirts&hoodies", methods=["GET", "POST"])
def men_Sweetshirts_Hoodies():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_Sweetshirts_Hoodies_products = len(Products.query.filter_by(section="Men-sweetshirts&hoodies").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_sweetshirts&hoodies.html", title="Men Sweetshirts & Hoodies", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Sweetshirts_Hoodies_products=men_Sweetshirts_Hoodies_products)
                else:
                    return render_template("men_sweetshirts&hoodies.html", title="Men Sweetshirts & Hoodies", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Sweetshirts_Hoodies_products=men_Sweetshirts_Hoodies_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_sweetshirts&hoodies.html", title="Men Sweetshirts & Hoodies", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Sweetshirts_Hoodies_products=men_Sweetshirts_Hoodies_products)
    return render_template("men_sweetshirts&hoodies.html", title="Men Sweetshirts & Hoodies", css="men.css", del_mode_row=del_mode_row, products=products, men_Sweetshirts_Hoodies_products=men_Sweetshirts_Hoodies_products)
#ok



# Men Pullover & Sweeters:
@app.route("/men_pullover&sweeters", methods=["GET", "POST"])
def men_pullover_sweeters():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_pullover_sweeters_products = len(Products.query.filter_by(section="Men-pullover&sweeters").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_pullover&sweeters.html", title="Men Pullover & Sweeters", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pullover_sweeters_products=men_pullover_sweeters_products)
                else:
                    return render_template("men_pullover&sweeters.html", title="Men Pullover & Sweeters", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pullover_sweeters_products=men_pullover_sweeters_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_pullover&sweeters.html", title="Men Pullover & Sweeters", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pullover_sweeters_products=men_pullover_sweeters_products)
    return render_template("men_pullover&sweeters.html", title="Men Pullover & Sweeters", css="men.css", del_mode_row=del_mode_row, products=products, men_pullover_sweeters_products=men_pullover_sweeters_products)
#ok



# Men Jackets:
@app.route("/men_jackets", methods=["GET", "POST"])
def men_jackets():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_jackets_products = len(Products.query.filter_by(section="Men-jackets").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_jackets.html", title="Men Jackets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_jackets_products=men_jackets_products)
                else:
                    return render_template("men_jackets.html", title="Men Jackets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_jackets_products=men_jackets_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_jackets.html", title="Men Jackets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_jackets_products=men_jackets_products)
    return render_template("men_jackets.html", title="Men Jackets", css="men.css", del_mode_row=del_mode_row, products=products, men_jackets_products=men_jackets_products)
#ok



# Men Shirts:
@app.route("/men_shirts", methods=["GET", "POST"])
def men_shirts():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_shirts_products = len(Products.query.filter_by(section="Men-shirts").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_shirts.html", title="Men Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shirts_products=men_shirts_products)
                else:
                    return render_template("men_shirts.html", title="Men Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shirts_products=men_shirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_shirts.html", title="Men Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shirts_products=men_shirts_products)
    return render_template("men_shirts.html", title="Men Shirts", css="men.css", del_mode_row=del_mode_row, products=products, men_shirts_products=men_shirts_products)
#ok




# Men T-Shirts:
@app.route("/men_tshirts", methods=["GET", "POST"])
def men_Tshirts():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_Tshirts_products = len(Products.query.filter_by(section="Men-tshirts").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_Tshirts.html", title="Men T-Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Tshirts_products=men_Tshirts_products)
                else:
                    return render_template("men_Tshirts.html", title="Men T-Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Tshirts_products=men_Tshirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_Tshirts.html", title="Men T-Shirts", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_Tshirts_products=men_Tshirts_products)
    return render_template("men_Tshirts.html", title="Men T-Shirts", css="men.css", del_mode_row=del_mode_row, products=products, men_Tshirts_products=men_Tshirts_products)
#ok



# Men Pants & SweetPants:
@app.route("/men_pants&sweetpants", methods=["GET", "POST"])
def men_pants_sweetpants():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_pants_sweetpants_products = len(Products.query.filter_by(section="Men-pants&sweetpants").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_Pants&Sweetpants.html", title="Men Pants & SweetPants", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pants_sweetpants_products=men_pants_sweetpants_products)
                else:
                    return render_template("men_Pants&Sweetpants.html", title="Men Pants & SweetPants", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pants_sweetpants_products=men_pants_sweetpants_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_Pants&Sweetpants.html", title="Men Pants & SweetPants", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_pants_sweetpants_products=men_pants_sweetpants_products)
    return render_template("men_Pants&Sweetpants.html", title="Men Pants & SweetPants", css="men.css", del_mode_row=del_mode_row, products=products, men_pants_sweetpants_products=men_pants_sweetpants_products)
#ok





# Men SportsWear:
@app.route("/men_sportswear", methods=["GET", "POST"])
def men_sportswear():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_sportswear_products = len(Products.query.filter_by(section="Men-sportwear").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_sportswear.html", title="Men SportsWear", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sportswear_products=men_sportswear_products)
                else:
                    return render_template("men_sportswear.html", title="Men SportsWear", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sportswear_products=men_sportswear_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_sportswear.html", title="Men SportsWear", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sportswear_products=men_sportswear_products)
    return render_template("men_sportswear.html", title="Men SportsWear", css="men.css", del_mode_row=del_mode_row, products=products, men_sportswear_products=men_sportswear_products)
#ok






# Men Full Suits:
@app.route("/men_FullSuits", methods=["GET", "POST"])
def men_Full_Suits():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_FullSuits_products = len(Products.query.filter_by(section="Men-fullsuits").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_fullsuits.html", title="Men Full Suits", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_FullSuits_products=men_FullSuits_products)
                else:
                    return render_template("men_fullsuits.html", title="Men Full Suits", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_FullSuits_products=men_FullSuits_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_fullsuits.html", title="Men Full Suits", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_FullSuits_products=men_FullSuits_products)
    return render_template("men_fullsuits.html", title="Men Full Suits", css="men.css", del_mode_row=del_mode_row, products=products, men_FullSuits_products=men_FullSuits_products)
#ok


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                       ===> MEN FOOTWEAR <=== :
# Men Shoes:
@app.route("/men_shoes", methods=["GET", "POST"])
def men_shoes():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_shoes_products = len(Products.query.filter_by(section="Men-shoes").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_shoes.html", title="Men Shoes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shoes_products=men_shoes_products)
                else:
                    return render_template("men_shoes.html", title="Men Shoes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shoes_products=men_shoes_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_shoes.html", title="Men Shoes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_shoes_products=men_shoes_products)
    return render_template("men_shoes.html", title="Men Shoes", css="men.css", del_mode_row=del_mode_row, products=products, men_shoes_products=men_shoes_products)
#ok



# Men Sneakers:
@app.route("/men_sneakers", methods=["GET", "POST"])
def men_sneakers():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_sneakers_products = len(Products.query.filter_by(section="Men-sneakers").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_sneakers.html", title="Men Sneakers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sneakers_products=men_sneakers_products)
                else:
                    return render_template("men_sneakers.html", title="Men Sneakers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sneakers_products=men_sneakers_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_sneakers.html", title="Men Sneakers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_sneakers_products=men_sneakers_products)
    return render_template("men_sneakers.html", title="Men Sneakers", css="men.css", del_mode_row=del_mode_row, products=products, men_sneakers_products=men_sneakers_products)
#ok




#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                           ===> MEN ACCESSORIES <===:
# Men Bracelets:
@app.route("/men_bracelets", methods=["GET", "POST"])
def men_bracelets():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_bracelets_products = len(Products.query.filter_by(section="Men-bracelets").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_bracelets.html", title="Men Bracelets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_bracelets_products=men_bracelets_products)
                else:
                    return render_template("men_bracelets.html", title="Men Bracelets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_bracelets_products=men_bracelets_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_bracelets.html", title="Men Bracelets", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_bracelets_products=men_bracelets_products)
    return render_template("men_bracelets.html", title="Men Bracelets", css="men.css", del_mode_row=del_mode_row, products=products, men_bracelets_products=men_bracelets_products)
#ok




# Men Socks:
@app.route("/men_socks", methods=["GET", "POST"])
def men_socks():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_socks_products = len(Products.query.filter_by(section="Men-socks").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_socks.html", title="Men Socks", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_socks_products=men_socks_products)
                else:
                    return render_template("men_socks.html", title="Men Socks", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_socks_products=men_socks_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_socks.html", title="Men Socks", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_socks_products=men_socks_products)
    return render_template("men_socks.html", title="Men Socks", css="men.css", del_mode_row=del_mode_row, products=products, men_socks_products=men_socks_products)
#ok



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                                       ===> MEN BEAUTY <===:
# Men Perfumes:
@app.route("/men_perfumes", methods=["GET", "POST"])
def men_perfumes():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    men_perfumes_products = len(Products.query.filter_by(section="Men-perfumes").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("men_perfumes.html", title="Men Perfumes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_perfumes_products=men_perfumes_products)
                else:
                    return render_template("men_perfumes.html", title="Men Perfumes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_perfumes_products=men_perfumes_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("men_perfumes.html", title="Men Perfumes", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, men_perfumes_products=men_perfumes_products)
    return render_template("men_perfumes.html", title="Men Perfumes", css="men.css", del_mode_row=del_mode_row, products=products, men_perfumes_products=men_perfumes_products)



#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#                                           ===> KIDS <===:
@app.route("/kids", methods=["GET","POST"])
def kids():
    products = Products.query.order_by(Products.id.desc()).all()
    KL = 0
    for i in products:
        if "kids" in i.section:
            KL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids.html", css="kids.css", title="Kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, KL=KL)
                else:

                    return render_template("kids.html", css="kids.css", title="Kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, KL=KL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids.html", css="kids.css", title="Kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, KL=KL)
    return render_template("kids.html", css="kids.css", title="Kids", products=products, del_mode_row=del_mode_row, KL=KL)
#ok


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                                       ===> BOYS <===:
# KIDS BOYS SWEETSHIRTS & HOODIES:

@app.route("/kids_boys_sweetshirts&hoodies", methods=["GET", "POST"])
def kids_boys_Sweetshirts_Hoodies():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_boys_Sweetshirts_Hoodies_products = len(Products.query.filter_by(section="kids-boys_sweetshirts&hoodies").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_boys_sweetshirts&hoodies.html", title="Boys Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Sweetshirts_Hoodies_products=kids_boys_Sweetshirts_Hoodies_products)
                else:
                    return render_template("kids_boys_sweetshirts&hoodies.html", title="Boys Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Sweetshirts_Hoodies_products=kids_boys_Sweetshirts_Hoodies_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_boys_sweetshirts&hoodies.html", title="Boys Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Sweetshirts_Hoodies_products=kids_boys_Sweetshirts_Hoodies_products)
    return render_template("kids_boys_sweetshirts&hoodies.html", title="Boys Sweetshirts & Hoodies", css="kids.css", del_mode_row=del_mode_row, products=products, kids_boys_Sweetshirts_Hoodies_products=kids_boys_Sweetshirts_Hoodies_products)
#ok




# KIDS BOYS T-SHIRTS & POLOS:

@app.route("/kids_boys_Tshirts&Polos", methods=["GET", "POST"])
def kids_boys_Tshirts_Polos():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_boys_Tshirts_Polos_products = len(Products.query.filter_by(section="kids-boys_tshirts&polos").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_boys_Tshirts&Polos.html", title="Boys T-shirts & Polos", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Tshirts_Polos_products=kids_boys_Tshirts_Polos_products)
                else:
                    return render_template("kids_boys_Tshirts&Polos.html", title="Boys T-shirts & Polos", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Tshirts_Polos_products=kids_boys_Tshirts_Polos_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_boys_Tshirts&Polos.html", title="Boys T-shirts & Polos", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_Tshirts_Polos_products=kids_boys_Tshirts_Polos_products)
    return render_template("kids_boys_Tshirts&Polos.html", title="Boys T-shirts & Polos", css="kids.css", del_mode_row=del_mode_row, products=products, kids_boys_Tshirts_Polos_products=kids_boys_Tshirts_Polos_products)
#ok




# KIDS BOYS PANTS & SWEETPANTS:

@app.route("/kids_boys_Pants&Sweetpants", methods=["GET", "POST"])
def kids_boys_pants_sweetpants():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_boys_pants_sweetpants_products = len(Products.query.filter_by(section="kids-boys_pants&sweetpants").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_boys_Pants&Sweetpants.html", title="Boys Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_pants_sweetpants_products=kids_boys_pants_sweetpants_products)
                else:
                    return render_template("kids_boys_Pants&Sweetpants.html", title="Boys Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_pants_sweetpants_products=kids_boys_pants_sweetpants_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_boys_Pants&Sweetpants.html", title="Boys Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_pants_sweetpants_products=kids_boys_pants_sweetpants_products)
    return render_template("kids_boys_Pants&Sweetpants.html", title="Boys Pants & Sweetpants", css="kids.css", del_mode_row=del_mode_row, products=products, kids_boys_pants_sweetpants_products=kids_boys_pants_sweetpants_products)
#ok




# KIDS BOYS SHORTS:

@app.route("/kids_boys_shorts", methods=["GET", "POST"])
def kids_boys_shorts():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_boys_shorts_products = len(Products.query.filter_by(section="kids-boys_shorts").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_boys_shorts.html", title="Boys Shorts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_shorts_products=kids_boys_shorts_products)
                else:
                    return render_template("kids_boys_shorts.html", title="Boys Shorts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_shorts_products=kids_boys_shorts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_boys_shorts.html", title="Boys Shorts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_shorts_products=kids_boys_shorts_products)
    return render_template("kids_boys_shorts.html", title="Boys Shorts", css="kids.css", del_mode_row=del_mode_row, products=products, kids_boys_shorts_products=kids_boys_shorts_products)
#ok





# KIDS BOYS FOOTWEAR:

@app.route("/kids_boys_footwear", methods=["GET", "POST"])
def kids_boys_footwear():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_boys_footwear_products = len(Products.query.filter_by(section="kids-boys_footwears").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_boys_footwear.html", title="Boys Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_footwear_products=kids_boys_footwear_products)
                else:
                    return render_template("kids_boys_footwear.html", title="Boys Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_footwear_products=kids_boys_footwear_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_boys_footwear.html", title="Boys Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_boys_footwear_products=kids_boys_footwear_products)
    return render_template("kids_boys_footwear.html", title="Boys Footwear", css="kids.css", del_mode_row=del_mode_row, products=products, kids_boys_footwear_products=kids_boys_footwear_products)
#ok



#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------:
#                                    ===> GIRLS <===:
# KIDS GIRLS TOPS:

@app.route("/kids_girls_tops", methods=["GET", "POST"])
def kids_girls_tops():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_tops_products = len(Products.query.filter_by(section="kids-girls_tops").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_tops.html", title="Girls Tops", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_tops_products=kids_girls_tops_products)
                else:
                    return render_template("kids_girls_tops.html", title="Girls Tops", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_tops_products=kids_girls_tops_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_tops.html", title="Girls Tops", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_tops_products=kids_girls_tops_products)
    return render_template("kids_girls_tops.html", title="Girls Tops", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_tops_products=kids_girls_tops_products)
#ok




# KIDS GIRLS SWEETSHIRTS & HOODIES:

@app.route("/kids_girls_Sweetshirts&Hoodies", methods=["GET", "POST"])
def kids_girls_Sweetshirts_Hoodies():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_Sweetshirts_Hoodies_products = len(Products.query.filter_by(section="kids-girls_sweetshirts&hoodies").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_Sweetshirts&Hoodies.html", title="Girls Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Sweetshirts_Hoodies_products=kids_girls_Sweetshirts_Hoodies_products)
                else:
                    return render_template("kids_girls_Sweetshirts&Hoodies.html", title="Girls Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Sweetshirts_Hoodies_products=kids_girls_Sweetshirts_Hoodies_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_Sweetshirts&Hoodies.html", title="Girls Sweetshirts & Hoodies", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Sweetshirts_Hoodies_products=kids_girls_Sweetshirts_Hoodies_products)
    return render_template("kids_girls_Sweetshirts&Hoodies.html", title="Girls Sweetshirts & Hoodies", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_Sweetshirts_Hoodies_products=kids_girls_Sweetshirts_Hoodies_products)
#ok






# KIDS GIRLS DRESSES & JUMPSUITS:

@app.route("/kids_girls_Dresses&JumpSuits", methods=["GET", "POST"])
def kids_girls_Dresses_JumpSuits():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_Dresses_Jumpsuits_products = len(Products.query.filter_by(section="kids-girls_dresses&jumpsuits").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_Dresses&Jumpsuits.html", title="Girls Dresses & Jumpsuits", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Dresses_Jumpsuits_products=kids_girls_Dresses_Jumpsuits_products)
                else:
                    return render_template("kids_girls_Dresses&Jumpsuits.html", title="Girls Dresses & Jumpsuits", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Dresses_Jumpsuits_products=kids_girls_Dresses_Jumpsuits_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_Dresses&Jumpsuits.html", title="Girls Dresses & Jumpsuits", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Dresses_Jumpsuits_products=kids_girls_Dresses_Jumpsuits_products)
    return render_template("kids_girls_Dresses&Jumpsuits.html", title="Girls Dresses & Jumpsuits", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_Dresses_Jumpsuits_products=kids_girls_Dresses_Jumpsuits_products)
#ok




# KIDS GIRLS JACKET & COATS:

@app.route("/kids_girls_Jacket&Coats", methods=["GET", "POST"])
def kids_girls_Jacket_Coats():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_Jacket_Coats_products = len(Products.query.filter_by(section="kids-girls_jacket&coats").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_Jacket&Coats.html", title="Girls Jacket & Coats", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Jacket_Coats_products=kids_girls_Jacket_Coats_products)
                else:
                    return render_template("kids_girls_Jacket&Coats.html", title="Girls Jacket & Coats", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Jacket_Coats_products=kids_girls_Jacket_Coats_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_Jacket&Coats.html", title="Girls Jacket & Coats", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Jacket_Coats_products=kids_girls_Jacket_Coats_products)
    return render_template("kids_girls_Jacket&Coats.html", title="Girls Jacket & Coats", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_Jacket_Coats_products=kids_girls_Jacket_Coats_products)






# KIDS GIRLS PANTS & SWEETPANTS:

@app.route("/kids_girls_Pants&SweetPants", methods=["GET", "POST"])
def kids_girls_Pants_SweetPants():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_Pants_SweetPants_products = len(Products.query.filter_by(section="kids-girls_pants&sweetpants").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_Pants&SweetPants.html", title="Girls Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Pants_SweetPants_products=kids_girls_Pants_SweetPants_products)
                else:
                    return render_template("kids_girls_Pants&SweetPants.html", title="Girls Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Pants_SweetPants_products=kids_girls_Pants_SweetPants_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_Pants&SweetPants.html", title="Girls Pants & Sweetpants", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_Pants_SweetPants_products=kids_girls_Pants_SweetPants_products)
    return render_template("kids_girls_Pants&SweetPants.html", title="Girls Pants & Sweetpants", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_Pants_SweetPants_products=kids_girls_Pants_SweetPants_products)




# KIDS GIRLS SKIRTS:

@app.route("/kids_girls_skirts", methods=["GET", "POST"])
def kids_girls_skirts():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_skirts_products = len(Products.query.filter_by(section="kids-girls_skirts").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_skirts.html", title="Girls Skirts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_skirts_products=kids_girls_skirts_products)
                else:
                    return render_template("kids_girls_skirts.html", title="Girls Skirts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_skirts_products=kids_girls_skirts_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_skirts.html", title="Girls Skirts", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_skirts_products=kids_girls_skirts_products)
    return render_template("kids_girls_skirts.html", title="Girls Skirts", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_skirts_products=kids_girls_skirts_products)





# KIDS GIRLS FOOTWEAR:

@app.route("/kids_girls_footwear", methods=["GET", "POST"])
def kids_girls_footwear():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    kids_girls_footwear_products = len(Products.query.filter_by(section="kids-girls_footwear").all())
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("kids_girls_footwear.html", title="Girls Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_footwear_products=kids_girls_footwear_products)
                else:
                    return render_template("kids_girls_footwear.html", title="Girls Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_footwear_products=kids_girls_footwear_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("kids_girls_footwear.html", title="Girls Footwear", css="kids.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, kids_girls_footwear_products=kids_girls_footwear_products)
    return render_template("kids_girls_footwear.html", title="Girls Footwear", css="kids.css", del_mode_row=del_mode_row, products=products, kids_girls_footwear_products=kids_girls_footwear_products)
#ok




#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#                                           ===> NEW ARRIVALS <===:
@app.route("/new_arrivals", methods=["GET","POST"])
def new_arrivals():
    products = Products.query.order_by(Products.id.desc()).all()
    NL = 0
    for i in products:
        if "newarrival" in i.section:
            NL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("newarrivals.html", css="newarrivals.css", title="New Arrivals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, NL=NL)
                else:

                    return render_template("newarrivals.html", css="newarrivals.css", title="New Arrivals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, NL=NL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("newarrivals.html", css="newarrivals.css", title="New Arrivals", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, NL=NL)
    return render_template("newarrivals.html", css="newarrivals.css", title="New Arrivals", products=products, del_mode_row=del_mode_row, NL=NL)
#ok



# New Arrivals Women:
@app.route("/new_arrivals_women", methods=["GET", "POST"])
def new_arrivals_women():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    new_arrivals_women_products = len(Products.query.filter_by(section="newarrival-women").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("newarrivals_women.html", title="New Arrivals Women", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_women_products=new_arrivals_women_products)
                else:
                    return render_template("newarrivals_women.html", title="New Arrivals Women", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_women_products=new_arrivals_women_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("newarrivals_women.html", title="New Arrivals Women", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_women_products=new_arrivals_women_products)
    return render_template("newarrivals_women.html", title="New Arrivals Women", css="newarrivals.css", del_mode_row=del_mode_row, products=products, new_arrivals_women_products=new_arrivals_women_products)
#ok




# New Arrivals Men:
@app.route("/new_arrivals_men", methods=["GET", "POST"])
def new_arrivals_men():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    new_arrivals_men_products = len(Products.query.filter_by(section="newarrival-men").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("newarrivals_men.html", title="New Arrivals Men", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_men_products=new_arrivals_men_products)
                else:
                    return render_template("newarrivals_men.html", title="New Arrivals Men", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_men_products=new_arrivals_men_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("newarrivals_men.html", title="New Arrivals Men", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_men_products=new_arrivals_men_products)
    return render_template("newarrivals_men.html", title="New Arrivals Men", css="newarrivals.css", del_mode_row=del_mode_row, products=products, new_arrivals_men_products=new_arrivals_men_products)
#ok




# New Arrivals Kids:
@app.route("/new_arrivals_kids", methods=["GET", "POST"])
def new_arrivals_kids():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    new_arrivals_kids_products = len(Products.query.filter_by(section="newarrival-kids").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("newarrivals_kids.html", title="New Arrivals Kids", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_kids_products=new_arrivals_kids_products)
                else:
                    return render_template("newarrivals_kids.html", title="New Arrivals Kids", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_kids_products=new_arrivals_kids_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("newarrivals_kids.html", title="New Arrivals Kids", css="newarrivals.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, new_arrivals_kids_products=new_arrivals_kids_products)
    return render_template("newarrivals_kids.html", title="New Arrivals Kids", css="newarrivals.css", del_mode_row=del_mode_row, products=products, new_arrivals_kids_products=new_arrivals_kids_products)
#ok






#=============================================================================================================================================================================================================================================================================================:
#                                          ===> BEST SELLERS <===:
@app.route("/best_sellers", methods=["GET","POST"])
def best_sellers():
    products = Products.query.order_by(Products.id.desc()).all()
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()
    length_to_show = len(OwnerTransactions.query.filter(OwnerTransactions.purchases > 3).all())
    for j in products:
        if "bestsellers" in j.section:
            length_to_show += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("bestsellers.html", css="bestsellers.css", title="Best sellers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, length_to_show=length_to_show)
                else:

                    return render_template("bestsellers.html", css="bestsellers.css", title="Best sellers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, length_to_show=length_to_show)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("bestsellers.html", css="bestsellers.css", title="Best sellers", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, length_to_show=length_to_show)
    return render_template("bestsellers.html", css="bestsellers.css", title="Best sellers", products=products, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, length_to_show=length_to_show)
#ok




# Best Sellers Women:
@app.route("/best_sellers_women", methods=["GET","POST"])
def best_sellers_women():
    products = Products.query.order_by(Products.id.desc()).all()
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()

    BL = 0
    for i in best_sellers_products:
        if "women" in i.section:
            if i.purchases > 3:
                BL += 1
    for j in products:
        if "bestsellers-women" in j.section:
            BL += 1


    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()

                    return render_template("bestsellers_women.html", css="bestsellers.css", title="Best sellers women", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
                else:
                    return render_template("bestsellers_women.html", css="bestsellers.css", title="Best sellers women", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("bestsellers_women.html", css="bestsellers.css", title="Best sellers women", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    return render_template("bestsellers_women.html", css="bestsellers.css", title="Best sellers women", products=products, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
#ok





# Best Sellers Men:
@app.route("/best_sellers_men", methods=["GET","POST"])
def best_sellers_men():
    products = Products.query.order_by(Products.id.desc()).all()
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()

    BL = 0
    for i in best_sellers_products:
        if "Men" in i.section:
            if i.purchases > 3:
                BL += 1
    for j in products:
        if "bestsellers-men" in j.section:
            BL += 1


    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()

                    return render_template("bestsellers_men.html", css="bestsellers.css", title="Best sellers men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
                else:
                    return render_template("bestsellers_men.html", css="bestsellers.css", title="Best sellers men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("bestsellers_men.html", css="bestsellers.css", title="Best sellers men", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    return render_template("bestsellers_men.html", css="bestsellers.css", title="Best sellers men", products=products, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
#ok





# Best Sellers Kids:
@app.route("/best_sellers_kids", methods=["GET","POST"])
def best_sellers_kids():
    products = Products.query.order_by(Products.id.desc()).all()
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()

    BL = 0
    for i in best_sellers_products:
        if "kids" in i.section:
            if i.purchases > 3:
                BL += 1
    for j in products:
        if "bestsellers-kids" in j.section:
            BL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()

                    return render_template("bestsellers_kids.html", css="bestsellers.css", title="Best sellers kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
                else:
                    return render_template("bestsellers_kids.html", css="bestsellers.css", title="Best sellers kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("bestsellers_kids.html", css="bestsellers.css", title="Best sellers kids", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    return render_template("bestsellers_kids.html", css="bestsellers.css", title="Best sellers kids", products=products, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
#ok







# Best Sellers Jewelry & Beauty:
@app.route("/best_sellers_jewelry", methods=["GET","POST"])
def best_sellers_jewelry():
    products = Products.query.order_by(Products.id.desc()).all()
    best_sellers_products = OwnerTransactions.query.order_by(OwnerTransactions.purchases.desc()).all()

    BL = 0
    for i in best_sellers_products:
        if "women-earrings" in i.section or "women-necklaces" in i.section or "women-rings" in i.section or "women-hair_accessories" in i.section or "women-phone_accessories" in i.section:
            if i.purchases > 3:
                BL += 1

    for j in products:
        if "bestsellers-jewlry&beauty" in j.section:
            BL += 1


    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()

                    return render_template("bestsellers_jewelry.html", css="bestsellers.css", title="Best sellers jewelry & beauty", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
                else:
                    return render_template("bestsellers_jewelry.html", css="bestsellers.css", title="Best sellers jewelry & beauty", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("bestsellers_jewelry.html", css="bestsellers.css", title="Best sellers jewelry & beauty", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
    return render_template("bestsellers_jewelry.html", css="bestsellers.css", title="Best sellers jewelry & beauty", products=products, del_mode_row=del_mode_row, best_sellers_products=best_sellers_products, BL=BL)
#ok






#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#                                           ===> BRANDS <===:
@app.route("/brands", methods=["GET","POST"])
def brands():
    products = Products.query.order_by(Products.id.desc()).all()
    BRL = 0
    for i in products:
        if "brands" in i.section:
            BRL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands.html", css="men.css", title="Brands", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, BRL=BRL)
                else:
                    return render_template("brands.html", css="men.css", title="Brands", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, BRL=BRL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands.html", css="men.css", title="Brands", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, BRL=BRL)
    return render_template("brands.html", css="men.css", title="Brands", products=products, del_mode_row=del_mode_row, BRL=BRL)
#ok





# Brands Calvin:
@app.route("/brands_calvin", methods=["GET", "POST"])
def brands_calvin():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    brands_calvin_products = len(Products.query.filter_by(section="brands-calvin").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands_calvin.html", title="Brands Calvin", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_calvin_products=brands_calvin_products)
                else:
                    return render_template("brands_calvin.html", title="Brands Calvin", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_calvin_products=brands_calvin_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands_calvin.html", title="Brands Calvin", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_calvin_products=brands_calvin_products)
    return render_template("brands_calvin.html", title="Brands Calvin", css="men.css", del_mode_row=del_mode_row, products=products, brands_calvin_products=brands_calvin_products)
#ok







# Brands Puma:
@app.route("/brands_puma", methods=["GET", "POST"])
def brands_puma():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    brands_puma_products = len(Products.query.filter_by(section="brands-puma").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands_puma.html", title="Brands Puma", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_puma_products=brands_puma_products)
                else:
                    return render_template("brands_puma.html", title="Brands Puma", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_puma_products=brands_puma_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands_puma.html", title="Brands Puma", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_puma_products=brands_puma_products)
    return render_template("brands_puma.html", title="Brands Puma", css="men.css", del_mode_row=del_mode_row, products=products, brands_puma_products=brands_puma_products)
#ok





# Brands Lacoste:
@app.route("/brands_lacoste", methods=["GET", "POST"])
def brands_lacoste():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    brands_lacoste_products = len(Products.query.filter_by(section="brands-lacoste").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands_lacoste.html", title="Brands Lacoste", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_lacoste_products=brands_lacoste_products)
                else:
                    return render_template("brands_lacoste.html", title="Brands Lacoste", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_lacoste_products=brands_lacoste_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands_lacoste.html", title="Brands Lacoste", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_lacoste_products=brands_lacoste_products)
    return render_template("brands_lacoste.html", title="Brands Lacoste", css="men.css", del_mode_row=del_mode_row, products=products, brands_lacoste_products=brands_lacoste_products)
#ok







# Brands Fila:
@app.route("/brands_fila", methods=["GET", "POST"])
def brands_fila():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    brands_fila_products = len(Products.query.filter_by(section="brands-fila").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands_fila.html", title="Brands Fila", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_fila_products=brands_fila_products)
                else:
                    return render_template("brands_fila.html", title="Brands Fila", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_fila_products=brands_fila_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands_fila.html", title="Brands Fila", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_fila_products=brands_fila_products)
    return render_template("brands_fila.html", title="Brands Fila", css="men.css", del_mode_row=del_mode_row, products=products, brands_fila_products=brands_fila_products)
#ok




# Brands Dockers:
@app.route("/brands_dockers", methods=["GET", "POST"])
def brands_dockers():
    products = Products.query.order_by(Products.id.desc()).all()
    del_mode_row=0
    brands_dockers_products = len(Products.query.filter_by(section="brands-dockers").all())

    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("brands_dockers.html", title="Brands Dockers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_dockers_products=brands_dockers_products)
                else:
                    return render_template("brands_dockers.html", title="Brands Dockers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_dockers_products=brands_dockers_products)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("brands_dockers.html", title="Brands Dockers", css="men.css", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, brands_dockers_products=brands_dockers_products)
    return render_template("brands_dockers.html", title="Brands Dockers", css="men.css", del_mode_row=del_mode_row, products=products, brands_dockers_products=brands_dockers_products)
#ok





#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#=============================================================================================================================================================================================================================================================================================:
#                                           ===> SALE <===:
@app.route("/sale", methods=["GET","POST"])
def sale():
    products = Products.query.order_by(Products.id.desc()).all()
    SL = 0
    for i in products:
        if "sale" in i.section:
            SL += 1

    del_mode_row=0
    if request.method == "POST":
        if g.user:
            if g.id:
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                del_take = request.form.get('del_take')
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                if del_take:

                    del_mode_row.del_mode = 0
                    db.session.commit()
                    return render_template("sale.html", css="newarrivals.css", title="Sale", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, SL=SL)
                else:
                    return render_template("sale.html", css="newarrivals.css", title="Sale", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, SL=SL)
    else:
        if g.user:
            if g.id:
                user_car = UserProducts.query.filter_by(user_id=session['id']).all()
                L = len(user_car)
                del_mode_row = DeleteMode.query.filter_by(user_id=session["id"]).first()
                return render_template("sale.html", css="newarrivals.css", title="Sale", user=session["user"], products=products, user_car=user_car, L=L, del_mode_row=del_mode_row, SL=SL)
    return render_template("sale.html", css="newarrivals.css", title="Sale", products=products, del_mode_row=del_mode_row, SL=SL)








if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
