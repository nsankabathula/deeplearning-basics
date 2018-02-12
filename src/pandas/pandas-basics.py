import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print ('DataFrame:\n', df);

df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print ('DataFrame:\n', df);


data =[ {'name':'Sandy', 'gender':'F', 'isHuman':False}, {'name':'Naveen', 'gender':'M', 'isHuman':1000.23}]
df = pd.DataFrame(data)
print ('DataFrame:\n', df);


# Test https://www.w3resource.com/python-exercises/pandas/index.php (Panda.Series)
ds = pd.Series([2, 4, 6, 8, 10])
print('\n', ds.tolist());

a = pd.Series([2, 4, 6, 8, 10]);
b = pd.Series([1, 3, 5, 7, 9]);

print ("Add \n", a + b);
print ("Diff \n", a - b);
print ("Product \n", a * b);
print ("Division \n", a / b);


#Test 4
print ("\n******************Test 4***********************\n ")
test4_a = pd.Series([2, 4, 6, 8, 10]);
test4_b = pd.Series([1, 3, 5, 7, 9]);

# incomplete..
print ("\n=======================End=====================\n ")

# Panda DataFrame Test


print ("\n****************** DataFrame Test 2 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print ("DataFrame Test 2 \n", df);


print ("\n=======================End=====================\n ")

print ("\n****************** DataFrame Test 3 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print ("DataFrame Test 3 \n", df.groupby('qualify').count());

print ("DataFrame Test Actual sol \n", df.info());


print ("\n=======================End=====================\n ")

print ("\n****************** DataFrame Test 4 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print ("DataFrame Test 4 \n", df[:3]);
print ("Actual Sol 4 \n", df.iloc[:3]);

print ("\n=======================End=====================\n ")



print ("\n****************** DataFrame Test 5 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print ("DataFrame Test 5 \n", df[:3][['name','score']]);


print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 6 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print(df.iloc[[1, 3, 5, 6]][['name', 'score']])


print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 7 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

print(df[df.attempts > 2])


print ("\n=======================End=====================\n ")

print ("\n****************** DataFrame Test 8 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print(df.__len__());
print(df.transpose().__len__());

print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 9 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print(df[df.score.isnull()])

print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 10 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print(df[df.score.between(15, 20)])
print(df[(df['score'] >=15) & (df['score'] <= 20)])

print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 11 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print(df[(df['score'] >15) & (df['attempts'] < 2)])

print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 12 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
df.loc['d','score'] = 11.5;
print(df.loc['d'])


print ("\n=======================End=====================\n ")

print ("\n****************** DataFrame Test 13 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print (df['attempts'].sum());


print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 14 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
print (df['score'].mean());


print ("\n=======================End=====================\n ")

print ("\n****************** DataFrame Test 15 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

newrow = {'name' : "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}

df = pd.DataFrame(exam_data, index=labels);
df.loc['k'] = newrow

#print('!!! INCOMPLETE !!!');

print ('New Row:\n', df);

df = df.drop('k');

print ('Row Drop:\n', df);
print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 16 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

newrow = {'name' : "Suresh", 'score': 15.5, 'attempts': 1, 'qualify': "yes"}

df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');

#print (df.sort_values(ascending=False,by='name').sort_values(ascending=True, by='score'));
print ('Actual Solution:\n', df.sort_values(ascending=[False,True],by=['name','score']));
print ("\n=======================End=====================\n ")


print ("\n****************** DataFrame Test 17 ***********************\n ")
exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    }
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']



df = pd.DataFrame(exam_data, index=labels);

#print('!!! INCOMPLETE !!!');
df['qualify'] = df['qualify'].map({'yes': True, 'no': False});

print ('Solution: \n', df);


print ("\n=======================End=====================\n ")


PATH="C:\\Users\\nsankabathula\\Downloads\\Zip_Zri_AllHomesPlusMultifamily.csv"
table_names = ['zillow']
tables_data = [pd.read_csv(PATH, low_memory=False) for fname in table_names];

for t in tables_data: print(t.head())

tbl_data = tables_data[0]

print ('Count', tbl_data.count())

print ('Sum:', tbl_data.sum())

print ('SD:', tbl_data.std())

#print ('Summary:', tbl_data.describe(include='all'))

summary = tbl_data.describe(include='all')
grouped = tbl_data.groupby('State');

ny_indexs = np.where(tbl_data['State']=='NY')

print (ny_indexs);

ny_data =tbl_data.iloc[ny_indexs][['City','RegionName','SizeRank','2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12']]
print (ny_data);

#df[:3][['name','score']]
x_axis = ny_data.loc[150:,['SizeRank']]['SizeRank'].values;
y_axis = ny_data.loc[150:,['City']]['City'].values;
#y_axis = np.array(['2017-01','2017-02','2017-03','2017-04','2017-05','2017-06','2017-07','2017-08','2017-09','2017-10','2017-11','2017-12']);

#print (y_axis['RegionName'].values);
#print (x_axis['SizeRank'].values);

#plt.plot(y_axis, x_axis)
# Show the plot
#plt.show()

#plt.plot(x_axis, ['2017-01']);
#plt.legend()
#plt.show();
