def update_server_config(file_path,key,value):
    """
    Update the server configuration file with the specified key-value pair.

    This function reads the server configuration file, updates the specified key
    with the given value, and writes the changes back to the file. If the key
    doesn't exist, it will be added to the file.

    Args:
    file_path (str): The path to the server configuration file.
    key (str): The configuration key to update.
    value (str): The new value for the specified key.

    Returns:
    bool: True if the update was successful, False otherwise.

    Raises:
    FileNotFoundError: If the specified file doesn't exist.
    PermissionError: If the function lacks permission to read or write the file.
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        with open(file_path, 'w') as file:
            for line in lines:
                if key in line:
                    file.write(f"{key}={value}\n")
                else:
                    file.write(line)
    except (FileNotFoundError, PermissionError):
        return False

x = input("file_name:")
y = input("key:")
z = input("value:") 

update_server_config(x,y,z)

