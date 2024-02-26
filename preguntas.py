"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""

import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    filas = tbl0.shape[0]

    return filas


def pregunta_02():
    columnas = tbl0.shape[1]

    return columnas


def pregunta_03():
    cantidadLetras = tbl0["_c1"].value_counts().sort_index()

    return cantidadLetras


def pregunta_04():
    promedioPorLetra = tbl0.groupby("_c1")["_c2"].mean()

    return promedioPorLetra


def pregunta_05():
    maximoPorLetra = tbl0.groupby("_c1")["_c2"].max()

    return maximoPorLetra


def pregunta_06():
    valoresUnicos = sorted(tbl1["_c4"].str.upper().unique())

    return valoresUnicos


def pregunta_07():
    sumaValores = tbl0.groupby("_c1")["_c2"].sum()

    return sumaValores


def pregunta_08():
    tabla0Suma = tbl0.assign(suma=tbl0["_c0"] + tbl0["_c2"])

    return tabla0Suma


def pregunta_09():
    tbl0Copy = tbl0.copy()
    tbl0Copy["year"] = tbl0["_c3"].str.split("-").str[0]

    return tbl0Copy


def pregunta_10():
    tabla = (
        tbl0.groupby("_c1")["_c2"]
        .apply(lambda x: ":".join(map(str, sorted(x))))
        .reset_index()
    )
    tabla.columns = ["_c0", "_c1"]

    return tabla


def pregunta_11():
    tabla = (
        tbl1.groupby("_c0")["_c4"].apply(lambda x: ",".join(sorted(x))).reset_index()
    )

    return tabla


def pregunta_12():
    tabla = (
        tbl2.groupby("_c0")[["_c5a", "_c5b"]]
        .apply(
            lambda x: ",".join(sorted(f"{a}:{b}" for a, b in zip(x["_c5a"], x["_c5b"])))
        )
        .reset_index()
    )
    tabla.columns = ["_c0", "_c5"]

    return tabla


def pregunta_13():
    tablaCombinada = pd.merge(tbl0, tbl2, on="_c0")
    sumaValorc1 = tablaCombinada.groupby("_c1")["_c5b"].sum()

    return sumaValorc1
