# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 11:50:16 2016

@author: cesar
"""

import csv as csv 
import numpy as np
import re
#import os

#os.getcwd()
#os.chdir("../Escritorio")

csv_file_object = csv.reader(open('data.csv', 'rb')) 
header = csv_file_object.next()
data=[]
for row in csv_file_object:
    data.append(row)
data = np.array(data) #añadir dtype

#estandarizar renovar periodo
renovarPeriodo = data[0::,1]
renovarPeriodoTemp = []
for row in renovarPeriodo:
    row = row.lower()
    if re.search("pri",row):
        if re.search("14",row):
            row = '1-2014'
            renovarPeriodoTemp.append(row)
            continue
        if re.search("15",row):
            row = '1-2015'
            renovarPeriodoTemp.append(row)
            continue
        renovarPeriodoTemp.append('?')
        continue
    if re.search("seg",row):
        if re.search("14",row):
            row = '2-2014'
            renovarPeriodoTemp.append(row)
            continue
        if re.search("15",row):
            row = '2-2015'
            renovarPeriodoTemp.append(row)
            continue
        renovarPeriodoTemp.append('?')
        continue
    if re.search("i-",row):
        if re.search("14",row):
            row = '1-2014'
        if re.search("15",row):
            row = '1-2015'
        renovarPeriodoTemp.append(row)
        continue
    if re.search("ii",row):
        if re.search("14",row):
            row = '2-2014'
        if re.search("15",row):
            row = '2-2015'
        renovarPeriodoTemp.append(row)
        continue
    if re.search("2014",row):
        if re.search("02",row) or re.search("-2",row):
            row="2-2014"
            renovarPeriodoTemp.append(row)
            continue
        if re.search("2015",row):
            row="2-2014"
            renovarPeriodoTemp.append(row)
            continue
        row = "1-2014"
        renovarPeriodoTemp.append(row)
        continue
    if re.search("2015",row):
        if re.search("02",row) or re.search("-2",row):
            row="2-2015"
            renovarPeriodoTemp.append(row)
            continue
        if re.search("2016",row):
            row="2-2015"
            renovarPeriodoTemp.append(row)
            continue
        row = "1-2015"
        renovarPeriodoTemp.append(row)
        continue
    renovarPeriodoTemp.append('?')
renovarPeriodo = np.array(renovarPeriodoTemp)
data[0::,1] = renovarPeriodo

#estandarizar fechas de nacimiento
fechaNacimiento = data[0::,3]
fechaNAcimientoTemp = []
falta = []
for row in fechaNacimiento:
    row=row.replace("-","/")
    row=row.replace(" ","/")
    if re.search("(([1-2][0-9])|0?[1-9]|30|31)\/(0?[1-9]|10|11|12)\/(19[0-9][0-9])",row):
        temp=row.split("/")
        row=temp[0].zfill(2)+"/"+temp[1].zfill(2)+"/"+temp[2]       
        fechaNAcimientoTemp.append(row)
        continue
    if re.search("(([1-2][0-9])|0?[1-9]|30|31)\/(0?[1-9]|10|11|12)\/([0-9][0-9])",row):
        temp=row.split("/")
        row=temp[0]+"/"+temp[1]+"/19"+temp[2]
        if len(temp[2])>2:
            row= '?'
        fechaNAcimientoTemp.append(row)
        continue
    falta.append(row)
    row = str(row).zfill(8)
    if re.search("19[0-9][0-9]",row[4:8]):
        row=row[0:2]+"/"+row[2:4]+"/"+row[4:8]
        fechaNAcimientoTemp.append(row)
    else:
        row=row[4:6]+"/"+row[6:8]+"/"+row[0:4]
        fechaNAcimientoTemp.append(row)
fechaNacimiento = np.array(fechaNAcimientoTemp)
data[0::,3] = fechaNacimiento

#estandarizar edad
edad = data[0::,4]
edadTemp = []
for row in edad:
    edadTemp.append(re.sub("\D","",row))
edad = np.array(edadTemp)
data[0::,4] = edad

#estandarizar estadoCivil - 0 soltero - 1 casadp - 2 viudo - 3 unido
estadoCivil = data[0::,5]
estadoCivilTemp = []
for row in estadoCivil:
    row = row.lower()
    if re.search("soltero", row):
        estadoCivilTemp.append(0)
        continue
    if re.search("casado", row):
        estadoCivilTemp.append(1)
        continue
    if re.search("viudo", row):
        estadoCivilTemp.append(2)
        continue
    if re.search("unido", row):
        estadoCivilTemp.append(3)
        continue
estadoCivil = np.array(estadoCivilTemp)
data[0::,5] = estadoCivil  
    
#estadarizar sexo - 0 masculino - 1 femenino
sexo = data[0::,6]
sexoTemp = []
for row in sexo:
    row = row.lower()
    if re.search("masculino", row):
        sexoTemp.append(0)
        continue
    if re.search("femenino", row):
        sexoTemp.append(1)
        continue
sexo = np.array(sexoTemp)
data[0::,6] = sexo  

#estadarizar escuela - 0 enfermeria - 1 bionalisis
escuela = data[0::,7]
escuelaTemp = []
for row in escuela:
    row = row.lower()
    if re.search("bio", row):
        escuelaTemp.append(0)
        continue
    if re.search("enf", row):
        escuelaTemp.append(1)
        continue
escuela = np.array(escuelaTemp)
data[0::,7] = escuela 

#estadarizar modalidadIngreso - 0 Convenio Intitucional - 1 OPSU - 2 Prueba Interna - 3 Convenio Interno
modalidadIngreso = data[0::,9]
modalidadIngresoTemp = []
falta = []
for row in modalidadIngreso:
    row = row.lower()
    if re.search("institucional", row):
        modalidadIngresoTemp.append(0)
        continue
    if re.search("opsu", row):
        modalidadIngresoTemp.append(1)
        continue
    if re.search("interna", row):
        modalidadIngresoTemp.append(2)
        continue
    if re.search("interno", row):
        modalidadIngresoTemp.append(3)
        continue
    falta.append(row)
modalidadIngreso = np.array(modalidadIngresoTemp)
data[0::,9] = modalidadIngreso

#estandarizar semestreActual
semestreActual = data[0::,10]
semestreActualTemp = []
for row in semestreActual:
    semestreActualTemp.append(re.sub("\D","",row))
semestreActual = np.array(semestreActualTemp)
data[0::,10] = semestreActual

#estandarizar cambioDireccion
cambioDireccion = data[0::,11]
motivoCambioDireccion = data[0::,12]
cambioDireccionTemp = []
for i in range(0,len(data)):
    row1 = cambioDireccion[i].lower()
    if re.search("no", row1):
        cambioDireccionTemp.append('NA')
        continue
    if re.search("si", row1):
        cambioDireccionTemp.append(motivoCambioDireccion[i].lower())
        continue
cambioDireccion = np.array(cambioDireccionTemp)
data[0::,11] = cambioDireccion

#estandarizar materiasInscritasSemAnterior
materiasInscritasSemAnterior = data[0::,13]
materiasAprovadasSemAnterior = data[0::,14]
materiasRetiradasSemAnterior = data[0::,15]
materiasReprobadasSemAnterior = data[0::,16]
materiasInscritasSemAnteriorTemp = []
materiasAprovadasSemAnteriorTemp = []
materiasRetiradasSemAnteriorTemp = []
materiasReprobadasSemAnteriorTemp = []

for i in range(0,len(data)):
    row1 = re.sub("\D","",materiasInscritasSemAnterior[i])
    row2 = re.sub("\D","",materiasAprovadasSemAnterior[i])
    row3 = re.sub("\D","",materiasRetiradasSemAnterior[i])
    row4 = re.sub("\D","",materiasReprobadasSemAnterior[i])
    if int(row2)>int(row1):
        materiasAprovadasSemAnteriorTemp.append(row1)
        row2 = row1
    else:
        materiasAprovadasSemAnteriorTemp.append(row2)
    if int(row3)>int(row1):
        materiasRetiradasSemAnteriorTemp.append(row1)
        row3 = row1
    else:
        materiasRetiradasSemAnteriorTemp.append(row3)
    if int(row4)>int(row1):
        materiasReprobadasSemAnteriorTemp.append(row1)
        row4 = row1
    else:
        materiasReprobadasSemAnteriorTemp.append(row4)
    materiasInscritasSemAnteriorTemp.append(str(int(row2)+int(row3)+int(row4)))
materiasInscritasSemAnterior = np.array(materiasInscritasSemAnteriorTemp)
data[0::,13] = materiasInscritasSemAnterior
materiasAprovadasSemAnterior = np.array(materiasAprovadasSemAnteriorTemp)
data[0::,14] = materiasAprovadasSemAnterior
materiasRetiradasSemAnterior = np.array(materiasRetiradasSemAnteriorTemp)
data[0::,15] = materiasRetiradasSemAnterior
materiasReprobadasSemAnterior = np.array(materiasReprobadasSemAnteriorTemp)
data[0::,16] = materiasReprobadasSemAnterior

#Estadarizar promedioPonderadoAprobado
promedioPonderadoAprobado = data[0::,17]
promedioPonderadoAprobadoTemp = []
for row in promedioPonderadoAprobado:
    if re.search('\d{1,2}\.\d+',row):
        if row.find('.') == 1:
            row = '0'+row[0]+'.'+row[2::]
            row = row.ljust(6,'0')
            row = row[0:6]
        else:
            row = row[0:2]+'.'+row[3::]
            row = row.ljust(6,'0')
            row = row[0:6]
        promedioPonderadoAprobadoTemp.append(row)
        continue
    row = re.sub("\D","",row)
    if int(row[0:2])>19:
        row = '0'+row[0]+'.'+row[1::]
        row = row.ljust(6,'0')
        row = row[0:6]
        promedioPonderadoAprobadoTemp.append(row)
    else:
        row = row[0:2]+'.'+row[2::]
        row = row.ljust(6,'0')
        row = row[0:6]
        promedioPonderadoAprobadoTemp.append(row)
promedioPonderadoAprobado = np.array(promedioPonderadoAprobadoTemp)
data[0::,17] = promedioPonderadoAprobado

#Estadarizar eficiencia
eficiencia = data[0::,18]
eficienciaTemp = []
for row in eficiencia:
    if row == '1' or row == '1000' or row == '10000':
        row = '1'+'.'+'0000'
        eficienciaTemp.append(row)
        continue
    if re.search('0\.\d+',row):
        row = row.ljust(6,'0')
        row = row[0:6]
        eficienciaTemp.append(row)
        continue
    row = re.sub("\D","",row)
    row = '0.'+row[0::]
    row = row.ljust(6,'0')
    row = row[0:6]
    eficienciaTemp.append(row)
eficiencia = np.array(eficienciaTemp)
data[0::,18] = eficiencia

#estandarizar cambioDireccion
motivoReprobado = data[0::,19]
motivoReprobadoTemp = []
for row in motivoReprobado:
    row = row.lower()
    if row == '':
        motivoReprobadoTemp.append('NA')
    else:
        motivoReprobadoTemp.append(row)
motivoReprobado = np.array(motivoReprobadoTemp)
data[0::,19] = motivoReprobado

#estandarizar tesisPasantias
tesisPasantias = data[0::,21]
cantidadTesisPasantias = data[0::,22]
tesisPasantiasTemp = []
for i in range(0,len(data)):
    row = tesisPasantias[i].lower()
    if re.search("no", row):
        tesisPasantiasTemp.append('0')
        continue
    if re.search("si", row):
        row1 = cantidadTesisPasantias[i].lower()
        if re.search("primera", row1):
            tesisPasantiasTemp.append('1')
            continue
        if re.search("segunda", row1):
            tesisPasantiasTemp.append('2')
            continue
        tesisPasantiasTemp.append('3')
tesisPasantias = np.array(tesisPasantiasTemp)
data[0::,21] = tesisPasantias

#estandarizar procedencia
procedencia = data[0::,23]
procedenciaTemp = []
for row in procedencia:
    row = row.lower()
    if row == 'municipio libertador caracas':
        procedenciaTemp.append('0')
        continue
    if row == 'municipio sucre':
        procedenciaTemp.append('1')
        continue
    if row == 'guarenas - guatire':
        procedenciaTemp.append('2')
        continue
    if row == 'municipio baruta':
        procedenciaTemp.append('3')
        continue
    if row == 'altos mirandinos':
        procedenciaTemp.append('4')
        continue
    if row == 'municipio el hatillo':
        procedenciaTemp.append('5')
        continue
    if row == 'municipio chacao':
        procedenciaTemp.append('6')
        continue
    if row == 'valles del tuy':
        procedenciaTemp.append('7')
        continue
    if row == 'aragua':
        procedenciaTemp.append('8')
        continue
    if row == 'apure':
        procedenciaTemp.append('9')
        continue
    if row == 'táchira':
        procedenciaTemp.append('10')
        continue
    if row == 'vargas':
        procedenciaTemp.append('11')
        continue
    if row == 'monagas':
        procedenciaTemp.append('12')
        continue
    if row == 'portuguesa':
        procedenciaTemp.append('13')
        continue
    if row == 'nueva esparta':
        procedenciaTemp.append('14')
        continue
    if row == 'trujillo':
        procedenciaTemp.append('15')
        continue
    if row == 'bolívar':
        procedenciaTemp.append('16')
        continue
    if row == 'barinas':
        procedenciaTemp.append('17')
        continue
    if row == 'sucre':
        procedenciaTemp.append('18')
        continue
    if row == 'anzoategui':
        procedenciaTemp.append('19')
        continue
    if row == 'barlovento':
        procedenciaTemp.append('20')
        continue
    if row == 'mérida':
        procedenciaTemp.append('21')
        continue
    if row == 'delta amacuro':
        procedenciaTemp.append('22')
        continue
    if row == 'lara':
        procedenciaTemp.append('23')
        continue
    if row == 'yaracuy':
        procedenciaTemp.append('24')
        continue
    if row == 'guárico':
        procedenciaTemp.append('25')
        continue
procedencia = np.array(procedenciaTemp)
data[0::,23] = procedencia

#estandarizar lugarResidencia
lugarResidencia = data[0::,24]
lugarResidenciaTemp = []
for row in lugarResidencia:
    row = row.lower()
    if row == 'municipio sucre':
        lugarResidenciaTemp.append('1')
        continue
    if row == 'guarenas - guatire':
        lugarResidenciaTemp.append('2')
        continue
    if row == 'municipio baruta':
        lugarResidenciaTemp.append('3')
        continue
    if row == 'altos mirandinos':
        lugarResidenciaTemp.append('4')
        continue
    if row == 'municipio el hatillo':
        lugarResidenciaTemp.append('5')
        continue
    if row == 'municipio chacao':
        lugarResidenciaTemp.append('6')
        continue
    if row == 'valles del tuy':
        lugarResidenciaTemp.append('7')
        continue
    lugarResidenciaTemp.append('0') 
lugarResidencia = np.array(lugarResidenciaTemp)
data[0::,24] = lugarResidencia

#estandarizar viveCon
viveCon = data[0::,25]
viveConTemp = []
for row in viveCon:
    row = row.lower()
    if re.search('ambos padres',row):
        viveConTemp.append('0')
        continue
    if re.search('madre',row) or re.search('mamá',row):
        viveConTemp.append('1')
        continue
    if re.search('padre',row):
        viveConTemp.append('2')
        continue
    if re.search('esposo',row):
        viveConTemp.append('4')
        continue
    if re.search('familiares paternos',row):
        viveConTemp.append('5')
        continue
    if re.search('familiares maternos',row):
        viveConTemp.append('6')
        continue
    if re.search('sola',row) or re.search('solo',row):
        viveConTemp.append('7')
        continue
    if re.search('herman',row):
        viveConTemp.append('8')
        continue
    if re.search('amig',row):
        viveConTemp.append('9')
        continue
    viveConTemp.append('3')
viveCon = np.array(viveConTemp)
data[0::,25] = viveCon

#estandarizar tipoVivienda
tipoVivienda = data[0::,26]
tipoViviendaTemp = []
falta = []
for row in tipoVivienda:
    row = row.lower()
    if re.search('edifico',row):
        tipoViviendaTemp.append('0')
        continue
    if re.search('quinta',row):
        tipoViviendaTemp.append('1')
        continue
    if re.search('barrio',row):
        tipoViviendaTemp.append('2')
        continue
    if re.search('alquilada',row):
        tipoViviendaTemp.append('3')
        continue
    if re.search('casa',row):
        tipoViviendaTemp.append('4')
        continue
    tipoViviendaTemp.append('5')
    falta.append(row) 
tipoVivienda = np.array(tipoViviendaTemp)
data[0::,26] = tipoVivienda

#estandarizar matrimonio
matrimonio = data[0::,29]
matrimonioTemp = []
for row in matrimonio:
    row = row.lower()
    if re.search("no", row):
        matrimonioTemp.append('0')
        continue
    if re.search("si", row):
        matrimonioTemp.append('1')
        continue
matrimonio = np.array(matrimonioTemp)
data[0::,29] = matrimonio

#estandarizar otroBeneficiod
otroBeneficiod = data[0::,30]
motivoOtroBeneficiod = data[0::,31]
otroBeneficiodTemp = []
for i in range(0,len(data)):
    row1 = otroBeneficiod[i].lower()
    if re.search("no", row1):
        otroBeneficiodTemp.append('NA')
        continue
    if re.search("si", row1):
        otroBeneficiodTemp.append(motivoOtroBeneficiod[i].lower())
        continue
otroBeneficiod = np.array(otroBeneficiodTemp)
data[0::,30] = otroBeneficiod

#estandarizar ingresoExtra
ingresoExtra = data[0::,32]
motivoIngresoExtra = data[0::,33]
ingresoExtraTemp = []
for i in range(0,len(data)):
    row1 = ingresoExtra[i].lower()
    if re.search("no", row1):
        ingresoExtraTemp.append('NA')
        continue
    if re.search("si", row1):
        ingresoExtraTemp.append(motivoIngresoExtra[i].lower())
        continue
ingresoExtra = np.array(ingresoExtraTemp)
data[0::,32] = ingresoExtra

#estandarizar aporteREsponsableEconomico
aporteREsponsableEconomico = data[0::,35]
aporteREsponsableEconomicoTemp = []
for row in aporteREsponsableEconomico:
    row = row.lower()
    if row == 'na':
        aporteREsponsableEconomicoTemp.append('0')
    else:
        aporteREsponsableEconomicoTemp.append(row)
aporteREsponsableEconomico = np.array(aporteREsponsableEconomicoTemp)
data[0::,35] = aporteREsponsableEconomico

#estandarizar aporteFamiliarAmigo
aporteFamiliarAmigo = data[0::,36]
aporteFamiliarAmigoTemp = []
for row in aporteFamiliarAmigo:
    row = row.lower()
    if row == 'na':
        aporteFamiliarAmigoTemp.append('0')
    else:
        aporteFamiliarAmigoTemp.append(row)
aporteFamiliarAmigo = np.array(aporteFamiliarAmigoTemp)
data[0::,36] = aporteFamiliarAmigo

#estandarizar aporteIngresoDestajo
aporteIngresoDestajo = data[0::,37]
aporteIngresoDestajoTemp = []
for row in aporteIngresoDestajo:
    row = row.lower()
    if row == 'na':
        aporteIngresoDestajoTemp.append('0')
    else:
        aporteIngresoDestajoTemp.append(row)
aporteIngresoDestajo = np.array(aporteIngresoDestajoTemp)
data[0::,37] = aporteIngresoDestajo

#estandarizar alimentacion
alimentacion = data[0::,39]
alimentacionTemp = []
for row in alimentacion:
    row = row.lower()
    if row == 'na':
        alimentacionTemp.append('0')
    else:
        alimentacionTemp.append(row)
alimentacion = np.array(alimentacionTemp)
data[0::,39] = alimentacion

#estandarizar transporte
transporte = data[0::,40]
transporteTemp = []
for row in transporte:
    row = row.lower()
    if row == 'na':
        transporteTemp.append('0')
    else:
        transporteTemp.append(row)
transporte = np.array(transporteTemp)
data[0::,40] = transporte

#estandarizar gastosMedicos
gastosMedicos = data[0::,41]
gastosMedicosTemp = []
for row in gastosMedicos:
    row = row.lower()
    if row == 'na':
        gastosMedicosTemp.append('0')
    else:
        gastosMedicosTemp.append(row)
gastosMedicos = np.array(transporteTemp)
data[0::,41] = gastosMedicos

#estandarizar gastosOdontologicos
gastosOdontologicos = data[0::,42]
gastosOdontologicosTemp = []
for row in gastosOdontologicos:
    row = row.lower()
    if row == 'na':
        gastosOdontologicosTemp.append('0')
    else:
        gastosOdontologicosTemp.append(row)
gastosOdontologicos = np.array(gastosOdontologicosTemp)
data[0::,42] = gastosOdontologicos

#estandarizar gastospersonales
gastospersonales = data[0::,43]
gastospersonalesTemp = []
for row in gastospersonales:
    row = row.lower()
    if row == 'na':
        gastospersonalesTemp.append('0')
    else:
        gastospersonalesTemp.append(row)
gastospersonales = np.array(gastospersonalesTemp)
data[0::,43] = gastospersonales

#estandarizar gastosResidenciaAlquiler
gastosResidenciaAlquiler = data[0::,44]
otroResidenciaAlquiler = data[0::,27]
gastosResidenciaAlquilerTemp = []
for i in range(0,len(data)):
    row1 = re.sub('\D','',gastosResidenciaAlquiler[i].lower())
    row2 = re.sub('\D','',otroResidenciaAlquiler[i].lower())
    if row1=='':
        if row2=='':
            gastosResidenciaAlquilerTemp.append('0')
        else:
            gastosResidenciaAlquilerTemp.append(row2)
        continue
    else:
        gastosResidenciaAlquilerTemp.append(row1)
        continue
gastosResidenciaAlquiler = np.array(gastosResidenciaAlquilerTemp)
data[0::,44] = gastosResidenciaAlquiler

#estandarizar gastosMaterialesEstudio
gastosMaterialesEstudio = data[0::,45]
gastosMaterialesEstudioTemp = []
for row in gastosMaterialesEstudio:
    row = row.lower()
    if row == 'na':
        gastosMaterialesEstudioTemp.append('0')
    else:
        gastosMaterialesEstudioTemp.append(row)
gastosMaterialesEstudio = np.array(gastosMaterialesEstudioTemp)
data[0::,45] = gastosMaterialesEstudio

#estandarizar gastosRecreacion
gastosRecreacion = data[0::,46]
gastosRecreacionTemp = []
for row in gastosRecreacion:
    row = row.lower()
    if row == 'na':
        gastosRecreacionTemp.append('0')
    else:
        gastosRecreacionTemp.append(row)
gastosRecreacion = np.array(gastosRecreacionTemp)
data[0::,46] = gastosRecreacion

#estandarizar gastosOtros
gastosOtros = data[0::,47]
gastosOtrosTemp = []
for row in gastosOtros:
    row = row.lower()
    if row == 'na':
        gastosOtrosTemp.append('0')
    else:
        gastosOtrosTemp.append(row)
gastosOtros = np.array(gastosOtrosTemp)
data[0::,47] = gastosOtros

#estandarizar responsableEconimico
responsableEconimico = data[0::,49]
responsableEconimicoTemp = []
falta = []
for row in responsableEconimico:
    row = row.lower()
    if re.search('usted mismo',row) or re.search('ninguno',row):
        responsableEconimicoTemp.append('0')
        continue
    if re.search('madre',row) or re.search('mamá',row):
        responsableEconimicoTemp.append('1')
        continue
    if re.search('padre',row):
        responsableEconimicoTemp.append('2')
        continue
    if re.search('ambos padres',row):
        responsableEconimicoTemp.append('3')
        continue
    if re.search('esposo',row) or re.search('cónyugue',row):
        responsableEconimicoTemp.append('4')
        continue
    responsableEconimicoTemp.append('5')
    falta.append(row)
responsableEconimico = np.array(responsableEconimicoTemp)
data[0::,49] = responsableEconimico

#estandarizar responsableVivienda
responsableVivienda = data[0::,54]
responsableViviendaTemp = []
for row in responsableVivienda:
    row = re.sub("\D","",row)
    if row == '':
        responsableViviendaTemp.append('0')
    else:
        responsableViviendaTemp.append(row)
responsableVivienda = np.array(responsableViviendaTemp)
data[0::,54] = responsableVivienda

#estandarizar responsableTransporte
responsableTransporte = data[0::,56]
responsableTransporteTemp = []
for row in responsableTransporte:
    row = re.sub("\D","",row)
    responsableTransporteTemp.append(row)
responsableTransporte = np.array(responsableTransporteTemp)
data[0::,56] = responsableTransporte

#estandarizar responsableGastosMedicos
responsableGastosMedicos = data[0::,57]
responsableGastosMedicosTemp = []
for row in responsableGastosMedicos:
    row = row[0:row.find('.')]
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosMedicosTemp.append('0')
    else:
        responsableGastosMedicosTemp.append(row)
responsableGastosMedicos = np.array(responsableGastosMedicosTemp)
data[0::,57] = responsableGastosMedicos

#estandarizar responsableGastosOdontologicos
responsableGastosOdontologicos = data[0::,58]
responsableGastosOdontologicosTemp = []
for row in responsableGastosOdontologicos:
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosOdontologicosTemp.append('0')
    else:
        responsableGastosOdontologicosTemp.append(row)
responsableGastosOdontologicos = np.array(responsableGastosOdontologicosTemp)
data[0::,58] = responsableGastosOdontologicos

#estandarizar responsableGastosEducativos
responsableGastosEducativos = data[0::,59]
responsableGastosEducativosTemp = []
for row in responsableGastosEducativos:
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosEducativosTemp.append('0')
    else:
        responsableGastosEducativosTemp.append(row)
responsableGastosEducativos = np.array(responsableGastosEducativosTemp)
data[0::,59] = responsableGastosEducativos

#estandarizar responsableGastosServicios
responsableGastosServicios = data[0::,60]
responsableGastosServiciosTemp = []
for row in responsableGastosServicios:
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosServiciosTemp.append('0')
    else:
        responsableGastosServiciosTemp.append(row)
responsableGastosServicios = np.array(responsableGastosServiciosTemp)
data[0::,60] = responsableGastosServicios

#estandarizar responsableGastosCondominio
responsableGastosCondominio = data[0::,61]
responsableGastosCondominioTemp = []
for row in responsableGastosCondominio:
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosCondominioTemp.append('0')
    else:
        responsableGastosCondominioTemp.append(row)
responsableGastosCondominio = np.array(responsableGastosCondominioTemp)
data[0::,61] = responsableGastosCondominio

#estandarizar responsableGastosOtros
responsableGastosOtros = data[0::,62]
responsableGastosOtrosTemp = []
for row in responsableGastosOtros:
    row = re.sub("\D","",row)
    if row == '':
        responsableGastosOtrosTemp.append('0')
    else:
        responsableGastosOtrosTemp.append(row)
responsableGastosOtros = np.array(responsableGastosOtrosTemp)
data[0::,62] = responsableGastosOtros


#estandarizar ResponsableIngresos
responsableIngresos = data[0::,51]
responsableIngresosTemp = []
falta = []
for row in responsableIngresos:
    row = re.sub("\s","",row)
    if re.search(',', row) or re.search("\.",row):
        if re.search('bs', row):
            responsableIngresosTemp.append('16000')
            continue
        if re.search('\d+\.\d{1,2}',row):
            row = re.sub('\D','',row)
            responsableIngresosTemp.append(row[0:row.find('.')])
            continue
        row = re.sub('\D','',row)
        responsableIngresosTemp.append(row[0:(len(row)-2)])
        continue
    row = re.sub('\D','',row)
    responsableIngresosTemp.append(row)
    
#estandarizar ResponsableIngresosOtros
ResponsableIngresosOtros = data[0::,52]
ResponsableIngresosOtrosTemp = []
falta = []
for row in ResponsableIngresosOtros:
    row = re.sub("\s","",row)
    if re.search("\.",row):
        ResponsableIngresosOtrosTemp.append(row[0:row.find('.')])
        continue
    row = re.sub('\D','',row)
    if row == '':
        ResponsableIngresosOtrosTemp.append('0')
        continue
    ResponsableIngresosOtrosTemp.append(row)

responsableIngresoTotal = []    
for i in range(0,190):
    responsableIngresoTotal.append(str(int(responsableIngresosTemp[i])+int(ResponsableIngresosOtrosTemp[i])))
responsableIngresoTotal = np.array(responsableIngresoTotal)
data[0::,53] = responsableIngresoTotal

delete = np.s_[0,12,22,27,28,31,33,38,48,51,52,63]
data = np.delete(data, delete, 1)

newHeader = ['renovarPeriodo','cedulaIdentidad','fechaNacimiento','edad','estadoCivil','sexo','escuela','anoIngreso','modalidadIngreso','semestreActual','cambioDirecion','materiasInscritasSemAnterior','materiasAprovadasSemAnterior','materiasRetiradasSemAnterior','materiasReprobadasSemAnterior','promedioPonderadoAprobado','eficiencia','motivoReprobado','materiasInscritasSemActual','tesisPasantias','procedencia','lugarResidencia','viveCon','tipoVivienda','matrimonio','otroBeneficio','ingresoExtra','montoBeca','aporteResponsableEconomico','aporteRFamiliarAmigo','aporteIngresoDestajo','alimentacion','transporte','gastosMedicos','gastosOdontologicos','gastospersonales','gastosResidenciaAlquiler','gastosMaterialesEstudio','gastosRecreacion','gastosOtros','responsableEconimico','cargaFamiliar','responsableIngresoTotal','responsableVivienda','responsableAlimentacion','responsableTransporte','responsableGastosMedicos','responsableGastosOdontologicos','responsableGastosEducativos','responsableGastosServicios','responsableGastosCondominio','responsableGastosOtros','calidadServOBE','sugerenciasServOBE']
output_file = open("minable.csv", "wb")
output_file_file_object = csv.writer(output_file)
output_file_file_object.writerow(newHeader)
for row in data:
    output_file_file_object.writerow(row)
output_file.close()

