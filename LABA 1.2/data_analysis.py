from matplotlib import pyplot
from openpyxl import load_workbook

wb=load_workbook("data_analysis_lab.xlsx")
sheet=wb["Data"]
ears = sheet['A'][1:]
temperatures = sheet['D'][1:]
relative_temperature = sheet['C'][1:]

def getvalue(x): return x.value
list_x=list(map(getvalue,ears))
list_z=list(map(getvalue,temperatures))
list_y=list(map(getvalue,relative_temperature))
pyplot.plot(list_x, list_y )
pyplot.plot(list_x, list_z )

pyplot.show()
