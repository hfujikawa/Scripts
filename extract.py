# https://github.com/bwiley1/pandleau
# https://help.tableau.com/current/api/sdk/en-us/help.htm#SDK/tableau_sdk_installing.htm%3FTocPath%3D_____3
# get 'dataextract' package for your python installation from http://www.tableau.com/data-extract-api
# script tested on Python 2.7 - 32 bit instance on Windows 10
# By Ashish Chauhan | originally published on http://doingdata.org/blog | follow on http://twitter.com/ashishyoungy for more

# step 01 import requirements
# #########################################################
import pandas
import dataextract as tde

# step 02 get the data into python
# #########################################################
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pandas.read_csv(url, names = names)

# step 03 create a blank extract
# #########################################################
dataExtract = tde.Extract('irisExtract.tde')

# step 04 define schema
# #########################################################
dataSchema = tde.TableDefinition()
dataSchema.addColumn('sepal-length',	tde.Type.DOUBLE)
dataSchema.addColumn('sepal-width',		tde.Type.DOUBLE)
dataSchema.addColumn('petal-length',	tde.Type.DOUBLE)
dataSchema.addColumn('petal-width',		tde.Type.DOUBLE)
dataSchema.addColumn('class',			tde.Type.CHAR_STRING)

# step 05 connect schema with blank extract
# #########################################################
table = dataExtract.addTable('Extract',dataSchema)

# step 06 fill extract with data
# #########################################################
newRow = tde.Row(dataSchema)
for i in range(0, len(dataset)):
	newRow.setDouble		(0, dataset['sepal-length'][i])
	newRow.setDouble		(1, dataset['sepal-width'][i])
	newRow.setDouble		(2, dataset['petal-length'][i])
	newRow.setDouble		(3, dataset['petal-width'][i])
	newRow.setCharString	(4, dataset['class'][i])
	table.insert(newRow)
	
# step 07 close the extract
# #########################################################
dataExtract.close()