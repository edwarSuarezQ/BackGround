import os
from datetime import datetime
from rembg import remove

class BackgroundRemover:

    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

    def process_images(self):
        today = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        process_folder = os.path.join(self.output_folder, today)
        os.makedirs(process_folder,exist_ok=True)

        for filename in os.listdir(self.input_folder):
            if filename.endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(process_folder, filename)
                self._remove_background(input_path, output_path)
                self._moveorioginals(input_path, process_folder)


    def _remove_background(self, input_p, output_p):
         with open(input_p, 'rb') as inp, open(output_p, 'wb') as oupt:
             background_output = remove(inp.read())
             oupt.write(background_output)


    def _moveorioginals(self,inputp, destp):
        orginals_folders = os.path.join(destp, "originals")
        os.makedirs(orginals_folders, exist_ok=True)

        filename = os.path.basename(inputp)
        new_paht = os.path.join(orginals_folders, filename)
        os.rename(inputp, new_paht)


if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"

    remover = BackgroundRemover(input_folder, output_folder)
    remover.process_images()