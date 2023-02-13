import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import constants, fft, optimize
import funzioni as fn
 
#estraggo le tabelle degli stati dai file csv
ar = pd.read_csv('arizona.csv')
ut = pd.read_csv('utah.csv')
wy = pd.read_csv('wyoming.csv')
col = pd.read_csv('colorado.csv')
nm = pd.read_csv('new_mexico.csv')

#creo le tabelle delle stazioni
ar3002d, ar3002m = fn.stazione(ar, 3002)
ar9997d, ar9997m = fn.stazione(ar, 9997)
ar1028d, ar1028m = fn.stazione(ar, 1028)
ut2d, ut2m = fn.stazione(ut, 2)
ut3006d, ut3006m = fn.stazione(ut, 3006)
ut5632d, ut5632m = fn.stazione(ut, 5632)
wy100d, wy100m = fn.stazione(wy, 100)
wy870d, wy870m = fn.stazione(wy, 870)
col2d, col2m = fn.stazione(col, 2)
col3d, col3m = fn.stazione(col, 3)
col3001d, col3001m = fn.stazione(col, 3001)
nm23d, nm23m = fn.stazione(nm, 23)

#grafico stazioni arizona
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ar3002d, ar3002m, color='forestgreen')
ax[1].plot(ar9997d, ar9997m, color='limegreen')
ax[2].plot(ar1028d, ar1028m, color='darkseagreen')
ax[0].set_title('stazione 3002', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 9997', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 1028', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Arizona')
plt.show()

#grafico stazioni utah
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ut2d, ut2m, color='darkorange')
ax[1].plot(ut3006d, ut3006m, color='orange')
ax[2].plot(ut5632d, ut5632m, color='sandybrown')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3006', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 5632', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Utah')
plt.show()

#grafico stazioni wyoming
fig,ax = plt.subplots(2,1, figsize=(40,40))
ax[0].plot(wy100d, wy100m, color='lightcoral')
ax[1].plot(wy870d, wy870m, color='indianred')
ax[0].set_title('stazione 100', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 870', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Wyoming')
plt.show()

#grafico stazioni colorado
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(col2d, col2m, color='lightskyblue')
ax[1].plot(col3d, col3m, color='mediumturquoise')
ax[2].plot(col3001d, col3001m, color='aquamarine')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 3001', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Colorado')
plt.show()

#grafico stazione new mexico
plt.plot(nm23d, nm23m, color='mediumslateblue')
plt.title('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in New Mexico')
plt.show()

#analisi di Fourier dei dati di NO2 delle stazioni
ar3002tf, ar3002sp, ar3002fr, ar3002max = fn.trasf(ar3002m)
ar9997tf, ar9997sp, ar9997fr, ar9997max = fn.trasf(ar9997m)
ar1028tf, ar1028sp, ar1028fr, ar1028max = fn.trasf(ar1028m)
ut2tf, ut2sp, ut2fr, ut2max = fn.trasf(ut2m)
ut3006tf, ut3006sp, ut3006fr, ut3006max = fn.trasf(ut3006m)
ut5632tf, ut5632sp, ut5632fr, ut5632max = fn.trasf(ut5632m)
wy100tf, wy100sp, wy100fr, wy100max = fn.trasf(wy100m)
wy870tf, wy870sp, wy870fr, wy870max = fn.trasf(wy870m)
col2tf, col2sp, col2fr, col2max = fn.trasf(col2m)
col3tf, col3sp, col3fr, col3max = fn.trasf(col3m)
col3001tf, col3001sp, col3001fr, col3001max = fn.trasf(col3001m)
nm23tf, nm23sp, nm23fr, nm23max = fn.trasf(nm23m)

#grafico spettro di potenza in funzione della frequenza
#arizona
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ar3002fr[1:ar3002tf.size//2], ar3002sp[1:ar3002tf.size//2], color='forestgreen')
ax[1].plot(ar9997fr[1:ar9997tf.size//2], ar9997sp[1:ar9997tf.size//2], color='limegreen')
ax[2].plot(ar1028fr[1:ar1028tf.size//2], ar1028sp[1:ar1028tf.size//2], color='darkseagreen')
ax[0].set_title('stazione 3002', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 9997', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 1028', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in Arizona')
plt.show()

#utah
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ut2fr[1:ut2tf.size//2], ut2sp[1:ut2tf.size//2], color='darkorange')
ax[1].plot(ut3006fr[1:ut3006tf.size//2], ut3006sp[1:ut3006tf.size//2], color='orange')
ax[2].plot(ut5632fr[1:ut5632tf.size//2], ut5632sp[1:ut5632tf.size//2], color='sandybrown')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3006', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 5632', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in Utah')
plt.show()

#wyoming
fig,ax = plt.subplots(2,1, figsize=(40,40))
ax[0].plot(wy100fr[1:wy100tf.size//2], wy100sp[1:wy100tf.size//2], color='lightcoral')
ax[1].plot(wy870fr[1:wy870tf.size//2], wy870sp[1:wy870tf.size//2], color='indianred')
ax[0].set_title('stazione 100', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 870', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in Wyoming')
plt.show()

#colorado
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(col2fr[1:col2tf.size//2], col2sp[1:col2tf.size//2], color='lightskyblue')
ax[1].plot(col3fr[1:col3tf.size//2], col3sp[1:col3tf.size//2], color='mediumturquoise')
ax[2].plot(col3001fr[1:col3001tf.size//2], col3001sp[1:col3001tf.size//2], color='aquamarine')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 3001', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in Colorado')
plt.show()

#new mexico
plt.plot(nm23fr[1:nm23tf.size//2], nm23sp[1:nm23tf.size//2], color='mediumslateblue')
plt.title('spettro di potenza [$\mu g^2/m^6$] su frequenza [$d^{-1}$] di NO2 in New Mexico')
plt.yscale('log')
plt.xscale('log')
plt.show()

print('Arizona 3002: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ar3002sp[ar3002max], ar3002fr[ar3002max], int(1/ar3002fr[ar3002max])))
print('Arizona 9997: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ar9997sp[ar9997max], ar9997fr[ar9997max], int(1/ar9997fr[ar9997max])))
print('Arizona 1028: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ar1028sp[ar1028max], ar1028fr[ar1028max], int(1/ar1028fr[ar1028max])))
print('Utah 2: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ut2sp[ut2max], ut2fr[ut2max], int(1/ut2fr[ut2max])))
print('Utah 3006: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ut3006sp[ut3006max], ut3006fr[ut3006max], int(1/ut3006fr[ut3006max])))
print('Utah 2: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( ut5632sp[ut5632max], ut5632fr[ut5632max], int(1/ut5632fr[ut5632max])))
print('Wyoming 100: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( wy100sp[wy100max], wy100fr[wy100max], int(1/wy100fr[wy100max])))
print('Wyoming 870: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( wy870sp[wy870max], wy870fr[wy870max], int(1/wy870fr[wy870max])))
print('Colorado 2: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( col2sp[col2max], col2fr[col2max], int(1/col2fr[col2max])))
print('Colorado 3: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( col3sp[col3max], col3fr[col3max], int(1/col3fr[col3max])))
print('Colorado 3001: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( col3001sp[col3001max], col3001fr[col3001max], int(1/col3001fr[col3001max])))
print('New Mexico 23: Massimo PS: {:f} - Freq {:f} - Periodo: {:d}'.format( nm23sp[nm23max], nm23fr[nm23max], int(1/nm23fr[nm23max])))

#i periodi sono tutti di circa un anno, tranne la stazione 2 in Utah che ha troppi pochi dati

#grafico spettro di potenza in funzione del periodo
#arizona
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(1/ar3002fr[1:ar3002tf.size//2], ar3002sp[1:ar3002tf.size//2], color='forestgreen')
ax[0].plot(1/ar3002fr[ar3002max], ar3002sp[ar3002max], 'o', color='darkgreen')
ax[1].plot(1/ar9997fr[1:ar9997tf.size//2], ar9997sp[1:ar9997tf.size//2], color='limegreen')
ax[1].plot(1/ar9997fr[ar9997max], ar9997sp[ar9997max], 'o', color='lime')
ax[2].plot(1/ar1028fr[1:ar1028tf.size//2], ar1028sp[1:ar1028tf.size//2], color='darkseagreen')
ax[2].plot(1/ar1028fr[ar1028max], ar1028sp[ar1028max], 'o', color='seagreen')
ax[0].set_title('stazione 3002', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 9997', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 1028', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su  periodo T [$d$] di NO2 in Arizona')
plt.show()

#utah
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(1/ut2fr[1:ut2tf.size//2], ut2sp[1:ut2tf.size//2], color='darkorange')
ax[0].plot(1/ut2fr[ut2max], ut2sp[ut2max], 'o', color='orangered')
ax[1].plot(1/ut3006fr[1:ut3006tf.size//2], ut3006sp[1:ut3006tf.size//2], color='orange')
ax[1].plot(1/ut3006fr[ut3006max], ut3006sp[ut3006max], 'o', color='tomato')
ax[2].plot(1/ut5632fr[1:ut5632tf.size//2], ut5632sp[1:ut5632tf.size//2], color='sandybrown')
ax[2].plot(1/ut5632fr[ut5632max], ut5632sp[ut5632max], 'o', color='chocolate')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3006', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 5632', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su periodo T [$d$] di NO2 in Utah')
plt.show()

#wyoming
fig,ax = plt.subplots(2,1, figsize=(40,40))
ax[0].plot(1/wy100fr[1:wy100tf.size//2], wy100sp[1:wy100tf.size//2], color='lightcoral')
ax[0].plot(1/wy100fr[wy100max], wy100sp[wy100max], 'o', color='firebrick')
ax[1].plot(1/wy870fr[1:wy870tf.size//2], wy870sp[1:wy870tf.size//2], color='indianred')
ax[1].plot(1/wy870fr[wy870max], wy870sp[wy870max], 'o', color='darkred')
ax[0].set_title('stazione 100', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 870', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su periodo T [$d$] di NO2 in Wyoming')
plt.show()

#colorado
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(1/col2fr[1:col2tf.size//2], col2sp[1:col2tf.size//2], color='lightskyblue')
ax[0].plot(1/col2fr[col2max], col2sp[col2max], 'o', color='deepskyblue')
ax[1].plot(1/col3fr[1:col3tf.size//2], col3sp[1:col3tf.size//2], color='mediumturquoise')
ax[1].plot(1/col3fr[col3max], col3sp[col3max], 'o', color='teal')
ax[2].plot(1/col3001fr[1:col3001tf.size//2], col3001sp[1:col3001tf.size//2], color='aquamarine')
ax[2].plot(1/col3001fr[col3001max], col3001sp[col3001max], 'o', color='aqua')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 3001', loc='left', y=0.75, x=0.02)
ax[0].set_yscale('log')
ax[0].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xscale('log')
ax[2].set_yscale('log')
ax[2].set_xscale('log')
fig.suptitle('spettro di potenza [$\mu g^2/m^6$] su periodo T [$d$] di NO2 in Colorado')
plt.show()

#new mexico
plt.plot(1/nm23fr[1:nm23tf.size//2], nm23sp[1:nm23tf.size//2], color='mediumslateblue')
plt.plot(1/nm23fr[nm23max], nm23sp[nm23max], 'o', color='rebeccapurple')
plt.title('spettro di potenza [$\mu g^2/m^6$] su periodo T [$d$] di NO2 in New Mexico')
plt.yscale('log')
plt.xscale('log')
plt.show()

#filtro ai coefficienti di fourier selezionando solo le componenti che descrivono l'andamento generale in funzione del tempo (escludendo futtuazioni di breve periodo) e faccio la trasformata FFT inversa con coeff filtrati 
ar3002f = fn.inv(ar3002sp, 5e6, ar3002tf, ar3002m)
ar9997f = fn.inv(ar9997sp, 5e6, ar9997tf, ar9997m)
ar1028f = fn.inv(ar1028sp, 5e6, ar1028tf, ar1028m)
ut2f = fn.inv(ut2sp, 55, ut2tf, ut2m)
ut3006f = fn.inv(ut3006sp, 5e6, ut3006tf, ut3006m)
ut5632f = fn.inv(ut5632sp, 5e4, ut5632tf, ut5632m)
wy100f = fn.inv(wy100sp, 2e5, wy100tf, wy100m)
wy870f = fn.inv(wy870sp, 7e4, wy870tf, wy870m)
col2f = fn.inv(col2sp, 5e6, col2tf, col2m)
col3f = fn.inv(col3sp, 1e3, col3tf, col3m)
col3001f = fn.inv(col3001sp, 5e6, col3001tf, col3001m)
nm23f = fn.inv(nm23sp, 6e6, nm23tf, nm23m)

#grafici di confronto tra segnale originale e il segnale filtrato
#grafico stazioni arizona
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ar3002d, ar3002m, color='forestgreen')
ax[0].plot(ar3002d, ar3002f, color='darkgreen')
ax[1].plot(ar9997d, ar9997m, color='limegreen')
ax[1].plot(ar9997d, ar9997f, color='lime')
ax[2].plot(ar1028d, ar1028m, color='darkseagreen')
ax[2].plot(ar1028d, ar1028f, color='springgreen')
ax[0].set_title('stazione 3002', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 9997', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 1028', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Arizona, dati originali e filtrati')
plt.show()

#grafico stazioni utah
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(ut2d, ut2m, color='darkorange')
ax[0].plot(ut2d, ut2f, color='orangered')
ax[1].plot(ut3006d, ut3006m, color='orange')
ax[1].plot(ut3006d, ut3006f, color='tomato')
ax[2].plot(ut5632d, ut5632m, color='sandybrown')
ax[2].plot(ut5632d, ut5632f, color='chocolate')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3006', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 5632', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Utah, dati originali e filtrati')
plt.show()

#grafico stazioni wyoming
fig,ax = plt.subplots(2,1, figsize=(40,40))
ax[0].plot(wy100d, wy100m, color='lightcoral')
ax[0].plot(wy100d, wy100f, color='firebrick')
ax[1].plot(wy870d, wy870m, color='indianred')
ax[1].plot(wy870d, wy870f, color='darkred')
ax[0].set_title('stazione 100', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 870', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Wyoming, dati originali e filtrati')
plt.show()

#grafico stazioni colorado
fig,ax = plt.subplots(3,1, figsize=(40,40))
ax[0].plot(col2d, col2m, color='lightskyblue')
ax[0].plot(col2d, col2f, color='dodgerblue')
ax[1].plot(col3d, col3m, color='mediumturquoise')
ax[1].plot(col3d, col3f, color='teal')
ax[2].plot(col3001d, col3001m, color='aquamarine')
ax[2].plot(col3001d, col3001f, color='aqua')
ax[0].set_title('stazione 2', loc='left', y=0.75, x=0.02)
ax[1].set_title('stazione 3', loc='left', y=0.75, x=0.02)
ax[2].set_title('stazione 3001', loc='left', y=0.75, x=0.02)
fig.suptitle('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in Colorado, dati originali e filtrati')
plt.show()

#grafico stazione new mexico
plt.plot(nm23d, nm23m, color='mediumslateblue')
plt.plot(nm23d, nm23f, color='rebeccapurple')
plt.title('media della densità di NO2 [$\mu g/m^3$] al giorno [d] in New Mexico, dati originali e filtrati')
plt.show()

#correlazione
#arizona
st3002 = pd.DataFrame()
st3002['date'] = ar3002d
st3002['staz 3002'] = ar3002m
st9997 = pd.DataFrame()
st9997['date'] = ar9997d
st9997['staz 9997'] = ar9997m
st1028 = pd.DataFrame()
st1028['date'] = ar1028d
st1028['staz 1028'] = ar1028m

ar1 = pd.merge(st3002, st9997, how='inner', left_on='date', right_on='date')
ar2 = pd.merge(ar1, st1028, how='inner', left_on='date', right_on='date')
ar = ar2[['staz 3002', 'staz 9997', 'staz 1028']]
print('correlazione arizona')
print(ar.corr())

#utah
# la stazione2 non è inserita perché ha pochi dati
st3006 = pd.DataFrame()
st3006['date'] = ut3006d
st3006['staz 3006'] = ut3006m
st5632 = pd.DataFrame()
st5632['date'] = ut5632d
st5632['staz 5632'] = ut5632m

ut1 = pd.merge(st3006, st5632, how='inner', left_on='date', right_on='date')
ut = ut1[['staz 3006', 'staz 5632']]
print('correlazione utah')
print(ut.corr())

#wyoming
st100 = pd.DataFrame()
st100['date'] = wy100d
st100['staz 100'] = wy100m
st870 = pd.DataFrame()
st870['date'] = wy870d
st870['staz 870'] = wy870m

wy1 = pd.merge(st100, st870, how='inner', left_on='date', right_on='date')
wy = wy1[['staz 100', 'staz 870']]
print('correlazione wyoming')
print(wy.corr())
#colorado
# la stazione 3 non è inserita perché ha pochi dati
st2 = pd.DataFrame()
st2['date'] = col2d
st2['staz 2'] = col2m
st3001 = pd.DataFrame()
st3001['date'] = col3001d
st3001['staz 3001'] = col3001m

col1 = pd.merge(st2, st3001, how='inner', left_on='date', right_on='date')
col = col1[['staz 2', 'staz 3001']]
print('correlazione colorado')
print(col.corr())
#new mwxico
# il new mwxico ha solo una stazione, non h senso fare la correlazione

