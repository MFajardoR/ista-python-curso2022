from asyncore import read, write
from flask import Flask, jsonify, request
import csv
##import urllib
import urllib.request
###import pandas as pd
from csv import writer

app = Flask(__name__)


def leer_archivo():
    archivo = None
    with open("datos\estudiante.csv") as a:
        ##archivo = a.readlines()
        archivo = a.readlines()
    return archivo

def leer():
    archivo = None
    with open("datos\sistencia.csv") as a:
        ##archivo = a.readlines()
        archivo = a.readlines()
    return archivo

@app.route("/")
def mostar_informacion():
    contenido = leer_archivo()
    return jsonify(contenido)


@app.route("/crear")
def crear_asistencia():
    list = ['0245547', "python", "2022", "6", "12"]
    with open("datos\sistencia.csv", "w") as a:
        writer = csv.writer(a)
        writer.writerow(list)
        contenido = leer()

    return jsonify(contenido)
