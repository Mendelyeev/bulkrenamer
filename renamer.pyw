import os
import sys
import glob
from contextlib import suppress

# author Athul A
# use python3.exe 'scriptname'.py aspx html <- exemplo


def change(old_ext, new_ext):
    [os.rename(f, "%s.%s" % (os.path.splitext(f)[0], new_ext))
     for f in glob.glob(os.getcwd() + "/*." + old_ext)]


with suppress(Exception):
    change(sys.argv[1], sys.argv[2])

# MODELO ANTERIOR
#  import glob
# import os

# folder = r'<YOUR FOLDER HERE>'

# for filename in glob.iglob(os.path.join(folder, '*.html')):
#     os.rename(filename, filename[:-5] + '.aspx')
