
#Problem 5
from collections import Counter


def count_word(file_path):
        with open(file_path, 'r') as file:
            text = file.read()

        lines=text.split('\n')

        words=[]
        for l in lines:
            line=l.split(": ",1)
            if len(line)>1:
                person,content=line
                words.append(person)
                content_words=content.split()
                words.extend(content_words)

        counts=Counter(words)

        for word, count in counts.items():
            print(f"{word}: {count}")


file_path = "simple_text.txt"
count_word(file_path)

