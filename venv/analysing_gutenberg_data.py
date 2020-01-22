import nltk

#nltk.download_shell()
nltk.download("gutenberg")

guten = nltk.corpus.gutenberg
print("Gutenberg files : ", guten.fileids())

def analyse_book():
    print("Priting information about the selected book")
    print("Please input your preference, the options are as follows, please ensure you type the name of the book correctly:\n", guten.fileids)
    user_in = input()
    book = nltk.corpus.gutenberg.words(user_in)

macbth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
print(len(macbth))