# HOWTO: Plugin e Skill (solo Antigravity)

Riferimento per JARVIS. Consultare quando si crea, si modifica, si sposta o si cancella una skill o un plugin, e quando si aggiorna `.agents/plugins/plugins.md`.

**Fonti verificate il 2026-10-11**: [Plugins](https://antigravity.google/docs/plugins/) e [Agent skills](https://antigravity.google/docs/skills/). Tutto ciò che non è in quelle pagine è marcato `unverified` nella sezione 11.
**Scope**: solo Antigravity. Nessun adapter per Claude Code, Codex o ChatGPT. La skill (cartella con `SKILL.md`) è un formato aperto e si copia così com'è se in futuro servirà.

---

## 1. Definizioni

| Blocco | Cos'è | Dove vive |
| :-- | :-- | :-- |
| **Skill** | Cartella con `SKILL.md`. Il agent vede nome e `description`, legge il corpo solo se il task corrisponde (progressive disclosure) | Standalone: `.agents/skills/<skill>/`. In un plugin: `.agents/plugins/<plugin>/skills/<skill>/` |
| **Plugin** | Cartella con `plugin.json` che impacchetta skill, agents, rules, config MCP e hooks in un solo asset | `.agents/plugins/<plugin>/` |
| **Agent (vault)** | Contratto sottile con tool e permessi, rimanda a un workflow. Vedi `howto-creating-subagents.md` | `.agents/agents/agt-*.md` |
| **Command** | Playbook invocato con `/nome`. Non è un componente di plugin nella documentazione | `.agents/commands/` |

Quale blocco usare:

| Se serve... | usa... |
| :-- | :-- |
| Conoscenza o regole riusabili, caricate solo quando servono | skill |
| Più skill dello stesso dominio da tenere insieme | plugin |
| Orchestrare tool con permessi ristretti e alta ricorrenza | agent (2 criteri su 3) |
| Un playbook a comando con gate `[ASK]` | command |
| Una regola di comportamento ("sempre", "mai") | `AGENTS.md` |

---

## 2. Struttura

```text
.agents/
├── skills/                          # SOLO skill standalone
│   └── <skill>/
│       └── SKILL.md
├── agents/                          # agt-*.md (convenzione vault, non dentro i plugin)
├── commands/
└── plugins/
    ├── plugins.md                   # indice, un paragrafo per plugin (file, non plugin)
    └── <plugin>/
        ├── plugin.json              # obbligatorio
        ├── skills/                  # opzionale
        │   └── <skill>/
        │       ├── SKILL.md         # obbligatorio
        │       ├── scripts/         # opzionale
        │       ├── examples/        # opzionale
        │       └── resources/       # opzionale
        ├── rules/                   # opzionale, file .md
        ├── mcp_config.json          # opzionale
        ├── hooks.json               # opzionale
        └── agents/                  # supportato da Antigravity, NON usato nel vault (vedi 4.3)
```

Un plugin senza `plugin.json` non è un plugin: non verrà riconosciuto.

---

## 3. Regole di scrittura

### 3.1 `plugin.json`

Schema ufficiale: solo `name` (obbligatorio) e `description`. `additionalProperties: false`: **qualsiasi altro campo (version, author, tags...) invalida il file**.

```json
{
  "$schema": "https://antigravity.google/schemas/v1/plugin.json",
  "name": "moda",
  "description": "Skill per creare e rifinire contenuti del brand MODA: newsletter, post LinkedIn, Substack Notes, infografiche, tono di voce."
}
```

- `name`: regex `^[a-zA-Z0-9-_]+$`. Nel vault: `kebab-case`, **identico al nome della cartella**. Obbligatorio per i comandi CLI; in 2.0 e IDE ha default il nome cartella, ma lo scriviamo sempre.
- `description`: una frase, dice cosa fa il plugin. Compare negli elenchi dei plugin.
- Tenere `$schema`: dà validazione e autocomplete nell'editor.

### 3.2 `SKILL.md`

- Frontmatter: `description` obbligatoria, `name` opzionale (default: nome cartella). Nel vault scriviamo sempre entrambi. Altri campi: non garantiti.
- `description` in terza persona, con le parole con cui Francesco la chiederebbe. È l'unico testo che l'agent vede per decidere. Vaga = non si attiva.
- Una skill, un compito. Oltre ~300 righe, sposta il dettaglio in `resources/` o `examples/`.
- Script: nel corpo istruisci a lanciarli con `--help` prima di leggerli (restano "black box", meno contesto consumato).
- Complessa? Aggiungi una sezione decision tree.
- Percorsi sempre relativi. File sciolti, mai pacchettizzati in `.skill` o zip.
- In CLI ogni skill diventa uno slash command `/<skill-name>`: il nome è anche un comando.

### 3.3 Altri componenti

- **`rules/`**: ammesso, ma le regole di comportamento del vault vanno in `AGENTS.md`. Usalo solo per vincoli validi esclusivamente quando il plugin è attivo.
- **`agents/` nel plugin**: non usarlo. Il vault impone `.agents/agents/agt-*.md`. Due posti per gli agent = duplicazione. Se un giorno cambierà la regola, si decide con `/decompose`.
- **`mcp_config.json`**: dichiara solo server verificati e realmente in uso. Elenca le dipendenze anche in `plugins.md`.
- **`hooks.json`**: esegue **comandi shell** prima o dopo i tool call. Rischio reale. Mai crearlo senza **[ASK]** a Francesco che mostri il comando esatto.
- Scope globale (`~/.gemini/config/plugins/`): fuori dal vault, vietato dalla regola "mai accedere fuori dalla root". Tutti i plugin vivono nel workspace.

### 3.4 Naming

- Cartelle e file in `lowercase` `kebab-case`. Fanno eccezione `SKILL.md` e `plugin.json`.
- Plugin: nome breve, una parola, coincidente con l'area quando possibile (`moda`, `career`).
- Skill dentro un plugin: il prefisso `<plugin>-` non serve più per raggruppare, lo fa la cartella. **Il nome però deve restare unico in tutto il vault** (plugin + standalone), perché diventa slash command. Se due plugin potrebbero collidere, usa il prefisso.

---

## 4. Quando raggruppare

Una skill entra in un plugin se condivide con altre **almeno una** di queste:

1. stesso dominio o brand;
2. stesso tool o server MCP;
3. uso frequente in sequenza.

Altrimenti resta standalone. **Un plugin con una sola skill non è un plugin**: torna standalone. Non creare un plugin "per ordine": ogni plugin è una riga da mantenere in `plugins.md`.
Attenzione adozione: spostare una skill dentro un plugin cambia il suo percorso. Controlla riferimenti in `AGENTS.md`, agent, commands e workflow prima di spostare.

---

## 5. Procedure

Ogni procedura finisce con gli ultimi due passi, sempre: **aggiorna `plugins.md`** (sezione 8) e **scrivi la riga di log** (sezione 10). Senza questi due passi l'operazione non è conclusa.

### A. Nuovo plugin
1. Controlla `plugins.md` e `.agents/skills/`: esiste già un plugin o una skill che copre il caso?
2. Verifica il criterio della sezione 5: servono almeno 2 skill.
3. Crea `.agents/plugins/<plugin>/plugin.json` (4.1) e `skills/`.
4. Crea o sposta le skill (procedura B o E).
5. Aggiorna `plugins.md`. Log.

### B. Nuova skill in un plugin
1. Verifica che il nome sia unico nel vault.
2. Crea `.agents/plugins/<plugin>/skills/<skill>/SKILL.md` (3.2).
3. Test: una richiesta reale che dovrebbe attivarla. Se non parte, riscrivi la `description`.
4. Aggiorna il paragrafo del plugin in `plugins.md`. Log.

### C. Nuova skill standalone
1. Crea `.agents/skills/<skill>/SKILL.md`.
2. Test come sopra.
3. Aggiungi la riga in `plugins.md`, sezione Standalone. Log.

### D. Modifica
- Cambia solo il file necessario (edit chirurgico).
- Se cambia la `description` o lo scopo, aggiorna il paragrafo in `plugins.md` nello stesso intervento.
- Se cambia solo il corpo di una skill e non il suo scopo, `plugins.md` non cambia, ma il log sì.

### E. Rinomina o spostamento (standalone <-> plugin, plugin <-> plugin)
1. Cerca i riferimenti al vecchio percorso in tutto il vault (agent, commands, workflow, `AGENTS.md`).
2. Sposta/rinomina. Se rinomini un plugin: cartella **e** `name` in `plugin.json`.
3. Correggi i riferimenti (solo il link, nient'altro).
4. Aggiorna `plugins.md` (rimuovi dal vecchio posto, aggiungi al nuovo). Log.

### F. Cancellazione
- **Solo su richiesta esplicita di Francesco.** Mai per "pulizia".
- Prima **[ASK]**: mostra cosa viene rimosso (cartella, skill contenute, riferimenti trovati) e aspetta conferma.
- Rimuovendo un plugin si rimuovono anche le sue skill: elencale nell'[ASK].
- Rimuovi la riga/paragrafo da `plugins.md`. Log.

---

## 6. `.agents/plugins/plugins.md`

Indice **derivato**: le fonti di verità sono `plugin.json` e `SKILL.md`. Se divergono, si corregge `plugins.md`, mai le skill.

Regole:
- Un paragrafo per plugin: cosa fa, per chi/quando, **quali skill contiene** (nome in grassetto + mezza riga ciascuna), dipendenze (MCP, hooks, rules) se esistono.
- Una riga per ogni skill standalone.
- Nessun contenuto copiato dal corpo delle skill: si riassume la `description`.
- Percorsi relativi.
- Ordine alfabetico dei plugin. Header `Last updated: YYYY-MM-DD`.

Formato:

```markdown
# Plugins

Last updated: YYYY-MM-DD

## moda
Stato: attivo | Dipendenze: nessuna | Percorso: [moda/](./moda/)

Raggruppa le skill per produrre contenuti del brand MODA, dalla newsletter ai post social, con tono di voce e regole anti-AI già incorporati. Contiene: **moda-newsletter** (newsletter complete per Substack), **moda-linkedin-post** (post LinkedIn con framework narrativo scelto in automatico), **moda-substack-notes** (note brevi derivate da un contenuto esistente) e **moda-infographic** (brief e prompt per infografiche).

## career
Stato: attivo | Dipendenze: nessuna | Percorso: [career/](./career/)

(paragrafo)

## Standalone
Skill in `.agents/skills/`, non appartenenti a nessun plugin.

- **fanta-advisor**: consulente fantacalcio sui dati locali di fantacalcio.it. [SKILL.md](../skills/fanta-advisor/SKILL.md)
```

---

## 7. Aggiornamento automatico di `plugins.md`

"Automatico" qui significa **regola obbligatoria per JARVIS**, non un hook: Antigravity non aggiorna il file da solo. Per questo servono due livelli.

**Livello 1: regola in `AGENTS.md` (root)**, sezione Global Rules, da aggiungere:

```markdown
- **Plugin & Skill Index**: ogni volta che si crea, modifica, sposta, rinomina o cancella una skill o un plugin, aggiornare nello stesso intervento `.agents/plugins/plugins.md` e scrivere la riga di log. L'operazione non è conclusa senza questi due passi. Procedure complete in `howto-plugins-and-skills.md`.
```

Aggiungere anche il riferimento nella tabella References di `AGENTS.md` (oggi punta a `howto-plugins-and-skills` senza estensione).

**Livello 2: sync check a fine operazione.** Confronta il disco con l'indice:
1. Elenca `.agents/plugins/*/plugin.json` e `.agents/skills/*/SKILL.md`.
2. Elenca le skill di ogni `.agents/plugins/*/skills/*/SKILL.md`.
3. Verifica che ogni plugin abbia un paragrafo, che ogni skill compaia nel paragrafo giusto o in Standalone, e che nessuna voce di `plugins.md` punti a qualcosa che non esiste.
4. Se trovi differenze: correggi `plugins.md` e dichiara cosa hai cambiato. Se non sei sicuro di quale lato sia giusto: **[ASK]**.

Limite onesto: una regola testuale può essere saltata da un agent distratto. Il sync check è la rete di sicurezza. Possibile evoluzione: aggiungere il controllo a `/audit` (oggi `/audit` lavora solo su `04_Wiki/`).

---

## 8. Log

Daily log (`logs/YYYY-MM-DD.log`), dopo ogni operazione riuscita:

```
YYYY-MM-DD HH:MM:SS | INFO | SESSION | skills: created <relative-path> plugin=<plugin|standalone>
YYYY-MM-DD HH:MM:SS | INFO | SESSION | skills: updated <relative-path> plugin=<plugin|standalone>
YYYY-MM-DD HH:MM:SS | INFO | SESSION | skills: moved <old-path> -> <new-path> plugin=<plugin|standalone>
YYYY-MM-DD HH:MM:SS | INFO | SESSION | skills: removed <relative-path> plugin=<plugin|standalone>
YYYY-MM-DD HH:MM:SS | INFO | SESSION | plugins: created|updated|renamed|removed <relative-path>
YYYY-MM-DD HH:MM:SS | INFO | SESSION | plugins: index synced <relative-path> changes=<n>
```

Prima di usarle la prima volta, aggiungile al catalogo in `howto-logging.md` (sezione 1.4), come richiede lo standard.

---

## 9. Migrazione dallo stato attuale

1. Elenca le skill in `.agents/skills/` e raggruppale con il criterio della sezione 5.
2. Per ogni gruppo con almeno 2 skill: procedura A.
3. Sposta le skill una alla volta (procedura E), non in blocco, correggendo i riferimenti.
4. Crea `.agents/plugins/plugins.md` e rimuovi il vecchio `.agents/plugins.md` (solo dopo conferma, regola di cancellazione).
5. Esegui il sync check e un test di attivazione per ogni plugin.

---

## 10. Non verificato (da testare prima di fidarsi)

| Punto | Perché è un rischio | Come testare |
| :-- | :-- | :-- |
| `plugins.md` dentro `.agents/plugins/` | La documentazione non dice come vengono trattati i file sciolti nella cartella. Dovrebbe essere ignorato (non ha `plugin.json`), ma non è garantito | Dopo la creazione, `agy plugin list` e `/plugin list`: deve mostrare solo i plugin veri, senza errori |
| Plugin di workspace attivi senza installazione | La doc dice che basta mettere la cartella in `.agents/plugins/`; non specifica se serva un enable | `agy plugin list` mostra il plugin? Le sue skill compaiono come `/<skill-name>`? |
| Collisioni di nome tra skill di plugin e standalone | Non documentato quale vince | Tieni i nomi unici (4.4) |
| `agents/` dentro il plugin vs `.agents/agents/` | Non documentato come interagiscono | Non usare `agents/` nei plugin |
| Comportamento su Codex | Fuori scope | Non assumere compatibilità |

Se un test fallisce, la fonte di verità è la documentazione ufficiale: aggiorna questo file con quello che hai osservato.

---

## 11. Problemi frequenti

| Problema | Causa probabile e rimedio |
| :-- | :-- |
| Il plugin non compare | Manca `plugin.json`, JSON non valido, o campo extra (`additionalProperties: false`). Controlla con `$schema` nell'editor |
| La skill non si attiva | `description` vaga; oppure cartella nel percorso sbagliato (`.agent/` vs `.agents/`) |
| Skill non vista dopo averla creata | Riavvia la sessione; il file deve chiamarsi esattamente `SKILL.md` |
| Plugin con una sola skill | Non è un plugin: torna standalone |
| `plugins.md` non allineato | Esegui il sync check (sezione 9) |
| Slash command duplicato | Due skill con lo stesso nome: rinomina una, aggiorna `plugins.md` |
| Hook che esegue comandi inattesi | `hooks.json` non approvato: rimuovilo e rivedi con **[ASK]** |