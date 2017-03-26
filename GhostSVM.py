from sklearn import svm
import pandas
import numpy


trainArr_data = pandas.read_csv("xgboost.csv")
result_data = pandas.read_csv("xgboosttest.csv")
sub = pandas.read_csv("sample_submission.csv")
trainArr = pandas.DataFrame(trainArr_data, columns= [
'bone_length', 'rotting_flesh', 'hair_length', 'has_soul', 'black', 'blood', 'blue', 'clear', 'green', 'white'])
#trainArr['rotting_flesh'] = trainArr['rotting_flesh']*2
# trainArr['bone_length'] = trainArr['bone_length']*2
#trainArr['hair_length'] = trainArr['hair_length']*4
#trainArr['has_soul'] = trainArr['has_soul']*3
 # 리스트값
typeArr = pandas.Series(trainArr_data['type'])
resultObj = pandas.DataFrame(result_data, columns= [
	'bone_length', 'rotting_flesh', 'hair_length', 'has_soul', 'black', 'blood', 'blue', 'clear', 'green', 'white'])
# resultObj['bone_length'] = resultObj['bone_length']*2
#resultObj['rotting_flesh'] = resultObj['rotting_flesh']*2
#resultObj['hair_length'] = resultObj['hair_length']*4
#resultObj['has_soul'] = resultObj['has_soul']*3
clf = svm.SVC()
clf.fit(trainArr,typeArr)
result = []
c = ""
for a in resultObj.index:
	b = list(resultObj.ix[a])
	c = str(clf.predict([b])).replace("['","").replace("']","")
	result.append(c)
	print(clf.predict([b]))

id = sub['id']
df = pandas.DataFrame(id)
df["type"] = result
df.to_csv("GhostSVMxgboost.csv",index=False)