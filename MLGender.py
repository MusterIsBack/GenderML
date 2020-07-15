import csv
from sklearn import tree

x = []
y = []
# Reading data in CSV file
with open ('myfile.csv' , 'r') as csvfile:
    data = csv.reader(csvfile)
    for line in data:
        x.append(line[0:2])
        y.append(line[2])

# Machine learning to calculate gender
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x , y)

# Enter data from user
new_data = []
entry = int(input("How much data you wanna enter? (Like: 3) \n"))
for i in range (0 , entry):
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    z = height , weight
    new_data.append(z)

# Calculate ML
answer = clf.predict(new_data)

# Display result line by line
counter1 , counter2 = 0 , 1
for n in range (0 , entry):
    print('Gender number {} is: ' .format(counter2) , answer[counter1])
    counter1 += 1
    counter2 += 1