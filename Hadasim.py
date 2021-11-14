from collections import Counter

class test_file:
    def __init__(self, file):
        self.file = file

    def count_lines(self):
        with open(self.file,'r') as f:
            return len(f.readlines())

    def count_words(self):
        count = 0
        with open(self.file, 'r') as f:
            for line in f:
                array_word_in_line = line.split(" ")
                count = count + len(array_word_in_line)
        return count

    def count_uniq_words(self):
        dict_counter = Counter() #Data Structure like dictinary that come with using function for counter
        count = 0
        with open(self.file, 'r') as f:
            for line in f:
                array_word_in_line = line.split(" ") #Separate the lines to words
                for word in array_word_in_line:
                    word = word.strip("\n-,!?:'/ .").lower() #Cut all the special characters from the word
                    dict_counter[word] += 1
        for key, val in dict_counter.items():
            if val == 1:
                count = count + 1
        return count

    def len_sentence(self):
        max = 0
        count = 0
        with open(self.file, 'r') as f:
            context = f.read().split(".")
        for sen in context:
            if max < len(sen):
                max = len(sen)
            count = count + len(sen)
        return max, count / len(context)

    def colors_in_file(self):
        color_dict = {'Black':0, 'Blue':0, 'Brown':0, 'Green':0, 'Gray':0, 'Orange':0, 'Pink':0, 'Purple':0, 'Red':0, 'White':0, 'Yellow':0, 'Gold':0, 'Silver':0}
        with open(self.file, 'r') as f:
            for line in f:
                array_words_in_line = line.split(" ")
                for word in array_words_in_line:
                    word = word.strip("\n-,!?:'/ .").lower().title()
                    if word in color_dict:
                        color_dict[word] = color_dict[word] + 1
        dict_ret = {}
        for key, val in color_dict.items():
            if val > 0:
                dict_ret[key]=val
        return dict_ret

    def popular_word(self):
        special_words = ['am', 'is', 'are', "don't", "does", "didn't", "did",
                        "will", "won't", "aren't", "isn't", "was", "wasn't",
                        "were", "have", "has", "hasn't", "haven't", "had",
                        "hadn't", "been", 'at', 'that', 'then', 'the',
                        'a', 'be', 'to', 'this', 'by', 'for' ]
        counter_dict = Counter()
        with open(self.file, 'r') as f:
            for line in f:
                array_word_in_line = line.split(" ") #Separate the lines to words
                for word in array_word_in_line:
                    word = word.strip("\n-,!?:'/ .").lower() #Cut all the special characters from the word
                    counter_dict[word] += 1
        for item in counter_dict.most_common():
            #because item is tuple, I need to cut only the word
            item = item.__str__().strip("('")
            x = item.find("'")
            item = item[0:x]
            if item not in special_words:
                most_common_not_syntactic_word = item
                break

        return counter_dict.most_common()[0], most_common_not_syntactic_word

    def max_words_without_k(self):
        max = 0
        count = 0
        with open(self.file, 'r') as f:
            for line in f:
                array_word_in_line = line.split(" ") #Separate the lines to words
                for word in array_word_in_line:
                    if 'k' not in word:
                        count+=1
                    else:
                        if(max < count):
                            max = count
                        count = 0
        return max


s='C:\\Users\\user\\Searches\\Downloads\\hadasim.txt'
tf=test_file(s)
print("Count lines: ",tf.count_lines())
print("Count words: ",tf.count_words())
print("Count uniq words: ",tf.count_uniq_words())
print("Max len, Avd len: ",tf.len_sentence())
print("Coloer in the file: ",tf.colors_in_file())
print("Popular word, popular word doesn't syntactic word: ",tf.popular_word())
print("Maximum length of words without 'k': ", tf.max_words_without_k())

