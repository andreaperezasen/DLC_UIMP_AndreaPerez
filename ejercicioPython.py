### EJERCICIO PARA CLASE.
#Máster Data Science.
#Este análisis no tiene ningun valor :)
#Se ha hecho para una práctica de Zenodo, no de análisis 


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("MentalHealth.csv")
m = data[data["sex"] == 2]
h = data[data["sex"] == 1]

m_menor20 = m[m["age"] <= 20]
m_menor25 = m[(m["age"] >= 21) & (m["age"] <= 25)]
m_menor30 = m[(m["age"] >= 26) & (m["age"] <= 30)]
m_mayor30 = m[m["age"] > 30]

media_m = [m_menor20["health"].mean(), m_menor25["health"].mean(), 
           m_menor30["health"].mean(), m_mayor30["health"].mean()]

h_menor20 = h[h["age"] <= 20]
h_menor25 = h[(h["age"] >= 21) & (h["age"] <= 25)]
h_menor30 = h[(h["age"] >= 26) & (h["age"] <= 30)]
h_mayor30 = h[h["age"] > 30]

media_h = [h_menor20["health"].mean(), h_menor25["health"].mean(), 
           h_menor30["health"].mean(), h_mayor30["health"].mean()]

x_labels = ["<=20", "21-25", "26-30", ">30"]

## Se estudia la satisfacción con su salud dependiendo de la edad

# 1=Very dissatisfied
# 2=Dissatisfied
# 3=Neither satisfied nor dissatisfied
# 4=Satisfied
# 5=Verysatisfied

# Set the width of each bar
bar_width = 0.35

# Set the positions of the bars on the x-axis
r1 = np.arange(len(media_m))
r2 = [x + bar_width for x in r1]

# Create the multiple bar chart
plt.bar(r1, media_m, color="red", width=bar_width, edgecolor="white", label="Females")
plt.bar(r2, media_h, color="blue", width=bar_width, edgecolor="white", label="Males")

# Add x-axis and y-axis labels and a title to the plot
plt.xlabel("Age")
plt.ylabel("Health Satisfaction")
plt.title("Health Satisfaction by Age and Sex")

# Add x-axis tick labels
plt.xticks([r + bar_width/2 for r in range(len(media_m))], x_labels)

# Add a legend to the plot
plt.legend()

plt.savefig('mentalhealthsatisfacion.png')

# Show the plot
plt.show()
