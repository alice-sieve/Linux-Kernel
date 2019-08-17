import glob, os, shutil, re

os.chdir("topics")
for file in glob.glob("*.txt"):
    dir_name = file.replace(".txt","")
    if not os.path.exists(dir_name):
        print("Scraping in {}".format(dir_name))
        os.mkdir(dir_name)
        with open(file) as f:
            for line in f:
                urls = re.findall('https[^\]]+', line)
                msg_name = re.findall("\w+\.html", urls[0])[0]
                os.system("lynx -dump -source {} > {}/{}".format(urls[0], dir_name, msg_name))
            print("Finished Scraping... {}".format(file))
    else:
        pass