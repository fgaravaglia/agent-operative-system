# HOWTO Google Calendar Conventions

Linee guida e convenzioni operative obbligatorie per la gestione e creazione di eventi su Google Calendar all'interno del sistema Jarvis.

---

## 1. Durata Predefinita (Default Duration)

* **Durata Standard:** Salvo diversa e specifica indicazione dell'utente, ogni nuovo meeting o evento deve essere pianificato con una **durata predefinita di 45 minuti**.
* **Buffer & Focus:** La durata di 45 minuti favorisce il time boxing ed evita sovrapposizioni consecutive a ridosso dell'ora piena.

---

## 2. Convenzione di Naming e Tagging (Title & Tags)

* **Prefisso Obbligatorio:** Ogni evento **deve sempre** includere all'inizio del titolo un tag racchiuso tra parentesi quadre:
  ```text
  [Tag] Descrizione dell'evento
  ```
* **Formato:** Iniziale maiuscola per il tag, seguita da spazio singolo e descrizione chiara e sintetica (azione o oggetto).

### Esempi di Riferimento
* `[Casa] controllare caldaia con tecnico`
* `[Salute] visita di controllo dal medico`
* `[Casa] tagliando automobile`

### Tassonomia dei Tag (Allineata alle Aree del Vault)
Utilizzare coerentemente i tag in base all'area di pertinenza:
* **`[Casa]`**: Utenze, manutenzioni domestiche, auto, riparazioni, gestione immobile.
* **`[Salute]`**: Visite specialistiche, esami clinici, controlli, terapie, dentista.
* **`[Lavoro]`**: Riunioni professionali, allineamenti di progetto, colloqui.
* **`[Scuola]`** o **`[Daniele]`**: Riunioni scolastiche, colloqui docenti, impegni di Daniele.
* **`[Sport]`**: Allenamenti, visite medico-sportive, rinnovi o gare.
* **`[Fisco]`**: Commercialista, scadenze tributarie, dichiarazione dei redditi.
* **`[MODA]`**: Registrazioni podcast, interviste, uscite editoriali, meeting MODA.
* **`[Travel]`**: Voli, trasporti, hotel, pianificazione viaggi.

---

## 3. Regole Operative Prima della Scrittura (Pre-Flight Checks)

* **Verifica Conflitti (Read Before Write):** Prima di creare o spostare qualsiasi evento, verificare la disponibilità sullo slot temporale con i comandi di lettura (`readonly events` / `freebusy`) per evitare double-booking.
* **Conferma per Invitati Esterni:** Se l'evento prevede partecipanti esterni, chiedere sempre conferma preventiva all'utente prima di procedere all'invito.
* **Eliminazione Protetta:** Mai cancellare eventi esistenti senza specifica ed esplicita richiesta dell'utente.

---

## 4. Dettagli e Campi Aggiuntivi

* **Luogo (Location):** Specificare sempre l'indirizzo per eventi fisici o il link del meeting per eventi virtuali.
* **Descrizione (Description):** Includere note operative essenziali, contatti utili o l'ordine del giorno sintetico.
