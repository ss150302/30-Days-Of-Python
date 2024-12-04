import os

def search_in_file(file_path, search_terms):
    found = False
    try:
        with open(file_path, 'r') as file:
            for line_no, line in enumerate(file, start=1):
                for term in search_terms:
                    if term in line:
                        print(f"Found '{term}' in {file_path} on line {line_no}")
                        found = True
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    if not found:
        print(f"No keywords found in {file_path}")

def search_in_directory(directory, search_terms, file_extensions, exclude_dirs):
    for root, dirs, files in os.walk(directory):
        # Exclude specified directories
        dirs[:] = [d for d in dirs if os.path.join(root, d) not in exclude_dirs]
        for file in files:
            if any(file.endswith(ext) for ext in file_extensions):
                file_path = os.path.join(root, file)
                search_in_file(file_path, search_terms)

if __name__ == "__main__":
    directory_before = os.getcwd() + '/Before'
    directory_after = os.getcwd() + '/After'
    search_terms = ['usr100200','usr100300']  # Replace with your comma-separated strings

    file_extensions = ['.xml', '.txt']  # Add the file extensions you want to search
    exclude_dirs = [os.path.join(os.getcwd(), 'Before', 'exclude_dir1'), os.path.join(os.getcwd(), 'After', 'exclude_dir2')]  # Add directories to exclude
    search_in_directory(directory_before, search_terms, file_extensions, exclude_dirs)
    search_in_directory(directory_after, search_terms, file_extensions, exclude_dirs)
