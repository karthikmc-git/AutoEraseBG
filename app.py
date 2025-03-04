import os
import requests

class BackgroundRemover:
    def __init__(self, api_key):
        """
        Initialize BackgroundRemover with remove.bg API key
        """
        self.api_key = api_key
        self.base_url = 'https://api.remove.bg/v1.0/removebg'

    def remove_background(self, input_path, output_path):
        """
        Remove background from an image using remove.bg API
        """
        try:
            with open(input_path, 'rb') as image_file:
                response = requests.post(
                    self.base_url,
                    files={'image_file': image_file},
                    data={'size': 'auto'},
                    headers={'X-Api-Key': self.api_key}
                )
            
            if response.status_code == 200:
                with open(output_path, 'wb') as out_file:
                    out_file.write(response.content)
                print(f"Background removed for {input_path}")
            else:
                print(f"Error processing {input_path}: {response.status_code}")
        except Exception as e:
            print(f"Unexpected error processing {input_path}: {e}")

    def process_folder(self, folder_path):
        """
        Process all images in a given folder
        """
        # Supported image extensions
        image_extensions = ['.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.webp']
        
        # Collect all image files
        image_files = [
            os.path.join(folder_path, filename) 
            for filename in os.listdir(folder_path)
            if os.path.isfile(os.path.join(folder_path, filename)) and 
               os.path.splitext(filename)[1].lower() in image_extensions
        ]
        
        # Process each image
        for file_path in image_files:
            try:
                self.remove_background(file_path, file_path)
            except Exception as e:
                print(f"Failed to process {file_path}: {e}")

def main():
    # Predefined API key and folder path
    API_KEY = 'HgqwpdH7a8Pfa3zW3irJ7xs1'
    FOLDER_PATH = r'C:\Users\karth\OneDrive\Desktop\Vector_images'
    
    # Validate folder path
    if not os.path.isdir(FOLDER_PATH):
        print("Invalid folder path. Please check the directory.")
        return
    
    # Initialize background remover
    bg_remover = None
    try:
        bg_remover = BackgroundRemover(API_KEY)
        
        # Process images in the folder
        bg_remover.process_folder(FOLDER_PATH)
        
        print("Background removal process completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()
    

