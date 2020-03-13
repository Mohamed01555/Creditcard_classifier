"""
This classifier can predict with the help of Allah Creditcard Fraud and
nonfraud process
"""

from xgboost import XGBClassifier
import os
import numpy as np
import pandas as pd
import joblib
from flask import Flask,jsonify,request
from sklearn.model_selection import train_test_split

# df = pd.read_csv('creditcard.csv')


# X = df.drop('Class',axis=1)
# Y = df['Class']

# x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size = 0.2)
# x_train.shape,x_test.shape,y_train.shape,y_test.shape


# xg = XGBClassifier()
# xg.fit(x_train,y_train)
# print(xg.score(x_test,y_test))

model_dir = os.path.join(os.path.dirname(os.path.abspath("__file__")),'pikle','xg.pkl')

# def save_model():
#     joblib.dump(xg,model_dir,True)
def load_model():
    return joblib.load(model_dir)

# save_model()

def prepare_test_input(test_input):
    test_input = np.array(test_input)
    col = df.columns
    col = list(col)[:-1]
    prepared = pd.DataFrame(test_input.reshape(1,-1), columns=col)
    return prepared
    
x = load_model()
def test(test_input):
    p = prepare_test_input(test_input)
    pred = list(x.predict(p))
    prob = x.predict_proba(p)
    if pred[0] == 0:
        return f'Not Fraud with probability {prob[0][0]}'
    else:
        return f'Fraud with probability {prob[0][1]}'
    
app = Flask('__name__')
@app.route('/')
def index():
    return 'Welcome to CreditCard classifier'

@app.route('/clf',methods = ['POST'])
def classify():
    data = request.json
    pred = test(data)
    #print(type(data),pred[0])
    return jsonify(PREDICTION = pred)

app.run(debug = False)



