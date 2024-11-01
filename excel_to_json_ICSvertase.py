import re
import pandas
import json

def main():
    
    # Read excel document
    excel_data_df = pandas.read_excel("feature_requirements_adjust.xlsx", sheet_name="Sheet1")


    # Convert excel to string 
    # (define orientation of document in this case from up to down)
    data_as_json = excel_data_df.to_json(orient="records")

    # Print out the result
    # print("Excel Sheet to JSON:\n", thisisjson)

    # Make the string into a list to be able to input in to a JSON-file
    data_as_json_dict = json.loads(data_as_json)
    new_dict_arr = []

    for json_obj in data_as_json_dict:
        # print(json_obj["Technique"])
        
        new_dict = {}
        technique = json_obj["Technique"]

        if technique:
            # Use regex to split the string into the part outside and inside parentheses
            match = re.match(r"^(.*)\s+\((.*)\)$", technique)

            # Extracted parts if the match is found
            if match:
                # outside_parentheses 
                new_dict["Technique_Name"] = match.group(1).strip()
                # inside_parentheses
                new_dict["Technique_ID"] = match.group(2).strip()
            else:
                print("No parentheses found in the string.")

        
            new_dict["Features"] = {key: value for key, value in json_obj.items() if key != "Technique"}

            for key, val in new_dict["Features"].items():
                # print(f"{key}, {val}")

                new_dict["Features"][key] = [val]

                if "\n" in str(val):
                    new_val = str(val).split("\n")
                    new_dict["Features"][key] = new_val

        new_dict_arr.append(new_dict)

    # print(new_dict_arr)

    # return

    with open("feature_requirements.json", "w") as json_file:
        json.dump(new_dict_arr, json_file)


if __name__ == "__main__":
    main()