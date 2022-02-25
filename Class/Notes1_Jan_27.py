def main():
    #string data type
    word = "apple" #simple string
    empty = "" #simplest string
    #empty string does not equal NONE
    large = "The quick brown fox jumps over the lazy dog." #complicated string
    empty2 = str()

    #split example
    sentence = "I hate python."
    splitSentence = sentence.split("ha")
    print(splitSentence)

    #strip example
    favorite = "soccer"
    print(favorite.strip("s"))
    another = "     soccer dnllllllll"
    print(another.strip(" dnl"))

    #text files
    f = open("Sherlock Holme.txt", "r")
    for i in range (6):
        print(f.readline())

    print(len(f.read()))

    
if __name__ == "__main__":
    main()
