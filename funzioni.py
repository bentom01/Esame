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
    m = t3['NO2 Mean'].values
    return d, m

def csv_stato(t, n):
    #funzione che crea un file csv con i dati di un singolo stato
    #t= tabella da salvare
    #n= nome da dare al file
    t.to_csv(n+'.csv', index = False)

def stazione(t, s):
    #funzione che mi restituisce i dati con solo i valori di una stazione,
    #e mi resituisce la media delle rivelazioni fatte in un giorno,
    #fornendo così un solo dato al giorno
    t1 = t.groupby(['Site Num'])
    t2 = t1.get_group(s)
    return t2.groupby(['Date Local'], as_index = False).mean()

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