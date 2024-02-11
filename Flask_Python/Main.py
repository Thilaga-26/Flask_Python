from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

obj=Flask(__name__)

obj.config["MYSQL_HOST"]="localhost"
obj.config["MYSQL_USER"]="root"
obj.config["MYSQL_PASSWORD"]="Lanasri@26"
obj.config["MYSQL_DB"]="py"
obj.config["MYSQL_CURSORCLASS"]="DictCursor"
mysql=MySQL(obj)

#Home Page
@obj.route('/')
def homepage():
    con=mysql.connection.cursor()
    query="select * from employee"
    con.execute(query)
    result=con.fetchall()
    return render_template("homepage.html",database=result)

#Add Employees
@obj.route('/addemployee',methods=['POST','GET'])
def addemployee():
    if request.method=='POST':
        name=request.form.get("name")
        age = request.form.get("age")
        department = request.form.get("department")
        email = request.form.get("email")
        phoneno = request.form.get("phoneno")
        address = request.form.get("address")
        con = mysql.connection.cursor()
        query="insert into employee(Name,Age,Department,Email,PhoneNo,Address) values (%s,%s,%s,%s,%s,%s)"
        con.execute(query, [name,age,department,email,phoneno,address])
        mysql.connection.commit()
        con.close()
        flash("Employee Details Added!!!")
        return redirect(url_for("homepage"))
    return render_template("addemployee.html")

#Update Employee
@obj.route('/updateemployee/<string:id>',methods=['POST','GET'])
def updateemployee(id):
    con = mysql.connection.cursor()
    if request.method=='POST':
        name=request.form.get("name")
        age = request.form.get("age")
        department = request.form.get("department")
        email = request.form.get("email")
        phoneno = request.form.get("phoneno")
        address = request.form.get("address")
        query="update employee set Name=%s, Age=%s, Department=%s, Email=%s, PhoneNo=%s, Address=%s where Id=%s"
        con.execute(query, [name,age,department,email,phoneno,address,id])
        mysql.connection.commit()
        con.close()
        flash("Employee Details Updated!!!")
        return redirect(url_for("homepage"))

    query="select * from employee where Id=%s"
    con.execute(query, [id])
    result=con.fetchone()
    return render_template("updateemployee.html",data=result)

#Delete Employee
@obj.route('/deleteemployee/<string:id>',methods=['POST','GET'])
def deleteemployee(id):
    con=mysql.connection.cursor()
    query="delete from employee where Id=%s"
    con.execute(query, id)
    mysql.connection.commit()
    con.close()
    flash("Employee Details Deleted!!!")
    return redirect(url_for("homepage"))

if (__name__=='__main__'):
    obj.secret_key="Lana@123"
    obj.run(debug=True)