__author__ = 'Loganaich Mac Giolla Eoin'
"""




Income predictor

Using a dataset ( the "Adult Data Set") from the UCI Machine-Learning Repository we can predict based on a number of
factors whether someone's income will be greater than $50,000.

THE TECHNIQUE
The approach is to create a 'classifier' - a program that takes a new example record and, based on previous examples,
determines which 'class' it belongs to. In this problem we consider attributes of records and separate these into two
broad classes, <50K and >=50K.

We begin with a training data set - examples with known solutions. The classifier looks for patterns that indicate
classification. These patterns can be applied against new data to predict outcomes. If we already know the outcomes
of the test data, we can test the reliability of our model. if it proves reliable we could then use it to classify data
with unknown outcomes.

We must train the classifier to establish an internal model of the patterns that distinguish our two classes. Once
trained we can apply this against the test data - which has known outcomes.

We take our data and split it into two groups - training and test - with most of the data in the training set.

We need to write a program to find the patterns in the training set.

BUILDING THE CLASSIFIER
Look at the attributes and, for each of the two outcomes, make an average value for each one
Then average these two results for each attribute to compute a midpoint or 'class separation value'.

For each record, test whether each attribute is above or below its midpoint value and flag it accordingly.
For each record the overall result is the greater count of the individual results (<50K, >=50K)

You'll know your model works iff you achieve the same results as thee known result for the records. You should track
the accuracy of your model, i.e how many correct classifications you made as a percentage of the total
number of records.

PROCESS OVERVIEW
Create training set from data
Create classifier using training dataset to determine separator values for each attribute
Create test dataset
Use classifier to classify data in test set while maintaining accuracy score


THE DATA
The data is presented in the form of a comma-delimited text file (CSV) which has the following structure:

Listing of attributes:

1. Age: Number
2. Workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-workedde
3. fnlwgt: NOT NEEDED
4. Education: NOT NEEDED
5. Education-number: Number
6. Marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
7. Occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
8. Relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried
9. Race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
10. Sex: Female, Male.
11. Capital-gain: Number````````````
12. Capital-loss: Number
13. Hours-per-week: Number
14. Native-country: NOT NEEDED
15. Outcome for this record: Can be >50K or <=50K.

Data is available from http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
You should be able to read this directly from the Internet..

Fields that have 'discrete' attributes such as 'Relationship' can be given a numeric weight by counting the number of 4
occurrances as a fraction of the total number of positive records (outcome >= 50K) and negative records (outcome < 50K).
So, if we have 10 positive records and they have values Wife:2, Own-child: 3, Husband:2, Not-in-family:1,
Other-realtive:1 and Unmarried:1 then this would yield factors of 0.2, 0.3, 0.2, 0.1, 0.1 and 0.1 respectively.
"""

import httplib2
import string

listdata = []
total_under_fifty = 0
total_over_fifty = 0

workclass_dict_under50 = {}
marital_status_dict_under50 = {}
occupation_dict_under50 = {}
relationship_dict_under50 = {}
race_dict_under50 = {}
sex_dict_under50 = {}

workclass_dict_over50 = {}
marital_status_dict_over50 = {}
occupation_dict_over50 = {}
relationship_dict_over50 = {}
race_dict_over50 = {}
sex_dict_over50 = {}

items_under = {"workclass_dict_under50", 1,  "marital_status_dict_under50", 5,  "occupation_dict_under50", 6, "relationship_dict_under50", 7 , "race_dict_under50", 8 , "sex_dict_under50", 9}

items_over = {"workclass_dict_over50", 1, "marital_status_dict_over50", 5, "occupation_dict_over50", 6, "relationship_dict_over50", 7, "race_dict_over50", 8, "sex_dict_over50", 9}

try:

    h = httplib2.Http(".cache")
    resp, content = h.request("http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", "GET")
    print("Downloaded file successfully")
    content = content.decode("utf-8").split("\n")

    for line in content:
        store = list(line.strip(string.whitespace).lower().split(", "))
        listdata.append(store)

except ValueError:
    print("Unable to download file. Please ensure you are connected to the internet.")

try:
    for line in listdata:
        line[0] = int(line[0])
        line[13] = None
        line[2] = None
        line[3] = None
        line[4] = int(line[4])
        line[10] = int(line[10])
        line[11] = int(line[11])
        line[12] = int(line[12])


except ValueError:
    print("line has an error in it:", line)

cleandata = [line for line in listdata if "?" not in line]
print("len of cleandata:",len(cleandata))


try:
    for line in cleandata:

        if "<=50k" in line:
            total_under_fifty += 1

            if line[1] not in workclass_dict_under50:
                workclass_dict_under50[str(line[1])] = 1
            elif line[1] in workclass_dict_under50:
                workclass_dict_under50[str(line[1])] += 1

            if line[5] not in marital_status_dict_under50:
                marital_status_dict_under50[str(line[5])] = 1
            elif line[5] in marital_status_dict_under50:
                marital_status_dict_under50[str(line[5])] += 1

            if line[6] not in occupation_dict_under50:
                occupation_dict_under50[str(line[6])] = 1
            elif line[6] in occupation_dict_under50:
                occupation_dict_under50[str(line[6])] += 1

            if line[7] not in relationship_dict_under50:
                relationship_dict_under50[str(line[7])] = 1
            elif line[7] in relationship_dict_under50:
                relationship_dict_under50[str(line[7])] += 1

            if line[8] not in race_dict_under50:
                race_dict_under50[str(line[8])] = 1
            elif line[8] in race_dict_under50:
                race_dict_under50[str(line[8])] += 1

            if line[9] not in sex_dict_under50:
                sex_dict_under50[str(line[9])] = 1
            elif line[9] in sex_dict_under50:
                sex_dict_under50[str(line[9])] += 1


        elif line[-1] == ">50k":
            total_over_fifty += 1

            if line[1] not in workclass_dict_over50:
                workclass_dict_over50[str(line[1])] = 1
            elif line[1] in workclass_dict_over50:
                workclass_dict_over50[str(line[1])] += 1

            if line[5] not in marital_status_dict_over50:
                marital_status_dict_over50[str(line[5])] = 1
            elif line[5] in marital_status_dict_over50:
                marital_status_dict_over50[str(line[5])] += 1

            if line[6] not in occupation_dict_over50:
                occupation_dict_over50[str(line[6])] = 1
            elif line[6] in occupation_dict_over50:
                occupation_dict_over50[str(line[6])] += 1

            if line[7] not in relationship_dict_over50:
                relationship_dict_over50[str(line[7])] = 1
            elif line[7] in relationship_dict_over50:
                relationship_dict_over50[str(line[7])] += 1

            if line[8] not in race_dict_over50:
                race_dict_over50[str(line[8])] = 1
            elif line[8] in race_dict_over50:
                race_dict_over50[str(line[8])] += 1

            if line[9] not in sex_dict_over50:
                sex_dict_over50[str(line[9])] = 1
            elif line[9] in sex_dict_over50:
                sex_dict_over50[str(line[9])] += 1

except ValueError:
    print("This line caused an error", line)

for line in cleandata:
    if line[-1] == "<=50k":
        line[1] = workclass_dict_under50[str(line[1])] / total_under_fifty
        line[5] = marital_status_dict_under50[str(line[5])] / total_under_fifty
        line[6] = occupation_dict_under50[str(line[6])] / total_under_fifty
        line[7] = relationship_dict_under50[str(line[7])] / total_under_fifty
        line[8] = race_dict_under50[str(line[8])] / total_under_fifty
        line[9] = sex_dict_under50[str(line[9])] / total_under_fifty

    elif line[-1] == ">50k":
        line[1] = workclass_dict_over50[str(line[1])] / total_over_fifty
        line[5] = marital_status_dict_over50[str(line[5])] / total_over_fifty
        line[6] = occupation_dict_over50[str(line[6])] / total_over_fifty
        line[7] = relationship_dict_over50[str(line[7])] / total_over_fifty
        line[8] = race_dict_over50[str(line[8])] / total_over_fifty
        line[9] = sex_dict_over50[str(line[9])] / total_over_fifty


for line in cleandata:
    with open("dump.txt", "a") as out_file:
       out_file.write(str(line) + "\n")



traing_data = cleandata[:len(cleandata) / 75]
test_data = cleandata[len(cleandata) / 75:]


#print("workclass_dict_under50:", workclass_dict_under50)
#print("workclass_dict_over50:", workclass_dict_over50)
#print("marital_status_dict_under50:", marital_status_dict_under50)
#print("marital_status_dict_over50:", marital_status_dict_over50)
#print("---------------------------- \nless than fifty is", total_under_fifty)
#print("greater than fifty", total_over_fifty)

#print("values of workclass dictionary", workclass_dict_over50.values())


"""
1. Age: Number
2. Workclass: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-workedde
3. fnlwgt: NOT NEEDED
4. Education: NOT NEEDED
5. Education-number: Number
6. Marital-status: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
7. Occupation: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
8. Relationship: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried
9. Race: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black
10. Sex: Female, Male.
capital-gain: Number
capital-loss: Number
hours-per-week: Number
14. Native-country: NOT NEEDED
15. >50K or <=50K.








sum_of_ages = 0
count_of_ages = 0
try:
    for row in listdata:
        sum_of_ages += int(row[0])
        count_of_ages += 1
    else:
        print("dddd")
except ValueError as e:
    print(e)

average_age = sum_of_ages / count_of_ages
print("Avergae age is", average_age)

#except:
#    print ("Could not download the file required for this program. Please ensure you are connected to the internet.")



print (resp)
#strip()
datalines = []
for line in data:
    i = list(line)
    datalines.append(i)
print (datalines[1])


if __name__ == "__main__"
    main()

"""
