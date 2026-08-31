# Predicción de Abandono de Clientes — Telco Customer Churn

##  Descripción del proyecto

Este proyecto tiene como objetivo desarrollar un modelo de Machine Learning supervisado capaz de predecir si un cliente de una empresa de telecomunicaciones tiene probabilidad de abandonar el servicio (*Customer Churn*).

El proyecto utiliza el dataset **Telco Customer Churn** y aplica diferentes técnicas de preparación y transformación de datos antes de utilizar los datos para el entrenamiento de un modelo predictivo.

---

## Objetivo

Predecir la variable **`Churn`**, que indica si un cliente abandonó o no el servicio.

La variable objetivo contiene dos categorías:

* `Yes` → el cliente abandonó el servicio.
* `No` → el cliente permaneció con el servicio.

---

## Dataset

El dataset contiene información relacionada con:

* Datos demográficos de los clientes.
* Servicios contratados.
* Tipo de contrato.
* Método de pago.
* Antigüedad del cliente.
* Cargos mensuales.
* Cargos acumulados.
* Estado de abandono del cliente.

Después del proceso de preparación, se trabajó con **7,043 registros y 19 variables predictoras**, excluyendo `customerID` y `Churn`.

---

## Limpieza y preparación de datos

Durante la etapa de preparación se realizaron las siguientes tareas:

1. Diagnóstico inicial del dataset.
2. Identificación de tipos de datos.
3. Detección de `TotalCharges` como variable de texto.
4. Conversión de `TotalCharges` a formato numérico.
5. Tratamiento de valores nulos.
6. Revisión de registros duplicados.
7. Eliminación de `customerID` como variable predictora.

---

## Feature Engineering

Se crearon nuevas variables para aportar información adicional al modelo:

### `ClienteAntiguo`

Variable creada para representar la antigüedad del cliente.

### `GastoPromedioMensual`

Variable creada para representar el comportamiento promedio de gasto mensual del cliente.

Estas variables permiten enriquecer la información disponible para el modelo.

---

## Análisis exploratorio

Se realizaron visualizaciones para analizar la relación entre diferentes variables y el abandono de clientes.

### Contrato vs Churn

Se analizó la relación entre el tipo de contrato y el abandono de clientes.

### Método de pago vs Churn

Se analizó la relación entre el método de pago y el abandono de clientes.

Estas visualizaciones ayudan a identificar patrones relacionados con el comportamiento de los clientes.

---

## Train/Test Split

Los datos fueron divididos en:

* **80% para entrenamiento**
* **20% para prueba**

Se utilizó:

```python
random_state=42
```

para garantizar la reproducibilidad del experimento.

También se utilizó:

```python
stratify=y
```

para mantener una proporción similar de las clases de `Churn` en los conjuntos de entrenamiento y prueba.

### Dimensiones

| Dataset   | Dimensiones |
| --------- | ----------: |
| `X_train` |  5,634 × 19 |
| `X_test`  |  1,409 × 19 |
| `y_train` |       5,634 |
| `y_test`  |       1,409 |

---

## Encoding

Las variables categóricas fueron transformadas utilizando **One-Hot Encoding** mediante `OneHotEncoder` de Scikit-Learn.

Se utilizó:

```python
handle_unknown="ignore"
```

El encoder fue ajustado únicamente utilizando los datos de entrenamiento y posteriormente aplicado a los datos de prueba, evitando así problemas de *data leakage*.

El proceso generó **41 variables codificadas**.

---

## Escalado

Las variables numéricas fueron escaladas utilizando:

```python
StandardScaler
```

El scaler fue ajustado únicamente con los datos de entrenamiento y posteriormente aplicado al conjunto de prueba.

Las variables numéricas utilizadas fueron:

* `SeniorCitizen`
* `tenure`
* `MonthlyCharges`
* `TotalCharges`

---

##  Datos finales

Después del proceso de Encoding y Scaling se obtuvieron:

| Dataset         | Dimensiones |
| --------------- | ----------: |
| `X_train_final` |  5,634 × 45 |
| `X_test_final`  |  1,409 × 45 |

Los datos finales contienen:

* 4 variables numéricas escaladas.
* 41 variables categóricas codificadas.

**Total: 45 variables predictoras.**

---

## Archivos generados

El proyecto genera los siguientes archivos:

```text
X_train.csv
X_test.csv
y_train.csv
y_test.csv
```

Estos archivos contienen los datos preparados para la etapa de entrenamiento y evaluación del modelo.

---

## Tecnologías utilizadas

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Jupyter Notebook
* Visual Studio Code
* Git
* GitHub

---

##  Librerías principales

```python
pandas
numpy
matplotlib
scikit-learn
```

---

## Flujo del proyecto

```text
Dataset
   ↓
Diagnóstico
   ↓
Limpieza de datos
   ↓
Feature Engineering
   ↓
Análisis exploratorio
   ↓
Train/Test Split
   ↓
One-Hot Encoding
   ↓
Scaling
   ↓
Datos finales
   ↓
Entrenamiento del modelo
   ↓
Evaluación
   ↓
Predicción de Churn
```

---

##  Autor

**Wilbert Lora**

Proyecto académico de Machine Learning Supervisado.
