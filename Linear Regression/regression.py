import quandl as qdl
import pandas as pd
import math,datetime
import numpy as np
from sklearn import preprocessing,model_selection,svm
from sklearn.linear_model import  LinearRegression
import matplotlib.pyplot as plt
from   matplotlib import  style
import pickle

style.use('ggplot')
df = qdl.get('WIKI/GOOGL')

clf =  LinearRegression()
df = df[['Adj. Open','Adj. Low','Adj. High','Adj. Close','Adj. Volume']]

df['HL_PCT']= (df['Adj. High']-df['Adj. Low'])/df['Adj. Low'] *100.0
df['PCT_Change']= (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] *100.0

df = df[['Adj. Close','HL_PCT','PCT_Change','Adj. Volume']]

forecast_col ='Adj. Close'

df.fillna(-99999,inplace=True)

forecast_out= int(math.ceil(0.01*len(df)))
#print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)


x= np.array(df.drop(['label'],1))  #this feature
x= preprocessing.scale(x)
x_lately = x[-forecast_out:]
x=x[:-forecast_out]

df.dropna(inplace=True)
y= np.array(df['label']) #this is label


X_train,X_test,Y_train,Y_test = model_selection.train_test_split(x,y,test_size=0.2)


clf.fit(X_train,Y_train)

with open('linearregression.pickle','wb') as f :
    pickle.dump(clf,f)

#pickle_in = open('linearregression.pickle','rb')
# clf = pickle.load(pickle_in)

confidence=clf.score(X_test,Y_test)
forecast_set = clf.predict(x_lately)

print(forecast_set,confidence,forecast_out)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set :
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix+=one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
