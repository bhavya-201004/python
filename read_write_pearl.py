def check_for_word():
    word ="diverged"
    with open("rnt.txt","r") as f:
        data = f.read()
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")
            



##readline
def check_word():
    word ="diverged"
    data = True
    line = 1
    with open("rnt.txt","r") as f:
        while data:
            data = f.readline()
            if (word in data ):
                print(line)
            line += 1    
    
        