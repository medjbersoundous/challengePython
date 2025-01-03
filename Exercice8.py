def count_words(sentence):
    words = sentence.split()  
    return len(words)  
sentence = input("enter a sentence: ")
print(count_words(sentence))  
