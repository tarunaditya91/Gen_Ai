class tokenizer:
    def __init__(self):
        self.words = {}
        self.int_words = {}

    
    def build_words(self,text):
        words = text.lower().split()
        unique_words = sorted(set(words))
        for i,word in enumerate(unique_words):
            self.words[word] = i+1
        # self.words = {word : i for i,word in enumerate(unique_words)}
        self.words["dont_know"] = 0

        for i,word in enumerate(unique_words):
            self.int_words[i+1] = word
        # print(self.int_words)

        # print(self.words)
        # print(words)
    def encoder(self,sentence):
        words = sentence.lower().split()
        return [self.words.get(word,0) for word in words]
    def decoder(self,int_sentence):
        word = [self.int_words.get(ids,"dont_know") for ids in int_sentence]
        return " ".join(word)

sentence = "i am tarun doing my first assignment"
tokenizer1 = tokenizer()
tokenizer1.build_words(sentence)

encoder = tokenizer1.encoder("i am tarun 123")
print(f"the encoded sentence is :{encoder}")


decoder = tokenizer1.decoder(encoder)
print(f"the decoded sentence is :{decoder}")