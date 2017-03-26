import pandas
import sys
from sklearn.ensemble import RandomForestClassifier
import numpy
# val1 = sys.argv[1]
# val2 = sys.argv[2]
# val3 = sys.argv[3]

# train = pandas.read_csv(val1)
# test = pandas.read_csv(val2)
# sub = pandas.read_csv(val3)

train = pandas.read_csv("train.csv")
test = pandas.read_csv("test.csv")
sub = pandas.read_csv("sample_submission.csv")

cols = ['bone_length', 'rotting_flesh', 'hair_length', 'has_soul']
colsRes = ['type']

trainArr = train.as_matrix(cols)
trainRes = train.as_matrix(colsRes)

rf = RandomForestClassifier(n_estimators = 100)

rf.fit(trainArr, trainRes)
importances = rf.feature_importances_
feat_imp = pandas.Series(rf.feature_importances_)
print(feat_imp)
print ("Features sorted by their score:")
print (rf.feature_importances_)
testArr = test.as_matrix(cols)
results = rf.predict(testArr)
test['type'] = results
#print(test['type'])

id = sub['id']
df = pandas.DataFrame(id)
df["type"] = test['type']
#df.to_csv("results.csv",index = False)