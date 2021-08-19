from flask import Flask
from flask import render_template,request,redirect,flash
from flask.helpers import url_for
from flaskext.mysql import MySQL

app= Flask(__name__)
app.secret_key="USFA"

mysql= MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='rc 7 chichas'
mysql.init_app(app)


@app.route('/')
def index():

    sql ="SELECT * FROM `companía a` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    compania_a= cursor.fetchall()
    print(compania_a)
    conn.commit()



    return render_template('soldados/index.html', compania_a= compania_a)


@app.route('/destroy/<int:id>')
def destroy(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `companía a` WHERE `companía a`.`Id_A`=%s",(id))
    conn.commit()
    return redirect('/')


@app.route('/edit/<int:id>')
def edit(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `companía a` WHERE `Id_A`=%s", (id))
    compania_a= cursor.fetchall()
    conn.commit()
    print(compania_a)

    return render_template('soldados/editar.html', compania_a=compania_a)

@app.route('/update', methods=['POST'])
def update():

    _nombre= request.form['txt1']
    _app= request.form['txt2']
    _apm= request.form['txt3']
    _peso= request.form['txt4']
    _esta= request.form['txt5']
    _edad= request.form['txt6']
    _carnet= request.form['txt7']
    _grado= request.form['txt8']
    id=request.form['txt0']

    

    sql ="UPDATE `companía a` SET `Nombre` = '%s', `Apellido paterno` = '%s', `Apellido materno` = '%s', `Peso` = '%s', `Estatura` = '%s', `Edad` = '%s ' WHERE  `companía a`. `Id_A` = '%s' ;"
    datos= (id,_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/')



   

@app.route('/crear')
def create():

    return render_template('soldados/crear.html')


@app.route('/inicio')
def inicio():
    return render_template('soldados/inicio.html')
   

@app.route('/store', methods=['POST'])
def storage():

    _nombre= request.form['txt1']
    _app= request.form['txt2']
    _apm= request.form['txt3']
    _peso= request.form['txt4']
    _esta= request.form['txt5']
    _edad= request.form['txt6']
    _carnet= request.form['txt7']
    _grado= request.form['txt8']


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' or _esta=='' or _edad=='' or _carnet=='' or _grado=='':
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('create'))

    if _nombre== int or _app== int or _apm== int or _grado==int:
        flash('INGRESE DATOS DE TIPO TEXTO POR FABOR')
        return redirect( url_for ('create'))


    sql ="INSERT INTO `companía a` (`Id_A`, `Nombre`, `Apellido paterno`, `Apellido materno`, `Peso`, `Estatura`, `Edad`, `N° carnet`, `Grado`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/')




if __name__== '__main__':
    app.run(debug=True)
