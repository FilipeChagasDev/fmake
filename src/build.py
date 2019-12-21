import os
from fmake.main import make

#make(os.getcwd(), os.getcwd() + "/fmake", os.getcwd() + "/fmakeconfig.txt")
make(".", "./fmake",  "./fmakeconfig.txt")