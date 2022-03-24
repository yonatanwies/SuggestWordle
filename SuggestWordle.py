from english_words import english_words_lower_alpha_set


class Wordle:

    word_list = [word for word in english_words_lower_alpha_set if len(word) == 5]

    def __init__(self):
        self.word = input("Your word is: ").lower()
        self.notinword = [char for char in set(input("Enter unusable letters: ")) if char.isalpha()]

    def __str__(self):
        return f"Your word is {self.word}"

    def check_existence(self):
        if self.word in self.word_list:
            return 'Word exists'
        return 'Word does not exist'

        def word_update(self, letter, location):
        temp = [char for char in self.word]
        temp[location] = letter
        self.word = "".join(temp)

    def unusable_update(self,letters_lst):
        for letter in letters_lst:
            self.notinword.append(letter)
            
    def suggestion(self):
        suggestions = []
        counter = 0
        for word in self.word_list:
            for i in range(5):
                if self.word[i] == word[i] or self.word[i] == '_':
                    counter += 1
            if counter == 5:
                temp_count = 0
                for letter in word:
                    if letter in self.notinword:
                        temp_count += 1
                if temp_count == 0:
                    suggestions.append(word)
            counter = 0
        return suggestions

