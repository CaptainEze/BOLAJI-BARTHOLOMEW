from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def classify_adoption_delivery(df):
    X = df[["Adoption_Avg", "D_Position", "D_Experience"]]
    y = (df["Delivery_Avg"] > df["Delivery_Avg"].median()).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)

    report = classification_report(y_test, y_pred, output_dict=True)
    return report, clf
