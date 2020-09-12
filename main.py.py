# 1 Declaring the required dependencies for our project
from sklearn import tree
import pandas as pd
import pydotplus
from IPython.display import Image

# 2 Creating our data frame from scratch and print the data frame

# 2.1 Create an empty data frame
clubsDF = pd.DataFrame()

# 2.2 Adding the t-shirt column:
clubsDF['t-shirt'] = [
    'Red', 'Red', 'Red', 'Blue', 'White', 'White', 'Red',
    'White', 'Red', 'Yellow', 'Red', 'SkyBlue', 'Black',
    'Blue'
]

# 2.3 Adding the short column:
clubsDF['short'] = [
    'White', 'Red', 'White', 'Blue', 'Black', 'White', 'Blue',
    'White', 'Red', 'Black', 'Black', 'SkyBlue', 'White',
    'Black'
]

# 2.4 Adding the target (clubs) column:
clubsDF['clubs'] = [
    'Man Utd.', 'Liverpool', 'Arsenal', 'Chelsea', 'Tottenham',
    'Real Madrid', 'Barcelona', 'Sevilla', 'Bayern Munich',
    'Broussia Dortumond', 'AC. Milan', 'Napoli', 'Juventus',
    'Inter Milan'
]

print(clubsDF)

# 3 Convert the table data from string to binary (0 and 1)
ClubsBinaryData = pd.get_dummies(clubsDF[['t-shirt', 'short']])
print(ClubsBinaryData)

# 4 Creating our decision tree classifier
Clf = tree.DecisionTreeClassifier()

# 4.1 Train our model (Decision Tree Algorthim)
clfTrain = Clf.fit(ClubsBinaryData, clubsDF['clubs'])

# 4.2 Export our tree in DOT format
TreeDotData = tree.export_graphviz(clfTrain, out_file=None,
                                   feature_names=list(
                                       ClubsBinaryData.columns.values),
                                   rounded=True, filled=True, class_names=clubsDF['clubs'].unique())
print(TreeDotData)

# 5 Create an image graph for our model results
finalGraph = pydotplus.graph_from_dot_data(TreeDotData)
Image(finalGraph.create_png())

# 6 Test the model (the algorithm) with our data below:
# Assume that: t-shirt = "Black", short="White"

prediction = clfTrain.predict([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]])
print("The club is:", ''.join(prediction))
