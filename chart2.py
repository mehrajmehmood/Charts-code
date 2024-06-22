import plotly.express as px
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
fig = px.scatter(x=['Random Forest'], y=[accuracy], title='Model Performance')
fig.update_layout(yaxis_title='Accuracy')
fig.show()
feature_importance = rf.feature_importances_
fig = px.bar(x=X.columns, y=feature_importance, title='Feature Importance')
fig.update_layout(xaxis_title='Features', yaxis_title='Importance')
fig.show()
