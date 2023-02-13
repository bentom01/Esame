import numpy as np
import pandas as pd
from scipy import constants, fft, optimize

def stato(t, s):
    #funzione che mi resituisce due array con solo i valori delle date
    #e della media di NO2 di uno stato
    #e mi resituisce la media delle rivelazioni fatte in un giorno
    #t= tabella di partenza
    #s= codice dello stato
    t1 = t.groupby(['State Code'])
    t2 = t1.get_group(s)
    t3 = t2.groupby(['Date Local'], as_index = False).mean()
    d = t3['Date Local'].values
    d = pd.to_datetime(d, format='%Y-%m-%d')
    m = t3['NO2 Mean'].values
    return d, m

def tab_stato(t, s, n):
    #funzione che crea un file csv con i dati di un singolo stato
    #t= tabella originale
    #s= codice dello stato di cui voglio creare il file
    #n= nome da dare al file
    t1 = t.groupby(['State Code'])
    t2 = t1.get_group(s)
    t2.to_csv(n+'.csv', index = False)

def stazione(t, s):
    #funzione che mi restituisce i dati con solo i valori di una stazione,
    #e mi resituisce la media delle rivelazioni fatte in un giorno,
    #fornendo così un solo dato al giorno
    t1 = t.groupby(['Site Num'])
    t2 = t1.get_group(s)
    t3 = t2.groupby(['Date Local'], as_index = False).mean()
    d = t3['Date Local'].values
    d = pd.to_datetime(d, format='%Y-%m-%d')
    m = t3['NO2 Mean'].values
    return d, m

def trasf(a):
    c = 0.5
    tf = fft.rfft(a)
    sp = np.absolute(tf)**2
    fr = c*fft.rfftfreq(tf.size, d=1)
    m = np.argmax(sp[1:tf.size//2])+1
    return tf, sp, fr, m

def inv(sp, s, tf, no2):
    #funzione che mi restituisce la trasformata FFT inversa con i coeff filtrati
    #sp è l'array dello spettro di potenza
    #s è la soglia
    #tf è l'array dei vaolori della trasformata FFT
    #no2 è l'array con le medie giornaliere di no2
    mask = sp < s
    filt_tf = tf.copy()
    filt_tf[mask] = 0
    filt = fft.irfft(filt_tf, n=len(no2))
    return filt

def noise(f, a, n):
    #funzione per fare il fit del rumore e capire la tipologia di rumore
    return a/(f**n)
#n=0 -> white noise, n=1 -> pink noise, n=2 -> red noise

def correl(d1, d2, d3, d4, d5, m1, m2, m3, m4, m5, s1, s2, s3, s4, s5):
    tab1 = pd.DataFrame()
    tab2 = pd.DataFrame()
    tab3 = pd.DataFrame()
    tab4 = pd.DataFrame()
    tab5 = pd.DataFrame()
    tab1['date'] = d1
    tab2['date'] = d2
    tab3['date'] = d3
    tab4['date'] = d4
    tab5['date'] = d5
    tab1[s1] = m1
    tab2[s2] = m2
    tab3[s3] = m3
    tab4[s4] = m4
    tab5[s5] = m5
    df1 = pd.merge(tab1, tab2, how='inner', left_on='date', right_on='date')
    df2 = pd.merge(df1, tab3, how='inner', left_on='date', right_on='date')
    df3 = pd.merge(df2, tab4, how='inner', left_on='date', right_on='date')
    df4 = pd.merge(df3, tab5, how='inner', left_on='date', right_on='date')
    df = df4[[s1, s2, s3, s4, s5]]
    return df
