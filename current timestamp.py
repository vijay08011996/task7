import datetime

def create_timestamp_file():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d_%H-%M-%S")  # Format the timestamp
    
    file_name = f"timestamp_{timestamp}.txt"  # Create the file name with timestamp
    with open(file_name, 'w') as file:
        file.write("This file was created with the current timestamp.")

    return file_name

# Example usage:
created_file = create_timestamp_file()
print(f"A file with the name '{created_file}' has been created.")
