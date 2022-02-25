def main():

    def gcs(s1, s2):
        subString1 = []
        subString2 = []
        #
        for i in range(len(s1)):
            for k in range(i, len(s1)):
                subString1.append(s1[i:k+1])
        print(subString1)
        
        for i in range(len(s2)):
            for k in range(i, len(s2)):
                subString2.append(s2[i:k+1])
        print(subString2)

        maxS = 0
        result = ""
        for i in range(len(subString1)):
            for k in range(len(subString2)):
                if subString1[i] == subString2[k]:
                    if len(subString1[i]) > maxS:
                        maxS = len(subString1[i])
                        result = subString1[i]
        return result



        s1 = "Hello"
        s2 = "There"
        gSub = gcs(s1, s2)
        print(gSub)

        # Example for loop
        for i in [1, 2, 3, 4]:
            print(i, end=", ") # prints: 1, 2, 3, 4,

    if __name__ == "__main__":
        main()
