import os
import docx

baseDir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'writing'))

targetDir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'outputTxtFile'))

print('basedir', baseDir)


def traverseFiles(folder):
    print('running')
    outputFile = docx.Document()
    for root, subdirs, files in os.walk(folder):
        for curFile in files:
            if curFile.endswith('.docx'):
                curDoc = docx.Document(root + '/' + curFile)
                for paragraph in curDoc.paragraphs:
                    outputFile.add_paragraph(paragraph.text)
    outputFile.save(targetDir + '/data.txt')


traverseFiles(baseDir)
