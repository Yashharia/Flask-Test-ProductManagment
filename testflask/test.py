from flask import Flask, render_template, redirect,request
from flask_mysqldb import MySQL
from flask_nav import Nav
from flask_nav.elements import Navbar,View,Subgroup
from wtforms import Form,StringField ,SelectField, IntegerField, validators
from flask_bootstrap import Bootstrap

nav = Nav()

app = Flask(__name__)
Bootstrap(app)

"""@app.route('/')
def index():
	return render_template('index.html')"""


#NAVIGATION BAR
@nav.navigation("mynavbar")
def mynavbar():
	
		home_view=View('Home page','home')
		Product_view=View('Products ','productspage')
		AddProduct_view=View('add products','addproducts')
		EditProduct_view=View('edit products','editproduct')
		Products_List_view=Subgroup('Products',Product_view,AddProduct_view,EditProduct_view)
		Location_View=View('location page','locationpage')
		AddLocation_view=View('add location','addlocation')
		EditLocation_view=View('edit location','editlocation')
		Location_List_view=Subgroup('Location',Location_View,AddLocation_view,EditLocation_view)
		ProductMovement_View=View('productmovement','productmovement')
		AddProductMovement_view=View('add ProductMovement','addproductmovement')
		EditProductMovement_view=View('edit ProductMovement','editpage')
		ProductMovement_List_view=Subgroup('ProductMovement',ProductMovement_View,AddProductMovement_view,EditProductMovement_view)

		return Navbar('mynavbar',home_view,Products_List_view,Location_List_view,ProductMovement_List_view)

nav.init_app(app)

#MYSQL VALUES
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_PORT']=3307
app.config['MYSQL_DB']='flaskapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

#MYSQL VALUES
mysql=MySQL(app)

@app.route('/',methods=['GET','POST'])
def index():
	return redirect('/home')

#REPORT PAGE
@app.route('/home',methods=['GET','POST'])
def home():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM location")
	locationDetails=cur.fetchall()
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM productmovement")
	movementDetails=cur.fetchall()
	return render_template('report.html',movementDetails=movementDetails,locationDetails=locationDetails)

#PRODUCT PAGE
@app.route('/productspage',methods=['GET','POST'])
def productspage():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM products")
	productDetails=cur.fetchall()
	return render_template('testproductspage.html',productDetails=productDetails)

#PRODUCT FORM
class ProductForm(Form):
	product_id = StringField(
        'product id', [validators.Required()])
	
class EditProductForm(Form):
	edit_product=SelectField('edit location',choices=[])
	product_id = StringField(
        'product id', [validators.Required()])

#ADD PRODUCT
@app.route('/addproducts',methods=['GET','POST'])
def addproducts():
	form = ProductForm(request.form)
	if request.method=='POST' and form.validate():
		product_id=form.product_id.data
		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO products VALUES(%s)",(product_id,))
		mysql.connection.commit()
		cur.close()
		return redirect('/productspage')
	return render_template('addproduct.html',form=form)

#EDIT PRODUCT
@app.route('/editproduct', methods=['GET','POST'])
def editproduct():
	form=EditProductForm(request.form)

	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM products")
	result=cur.fetchall()
	productlist=[]
	for i in result:
		productlist.append(list(i.values())[0])
	form.edit_product.choices=[(i,i)for i in productlist]
	if request.method=='POST' and form.validate():
		product_id=form.product_id.data
		edit_product=form.edit_product.data
		cur=mysql.connection.cursor()
		cur.execute("UPDATE products SET product_id=%s WHERE product_id=%s",(product_id,edit_product))
		mysql.connection.commit()
		cur.close()
		return redirect('/productspage')
	return render_template('editproduct.html',form=form)

#--------------------------------------------------------------------

@app.route('/locationpage',methods=['GET','POST'])
def locationpage():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM location")
	locationDetails=cur.fetchall()
	return render_template('locationpage.html',locationDetails=locationDetails)

#Location FORM
class Location(Form):
	location_id = StringField(
        'location id', [validators.Required()])

class EditLocationForm(Form):
	edit_location=SelectField('edit location',choices=[])
	location_id = StringField(
        'location id', [validators.Required()])


#ADD Location
@app.route('/addlocation',methods=['GET','POST'])
def addlocation():
	form = Location(request.form)
	if request.method=='POST' and form.validate():
		location_id=form.location_id.data
		cur=mysql.connection.cursor()
		cur.execute('INSERT INTO location VALUES(%s)',(location_id,))
		mysql.connection.commit()
		cur.close()
		return redirect('/locationpage')
	return render_template('addlocation.html',form=form)

#EDIT Location
@app.route('/editlocation', methods=['GET','POST'])
def editlocation():
	form=EditLocationForm(request.form)
	cur=mysql.connection.cursor()
	cur.execute("SELECT * from location")
	result=cur.fetchall()
	locationlist=[]
	for i in result:
		locationlist.append(list(i.values())[0])
	form.edit_location.choices=[(i,i)for i in locationlist]

	if request.method=='POST' and form.validate():
		location_id=form.location_id.data
		edit_location=form.edit_location.data
		cur=mysql.connection.cursor()
		cur.execute("UPDATE location SET location_id=%s WHERE location_id=%s",(location_id,edit_location))
		mysql.connection.commit()
		cur.close()
		return redirect('/locationpage')
	return render_template('editlocation.html',form=form)

#____________________________________________________________________________________________________________________________________-

#PRODUCT MOVEMENT

@app.route('/productmovement',methods=['GET','POST'])
def productmovement():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM productmovement")
	movementDetails=cur.fetchall()
	return render_template('productmovement.html',movementDetails=movementDetails)


#ADD PRODUCT MOVEMENT

class LocationForm(Form):
	from_location=SelectField('From Location',choices=[])
	to_location=SelectField('to Location',choices=[])
	product_idlist=SelectField('product id',choices=[])
	quantity=IntegerField('quantity')

@app.route('/addproductmovement',methods=['GET','POST'])
def addproductmovement():
	form=LocationForm(request.form)
	cur=mysql.connection.cursor()
	cur.execute("SELECT * from location")
	result=cur.fetchall()
	locationlist=[]
	for i in result:
		locationlist.append(list(i.values())[0])
	form.from_location.choices=[(i,i)for i in locationlist]
	form.from_location.choices.append(('null','null'))
	form.to_location.choices=[(i,i)for i in locationlist]
	form.to_location.choices.append(('null','null'))

	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM products")
	result=cur.fetchall()
	productlist=[]
	for i in result:
		productlist.append(list(i.values())[0])
	form.product_idlist.choices=[(i,i)for i in productlist]

	if request.method=='POST' and form.validate():
		from_location=form.from_location.data
		to_location=form.to_location.data
		product_id=form.product_idlist.data
		quantity=form.quantity.data
		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO productmovement(from_location,to_location,product_id,quantity) VALUES(%s,%s,%s,%s)",(from_location,to_location,product_id,quantity))
		mysql.connection.commit()
		cur.close()
		return redirect('/productmovement')
	return render_template('addproductmovement.html',form=form)

@app.route('/editpage',methods=['GET','POST'])
def editpage():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM productmovement")
	movementDetails=cur.fetchall()
	return render_template('editpage.html',movementDetails=movementDetails)


#EDIT PRODUCTMOVEMENT
@app.route('/editproductmovement/<string:id>',methods=['GET','POST'])
def editproductmovement(id):
	form=LocationForm(request.form)
	cur=mysql.connection.cursor()
	cur.execute("SELECT * from location")
	result=cur.fetchall()
	locationlist=[]
	for i in result:
		locationlist.append(list(i.values())[0])
	form.from_location.choices=[(i,i)for i in locationlist]
	form.from_location.choices.append(('null','null'))
	form.to_location.choices=[(i,i)for i in locationlist]
	form.to_location.choices.append(('null','null'))

	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM products")
	result=cur.fetchall()
	productlist=[]
	for i in result:
		productlist.append(list(i.values())[0])
	form.product_idlist.choices=[(i,i)for i in productlist]

	


	if request.method=='POST' and form.validate():
		from_location=form.from_location.data
		to_location=form.to_location.data
		product_id=form.product_idlist.data
		quantity=form.quantity.data
		cur=mysql.connection.cursor()
		cur.execute("UPDATE productmovement SET from_location=%s ,to_location= %s ,product_id=%s ,quantity=%s where movement_id=%s",(from_location,to_location,product_id,quantity,id))
		mysql.connection.commit()
		cur.close()
		return redirect('/productmovement')
	return render_template('editproductmovement.html',form=form)



#RUN SERVER
if __name__=='__main__':
	app.run(debug=True)

