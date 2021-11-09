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
        return max, count/len(context)

