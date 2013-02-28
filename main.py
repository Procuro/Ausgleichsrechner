# Ausgleichsrechner

import datetime
import datensatz

rr=datensatz.Rechnung()

rr.SetAmount(12)
rr.SetDate(datetime.date(2013,2,4))
rr.SetDescription("bloede beschreibung")
rr.SetComment("laeuft")
rr.SetCity("Brandenburg")

print("Betrag =", rr.GetAmount())
print("Datum =", rr.GetDate())
print("Ort =", rr.GetCity())
print("Beschreibung =", rr.GetDescription())
print("Kommentar =", rr.GetComment())



