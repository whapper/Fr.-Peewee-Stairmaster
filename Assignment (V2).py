import httplib2
import string


def get_data(url):
    "Downloads the contents of the URL passed in, splits it into new lines, strips all whitespace characters, changes all characters to lowercase, each line as a list."
    try:
        h = httplib2.Http(".cache")
        resp, content = h.request("{}".format(url), "GET")
        print("Downloaded file successfully")
        content = content.decode("utf-8").split("\n")

        listdata = []
        for line in content:
            store = line.lower().strip(string.whitespace)
            store = store.split(", ")
            listdata.append(store)
        return listdata

    except ValueError:
        print("Unable to download file. Please ensure you are connected to the internet.")


def clean_up(data):
    "Takes in a list and iterates over the lines to exclude any line containing bad data, delete unused entries and convert known numbers to intergers. Returns a list of cleaned data"
    cleandata = []
    try:
        for line in data:
            if "?" not in line:
                line[0] = int(line[0])
                line[4] = int(line[4])
                line[10] = int(line[10])
                line[11] = int(line[11])
                line[12] = int(line[12])
                del line[13]
                del line[3]
                del line[2]
                cleandata.append(line)

    except:
        pass

    return cleandata


def count_values(data):
    "Creates dictionaries to store the keys for the different entries and uses the value as a counter for the amount of times each one occurs in the dataset. String values in the dataset are then replaced with the average numeric value for their category"

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


    try:
        for line in data:
            if "<=50k" in line:
                total_under_fifty += 1

                if line[1] not in workclass_dict_under50:
                    workclass_dict_under50[str(line[1])] = 1
                elif line[1] in workclass_dict_under50:
                    workclass_dict_under50[str(line[1])] += 1

                if line[3] not in marital_status_dict_under50:
                    marital_status_dict_under50[str(line[3])] = 1
                elif line[3] in marital_status_dict_under50:
                    marital_status_dict_under50[str(line[3])] += 1

                if line[4] not in occupation_dict_under50:
                    occupation_dict_under50[str(line[4])] = 1
                elif line[4] in occupation_dict_under50:
                    occupation_dict_under50[str(line[4])] += 1

                if line[5] not in relationship_dict_under50:
                    relationship_dict_under50[str(line[5])] = 1
                elif line[5] in relationship_dict_under50:
                    relationship_dict_under50[str(line[5])] += 1

                if line[6] not in race_dict_under50:
                    race_dict_under50[str(line[6])] = 1
                elif line[6] in race_dict_under50:
                    race_dict_under50[str(line[6])] += 1

                if line[7] not in sex_dict_under50:
                    sex_dict_under50[str(line[7])] = 1
                elif line[7] in sex_dict_under50:
                    sex_dict_under50[str(line[7])] += 1

            elif line[-1] == ">50k":
                total_over_fifty += 1

                if line[1] not in workclass_dict_over50:
                    workclass_dict_over50[str(line[1])] = 1
                elif line[1] in workclass_dict_over50:
                    workclass_dict_over50[str(line[1])] += 1

                if line[3] not in marital_status_dict_over50:
                    marital_status_dict_over50[str(line[3])] = 1
                elif line[3] in marital_status_dict_over50:
                    marital_status_dict_over50[str(line[3])] += 1

                if line[4] not in occupation_dict_over50:
                    occupation_dict_over50[str(line[4])] = 1
                elif line[4] in occupation_dict_over50:
                    occupation_dict_over50[str(line[4])] += 1

                if line[5] not in relationship_dict_over50:
                    relationship_dict_over50[str(line[5])] = 1
                elif line[5] in relationship_dict_over50:
                    relationship_dict_over50[str(line[5])] += 1

                if line[6] not in race_dict_over50:
                    race_dict_over50[str(line[6])] = 1
                elif line[6] in race_dict_over50:
                    race_dict_over50[str(line[6])] += 1

                if line[7] not in sex_dict_over50:
                    sex_dict_over50[str(line[7])] = 1
                elif line[7] in sex_dict_over50:
                    sex_dict_over50[str(line[7])] += 1

    except ValueError:
        pass

    for line in data:
        if line[-1] == "<=50k":
            line[1] = workclass_dict_under50[str(line[1])] / total_under_fifty
            line[3] = marital_status_dict_under50[str(line[3])] / total_under_fifty
            line[4] = occupation_dict_under50[str(line[4])] / total_under_fifty
            line[5] = relationship_dict_under50[str(line[5])] / total_under_fifty
            line[6] = race_dict_under50[str(line[6])] / total_under_fifty
            line[7] = sex_dict_under50[str(line[7])] / total_under_fifty

        elif line[-1] == ">50k":
            line[1] = workclass_dict_over50[str(line[1])] / total_over_fifty
            line[3] = marital_status_dict_over50[str(line[3])] / total_over_fifty
            line[4] = occupation_dict_over50[str(line[4])] / total_over_fifty
            line[5] = relationship_dict_over50[str(line[5])] / total_over_fifty
            line[6] = race_dict_over50[str(line[6])] / total_over_fifty
            line[7] = sex_dict_over50[str(line[7])] / total_over_fifty

    return data

"""
averages_under = []
averages_over = []

age_total_under = 0
workclass_total_under = 0
education_num_total_under = 0
marital_status_total_under = 0
occupation_total_under = 0
relationship_total_under = 0
sex_total_under = 0
race_total_under = 0
gain_total_under = 0
loss_total_under = 0
hours_total_under = 0

age_total_over = 0
workclass_total_over = 0
education_num_total_over = 0
marital_status_total_over = 0
occupation_total_over = 0
relationship_total_over = 0
sex_total_over = 0
race_total_over = 0
gain_total_over = 0
loss_total_over = 0
hours_total_over = 0

total_training_under = 0
total_training_over = 0

for line in training_data:
    if line[-1] == "<=50k":
        total_training_under += 1
        age_total_under += line[0]
        workclass_total_under += line[1]
        education_num_total_under += line[4]
        marital_status_total_under += line[5]
        occupation_total_under += line[6]
        relationship_total_under += line[7]
        sex_total_under += line[8]
        race_total_under += line[9]
        gain_total_under += line[10]
        loss_total_under += line[11]
        hours_total_under += line[12]

    elif line[-1] == ">50k":
        total_training_over += 1
        age_total_over += line[0]
        workclass_total_over += line[1]
        education_num_total_over += line[4]
        marital_status_total_over += line[5]
        occupation_total_over += line[6]
        relationship_total_over += line[7]
        sex_total_over += line[8]
        race_total_over += line[9]
        gain_total_over += line[10]
        loss_total_over += line[11]
        hours_total_over += line[12]

averages_under.append(age_total_under / total_training_under)
averages_under.append(workclass_total_under / total_training_under)
averages_under.append(education_num_total_under / total_training_under)
averages_under.append(marital_status_total_under / total_training_under)
averages_under.append(occupation_total_under / total_training_under)
averages_under.append(relationship_total_under / total_training_under)
averages_under.append(sex_total_under / total_training_under)
averages_under.append(race_total_under / total_training_under)
averages_under.append(gain_total_under / total_training_under)
averages_under.append(loss_total_under / total_training_under)
averages_under.append(hours_total_under / total_training_under)

averages_over.append(age_total_over / total_training_over)
averages_over.append(workclass_total_over / total_training_over)
averages_over.append(education_num_total_over / total_training_over)
averages_over.append(marital_status_total_over / total_training_over)
averages_over.append(occupation_total_over / total_training_over)
averages_over.append(relationship_total_over / total_training_over)
averages_over.append(sex_total_over / total_training_over)
averages_over.append(race_total_over / total_training_over)
averages_over.append(gain_total_over / total_training_over)
averages_over.append(loss_total_over / total_training_over)
averages_over.append(hours_total_over / total_training_over)


midpoints = []
for index, item in enumerate(averages_under):
    totals = averages_under[index] + averages_over[index]
    midpoints.append(totals/2)
print(midpoints)

correct = 0
wrong = 0

try:
    for line in test_data:
        if line[0] > midpoints[0]:
            line[0] = "O"
        else:
            line[0] = "U"

        if line[1] > midpoints[1]:
            line[1] = "O"
        else:
            line[1] = "U"

        if line[4] > midpoints[2]:
            line[4] = "O"
        else:
            line[4] = "U"

        if line[5] > midpoints[3]:
            line[5] = "O"
        else:
            line[5] = "U"

        if line[6] > midpoints[4]:
            line[6] = "O"
        else:
            line[6] = "U"

        if line[7] > midpoints[5]:
            line[7] = "O"
        else:
            line[7] = "U"

        if line[8] > midpoints[6]:
            line[8] = "O"
        else:
            line[8] = "U"

        if line[9] > midpoints[7]:
            line[9] = "O"
        else:
            line[9] = "U"

        if line[10] > midpoints[8]:
            line[10] = "O"
        else:
            line[10] = "U"

        if line[11] > midpoints[9]:
            line[11] = "O"
        else:
            line[11] = "U"

        if line[12] > midpoints[10]:
            line[12] = "O"
        else:
            line[12] = "U"

        if line.count("O") > line.count("U") and line[-1] == ">50k":
            correct += 1
        elif line.count("U") > line.count("O") and line[-1] == "<=50k":
            correct += 1
        else:
            wrong += 1

except:
    pass

print("correct:", correct)
print("Wrong:", wrong)
print("Total:", len(test_data))
accuracy = correct * 100 / len(test_data)
print("Accuracy: ", int(accuracy), "%", sep="")

"""


def main():
    source = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    data = get_data(source)
    data = clean_up(data)
    data = count_values(data)
    print(data[:5])
    training_data = data[:int(len(data) * .75)]
    test_data = data[int(len(data) * .25):]

if __name__ == "__main__":
    main()
