import csv 

input_file = 'C:\\Users\\mtsotsha\\repos\\csv_coversion\\WEB - WEB_SUIT(41).txt'
output_file_1 = 'C:\\Users\\mtsotsha\\OneDrive - Open Box Software\\WEB - WEB_SUIT(41).csv'
output_file_2 = 'WEB - WEB_SUIT(41).csv'
#reding the dataset
with open(input_file, 'r') as file:
    dataset_content = file.read()
    
#manipulate the data to split into values
lines = dataset_content.split("\n")
data = [line.split() for line in lines]


with open(output_file_1, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
with open(output_file_2, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print(f"CSV file '{output_file_1 + output_file_2}' created successfully.") 
    
