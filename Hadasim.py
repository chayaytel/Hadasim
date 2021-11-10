
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
        dict = {}
        count = 0
        with open(self.file, 'r') as f:
            for line in f:
                array_word_in_line = line.split(" ")
                for word in array_word_in_line:
                    if dict.get(word.lower().strip(), 'None') == 'None':
                        dict[word.lower().strip()] = 0
                    else:
                        dict[word.lower().strip()] = dict[word.lower().strip()] + 1
        for key, val in dict.items():
            if val == 0:
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
                    if word.lower().title() in color_dict:
                        color_dict[word.title()] = color_dict[word.title()] + 1
        dict_ret = {}
        for key, val in color_dict.items():
            if val > 0:
                dict_ret[key]=val
        return dict_ret



s='C:\\Users\\user\\Searches\\Downloads\\hadasim.txt'
tf=test_file(s)
print("Count lines: ",tf.count_lines())
print("Count words: ",tf.count_words())
print("Count uniq words: ",tf.count_uniq_words())
print("Max len, Avd len: ",tf.len_sentence())
print(tf.colors_in_file())

