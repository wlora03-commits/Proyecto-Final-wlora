import pandas as pd
import numpy as np

# ==========================================
# PROYECTO FINAL - TELCO CUSTOMER CHURN
# MES 4 - CIENCIA DE DATOS PARA IA
# ==========================================

# 1. Cargar dataset
df = pd.read_csv("data/telco_churn.csv")

print("\n" + "=" * 60)
print("1. INFORMACIÓN GENERAL")
print("=" * 60)

print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")

print("\nPrimeras 5 filas:")
print(df.head())


# 2. Tipos de datos
print("\n" + "=" * 60)
print("2. TIPOS DE DATOS")
print("=" * 60)

print(df.dtypes)


# 3. Valores nulos
print("\n" + "=" * 60)
print("3. VALORES NULOS")
print("=" * 60)

print(df.isnull().sum())


# 4. Duplicados
print("\n" + "=" * 60)
print("4. DUPLICADOS")
print("=" * 60)

print(f"Filas duplicadas: {df.duplicated().sum()}")


# 5. Diagnóstico de TotalCharges
print("\n" + "=" * 60)
print("5. DIAGNÓSTICO DE TOTALCHARGES")
print("=" * 60)

print("Tipo actual:")
print(df["TotalCharges"].dtype)

espacios = df["TotalCharges"].astype(str).str.strip().eq("").sum()

print("\nValores con espacios en blanco:")
print(espacios)

print("\nRegistros problemáticos:")
print(
    df[df["TotalCharges"].astype(str).str.strip() == ""]
    [["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]]
)


# 6. Conversión temporal
total_charges_numeric = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\nValores convertidos a NaN:")
print(total_charges_numeric.isnull().sum())


# 7. Resumen estadístico
print("\n" + "=" * 60)
print("6. RESUMEN ESTADÍSTICO")
print("=" * 60)



# ==========================================
# 7. LIMPIEZA DEL DATASET -trabajo wlora
# ==========================================

print("\n" + "=" * 60)
print("7. LIMPIEZA DEL DATASET")
print("=" * 60)

# ------------------------------------------
# 7.1 Limpiar espacios en blanco
# ------------------------------------------

df["TotalCharges"] = df["TotalCharges"].str.strip()

# ------------------------------------------
# 7.2 Convertir TotalCharges a numérico
# ------------------------------------------

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

print("\nTipo de TotalCharges después de convertir:")
print(df["TotalCharges"].dtype)

print("\nValores nulos después de la conversión:")
print(df["TotalCharges"].isnull().sum())


# ------------------------------------------
# 7.3 Analizar los valores faltantes
# ------------------------------------------

print("\nRegistros con TotalCharges nulo:")

print(
    df[df["TotalCharges"].isnull()]
    [["customerID", "tenure", "MonthlyCharges", "TotalCharges", "Churn"]]
)


# ------------------------------------------
# 7.4 Corregir TotalCharges
# ------------------------------------------

# Los 11 registros tienen tenure = 0.
# Para estos clientes todavía no existe un cargo acumulado.
# Se utiliza MonthlyCharges como valor inicial de TotalCharges.

df.loc[
    df["TotalCharges"].isnull(),
    "TotalCharges"
] = df.loc[
    df["TotalCharges"].isnull(),
    "MonthlyCharges"
]


# ------------------------------------------
# 7.5 Verificar limpieza
# ------------------------------------------

print("\nNulos después de la limpieza:")
print(df.isnull().sum())

print("\nDuplicados después de la limpieza:")
print(df.duplicated().sum())

print("\nTipo final de TotalCharges:")
print(df["TotalCharges"].dtype)

print("\nDimensiones finales:")
print(df.shape)
