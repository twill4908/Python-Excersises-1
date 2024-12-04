from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()

logreg.fit(x_train, y_train)
#want to past a list of observations in the predications
print(logreg.predict([ [6.7, 3.3, 5.7, 2.5]]))

#probability of each diff species
print(logreg.predict_proba([ [6.7, 3.3, 5.7, 2.5]]))

#This is variable logreg
predictions_logreg = logreg.predict(x_test)
performance_logreg = metrics.accuracy_score(y_test, predictions_logreg)
print(performance_logreg)