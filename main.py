import time
import os 


class Bot:
    def __init__(self):
        self.dirs    = ["images", "videos", "scripts"]
        self.images  = ["png", "jpg", "jpeg", "jfif"]
        self.scripts = ["py", "js", "json", "cs", "cc", "c"]
        self.videos  = ["mp4", "mov", "gif"]

        self.setup()
        self.main()

    
    def setup(self):
        for dir in self.dirs:
            if not os.path.isdir(dir):
                os.mkdir(dir)



    def main(self):
        while True:
            files = os.listdir()

            for file in files:
                ext = file.lower().rsplit(".", 1)[-1]
                
                if file == os.path.basename(__file__):
                    continue


                try:
                    if ext in self.images:
                        os.rename(file, "images/" + file)
                        print(file + " => images")

                    elif ext in self.videos:
                        os.rename(file, "videos/" + file)
                        print(file + " => videos")

                    elif ext in self.scripts:
                        os.rename(file, "scripts/" + file) 
                        print(file + " => scripts")
                except:
                    pass
            
            time.sleep(2)


Bot()