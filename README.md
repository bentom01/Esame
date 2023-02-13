Progetto per l'esame di Metodi Computazionali per la Fisica

Lo scopo di questo progetto era di analizzare un inquinante a scelta, in questo caso NO2, presente negli Usa.
La consegna si trova nel file Inquinanti_USA_2011_2013.pdf, mentre i dati originali forniti sono nel file pollution_us_2011_2013.csv

Le librerie utilizzate sono:
1) numpy
2) pandas
3) matplotlib.pyplot
4) scipy
5) plotly.express

Sono state fatte tre tipologie di analisi:
1) per 5 stati confinanti che formano una regione: Arizona, Utah, New Mexico, Colorado e Wyoming nel file analisi_5stati.py, che deve essere eseguito prima di quello per l'analisi delle stazioni, perché creerè un file csv per ogni stato
2) per le stazioni dei 5 stati confinanti nel file analisi_stazioni.py
3) per tutti gli stati nel file analisi_tutti_stati.py

Il file funzioni.py contiene tutte le funzioni utilizzate negli altri file.
Il file geo.py contiene uno script python che crea una mappa degli Stati Uniti dove sono riportate, attraverso una scala di colore, le medie giornaliere di no2 nei 5 stati selezionati.