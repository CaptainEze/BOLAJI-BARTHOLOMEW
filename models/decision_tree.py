from sklearn.tree import DecisionTreeClassifier

def decision_tree_adoption(df, max_depth=3):
    df["Adoption_Level"] = (df["Adoption_Avg"] > df["Adoption_Avg"].median()).astype(int)

    X = df[["D_Position", "D_Experience", "Delivery_Avg", "Sustainability_Avg"]]
    y = df["Adoption_Level"]

    tree = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    tree.fit(X, y)

    return tree, X.columns
