f = open("SaveData.txt")




def get_email(filename):
    with open(filename, 'r') as file:
        for line in file:
            # Check if the line starts with 'middleName:'
            if line.startswith('email:'):
                # Extract the middle name
                email = line.split(':', 1)[1].strip()
                return email
    # If 'middleName:' is not found in the file
    return None


print(get_email('SaveData.txt'))