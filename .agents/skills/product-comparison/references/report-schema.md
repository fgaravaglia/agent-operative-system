# Schema dati del report

Il JSON va inserito in `assets/report-template.html` al posto di `__DATA_JSON__`. Testi in italiano, apostrofo tipografico (’).

```json
{
  "meta": {
    "title": "Confronto SUV cino-coreani",
    "subtitle": "10.000 km/anno, cane di taglia grande",
    "category": "Automotive",
    "date": "2026-10-18",
    "budget_max": 28000,
    "currency": "€",
    "tldr": "Due righe: cosa è emerso e chi vince per chi."
  },
  "brief": [ {"label": "Uso", "value": "…"}, {"label": "Budget", "value": "…"} ],
  "alerts": [ "Difetto o richiamo recente trasversale, se esiste" ],
  "drivers": [
    {"id": "d1", "name": "Spazio per il cane", "why": "Perché conta", "how": "Come misurato", "weight": 25}
  ],
  "products": [
    {
      "id": "p1", "name": "MG HS 1.5T", "brand": "MG",
      "price_low": 27490, "price_high": 31990, "price_label": "27.490 – 31.990 €", "price_date": "2026-10",
      "scores": {"d1": 9},
      "confidence": "alta | media | bassa",
      "specs": {"Bagagliaio": "507 L", "Lunghezza": "4,67 m"},
      "pros": ["…"], "cons": ["…"],
      "known_issues": ["Difetto o richiamo con data e fonte"],
      "fit_note": "Per chi è adatto / per chi no",
      "sources": [ {"label": "Testata X", "url": "https://…"} ]
    }
  ],
  "verdicts": [
    {"type": "best_buy | top | smart", "product": "p1", "headline": "opzionale", "why": "…", "caveat": "Attenzione a…"}
  ]
}
```

Regole: pesi dei driver sommano a 100; ogni prodotto ha un voto 0-10 per ogni driver; `price_low` è numero (serve al filtro budget); `confidence` bassa se meno di due fonti indipendenti; URL solo http/https; 3-5 prodotti; niente campo vuoto inventato, meglio ometterlo.
