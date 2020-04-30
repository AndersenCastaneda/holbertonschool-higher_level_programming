#!/usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *
    listdir = dir()

    for i in range(len(listdir)):
        if listdir[i][:2] != "__":
            print(listdir[i])
