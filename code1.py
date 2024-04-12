# PROBLEM STATEMENT:
# 1. Read a JSON rtf text file. Convert it using any method.
# 2. Replace the value of the key in the JSON dict. (It is guranteed to have the key.)
# 3. Duplicate an array components n number of times where n is a positive integer
# 4. Write the updated JSON to a file


import json
from copy import deepcopy
from striprtf.striprtf import rtf_to_text


def findKeyAndReplaceValue(keyToFind, valueToReplace, jsonObj):
    """Recursively search through nested dict and replace the value if the key is found."""

    # If jsonObj is a list then iterate through items and recurse on each item.
    if isinstance(jsonObj, list):
        for listNum, listItem in enumerate(jsonObj):
            findKeyAndReplaceValue(keyToFind=keyToFind, valueToReplace=valueToReplace, jsonObj=listItem)

    # If jsonObj is a dict then store keys in another variable for easy access
    elif isinstance(jsonObj, dict):
        # If keyToFind is in allCurrKeys, then update the value with valueToReplace and return
        allCurrKeys = jsonObj.keys()
        if keyToFind in allCurrKeys:
            jsonObj.update({keyToFind: valueToReplace})

        # If keyToFind is not found then recurse on the values of current jsonObj
        else:
            for key in allCurrKeys:
                findKeyAndReplaceValue(keyToFind=keyToFind, valueToReplace=valueToReplace, jsonObj=jsonObj[key])


def duplicateItemsInListOfDict(listOfDict, count):
    """Duplicates every item in a list of dict as per the count."""
    updatedList = []

    for i in range(count):
        for valDict in listOfDict:
            updatedList.append(valDict)

    return updatedList


if __name__ == "__main__":
    key = "dataLogMaxSize"
    value = "replacedword"

    # Read the RTF file
    with open('Json1.rtf', 'r') as f:
        rtfText = f.read()
        plainText = rtf_to_text(rtfText)
        originalJsonText = json.loads(plainText)

    copyJsonText = deepcopy(originalJsonText)

    # Replace value if searched key is found
    findKeyAndReplaceValue(keyToFind=key, valueToReplace=value, jsonObj=copyJsonText)

    # Verify if value was replaced
    print("Text replacement success: {}".format(not (originalJsonText == copyJsonText)))

    # Duplicate items in an array
    inputArr = deepcopy(copyJsonText['web-app']['servlet'])
    outputArr = duplicateItemsInListOfDict(listOfDict=inputArr, count=3)
    copyJsonText['web-app']['servlet'] = outputArr

    # Verify duplicated items
    print("Duplicate array success: {}".format(
        len(copyJsonText['web-app']['servlet']) > len(originalJsonText['web-app']['servlet']))
    )

    # Convert to string and write output to file
    textToWrite = json.dumps(copyJsonText, indent=4)
    with open('Json2.json', 'w') as f:
        f.write(textToWrite)
