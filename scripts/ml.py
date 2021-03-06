import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import re

!pip
install
emoji

hope = pd.read_csv('/content/preprocessed_KanHopeEDI.csv', delimiter=',', header=None, names=['class', 'sentence'])

hope

!pip
install
ecco
import warnings

warnings.filterwarnings('ignore')

!pip
install - U
tensorboard

# text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text, flags=re.MULTILINE)
import emoji


def preprocessing(df):
    # for text in df['sentence']:
    df['sentence'] = df['sentence'].str.replace(r'^https?:\/\/.*[\r\n]*', 'URL')
    #    text = re.sub(r'^https?:\/\/.*[\r\n]*', '', text)
    df['sentence'] = df['sentence'].str.replace(r"[+/#@&*$%:0-9]", '')
    # df['sentence'] = df['sentence']
    for i in range(len(df['sentence'])):
        df['sentence'][i] = emoji.demojize(df['sentence'][i], delimiters=(" ", " "))
    #    text = re.sub(r"[+/#@&*$%:0-9]",'',text)
    print(df)


preprocessing(hope)

hope.head(10)

hope.to_csv('demoji_KanHopeEDI.csv')

hope_new = hope[:6815]
print(hope_new.shape)
hope_new.head()

index_names = hope[hope['class'] == 'not-Kannada'].index
hope = hope.drop(index_names, inplace=False)

hope['class'].value_counts()

labels = hope['class'].values
X_train, X_test, y_train, y_test = train_test_split(hope['sentence'], labels, test_size=0.2, random_state=42)
X_test, X_val, y_test, y_val = train_test_split(hope['sentence'], labels, test_size=0.5, random_state=42)

train = pd.DataFrame()
val = pd.DataFrame()
test = pd.DataFrame()
train['sentence'] = X_train
train['class'] = y_train
test['class'] = X_test
test['sentence'] = y_test
val['class'] = X_val
val['sentence'] = y_val

train.to_csv('train_hope.csv', columns=['sentence', 'class'])
test.to_csv('test_hope.csv', columns=['sentence', 'class'])
val.to_csv('val_hope.csv', columns=['sentence', 'class'])

train = pd.read_csv('/content/multichannelhope.csv')
# train['labels']=LabelEncoder().fit_transform(train['class'])
train = train.drop(columns=['Unnamed: 0'])
train.head(10)

test = pd.read_csv('/content/multichannelhope_test.csv')
# test['lables'] = LabelEncoder().fit_transform(test['class'])
test['labels'] = test['lables']
test = test.drop(columns=['Unnamed: 0', 'lables'])
test.head(10)

X_train, y_train = train['translation'], train['labels']
X_test, y_test = test['translation'], test['labels']

vectorizer = TfidfVectorizer(min_df=10)
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

test = pd.read_csv('/content/multichannelhope_test.csv')
# test['lables'] = LabelEncoder().fit_transform(test['class'])
test['labels'] = test['lables']
test = test.drop(columns=['Unnamed: 0', 'lables'])
test.head(10)

"""# Logistic Regression"""

from sklearn.linear_model import LogisticRegression

model = LogisticRegression(penalty="l2", C=0.1)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

"""# KNN"""

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=7)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

"""# Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(min_samples_split=2)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

"""# Random Forest
"""

from sklearn.ensemble import RandomForestClassifier

# y_train = offensive['class'].values
text_classifier = RandomForestClassifier()
text_classifier.fit(X_train, y_train)

y_pred = text_classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

y_pred = text_classifier.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

"""# Naive Bayes
"""

from sklearn.naive_bayes import MultinomialNB

model = MultinomialNB()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

"""# SVM """

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))

from sklearn.svm import LinearSVC

model = LinearSVC()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, digits=3))
print(accuracy_score(y_test, y_pred))