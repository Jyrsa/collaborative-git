"""
This will import all files with the suffix of *.py and 

"""
import os

for filename in os.listdir("./tweets/"):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = "tweets." + filename[:-3]
        print(module_name)
        try:
            module = __import__(module_name, globals(), locals(), ["tweet"])
            print("module {0} tweets: {1}".format(filename, module.tweet().encode('utf-8')))
        except ImportError:
            pass
