from flask import Flask, sessions
from flask import render_template,request,redirect,flash
from flask.helpers import url_for
from flaskext.mysql import MySQL
from pymysql import connect

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

@app.route('/indexf')
def indexf():

    sql ="SELECT * FROM `info` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    info= cursor.fetchall()
    print(info)
    conn.commit()

    return render_template('infor/indexf.html', info= info)


@app.route('/indexa')
def indexa():

    sql ="SELECT * FROM `administrador` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    administrador= cursor.fetchall()
    print(administrador)
    conn.commit()



    return render_template('adm/indexa.html', administrador= administrador)

@app.route('/indexb ')
def indexb():

    sql ="SELECT * FROM `companía b` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    compania_b= cursor.fetchall()
    print(compania_b)
    conn.commit()



    return render_template('compania_b/indexb.html', compania_b= compania_b)

@app.route('/indexc')
def indexc():

    sql ="SELECT * FROM `companía c` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    compania_c= cursor.fetchall()
    print(compania_c)
    conn.commit()



    return render_template('compania_c/indexc.html', compania_c= compania_c)

@app.route('/indexi')
def indexi():

    sql ="SELECT * FROM `instructores` ;"
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    instructores= cursor.fetchall()
    print(instructores)
    conn.commit()



    return render_template('instructores/indexi.html', instructores= instructores)



@app.route('/destroy/<int:id>')
def destroy(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `companía a` WHERE `companía a`.`Id_A`=%s",(id))
    conn.commit()
    return redirect('/')


@app.route('/destroyf/<int:id>')
def destroyf(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `info` WHERE `info`.`ID`=%s",(id))
    conn.commit()
    return redirect('/indexf')


@app.route('/destroya/<int:id>')
def destroya(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `administrador` WHERE `administrador`.`Id_E`=%s",(id))
    conn.commit()
    return redirect('/indexa')

@app.route('/destroyb/<int:id>')
def destroyb(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `companía b` WHERE `companía b`.`Id_B`=%s",(id))
    conn.commit()
    return redirect('/indexb%20')

@app.route('/destroyc/<int:id>')
def destroyc(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `companía c` WHERE `companía c`.`Id_C`=%s",(id))
    conn.commit()
    return redirect('/indexc')

@app.route('/destroyi/<int:id>')
def destroyi(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM `instructores` WHERE `instructores`.`Id_I`=%s",(id))
    conn.commit()
    return redirect('/indexi')



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

    

    sql ="UPDATE `companía a` SET `Nombre` = %s, `Apellido paterno` = %s, `Apellido materno` = %s, `Peso` = %s, `Estatura` = %s, `Edad` = %s , `N° carnet` = %s, `Grado` = %s  WHERE  `companía a`. `Id_A` = %s ;"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/')


@app.route('/editf/<int:id>')
def editf(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `info` WHERE `ID`=%s", (id))
    info= cursor.fetchall()
    conn.commit()
    print(info)

    return render_template('infor/editarf.html', info=info)

@app.route('/updatef', methods=['POST'])
def updatef():

    _nombre= request.form['txt1f']
    _app= request.form['txt2f']
    _apm= request.form['txt3f']
    _peso= request.form['txt4f']
    _esta= request.form['txt5f']
    _edad= request.form['txt6f']
    _carnet= request.form['txt7f']
    _grado= request.form['txt8f']
    _esq= request.form['txt9f']
    _pat= request.form['txt10f']
    id=request.form['txt0f']

    

    sql ="UPDATE `info` SET `Nombre` = %s, `Apellido paterno` = %s, `Apellido materno` = %s, `Grado` = %s, `fecha_llegada` = %s, `fecha_salida` = %s , `Puesto` = %s, `carnet` = %s, `escuadron` = %s,`patrulla` = %s WHERE  `info`. `ID` = %s ;"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado,_esq,_pat,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/indexf')



@app.route('/editi/<int:id>')
def editi(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `instructores` WHERE `Id_I`=%s", (id))
    instructores= cursor.fetchall()
    conn.commit()
    print(instructores)

    return render_template('instructores/editari.html', instructores=instructores)

@app.route('/updatei', methods=['POST'])
def updatei():

    _nombre= request.form['txt1i']
    _app= request.form['txt2i']
    _apm= request.form['txt3i']
    _peso= request.form['txt4i']
    id=request.form['txt0i']

    

    sql ="UPDATE `instructores` SET `Nombre` = %s, `Apellido` = %s,  `Grado` = %s, `Compania` = %s WHERE  `instructores`. `Id_I` = %s ;"
    datos= (_nombre,_app,_apm,_peso,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/indexi')


@app.route('/edita/<int:id>')
def edita(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `administrador` WHERE `Id_E`=%s", (id))
    administrador= cursor.fetchall()
    conn.commit()
    print(administrador)

    return render_template('adm/editara.html', administrador=administrador)

@app.route('/updatea', methods=['POST'])
def updatea():

    _nombre= request.form['txt1a']
    _app= request.form['txt2a']
    _apm= request.form['txt3a']
    _peso= request.form['txt4a']
    id=request.form['txt0a']

    

    sql ="UPDATE `administrador` SET `Nombre` = %s, `Apellido` = %s,  `Grado` = %s, `Compania` = %s WHERE  `administrador`. `Id_E` = %s ;"
    datos= (_nombre,_app,_apm,_peso,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/indexa')



@app.route('/editc/<int:id>')
def editc(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `companía c` WHERE `Id_C`=%s", (id))
    compania_c= cursor.fetchall()
    conn.commit()
    print(compania_c)

    return render_template('compania_c/editarc.html', compania_c=compania_c)

@app.route('/updatec', methods=['POST'])
def updatec():

    _nombre= request.form['txt1c']
    _app= request.form['txt2c']
    _apm= request.form['txt3c']
    _peso= request.form['txt4c']
    _esta= request.form['txt5c']
    _edad= request.form['txt6c']
    _carnet= request.form['txt7c']
    _grado= request.form['txt8c']
    id=request.form['txt0c']

    

    sql ="UPDATE `companía c` SET `Nombre` = %s, `Apellido paterno` = %s, `Apellido materno` = %s, `Peso` = %s, `Estatura` = %s, `Edad` = %s , `N° carnet` = %s, `Grado` = %s WHERE  `companía c`. `Id_C` = %s ;"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/indexc')



@app.route('/editb/<int:id>')
def editb(id):

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM `companía b` WHERE `Id_B`=%s", (id))
    compania_b= cursor.fetchall()
    conn.commit()
    print(compania_b)

    return render_template('compania_b/editarb.html', compania_b=compania_b)

@app.route('/updateb', methods=['POST'])
def updateb():

    _nombre= request.form['txt1b']
    _app= request.form['txt2b']
    _apm= request.form['txt3b']
    _peso= request.form['txt4b']
    _esta= request.form['txt5b']
    _edad= request.form['txt6b']
    _carnet= request.form['txt7b']
    _grado= request.form['txt8b']
    id=request.form['txt0b']

    

    sql ="UPDATE `companía b` SET `Nombre` = %s, `Apellido paterno` = %s, `Apellido materno` = %s, `Peso` = %s, `Estatura` = %s, `Edad` = %s , `N° carnet` = %s, `Grado` = %s WHERE  `companía b`. `Id_B` = %s ;"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado,id)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql, datos)
    conn.commit()


    return redirect('/indexb%20')





@app.route('/crear')
def crear():

    return render_template('soldados/crear.html')

 

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
        return redirect( url_for ('crear'))

    if _nombre== int or _app== int or _apm== int or _grado==int:
        flash('INGRESE DATOS DE TIPO TEXTO POR FABOR')
        return redirect( url_for ('crear'))


    sql ="INSERT INTO `companía a` (`Id_A`, `Nombre`, `Apellido paterno`, `Apellido materno`, `Peso`, `Estatura`, `Edad`, `N° carnet`, `Grado`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/')




@app.route('/crearf')
def crearf():

    return render_template('infor/crearf.html')

 

@app.route('/storef', methods=['POST'])
def storagef():

    _nombre= request.form['txt1f']
    _app= request.form['txt2f']
    _apm= request.form['txt3f']
    _peso= request.form['txt4f']
    _esta= request.form['txt5f']
    _edad= request.form['txt6f']
    _carnet= request.form['txt7f']
    _grado= request.form['txt8f']
    _esq= request.form['txt9f']
    _pat= request.form['txt10f']


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' or _esta=='' or _edad=='' or _carnet=='' or _grado=='' or _esq=='' or _pat=='':
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('crearf'))

    if _nombre== int or _app== int or _apm== int or _grado==int:
        flash('INGRESE DATOS DE TIPO TEXTO POR FABOR')
        return redirect( url_for ('crearf'))


    sql ="INSERT INTO `info` (`ID`, `Nombre`, `Apellido paterno`, `Apellido materno`, `Grado`, `fecha_llegada`, `fecha_salida`, `Puesto`, `carnet`,`escuadrn`,`patrulla`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s);"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado,_esq,_pat)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/indexf')









@app.route('/creari')
def creari():

    return render_template('instructores/creari.html')

 

@app.route('/storei', methods=['POST'])
def storagei():

    _nombre= request.form['txt1i']
    _app= request.form['txt2i']
    _apm= request.form['txt3i']
    _peso= request.form['txt4i']
   


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' :
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('creari'))

    

    sql ="INSERT INTO `instructores` (`Id_I`, `Nombre`, `Apellido`, `Grado`, `Compania`) VALUES (NULL, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/indexi')


@app.route('/creara')
def creara():

    return render_template('adm/creara.html')

 

@app.route('/storea', methods=['POST'])
def storagea():

    _nombre= request.form['txt1a']
    _app= request.form['txt2a']
    _apm= request.form['txt3a']
    _peso= request.form['txt4a']
   


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' :
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('creara'))

    

    sql ="INSERT INTO `administrador` (`Id_E`, `Nombre`, `Apellido`, `Grado`, `Compania`) VALUES (NULL, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/indexa')





@app.route('/crearb')
def crearb():

    return render_template('compania_b/crearb.html')

 

@app.route('/storeb', methods=['POST'])
def storageb():

    _nombre= request.form['txt1b']
    _app= request.form['txt2b']
    _apm= request.form['txt3b']
    _peso= request.form['txt4b']
    _esta= request.form['txt5b']
    _edad= request.form['txt6b']
    _carnet= request.form['txt7b']
    _grado= request.form['txt8b']


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' or _esta=='' or _edad=='' or _carnet=='' or _grado=='':
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('crearb'))

    if _nombre== int or _app== int or _apm== int or _grado==int:
        flash('INGRESE DATOS DE TIPO TEXTO POR FABOR')
        return redirect( url_for ('crearb'))


    sql ="INSERT INTO `companía b` (`Id_B`, `Nombre`, `Apellido paterno`, `Apellido materno`, `Peso`, `Estatura`, `Edad`, `N° carnet`, `Grado`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/indexb%20')


@app.route('/crearc')
def crearc():

    return render_template('compania_c/crearc.html')

@app.route('/storec', methods=['POST'])
def storagec():

    _nombre= request.form['txt1c']
    _app= request.form['txt2c']
    _apm= request.form['txt3c']
    _peso= request.form['txt4c']
    _esta= request.form['txt5c']
    _edad= request.form['txt6c']
    _carnet= request.form['txt7c']
    _grado= request.form['txt8c']


    if _nombre=='' or _app=='' or _apm=='' or _peso=='' or _esta=='' or _edad=='' or _carnet=='' or _grado=='':
        flash('LLENA LOS DATOS DE LOS CAMPOS')
        return redirect( url_for ('crearc'))

    if _nombre== int or _app== int or _apm== int or _grado==int:
        flash('INGRESE DATOS DE TIPO TEXTO POR FABOR')
        return redirect( url_for ('crearc'))


    sql ="INSERT INTO `companía c` (`Id_C`, `Nombre`, `Apellido paterno`, `Apellido materno`, `Peso`, `Estatura`, `Edad`, `N° carnet`, `Grado`) VALUES (NULL, %s, %s, %s, %s, %s, %s, %s, %s);"
    datos= (_nombre,_app,_apm,_peso,_esta,_edad,_carnet,_grado)

    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()

    return redirect('/indexc')




@app.route('/inicio')
def inicio():

    return render_template('vistas/inicio.html')

@app.route('/inic', methods=['POST'])
def inic():

    _nombre= request.form['txt11']
  
    _carnet= request.form['txt71']
   

    sql =("SELECT * FROM `info` WHERE Nombre= %s AND carnet = %s ")
    datos=(_nombre,_carnet)
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    info= cursor.fetchall()
    conn.commit()
    
    if info:
        print(info)
        return render_template('vistas/informe.html', info= info)
    else:
        flash("verifique sus datos por fabor por favor")
        return render_template("vistas/inicio.html")





@app.route('/login')
def login():

    return render_template('vistas/login.html')


@app.route('/log', methods=["POST"])
def log():
    usuario = request.form["txto1"]
    palabra_secreta = request.form["txto2"]
  
    if usuario == "USFA@2021" and palabra_secreta == "123" :
        
        return redirect("/")
    elif usuario == "USFA@2022" and palabra_secreta == "1234" :
        return redirect("/indexb%20")

    elif usuario == "USFA@2023" and palabra_secreta == "12345" :
        return redirect("/indexc")

    elif usuario == "USFA@2024" and palabra_secreta == "123456" :
        return redirect("/indexi")



    elif usuario != "USFA@2021" and palabra_secreta == "123" or usuario != "USFA@2022" and palabra_secreta == "1234" or usuario != "USFA@2023" and palabra_secreta == "12345" or usuario != "USFA@2024" and palabra_secreta == "123456" :
        flash("Usuario incorrecto, verifique por favor")
        return render_template("vistas/login.html")

    elif usuario == "USFA@2021" and palabra_secreta != "123" or usuario != "USFA@2022" and palabra_secreta == "1234" or usuario != "USFA@2023" and palabra_secreta == "12345" or usuario != "USFA@2024" and palabra_secreta == "123456" :
        flash("Contraseña incorrecto, verifique por favor")
        return render_template("vistas/login.html")

    elif usuario == "" and palabra_secreta == "":
        flash("LLene los datos, de inicio de sesión por favor")
        return render_template("vistas/login.html")

    else:
        #
        flash("Usuario o contraseña incorrectos")
        return render_template("vistas/login.html")



    
    
    

    




if __name__== '__main__':
    app.run(debug=True)
