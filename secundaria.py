import functools
import tkinter as tk
import tkinter
import os
from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
import pymysql
import hashlib
from functools import partial
import socket, pickle

global salir
lista_archivos=[]
#entry_ip
#lista_md5=[]


_mysql_server = "163.178.107.10"
_mysql_database = "redes_2_proyecto_1"
_mysql_server_port = 3306
_mysql_user = "laboratorios"
_mysql_password = "KmZpo.2796"
#calculo de codigo md5
def md5sum(filename):
       with open(filename, mode='rb') as f:
           d = hashlib.md5()
           for buf in iter(partial(f.read, 128), b''):
               d.update(buf)
       return d.hexdigest()
    
def ventana_secundaria(master, callback=None, args=(), kwargs={}):
    if callback is not None:
        callback = functools.partial(callback, *args, **kwargs)

    main_frame = tk.Frame(master)
    global nombre_usuario
    global  contrasenna
    global ip
    nombre_usuario=tk.StringVar()
    contrasenna=tk.StringVar()
    ip=tk.StringVar()
    global st_nombre
    global st_contra
    global st_ip
    
    #botones
    boton2 = tk.Button(main_frame, text="Login", command=validar_usuario)
    #boton2.place(x=15, y=30)
    boton_volver = tk.Button(main_frame, text="Volver", command=callback)
    #boton_volver.place(x=110, y=30)
    #label
    label=tk.Label(main_frame, text="Nombre")
    label.place(x=15, y=10)
    #entry
    st_nombre=tk.Entry(main_frame, textvariable=nombre_usuario)
    st_nombre.place(x=15, y=70)
    label=tk.Label(main_frame, text="Contraseña")
    label.place(x=15, y=100)
    st_contra=tk.Entry(main_frame, show='*', textvariable=contrasenna)
    st_contra.place(x=15, y=130)
    label=tk.Label(main_frame, text="Ip a conectarse")
    label.place(x=20, y=160)
    st_ip=tk.Entry(main_frame, textvariable=ip)
    st_ip.place(x=20, y=200)
    boton2.place(x=15, y=230)
    boton_volver.place(x=110, y=230)
    return main_frame

def validar_archivo(md5 ,lista):
    cambiar=False
    for el in lista:
        if el in md5:
            lista_archivos.append(el)
            cambiar=True
    return cambiar
    
def getListOfFiles(dirName):
    # create a list of file and sub directories 
    # names in the given directory 
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory 
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles    
def open_path():
    file=filedialog.askdirectory()
    lista=getListOfFiles(file)
    lista_md5=[]
    for campo in lista:
        lista_md5.append(md5sum(campo))
    #print(file)
    Salir=True
    ClientSocket = socket.socket()
    host = st_ip.get()
    port = 1234

    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    Response = ClientSocket.recv(1024)
    #while True:
    Input = st_nombre.get()
    Input2 = 'bien'
    ClientSocket.send(str.encode(Input))
    ClientSocket.send(str.encode(Input2))
    Response = ClientSocket.recv(1024)
    Response2=ClientSocket.recv(4096)
    data_arr=pickle.loads(Response2)
    #print(Response.decode('utf-8'))
    print (data_arr)
    if validar_archivo:
        data_string = pickle.dumps(lista_archivos)
        ClientSocket.send(data_string)
        messagebox.showinfo(title="Estado de virus", message="Si tiene virus")
    else:
        messagebox.showinfo(title="Estado de virus", message="No tiene virus")
        data_string=pickle.dumps(lista_archivos)
        ClientSocket.send(data_string)
    final=ClientSocket.recv(1024)
    print("Busqueda "+final.decode('utf-8'))
    ClientSocket.close()
"""def open_root():
    file='C:\'
    lista=getListOfFiles(file)
    lista_md5=[]
    for campo in lista:
        lista_md5.append(md5sum(campo))
    #print(file)
    Salir=True
    ClientSocket = socket.socket()
    host = st_ip.get()
    port = 1234

    print('Waiting for connection')
    try:
        ClientSocket.connect((host, port))
    except socket.error as e:
        print(str(e))

    Response = ClientSocket.recv(1024)
    #while True:
    Input = st_nombre.get()
    Input2 = 'bien'
    ClientSocket.send(str.encode(Input))
    ClientSocket.send(str.encode(Input2))
    Response = ClientSocket.recv(1024)
    Response2=ClientSocket.recv(4096)
    data_arr=pickle.loads(Response2)
    #print(Response.decode('utf-8'))
    print (data_arr)
    if validar_archivo:
        data_string = pickle.dumps(lista_archivos)
        ClientSocket.send(data_string)
        messagebox.showinfo(title="Estado de virus", message="Si tiene virus")
    else:
        messagebox.showinfo(title="Estado de virus", message="No tiene virus")
        data_string=pickle.dumps(lista_archivos)
        ClientSocket.send(data_string)
    final=ClientSocket.recv(1024)
    print("Busqueda "+final.decode('utf-8'))
    ClientSocket.close()
"""
def validar_usuario():
    bd=pymysql.connect(
        host=_mysql_server,
        user=_mysql_user,
        password=_mysql_password,
        db=_mysql_database
        )
    fcursor=bd.cursor()
    
    fcursor.execute("SELECT contra FROM usuario WHERE nombre='"+st_nombre.get()+"' and contra='"+st_contra.get()+"'")

    if fcursor.fetchall():
        bd.close()
        pantalla()
        #messagebox.showinfo(title="Inicio de sesión correcto", message="Inicio de sesión correcto")
    else:
        messagebox.showinfo(title="Inicio de sesión incorrecto", message="Inicio de sesión incorrecto")
        bd.close()

def pantalla():
    global pantalla
    pantalla=tk.Tk()
    pantalla.title("Usar antivirus")
    #pantalla=Toplevel(pantalla)
    pantalla.geometry("300x300")
    print(st_nombre.get())
    Label(pantalla, text="Ingrese la ip a conectarse", bg="navy", fg="white", font=("Calibri", 15)).pack()
    Button(pantalla, text="Escaneo por carpeta", height="3", width="30", command=open_path).pack()
    Button(pantalla, text="Escaneo total", height="3", width="30", command=open_path).pack()
    

    pantalla.mainloop()
    #entry_ip.pack()
    #ip=Entry(pantalla)   
    
