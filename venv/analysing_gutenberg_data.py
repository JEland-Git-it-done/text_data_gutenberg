import nltk as nltk

#nltk.download_shell()
#nltk.download("gutenberg")
#nltk.download("stopwords")

guten = nltk.corpus.gutenberg
#print("Gutenberg files : ", guten.fileids())

def analyse_book():
    user_is_analysing = True
    user_is_finished = False
    print("Priting information about the selectable books")
    print("Gutenberg files : ", guten.fileids())
    print("Please input your preference, the options can be seen above, please ensure that your input is valid: ")
    while user_is_analysing and not user_is_finished:
        #own work to allow users to implement functions onto a book
        gt_checker = guten.fileids()

        user_in = input()
        simple_in = user_in + ".txt"
        if user_in in gt_checker:
            print(user_in)
            print("This input was valid, starting the analysis, a menu will appear shortly")
            book = nltk.corpus.gutenberg.words(user_in)
            print_menu()
            #print(book)
            user_is_finished=True
        elif simple_in in gt_checker:
            print(simple_in)
            print("This input was valid, starting the analysis, a menu will appear shortly")
            book = nltk.corpus.gutenberg.words(simple_in)
            options = print_menu()
            #print(book)
            print("Please type the number of the analyis you want to undertake: ")
            menu_in = input()
            select_function(menu_in, options)

        else:
            print("This input was invalid - please ensure the input is the same as the file above ")


def print_menu():
    print("Printing menu ...")
    for i in range(3):
        print("*****")
    options = ["Find basic information", "Count number of words", "Print the first 100 words",
               "Print the first 10 sents", "Find most common words", "Find Text", "Quit analysis"]
    for i in range(len(options)):
        x = i+1
        print("{0}: {1}".format(str(x), options[i]))
    return options

def select_function(user_in, options):
    print("Working...")
    for i in range(len(options)):
        if int(user_in) == i:
            print(options[i])
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


analyse_book()