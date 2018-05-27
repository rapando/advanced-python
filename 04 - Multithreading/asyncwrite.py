import threading
import time


class AsyncWrite(threading.Thread):
    def __init__(self, text, outfile):
        threading.Thread.__init__(self)
        self.text = text
        self.outfile = outfile

    def run(self):
        f = open(self.outfile, 'a')
        f.write(self.text + '\n')
        f.close()
        time.sleep(2)
        print("Finished background writing to ", self.outfile)


def main():
    message = input("Enter the message : ")
    background = AsyncWrite(message, 'out.txt')
    background.start()
    print ("Program can continue while it saves a file in the background")
    background.join()
    print ("The file has been saved now. Earth is safe")

if __name__ == "__main__":
    main()
