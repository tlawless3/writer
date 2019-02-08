from __future__ import absolute_import, division, print_function
import time
import os
import numpy as np
import docx2txt

import tensorflow as tf
tf.enable_eager_execution()

targetFile = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'outputTxtFile/data.docx'))

# text = open(targetFile, 'r').read().decode(encoding='UTF-8')

text = docx2txt.process(targetFile)

print(text[:250])
print('Length of text: {} characters'.format(len(text)))

vocab = sorted(set(text))
print('{} unique characters'.format(len(vocab)))

char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

text_as_int = np.array([char2idx[c] for c in text])
