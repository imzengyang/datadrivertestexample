import os


print(os.path.abspath(__file__),os.path.dirname(os.path.abspath(__file__)))
rootdir = os.path.dirname(os.path.abspath(__file__))
print(os.path.join(rootdir,'screenshots'))