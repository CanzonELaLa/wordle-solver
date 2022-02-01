import sys

def main():
    forbidden_letters = ""
    
    existing_letters = []
        
    with open("5_letter_words.txt", "r") as f:
        words = f.readlines()
        
    possible_words = words
    
    forbidden_letters += input("forbidden letters: ").lower()
    print("Now enter letters and positions (starting with 1) as such: a:-1 e:2 ...\n",
          "If unknown index, put -<index it is NOT> before the :")
    letter_placements = input("letter and position: ")
    while True:        
        pairs = letter_placements.split(" ")
        for pair in pairs:
            if pair == "":
                continue
            split_input = pair.split(":")
            existing_letters.append((int(split_input[1]), split_input[0].lower()))
        
        existing_letters_only = [i for j, i in existing_letters]
        wittled_down_words = []
        for word in possible_words:
            notFailForForbidden = True
            for letter in forbidden_letters:
                if letter in word.lower() and letter not in existing_letters_only:
                    notFailForForbidden = False
                    break

            if notFailForForbidden:
                wittled_down_words.append(word.strip())

        further_wittled_down_words = []
        for word in wittled_down_words:
            failForMissing = False
            for index, letter in existing_letters:
                assert index < 6 or index > -6
                failForMissing = False
                if index < 0:
                    if letter not in word.lower() or letter == word.lower()[abs(index + 1)]:
                        failForMissing = True
                        break
                else:
                    if letter != word.lower()[index - 1]:
                        failForMissing = True
                        break

            if not failForMissing:
                further_wittled_down_words.append(word.strip())
        
        possible_words = further_wittled_down_words
        print(possible_words)
        
        forbidden_letters += input("extra forbidden letters: ").lower()
        print("current forbidden letters:", forbidden_letters)
        print("extra letters and positions?:")
        letter_placements = input("letter and position: ")

if __name__ == "__main__":
	main()