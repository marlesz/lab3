import arcpy
import numpy
x = arcpy.da.FeatureClassToNumPyArray("powiaty","POP")
y = arcpy.da.FeatureClassToNumPyArray("powiaty","POLE_KM2")
print numpy.corrcoef(x,y)[0,1]

