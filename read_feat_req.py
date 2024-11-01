
import json
import os

def read_JSON_file(file_path: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    else:    
        with open(file_path, mode="r", encoding="utf-8") as input_file:
            try:
                data = json.load(input_file)
                return data
            except json.JSONDecodeError as e:
                return e

def main():

    data_as_json_dict = read_JSON_file("./feature_requirements.json")

    technique_IDs_list = ["T0807","T0867", "T0883", 
                          "T0888", "T0869", "T0853", 
                          "T0846"]
    
    activities_list = ["Network Monitoring", "System Activity Monitoring", 
                       "Network Analysis", "Software Manipulation", 
                       "Information Manipulation", "Network Manipulation"]
    
    for technique_ID in technique_IDs_list:
        for feature_req in data_as_json_dict:
            if feature_req["Technique_ID"] == technique_ID:
                for key, val in feature_req["Features"].items():
                    
                    if "All" in val:
                        print(f"{technique_ID} : {key}")
                    elif "Others" in val:
                        print(f"{technique_ID} : {key}")
                        
                    activities_set = set(activities_list)
                    file_set = set(val)
                
                    if (activities_set & file_set):
                        print(f"{technique_ID} : {key}")
        print("\n")
        
if __name__ == "__main__":
    main()