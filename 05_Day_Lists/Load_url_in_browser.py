import webbrowser
import requests
import os

def download_file(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"File downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
    except IOError as e:
        print(f"Error saving file: {e}")

def open_url_in_browser(url):
    webbrowser.open(url)

if __name__ == "__main__":
       file_refs_str = '439266'
       # Example comma-separated string of fileRef numbers
    file_refs = file_refs_str.split(",")
    base_url = "https://www.xxxxxx?fileRef="

    for file_ref in file_refs:
        url = f"{base_url}{file_ref}"
        open_url_in_browser(url)
