### EJERCICIO PARA CLASE.
#Máster Data Science.
#Este análisis no tiene ningun valor :)
#Se ha hecho para una práctica de Zenodo, no de análisis 

data <- read.csv("MentalHealth.csv")
m <- subset(data, sex==2)
h <- subset(data, sex==1)
m_menor20 <- subset(m, age<=20)
m_menor25 <- subset(m, age>=21 & age<=25)
m_menor30 <- subset(m, age>=26 & age<=30)
m_mayor30 <- subset(m, age>30)

media_m <- c(mean(m_menor20$health),mean(m_menor25$health),mean(m_menor30$health),mean(m_mayor30$health))

h_menor20 <- subset(h, age<=20)
h_menor25 <- subset(h, age>=21 & age<=25)
h_menor30 <- subset(h, age>=26 & age<=30)
h_mayor30 <- subset(h, age>30)

media_h <- c(mean(h_menor20$health),mean(h_menor25$health),mean(h_menor30$health),mean(h_mayor30$health))

## Se estudia la satisfacción con su salud dependiendo de la edad

# 1=Very dissatisfied
# 2=Dissatisfied
# 3=Neither satisfied nor dissatisfied
# 4=Satisfied
* 5=Verysatisfied

plot(media_m, col="red", pch=19,xlab='Edad',ylab='Satisfaccion')
points(media_h,col="blue",pch=12)