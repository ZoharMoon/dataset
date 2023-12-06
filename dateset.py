from datasets import load_dataset
import numpy as np

# Cargar el conjunto de datos
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición de entrenamiento
data = dataset["train"]

# Suponiendo que las características están presentes en el conjunto de datos
edades = data['age']  # 'age': Edad del paciente (años)
anaemia = data['has_anaemia']  # 'has_anaemia': Anemia (booleano)
presion_arterial_alta = data['has_high_blood_pressure']  # 'has_high_blood_pressure': Presión arterial alta (booleano)
cpk = data['creatinine_phosphokinase_concentration_in_blood']  # 'creatinine_phosphokinase_concentration_in_blood': CPK (mcg/L)
diabetes = data['has_diabetes']  # 'has_diabetes': Diabetes (booleano)
fraccion_eyeccion = data['heart_ejection_fraction']  # 'heart_ejection_fraction': Fracción de eyección (porcentaje)
plaquetas = data['platelets_concentration_in_blood']  # 'platelets_concentration_in_blood': Plaquetas (kiloplaquetas/mL)
sexo = data['is_male']  # 'is_male': Sexo (mujer u hombre, binario)
creatinina_serica = data['serum_creatinine_concentration_in_blood']  # 'serum_creatinine_concentration_in_blood': Creatinina sérica (mg/dL)
sodio_serico = data['serum_sodium_concentration_in_blood']  # 'serum_sodium_concentration_in_blood': Sodio sérico (mEq/L)
fumar = data['is_smoker']  # 'is_smoker': Fumar (booleano)
tiempo = data['days_in_study']  # 'days_in_study': Tiempo (período de seguimiento, días)
fallecimiento = data['is_dead']  # 'is_dead': Evento de fallecimiento (booleano)

# Convertir cada lista de características a arreglos de NumPy
edades_np = np.array(edades)

# Calcular el promedio de la edad
promedio_edad = np.mean(edades_np)

# Imprimir el resultado
print(f"Promedio de edad de las personas participantes en el estudio: {promedio_edad:.2f} años")
