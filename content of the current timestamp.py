import datetime

def create_timestamp_file_with_content():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")  # Format the timestamp
    
    file_name = f"timestamp_{timestamp}.txt"  # Create the file name with timestamp
    with open(file_name, 'w') as file:
        file.write(timestamp)  # Write the timestamp as the content

    return file_name

# Example usage:
created_file = create_timestamp_file_with_content()
print(f"A file with the name '{created_file}' has been created with the content of the current timestamp.")
