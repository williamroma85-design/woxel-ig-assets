# Contenuti riscritti dal corso (nostra rielaborazione). Modifica qui: PDF e slide si rigenerano con build.py
BRAND = "Lidia Nails"
TITOLO = "Gel Tip: guida all'applicazione"
SOTTOTITOLO = "Metodo passo passo – uso interno"

# (titolo, [punti], nota_relatore, slide?)
SEZIONI = [
 ("1. Cosa sono le Gel Tip", [
   "Estensioni preformate in soft gel che coprono tutta l'unghia naturale: dalla cuticola al bordo libero e su entrambi i laterali (incapsulano l'unghia).",
   "Si applicano con il gel, non con la colla.",
   "Vantaggi: tempi dimezzati, forme e lunghezze identiche su tutte le dita, più controllo e più durata.",
   "Nessun punto di stress scoperto: l'unghia naturale è protetta per intero e il rischio di rottura netta cala molto.",
 ], "Aprire con il problema che tutte conosciamo: forme irregolari e ore di lavoro. La tip risolve tempo e uniformità.", True),

 ("2. Non confondere: tip classiche, press-on, dual form", [
   "Tip classiche (anni 2000): estensioni parziali in plastica rigida incollate sul bordo libero, poi serve la struttura sopra.",
   "Gel Tip moderne: copertura totale in soft gel, applicate con gel.",
   "Press-on: unghie finte in ABS con colla, pensate per l'uso occasionale, non per il professionista. Mai applicarle con base gel: si formano bolle d'aria, umidità e rischio batteri.",
   "Dual form: tecnica manuale di ricostruzione con supporto in plastica da rimuovere. Non è una tip.",
 ], "Spesso la cliente dice 'le tip sono finte'. Serve chiarire la differenza in 30 secondi.", True),

 ("3. Gel vs plastica: come riconoscere la qualità", [
   "La tip in gel è flessibile ma resistente: accompagna l'urto e torna in posizione. La plastica ABS è rigida e cede di colpo.",
   "Segnali d'allarme: prezzo molto basso (scatole da centinaia di pezzi a pochi euro; indicazione del corso: i marchi seri stanno sopra circa 30 € a scatola), materiale ABS, struttura sbagliata.",
   "Test pratico: limare un bordo di una tip. Odore di plastica bruciata = plastica. Il tipico odore di gel limato = gel.",
   "Non fidarsi del nome dell'azienda: un marchio può cambiare qualità nel tempo. Si impara a valutare la tip, non il brand.",
 ], "Il test della lima si può fare davanti alla cliente o in formazione: è memorabile.", True),

 ("4. Struttura corretta di una tip professionale", [
   "Spessore distribuito, non uniforme: sottile al giro cuticola (si fonde con la cuticola), più spesso al bordo libero (regge gli urti).",
   "Giro cuticola tondo, a mezzaluna, senza angoli: l'unghia naturale non è squadrata.",
   "Profilo laterale morbido e armonioso, che copre bene i laterali e il punto di stress.",
   "Da evitare: apice troppo alto, discesa dritta 'a becco di pappagallo', angoli squadrati.",
   "Acquistare solo da schede che mostrano la tip da più angolazioni, anche di profilo.",
 ], "Slide chiave: mostrare foto di una tip corretta e una errata affiancate.", True),

 ("5. Quale tip scegliere", [
   "Trasparente (la preferita): si vede il gel camminare sotto la tip, quindi si capisce la quantità e dove arriva; la polimerizzazione lampo è rapida (circa 7-8 secondi) perché la luce penetra.",
   "Colorata: non si vede il gel, la luce penetra con più fatica (tempo più lungo, rischio che la cliente si muova), meno flessibile al giro cuticola. Meglio una passata di colore sopra.",
   "Semi-opaca di fabbrica: di solito opacizzata solo otticamente, resta liscia dentro e già più sottile. Va riopacizzata, quindi si scarta.",
 ], "Messaggio: la trasparente ci dà controllo visivo e velocità.", True),

 ("6. Lunghezze, forme e misure", [
   "Lunghezze: XS, S, M, L, XL (esistono anche XXL).",
   "In Italia spesso si trova una sola lunghezza: scegliere fornitori con gamma completa evita di accorciare o raddoppiare le tip.",
   "Le misure ideali sono 14 (0–9 con le mezze misure): ogni numero è una larghezza precisa.",
   "Orientamento: 0–1 pollice (a volte 00 per pollici larghi), 2–6,5 le tre dita centrali, 7–9 mignolo.",
   "La numerazione cambia anche tra forme dello stesso brand, e tra mano destra e sinistra può variare di una misura.",
 ], "Consiglio operativo: tenere un campionario con tutte le misure per forma.", True),

 ("7. Preparare l'unghia naturale", [
   "Unghia naturale corta, pari al polpastrello, e stondata (mai angoli).",
   "Se resta lunga: la tip la fa sporgere, si tende ad appoggiarla inclinata 'a pappagallo', si tira dal giro cuticola e si formano tasche d'aria.",
   "Con l'unghia corta, se la tip si rompe cede solo il bordo libero della tip: l'unghia sotto resta protetta.",
   "Rimuovere tutto il vecchio prodotto (semipermanente, gel, acrilico): sotto la tip serve una superficie liscia. Solo se si rifà un set di tip si può lasciare un velo sottile di base.",
   "Dry manicure e pulizia cuticole come sempre.",
 ], "Per la cliente che vuole le unghie lunghe: mostrarle foto prima/dopo di rotture. La lunghezza si fa con la tip, non con l'unghia naturale.", True),

 ("8. Scegliere la misura sull'unghia", [
   "Appoggiare la tip al centro e farla scorrere verso il basso, senza forzare sulla pelle.",
   "Deve combaciare con il punto di crescita e coprire entrambi i laterali, senza spazi e senza invadere la pelle.",
   "Se una è troppo piccola e l'altra un po' grande, scegliere la più grande: la tip in gel si flette leggermente.",
   "Una tip troppo piccola non si può allargare. Una troppo grande si può restringere con una passata leggera di lima sui laterali (pochi secondi).",
   "Se il problema si ripete su tutte le misure, è la forma della tip a essere sbagliata, non la tecnica.",
 ], "Fare la prova in diretta su un pollice: tip troppo grande, troppo piccola, giusta.", True),

 ("9. Preparare la tip (interno)", [
   "Mandrino con cilindro abrasivo (meglio se già usato; se nuovo, ammorbidirlo su una lima).",
   "Velocità 15.000–18.000 giri. Sotto i 15.000 la tip ballonzola, troppo alta la assottiglia.",
   "Opacizzare l'interno fino a dove arriva il letto ungueale: l'interno deve risultare ruvido e poroso.",
   "Movimento avanti-indietro al centro e sui laterali. Nel giro cuticola, all'inizio, solo in uscita; con l'esperienza anche avanti-indietro con micro movimenti.",
   "Fresa sempre parallela alla tip, mai di punta (rovina i laterali o buca).",
   "Mignolo: punta conica in ceramica, circa 15.000 giri.",
 ], "Ascoltare il rumore: cambia tra avanti-indietro e uscita. Appoggiare il mignolo per stabilità.", True),

 ("10. Applicazione passo passo", [
   "1. Dry manicure e unghia corta e stondata.",
   "2. Opacizzare l'interno della tip e spolverare tip e unghia.",
   "3. Deidratante, poi primer acid-free (anche dentro la tip).",
   "4. Base/extension gel sulla tip: una passata sottile 'a smalto' solo dove è opacizzata + una goccia scaricata nella tip.",
   "5. Appoggiare già con l'inclinazione giusta (niente colpo a vuoto), premere al centro e scendere lentamente, il gel cammina fino a fine letto ungueale.",
   "6. Polimerizzazione lampo 7-8 secondi per bloccare, poi 60 secondi in lampada.",
 ], "Con la cliente: la torcia la tiene lei, noi teniamo il dito e applichiamo la tip.", True),

 ("11. Errori di inclinazione e quantità", [
   "Movimento troppo veloce o troppo lento: il gel esce dai lati e sporca il giro cuticola.",
   "Colpo a vuoto o tip troppo vicina alla cuticola: scalino, bolle, pelle sporca.",
   "Il gel che 'cammina' indica la quantità giusta: né troppo né poco.",
   "Gel sbrodolato = rimozione lunga. Meglio prevenire con l'inclinazione corretta.",
 ], "Mostrare il video 'inclinazione errata vs corretta' come confronto.", True),

 ("12. Rifinitura e colore", [
   "Rimuovere il piccolo scalino al giro cuticola con punta dedicata, circa 18.000 giri: partire dal centro, mano leggera, stessa inclinazione del mandrino.",
   "Con la lima a grana fine solo una passata nel giro cuticola e intorno per togliere schegge.",
   "Pulire la punta sul buffer (i fori servono a liberare il gel) e riportare a velocità alta.",
   "Deidratante prima del colore. La tip è già lucida: non serve altro prima del colore.",
   "Colore: non partire dalla cuticola, un po' alla volta. Per i decori vicino alla cuticola, trattenere il respiro aiuta la precisione.",
 ], "Lo scalino rimosso evita che i capelli si impiglino durante la crescita.", True),

 ("13. Rimozione e rifacimento", [
   "Non esiste il refill: dopo 3–6 settimane si rimuove la tip e se ne applica una nuova.",
   "Tagliare la tip, poi rimuovere lucido e colore con la fresa: il remover non scioglie colore e top.",
   "Ammollo in remover per semipermanente per circa 5 minuti (oppure cotone + alluminio).",
   "Spingere via il gel con il pusher, una passata leggera di fresa per i residui, poi preparazione normale e nuova tip.",
   "Mentre una mano è in ammollo si lavora sull'altra: zero tempi morti.",
   "Vantaggio: la cliente può cambiare forma e lunghezza ad ogni appuntamento senza ricostruire nulla.",
 ], "Il vantaggio commerciale: nessun refill complicato, appuntamenti più rapidi e più clienti al giorno.", True),

 ("14. Messaggi chiave per la cliente", [
   "Unghia naturale corta = unghia protetta: se prendi un colpo, si rompe solo la tip.",
   "Risultato più sottile e naturale, senza bordi spessi.",
   "Appuntamento ogni 3–6 settimane per rimozione e nuova applicazione.",
   "Mai staccare la tip da sola.",
 ], "Da usare come script con la cliente, nel tono Lidia Nails.", True),
]

# Mini guida cliente (testo nostro, da validare con Lidia: le voci contrassegnate [nostra] non sono nel corso)
MINI_GUIDA = [
 ("Cosa sono le tue Gel Tip", ["Estensioni in gel morbido applicate su tutta l'unghia, leggere e naturali."]),
 ("Nei primi giorni", ["Evita acqua molto calda e prodotti aggressivi per 24 ore. [nostra]"]),
 ("Cura quotidiana", ["Usa i guanti per le pulizie. [nostra]", "Non usare le unghie come strumento (aprire lattine, grattare). [nostra]", "Olio per cuticole ogni giorno. [nostra]"]),
 ("Se ti si rompe qualcosa", ["La tua unghia naturale è protetta: si rompe solo la tip.", "Non staccarla da sola: scrivici e la sistemiamo."]),
 ("Quando tornare", ["Ogni 3–6 settimane: rimuoviamo la tip e ne applichiamo una nuova.", "Puoi cambiare forma e lunghezza a ogni appuntamento."]),
]

# Punti brevi per le slide (uno per sezione, stesso ordine di SEZIONI). Modificabili.
SLIDE_PUNTI = [
 ["Estensioni preformate in soft gel", "Coprono tutta l'unghia: cuticola → bordo libero + laterali", "Si applicano con il gel, non con la colla", "Metà del tempo, forme identiche su ogni dito"],
 ["Tip classiche: parziali, rigide, incollate", "Gel Tip: copertura totale, applicate con gel", "Press-on: unghie finte in ABS, uso occasionale", "Dual form: tecnica manuale, non è una tip"],
 ["Gel: flessibile ma resistente. ABS: rigida e cede", "Allarmi: prezzo troppo basso, ABS, struttura sbagliata", "Test della lima: odore di plastica bruciata = plastica", "Valutare la tip, non il marchio"],
 ["Spessore: sottile alla cuticola, più spesso al bordo libero", "Giro cuticola tondo a mezzaluna, senza angoli", "Profilo laterale morbido, laterali coperti", "No apice alto, no becco di pappagallo"],
 ["Trasparente: vedi il gel camminare, blocco in 7-8 secondi", "Colorata: meno controllo, luce più lenta, meno flessibile", "Semi-opaca: liscia dentro, già sottile → scartarla"],
 ["Lunghezze XS – XL", "14 misure (0–9 con le mezze)", "0–1 pollice · 2–6,5 dita centrali · 7–9 mignolo", "La numerazione cambia per forma e per mano"],
 ["Unghia corta, pari al polpastrello, stondata", "Lunga = tasche d'aria + effetto pappagallo", "Se si rompe, cede solo la tip", "Via TUTTO il vecchio prodotto"],
 ["Appoggia al centro e scorri", "Deve combaciare col punto di crescita", "Dubbio? La più grande (si flette)", "Troppo grande: lima i laterali. Troppo piccola: non si allarga"],
 ["15.000–18.000 giri, fresa parallela", "Opacizza l'interno fino al letto ungueale", "Giro cuticola: solo in uscita (all'inizio)", "Mignolo: punta conica in ceramica"],
 ["Dry manicure → opacizza → spolvera", "Deidratante + primer acid-free", "Base gel sottile + goccia nella tip", "Inclina, premi al centro, scendi lenta", "Lampo 7-8 s, poi 60 s in lampada"],
 ["Troppo veloce o troppo lento: gel sui lati", "Niente colpo a vuoto, non vicino alla cuticola", "Il gel che cammina = quantità giusta"],
 ["Scalino: punta dedicata 18.000 giri, mano leggera", "Lima fine solo nel giro cuticola", "Deidratante prima del colore", "Colore: mai partire dalla cuticola"],
 ["Nessun refill: si rimuove e si rifà (3–6 settimane)", "Taglia, togli colore con la fresa, ammollo 5 min", "Pusher + passata di fresa, poi nuova tip", "Una mano in ammollo, lavori sull'altra"],
 ["Unghia naturale corta = protetta", "Se prendi un colpo si rompe solo la tip", "Risultato sottile e naturale", "Mai staccarla da sola"],
]
