import gspread
from django.conf import settings
import pandas as pd


spreadsheetName = 'Copia de Control 2020 Test'
gc = gspread.oauth()
sh = gc.open(spreadsheetName)
calificaciones= sh.worksheet('Calificación')
calificaciones = calificaciones.get_all_values()
calificaciones= pd.DataFrame(calificaciones[1:], columns=calificaciones[0])



