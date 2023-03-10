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
fn.tab_stato(tab1, 4, 'arizona')
fn.tab_stato(tab1, 49, 'utah')
fn.tab_stato(tab1, 35, 'new_mexico')
fn.tab_stato(tab1, 8, 'colorado')
fn.tab_stato(tab1, 56, 'wyoming')

#array con date e medie di no2
ard, arm = fn.stato(tab1, 4)
utd, utm = fn.stato(tab1, 49)
nmd, nmm = fn.stato(tab1, 35)
cold, colm = fn.stato(tab1, 8)
wyd, wym = fn.stato(tab1, 56)

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
fig.savefig('dati_5_stati.png')
plt.show()

#analisi di Fourier dei dati di NO2 delle stazioni
#trasformate di fourier della serie temporale
artf, arsp, arfr, armax = fn.trasf(arm)
uttf, utsp, utfr, utmax = fn.trasf(utm)
nmtf, nmsp, nmfr, nmmax = fn.trasf(nmm)
coltf, colsp, colfr, colmax = fn.trasf(colm)
wytf, wysp, wyfr, wymax = fn.trasf(wym)

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
fig.savefig('sp_fr_5_stati.png')
plt.show()

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
fig.savefig('sp_T_5_stati.png')
plt.show()

#filtro ai coefficienti di fourier selezionando solo le componenti che descrivono l'andamento generale in funzione del tempo (escludendo futtuazioni di breve periodo) e faccio la trasformata FFT inversa con coeff filtrati 
arf = fn.inv(arsp, 5e6, artf, arm)
utf = fn.inv(utsp, 5e6, uttf, utm)
nmf = fn.inv(nmsp, 5e6, nmtf, nmm)
colf = fn.inv(colsp, 5e6, coltf, colm)
wyf = fn.inv(wysp, 1e5, wytf, wym)

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
fig.savefig('filtro_5_stati.png')
plt.show()

#correlazione tra i vari stati
df = fn.correl(ard, utd, nmd, cold, wyd, arm, utm, nmm, colm, wym, 'AZ', 'UT', 'NM', 'CO', 'WY')
print('correlazione tra gli stati')
print(df.corr())

#Analizzare andamento e caratteristiche di rumore della differenza fra i dati e le serie temporali filtrate
arr = arm - arf
utr = utm - utf
nmr = nmm - nmf
colr = colm - colf
wyr = wym - wyf

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
fig.savefig('rumore_5_stati.png')
plt.show()

arrtf, arrsp, arrfr, arrmax = fn.trasf(arr)
utrtf, utrsp, utrfr, utrmax = fn.trasf(utr)
nmrtf, nmrsp, nmrfr, nmrmax = fn.trasf(nmr)
colrtf, colrsp, colrfr, colrmax = fn.trasf(colr)
wyrtf, wyrsp, wyrfr, wyrmax = fn.trasf(wyr)

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
fig.savefig('sp_rumore_5_stati.png')
plt.show()

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
fig.savefig('fit_5_stati.png')
plt.show()
