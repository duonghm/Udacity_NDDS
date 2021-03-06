import sys
from sqlalchemy import create_engine
import pandas as pd
import nltk
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.multioutput import MultiOutputClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
import pickle


nltk.download(['omw-1.4', 'punkt', 'wordnet'])


def load_data(database_filepath):
    """Load data from sqlite database"""
    engine = create_engine(f'sqlite:///{database_filepath}')
    df = pd.read_sql_table('disaster_messages', con=engine)
    X = df['message']
    Y = df.drop(columns=['id', 'message', 'original', 'genre'])
    category_names = Y.columns
    return X, Y, category_names


def tokenize(text):
    """Tokenize and lemmatize text"""
    tokens = nltk.word_tokenize(text)
    lemmer = nltk.stem.wordnet.WordNetLemmatizer()
    lemmed = [lemmer.lemmatize(t).lower().strip() for t in tokens]
    return lemmed


def build_model():
    """Create data processing, model pipeline"""
    pipeline = Pipeline([
        ('vectorizer', CountVectorizer(tokenizer=tokenize)),
        ('tfidf', TfidfTransformer()),
        ('rf', MultiOutputClassifier(RandomForestClassifier()))
    ])
    parameters = {
        'rf__estimator__n_estimators': [50, 100],
        'rf__estimator__max_depth': [6, 10]
    }
    cv = GridSearchCV(pipeline, param_grid=parameters, verbose=5, n_jobs=-1, cv=2)
    return cv


def evaluate_model(model, X_test, Y_test, category_names):
    """Show the classification result for each output categories"""
    Y_pred = model.predict(X_test)
    for i, col in enumerate(category_names):
        print(i, col)
        print(classification_report(Y_test[col], Y_pred[:, i]))


def save_model(model, model_filepath):
    """Export model into pickle object"""
    pickle.dump(model, open(model_filepath, 'wb'))


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()