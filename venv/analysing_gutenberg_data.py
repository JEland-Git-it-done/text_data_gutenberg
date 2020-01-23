import nltk

#nltk.download_shell()
nltk.download("gutenberg")
ntlk.download("stopwords")

guten = nltk.corpus.gutenberg
print("Gutenberg files : ", guten.fileids())

def analyse_book():
    #own work to allow users to implement functions onto a book
    print("Priting information about the selected book")
    print("Please input your preference, the options are as follows, please ensure you type the name of the book correctly:\n", guten.fileids)
    user_in = input()
    book = nltk.corpus.gutenberg.words(user_in)

def analyse_macbeth():
    #Priting simple information about macbeth
    print("Printing simple information on MacBeth")
    macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
    print("There are {} words in Macbeth".format(len(macbeth)))
    print("The first 10 words are : {0}\nThe last 10 words are : {1}".format(macbeth[:10], macbeth[-11:-1]))
    macbeth_sents = nltk.corpus.gutenberg.sents('shakespeare-macbeth.txt')
    print("The first five sents are : ", macbeth_sents[:5])
    fd = nltk.FreqDist(macbeth)
    fd_out = fd.most_common(15)
    print(fd_out)

def find_text_macbeth():
    macbeth = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')
    text = nltk.Text(macbeth)
    stage_text = text.concordance("Stage")
    print("***")
    text.concordance("Wife")#Since the play is about a man and his wife, this seems like an apt search figure
    text.concordance("Dragon")

find_text_macbeth()