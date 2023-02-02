import numpy as np
import pandas as pd
import funzioni as fn
import matplotlib.pyplot as plt
from scipy import constants, fft, optimize

#importo il file csv
tab = pd.read_csv('pollution_us_2011_2013.csv')
#print(tab.columns)

#scelgo solo le colonne che mi interessano
tab1 = tab[['State Code','County Code', 'Site Num','Date Local', 'NO2 Mean']]

#5 stati che formano una regione
#codici: arizona=4, utha=49, new mexico=35, colorado=8, wyoming=56
#creo le tabelle dei singoli stati e salvo i file csv per poter lavorare
#sulle singole stazioni
pollAr = fn.stato(tab1, 4)
fn.csv_stato(pollAr, 'arizona')
pollUt = fn.stato(tab1, 49)
fn.csv_stato(pollUt, 'utah')
pollNM = fn.stato(tab1, 35)
fn.csv_stato(pollNM, 'new_mexico')
pollCol = fn.stato(tab1, 8)
fn.csv_stato(pollCol, 'colorado')
pollWy = fn.stato(tab1, 56)
fn.csv_stato(pollWy, 'wyoming')

#estraggo gli array con le date
ard = pollAr['Date Local'].values
utd = pollUt['Date Local'].values
nmd = pollNM['Date Local'].values
cold = pollCol['Date Local'].values
wyd = pollWy['Date Local'].values

#estraggo gli array con le medie di NO2
arm = pollAr['NO2 Mean'].values
utm = pollUt['NO2 Mean'].values
nmm = pollNM['NO2 Mean'].values
colm = pollCol['NO2 Mean'].values
wym = pollWy['NO2 Mean'].values
'''
#grafico stati
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(ard, arm, color='forestgreen')
ax[1].plot(utd, utm, color='darkorange')
ax[2].plot(nmd, nmm, color='mediumslateblue')
ax[3].plot(cold, colm, color='mediumturquoise')
ax[4].plot(wyd, wym, color='lightcoral')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in 5 stati confinanti')
plt.show()
'''
#analisi di Fourier dei dati di NO2 delle stazioni
#trasformate di fourier della serie temporale
artf = fft.rfft(arm)
uttf = fft.rfft(utm)
nmtf = fft.rfft(nmm)
coltf = fft.rfft(colm)
wytf = fft.rfft(wym)

#spettro di potenza
arsp = np.absolute(artf)**2
utsp = np.absolute(uttf)**2
nmsp = np.absolute(nmtf)**2
colsp = np.absolute(coltf)**2
wysp = np.absolute(wytf)**2

#freqenza
a = 0.5
arfr = a*fft.rfftfreq(artf.size, d=1)
utfr = a*fft.rfftfreq(uttf.size, d=1)
nmfr = a*fft.rfftfreq(nmtf.size, d=1)
colfr = a*fft.rfftfreq(coltf.size, d=1)
wyfr = a*fft.rfftfreq(wytf.size, d=1)
'''
#grafico spettro di potenza in funzione della frequenza
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(arfr[1:artf.size//2], arsp[1:artf.size//2], color='forestgreen')
ax[1].plot(utfr[1:uttf.size//2], utsp[1:uttf.size//2], color='darkorange')
ax[2].plot(nmfr[1:nmtf.size//2], nmsp[1:nmtf.size//2], color='mediumslateblue')
ax[3].plot(colfr[1:coltf.size//2], colsp[1:coltf.size//2], color='mediumturquoise')
ax[4].plot(wyfr[1:wytf.size//2], wysp[1:wytf.size//2], color='lightcoral')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
ax[3].set_yscale('log')
ax[3].set_xscale('log')
ax[4].set_yscale('log')
ax[4].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in 5 stati confinanti')
plt.show()
'''
#periodicità
#massimo dello spettro di potenza
armax = np.argmax(arsp[1:artf.size//2])+1
utmax = np.argmax(utsp[1:uttf.size//2])+1
nmmax = np.argmax(nmsp[1:nmtf.size//2])+1
colmax = np.argmax(colsp[1:coltf.size//2])+1
wymax = np.argmax(wysp[1:wytf.size//2])+1
'''
print('Arizona: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( arsp[armax], arfr[armax], int(1/arfr[armax])))
print('Utah: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( utsp[utmax], utfr[utmax], int(1/utfr[utmax])))
print('New Mexico: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( nmsp[nmmax], nmfr[nmmax], int(1/nmfr[nmmax])))
print('Colorado: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( colsp[colmax], colfr[colmax], int(1/colfr[colmax])))
print('Wyoming: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( wysp[wymax], wyfr[wymax], int(1/wyfr[wymax])))

fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(1/arfr[1:artf.size//2], arsp[1:artf.size//2], color='forestgreen')
ax[0].plot(1/arfr[armax], arsp[armax], 'o', color='darkgreen')
ax[1].plot(1/utfr[1:uttf.size//2], utsp[1:uttf.size//2], color='darkorange')
ax[1].plot(1/utfr[utmax], utsp[utmax], 'o', color='orangered')
ax[2].plot(1/nmfr[1:nmtf.size//2], nmsp[1:nmtf.size//2], color='mediumslateblue')
ax[2].plot(1/nmfr[nmmax], nmsp[nmmax], 'o', color='rebeccapurple')
ax[3].plot(1/colfr[1:coltf.size//2], colsp[1:coltf.size//2], color='mediumturquoise')
ax[3].plot(1/colfr[colmax], colsp[colmax], 'o', color='teal')
ax[4].plot(1/wyfr[1:wytf.size//2], wysp[1:wytf.size//2], color='lightcoral')
ax[4].plot(1/wyfr[wymax], wysp[wymax], 'o', color='firebrick')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
ax[3].set_yscale('log')
ax[3].set_xscale('log')
ax[4].set_yscale('log')
ax[4].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su periodo T [$d$] di NO2 in 5 stati confinanti')
plt.show()
'''
#filtro ai coefficienti di fourier selezionando solo le componenti che descrivono l'andamento generale in funzione del tempo (escludendo futtuazioni di breve periodo) e faccio la trasformata FFT inversa con coeff filtrati 
arf = fn.inv(arsp, 5e6, artf, arm)
utf = fn.inv(utsp, 5e6, uttf, utm)
nmf = fn.inv(nmsp, 5e6, nmtf, nmm)
colf = fn.inv(colsp, 5e6, coltf, colm)
wyf = fn.inv(wysp, 1e5, wytf, wym)
'''
#grafici di confronto tra segnale originale e il segnale filtrato
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(ard, arm, color='forestgreen')
ax[0].plot(ard, arf, color='darkgreen')
ax[1].plot(utd, utm, color='darkorange')
ax[1].plot(utd, utf, color='orangered')
ax[2].plot(nmd, nmm, color='mediumslateblue')
ax[2].plot(nmd, nmf, color='rebeccapurple')
ax[3].plot(cold, colm, color='mediumturquoise')
ax[3].plot(cold, colf, color='teal')
ax[4].plot(wyd, wym, color='lightcoral')
ax[4].plot(wyd, wyf, color='firebrick')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in 5 stati confinanti, dati originali e filtrati')
plt.show()
'''
#Analizzare andamento e caratteristiche di rumore della differenza fra i dati e le serie temporali filtrate
arr = arm - arf
utr = utm - utf
nmr = nmm - nmf
colr = colm - colf
wyr = wym - wyf
'''
#grafico rumori
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(ard, arr, color='forestgreen')
ax[1].plot(utd, utr, color='darkorange')
ax[2].plot(nmd, nmr, color='mediumslateblue')
ax[3].plot(cold, colr, color='mediumturquoise')
ax[4].plot(wyd, wyr, color='lightcoral')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
fig.suptitle('rumore della densità di NO2 [$\mu g/m^3$] al giorno [d] in 5 stati confinanti')
plt.show()
'''
arrtf = fft.rfft(arr)
utrtf = fft.rfft(utr)
nmrtf = fft.rfft(nmr)
colrtf = fft.rfft(colr)
wyrtf = fft.rfft(wyr)

arrsp = np.absolute(arrtf)**2
utrsp = np.absolute(utrtf)**2
nmrsp = np.absolute(nmrtf)**2
colrsp = np.absolute(colrtf)**2
wyrsp = np.absolute(wyrtf)**2

arrfr = a*fft.rfftfreq(arrtf.size, d=1)
utrfr = a*fft.rfftfreq(utrtf.size, d=1)
nmrfr = a*fft.rfftfreq(nmrtf.size, d=1)
colrfr = a*fft.rfftfreq(colrtf.size, d=1)
wyrfr = a*fft.rfftfreq(wyrtf.size, d=1)
'''
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(arrfr[1:arrtf.size//2], arrsp[1:arrtf.size//2], 'o', color='forestgreen')
ax[1].plot(utrfr[1:utrtf.size//2], utrsp[1:utrtf.size//2], 'o', color='darkorange')
ax[2].plot(nmrfr[1:nmrtf.size//2], nmrsp[1:nmrtf.size//2], 'o', color='mediumslateblue')
ax[3].plot(colrfr[1:colrtf.size//2], colrsp[1:colrtf.size//2], 'o', color='mediumturquoise')
ax[4].plot(wyrfr[1:wyrtf.size//2], wyrsp[1:wyrtf.size//2], 'o', color='lightcoral')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
ax[3].set_yscale('log')
ax[3].set_xscale('log')
ax[4].set_yscale('log')
ax[4].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] del rumore di NO2 in 5 stati confinanti')
plt.show()
'''
#sembrano essere tutti rumori bianchi

#fit
pstart = np.array([1, 1])
params1, params_covariance1 = optimize.curve_fit(fn.noise, arrfr[30:arrtf.size//2], arrsp[30:arrtf.size//2], p0=[pstart])
params2, params_covariance2 = optimize.curve_fit(fn.noise, utrfr[30:utrtf.size//2], utrsp[30:utrtf.size//2], p0=[pstart])
params3, params_covariance3 = optimize.curve_fit(fn.noise, nmrfr[30:nmrtf.size//2], nmrsp[30:nmrtf.size//2], p0=[pstart])
params4, params_covariance4 = optimize.curve_fit(fn.noise, colrfr[30:colrtf.size//2], colrsp[30:colrtf.size//2], p0=[pstart])
params5, params_covariance5 = optimize.curve_fit(fn.noise, wyrfr[30:wyrtf.size//2], wyrsp[30:wyrtf.size//2], p0=[pstart])

print('params arizona ', params1)
print('params_covariance arizona ', params_covariance1)
print('params utah', params2)
print('params_covariance utah ', params_covariance2)
print('params new mexico ', params3)
print('params_covariance new mexico ', params_covariance3)
print('params colorado ', params4)
print('params_covariance colorado ', params_covariance4)
print('params wyoming ', params3)
print('params_covariance wyoming ', params_covariance5)

y1=fn.noise(arrfr[1:arrtf.size//2], params1[0], params1[1])
y2=fn.noise(utrfr[1:utrtf.size//2], params2[0], params2[1])
y3=fn.noise(nmrfr[1:nmrtf.size//2], params3[0], params3[1])
y4=fn.noise(colrfr[1:colrtf.size//2], params4[0], params4[1])
y5=fn.noise(wyrfr[1:wyrtf.size//2], params5[0], params5[1])

#grafico fit e spettro
fig,ax = plt.subplots(5,1, figsize=(40,40))
ax[0].plot(arrfr[1:arrtf.size//2], arrsp[1:arrtf.size//2], 'o', color='forestgreen')
ax[1].plot(utrfr[1:utrtf.size//2], utrsp[1:utrtf.size//2], 'o', color='darkorange')
ax[2].plot(nmrfr[1:nmrtf.size//2], nmrsp[1:nmrtf.size//2], 'o', color='mediumslateblue')
ax[3].plot(colrfr[1:colrtf.size//2], colrsp[1:colrtf.size//2], 'o', color='mediumturquoise')
ax[4].plot(wyrfr[1:wyrtf.size//2], wyrsp[1:wyrtf.size//2], 'o', color='lightcoral')
ax[0].plot(arrfr[1:arrtf.size//2], y1, color='darkgreen')
ax[1].plot(utrfr[1:utrtf.size//2], y2, color='orangered')
ax[2].plot(nmrfr[1:nmrtf.size//2], y3, color='rebeccapurple')
ax[3].plot(colrfr[1:colrtf.size//2], y4, color='teal')
ax[4].plot(wyrfr[1:wyrtf.size//2], y5, color='firebrick')
ax[0].set_title('Arizona', loc='left', y=0.75, x=0.02)
ax[1].set_title('Utah', loc='left', y=0.75, x=0.02)
ax[2].set_title('New Mexico', loc='left', y=0.75, x=0.02)
ax[3].set_title('Colorado', loc='left', y=0.75, x=0.02)
ax[4].set_title('Wyoming', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
ax[3].set_yscale('log')
ax[3].set_xscale('log')
ax[4].set_yscale('log')
ax[4].set_xscale('log')
fig.suptitle('fit del rumore di NO2 in 5 stati confinanti')
plt.show()

'''
Alabama                      1.0
Arizona                      4.0
Arkansas                     5.0
California                   6.0
Colorado                     8.0
Connecticut                  9.0
Country Of Mexico           80.0
Delaware                    10.0
District Of Columbia        11.0
Florida                     12.0
Georgia                     13.0
Hawaii                      15.0
Idaho                       16.0
Illinois                    17.0
Indiana                     18.0
Iowa                        19.0
Kansas                      20.0
Kentucky                    21.0
Louisiana                   22.0
Maine                       23.0
Maryland                    24.0
Massachusetts               25.0
Minnesota                   27.0
Missouri                    29.0
Nevada                      32.0
New Jersey                  34.0
New Mexico                  35.0
New York                    36.0
North Carolina              37.0
North Dakota                38.0
Ohio                        39.0
Oklahoma                    40.0
Oregon                      41.0
Pennsylvania                42.0
Rhode Island                44.0
South Dakota                46.0
Texas                       48.0
Utah                        49.0
Virginia                    51.0
Washington                  53.0
Wyoming                     56.0
'''
