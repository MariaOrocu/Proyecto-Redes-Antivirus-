import functools
import tkinter as tk
import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox

_mysql_server = "163.178.107.10"
_mysql_database = "redes_2_proyecto_1"
_mysql_server_port = 3306
_mysql_user = "laboratorios"
_mysql_password = "KmZpo.2796"


def ventana_tercera(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    global nombre_usuario_r
    global  contrasenna_r

    nombre_usuario_r=tk.StringVar()
    contrasenna_r=tk.StringVar()

    global st_nombre_r
    global st_contra_r
    label=tk.Label(main_frame, text="Nombre")
    label.place(x=15, y=10)
    #entry
    st_nombre_r=tk.Entry(main_frame, textvariable=nombre_usuario_r)
    st_nombre_r.place(x=15, y=70)
    label=tk.Label(main_frame, text="Contraseña")
    label.place(x=15, y=100)
    st_contra_r=tk.Entry(main_frame, show='*', textvariable=contrasenna_r)
    st_contra_r.place(x=15, y=130)
    boton3 = tk.Button(main_frame, text="Registro", command=insertar)
    boton3.place(x=15, y=160)
    boton_volver1 = tk.Button(main_frame, text="Volver", command=callback)
    boton_volver1.place(x=110, y=160)
    #label1=tk.Label(main_frame, text="Ingresa las credenciales")
    #label1.place(x=15, y=70)
    return main_frame

def insertar():
    bd=pymysql.connect(
        host=_mysql_server,
        user=_mysql_user,
        password=_mysql_password,
        db=_mysql_database
        )
    fcursor=bd.cursor()
    
    sql="INSERT INTO usuario(nombre, contra) VALUES ('{0}','{1}')".format(st_nombre_r.get(),st_contra_r.get())

    try:
        fcursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="registrado correctamente", title="success")
    except:
        bd.rollback()
        messagebox.showinfo(message="no registrado", title="error")

    bd.close()


