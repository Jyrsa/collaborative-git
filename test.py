"""
This will import all files with the suffix of *.py and 

"""
import os

for filename in os.listdir("./tweets/"):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = "tweets." + filename[:-3]
        try:
            module = __import__(module_name, globals(), locals(), ["tweet"])
            assert len(module.tweet().encode('utf-8')) < 140,\
                    "A tweet must be under 140 characters!"
        except ImportError:
            pass
