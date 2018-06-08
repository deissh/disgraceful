from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
l = TreebankWordTokenizer().tokenize(input())
l.sort()
print(TreebankWordDetokenizer().detokenize(l))
