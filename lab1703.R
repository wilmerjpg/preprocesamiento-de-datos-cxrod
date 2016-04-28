entrada1 <- read.csv("entrada_1.csv", row.name = 1, header = TRUE)
plot(entrada1$X, entrada1$Y, col = entrada1$class)
model <- kmeans(entrada1[ ,1:2], centers = 4)
plot(entrada1$X, entrada1$Y, col = model$cluster)
points(model$centers[, c("X","Y")], col = 1:4, pch = 19, cex = 2)

entrada2 <- read.csv("entrada_2.csv", row.name = 1, header = TRUE)
model2 <- kmeans(entrada2[ ,1:2], centers = 4)
plot(entrada2$x, entrada2$y, col = model2$cluster)
points(model2$centers[, c("x","y")], col = 1:4, pch = 19, cex = 2)
model2$centers

centros = rbind(cbind(-50,50),cbind(60,-60), cbind(50,30),  cbind(-60,-50))
model2 <- kmeans(entrada2[ ,1:2], centers = centros)
plot(entrada2$x, entrada2$y, col = model2$cluster)
points(model2$centers[, c("x","y")], col = 1:4, pch = 19, cex = 2)


entrada3 <- read.csv("entrada_3.csv", row.name = 1, header = TRUE)
model3 <- kmeans(entrada3[ ,1:2], centers = 4)
plot(entrada3$x, entrada3$y, col = model3$cluster)
points(model3$centers[, c("x","y")], col = 1:4, pch = 19, cex = 2)
model3$centers


entrada4 <- read.csv("entrada_4.csv", row.name = 1, header = TRUE)
model4 <- kmeans(entrada4[ ,1:2], centers = 4)
plot(entrada4$x, entrada4$y, col = model4$cluster)
points(model4$centers[, c("x","y")], col = 1:4, pch = 19, cex = 2)
model4$centers

entrada4 <- rbind(entrada4, c(50,50,3))
model4 <- kmeans(entrada4[ ,1:2], centers = 4)
plot(entrada4$x, entrada4$y, col = model4$cluster)
points(model4$centers[, c("x","y")], col = 1:4, pch = 19, cex = 2)
model4$centers

#copia dataframe
entrada1.num = entrada1

entrada1.num$class <- NULL
#CONVERTIMOS EN MATRIZ
entrada1.num = as.matrix(entrada1.num)
#conseguimos la matriz de distancia
distancia1 = dist(entrada1.num)
cluster1 = hclust(distancia1, method = "single")
cluster1
#Endograma, dado el endrograma cortemos en altura h
plot(cluster1)
ct1 = cutree(cluster1, k = 4)

table(ct1, entrada1$class)

plot(entrada1$X, entrada1$Y, col = ct1)

ct1 = cutree(cluster1, h = 1)

table(ct1, entrada1$class)

plot(entrada1$X, entrada1$Y, col = ct1)

dendogram = as.dendrogram(cluster1)
plot(dendogram)

corte = cut(dendogram, h =2)$upper
plot(corte)

entrada3 <- read.csv("entrada_3.csv", row.name = 1, header = TRUE)
entrada3.num = entrada3

entrada3.num$class <- NULL

entrada3.num = as.matrix(entrada3.num)
#conseguimos la matriz de distancia
distancia3 = dist(entrada3.num)
cluster3 = hclust(distancia3, method = "single")
cluster3
#Endograma, dado el endrograma cortemos en altura h
plot(cluster3)
ct3 = cutree(cluster3, k = 4)

table(ct3, entrada3$class)

plot(entrada3$X, entrada3$Y, col = ct3)



entrada2 <- read.csv("entrada_2.csv", row.name = 1, header = TRUE)
entrada2.num = entrada2

entrada2.num$class <- NULL

entrada2.num = as.matrix(entrada2.num)
#conseguimos la matriz de distancia
distancia2 = dist(entrada2.num)
cluster2 = hclust(distancia2,method = "single")
cluster2
#Endograma, dado el endrograma cortemos en altura h
plot(cluster2)
ct2 = cutree(cluster2, k = 4)

table(ct2, entrada2$class)

plot(entrada2$X, entrada2$Y, col = ct2)

#Preprocedemaiento para df de 1000 registros, casi siempre size = 5%
#for n veces, con 30 veces esta bien
sub.df = df[sample(1:nrow(df), replace = false, size = 20), c("X","Y", "Class")]
kmedias.pre = kmeans(sub.df[,1:2],4)
centers = c(centers, kmedias.pre$centers)
#finn for

medias.verdadero = kmeans(df[,1:2], centers = kmedias.pre$centers)
kmeans()$center