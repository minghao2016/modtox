import os
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import ensemble
import modtox.ML.preprocess as Pre
import modtox.ML.postprocess as Post
import modtox.ML.model2 as model

def retrieve_data(size=1500, split=True):
    X, y = datasets.make_blobs(n_samples=size, random_state=170, centers=2)
    if split==True:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        return X_train, X_test, y_train, y_test   
    else:
        return X,y

def retrieve_preprocessor(csv=None, fp=False, descriptors=False, MACCS=True, columns=None, app_domain=False):
    return Pre.ProcessorSDF(csv=csv, fp=fp, descriptors=descriptors, MACCS=MACCS, columns=columns, app_domain=app_domain)

def retrieve_model(clf, tpot=None):
    return model.GenericModel(clf=clf, tpot=tpot)

def retrieve_imputer():
    return model.Imputer(imputer_type='cluster_based', n_clusters=1)

def retrieve_processor(train_data=False):

    X_train, X_test, y_train, y_test = retrieve_data()
    clf = ensemble.RandomForestClassifier()
    clf.fit(X_train,y_train)
    y_pred = clf.predict(X_test)
    y_proba = clf.predict_proba(X_test)
 
    if train_data:
        return Post.PostProcessor(X_test, y_test, y_pred, y_proba, x_train=X_train, y_true_train=y_train)
    else:
        return Post.PostProcessor(X_test, y_test, y_pred, y_proba)


def clean(data):
    if isinstance(data, list):
        for i in data:
            if os.path.exists(i):
                os.remove(i)
    else:
        if os.path.exists(data):
            os.remove(data)
