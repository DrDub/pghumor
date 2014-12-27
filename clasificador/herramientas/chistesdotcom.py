# coding=utf-8
from __future__ import absolute_import, unicode_literals

import mysql.connector

from clasificador.herramientas.define import DB_HOST, DB_NAME_CHISTES_DOT_COM, DB_PASS, DB_USER
from clasificador.realidad.chiste import Chiste


def cargar_chistes_pagina():
    conexion = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME_CHISTES_DOT_COM)
    cursor = conexion.cursor(buffered=True)  # buffered así sé la cantidad que son antes de iterarlos

    consulta = """
    SELECT id_chiste,
           texto_chiste,
           id_clasificacion,
           nombre_clasificacion,
           votacion,
           cantidad_votantes
    FROM   chistes
    """

    cursor.execute(consulta)

    chistes = []
    for (id_chiste, texto_chiste, id_clasificacion, nombre_clasificacion, votacion, cantidad_votantes) in cursor:
        chiste = Chiste()
        chiste.id_chiste = id_chiste
        chiste.texto_chiste = texto_chiste
        chiste.id_clasificacion = id_clasificacion
        chiste.nombre_clasificacion = nombre_clasificacion
        chiste.votacion = votacion
        chiste.cantidad_votantes = cantidad_votantes
        chistes.append(chiste)

    return chistes


def obtener_chistes_categoria(categoria):
    conexion = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME_CHISTES_DOT_COM)
    cursor = conexion.cursor(buffered=True)  # buffered así sé la cantidad que son antes de iterarlos

    consulta = """
    SELECT id_chiste,
           texto_chiste,
           id_clasificacion,
           nombre_clasificacion,
           votacion,
           cantidad_votantes
    FROM   chistes
    WHERE id_clasificacion =
    """

    consulta += str(categoria)

    cursor.execute(consulta)

    chistes = []
    for (id_chiste, texto_chiste, id_clasificacion, nombre_clasificacion, votacion, cantidad_votantes) in cursor:
        chiste = Chiste()
        chiste.id_chiste = id_chiste
        chiste.texto_chiste = texto_chiste
        chiste.id_clasificacion = id_clasificacion
        chiste.nombre_clasificacion = nombre_clasificacion
        chiste.votacion = votacion
        chiste.cantidad_votantes = cantidad_votantes
        chistes.append(chiste)

    return chistes


def obtener_categorias():
    conexion = mysql.connector.connect(user=DB_USER, password=DB_PASS, host=DB_HOST, database=DB_NAME_CHISTES_DOT_COM)
    cursor = conexion.cursor()

    consulta = """
        SELECT id_clasificacion, nombre_clasificacion
        FROM chistesdotcom.chistes
        GROUP BY id_clasificacion, nombre_clasificacion
        HAVING count(*) > 99;
    """

    cursor.execute(consulta)

    categorias = []
    for (id_clasificacion, nombre_clasificacion) in cursor:
        categoria = {'id_clasificacion': id_clasificacion, 'nombre_clasificacion': nombre_clasificacion}
        categorias.append(categoria)

    return categorias