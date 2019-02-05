import os
from docx import Document

baseDir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'templates'))

for root, subdirs, files in os.walk(baseDir):
    print('--\\nroot = ' + root)
