import os

def rename_files(directory, prefix):
    # Change the current working directory to the specified path
    os.chdir(directory)
    
    # Loop through all files in the directory
    for count, filename in enumerate(os.listdir(directory)):
        # Construct the new file name
        new_name = f"{prefix}_{count}{os.path.splitext(filename)[1]}"
        
        # Rename the file
        os.rename(filename, new_name)
        print(f"Renamed '{filename}' to '{new_name}'")

# Example usage
directory_path = '/path/to/your/directory'
file_prefix = 'new_name'
rename_files(directory_path, file_prefix)
