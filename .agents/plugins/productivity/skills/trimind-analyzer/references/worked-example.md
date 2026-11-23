# Worked example (illustrative, in Italian)

Tutte le cifre sono inventate per mostrare il formato. Non riusarle come fatti.
Mostra come appare l'output finale quando l'utente scrive in italiano.

**Input utente:** "Siamo una software house da 40 persone. Costruire o comprare un modulo di reporting? Due senior part-time, i clienti lo vogliono entro due trimestri, nessun preventivo ancora."

## 🏗️ Analisi dell'Architetto

**Domanda:** Costruire o comprare un modulo di reporting da rilasciare in due trimestri?

| ID | Assunzione | Confidenza |
| --- | --- | --- |
| AS1 | La capacità part-time vale circa 1 FTE totale | 🟡 media |
| AS2 | I clienti vogliono report standard, non analytics differenzianti | 🔴 bassa |
| AS3 | Le licenze scalano per cliente o per utente | 🔴 bassa |

| Opzione | Pro | Contro |
| --- | --- | --- |
| A Costruire | Controllo totale, nessuna licenza | Tempi stretti, manutenzione a carico nostro |
| B Comprare e integrare | Time-to-market rapido | Costo ricorrente, lock-in |
| C Comprare ora, sostituire poi | Velocità e via d'uscita | Serve un data layer pulito |

**Catena di ragionamento**

- **A1** Due trimestri e circa 1 FTE rendono tesa una build completa — *perché* il lavoro include design, sicurezza e supporto, non solo codice.
- **A2** Se AS2 regge, il reporting non è un differenziante — *perché* i clienti giudicano i risultati, non il motore.
- **A3** Comprare sposta il costo da ore di sviluppo a licenze — *perché* il confronto dipende da AS3.

**👉 Bozza di raccomandazione:** Opzione C, comprare e integrare ora, mantenendo il data layer sostituibile.

## 🔍 Critica dell'Esaminatore

**💪 Cosa regge:** l'idea che il reporting probabilmente non differenzi, e che la scadenza sia stretta.

| # | Colpisce | Angolo | Problema e impatto | Fix |
| --- | --- | --- | --- | --- |
| E1 | AS2 | 📌 assunzione | Mai verificata. Se i clienti vogliono dashboard custom, il fornitore diventa un limite | Chiedere a 5 clienti cosa usano davvero |
| E2 | A3 | 🕳️ dati mancanti | Le licenze potrebbero costare più della build al nostro numero di clienti | Ottenere 2 preventivi prima di decidere |
| E3 | A1 | 🧠 logica | Possibile planning fallacy: le stime sul part-time sono di solito ottimistiche | Trattare la stima come best case, aggiungere buffer |
| E4 | Opzione C | 👥 adozione | I tecnici possono rifiutare un componente acquistato; le vendite possono promettere funzioni che il fornitore non ha | Coinvolgerli presto, definire una clausola di uscita |

**🧪 Bias scan:** planning fallacy (E3), status-quo bias non rilevato.

**💥 Pre-mortem (fallita dopo 12 mesi)**

1. Le licenze crescono più dei ricavi.
2. I limiti del fornitore bloccano una richiesta cliente.
3. L'integrazione dura più della build stimata.

**🔄 Cosa mi farebbe cambiare idea:** preventivi con costo licenze sopra il costo build a 3 anni, o clienti che chiedono forte personalizzazione.

## ⚖️ Sintesi dell'Integratore

| Critica | Decisione | Motivo |
| --- | --- | --- |
| E1 | ✏️ modifica | La validazione clienti diventa un gate prima di firmare |
| E2 | ✅ accetta | I preventivi diventano precondizione |
| E3 | ✅ accetta | Stima build come best case, con buffer |
| E4 | ✏️ modifica | Briefing anticipato a tecnici e vendite, clausola di uscita nel contratto |

**Piano finale:** due settimane di validazione (5 chiamate cliente, 2 preventivi). Decisione su costo a 3 anni e bisogno di personalizzazione. Default: comprare e integrare con clausola di uscita, se entrambi i controlli passano.

## 🎯 Verdetto e Confidenza

| Voce | Esito |
| --- | --- |
| ✅ Raccomandazione | Comprare e integrare, solo dopo i due gate di validazione |
| ⚠️ Rischio principale | Costo licenze e lock-in non ancora quantificati |
| 📊 Confidenza | 🟡 █████░░░░░ 5/10 |

**Cosa è cambiato rispetto alla bozza**

- La bozza decideva prima di validare AS2 e AS3; il piano finale li trasforma in gate.
- Aggiunta la clausola di uscita: il lock-in era il rischio più sottovalutato.

**Perché 5/10:** logica solida (ancoraggio 5-6), ma AS2 e AS3 non sono verificate, quindi vale il tetto a 6, con −1 perché l'adozione non è ancora valutata.

| Incertezza residua | Effetto sull'esito |
| --- | --- |
| Bisogni reali dei clienti | Può ribaltare la scelta |
| Prezzi delle licenze | Può ribaltare la scelta |
| Capacità reale del team | Sposta la data di rilascio |

**📈 Per alzare il punteggio:** le chiamate ai clienti e i due preventivi.
**Dati utili:** storico delle richieste di reporting già ricevute.

**👉 Prossima azione:** fissa oggi 5 chiamate cliente per questa settimana e richiedi 2 preventivi.
