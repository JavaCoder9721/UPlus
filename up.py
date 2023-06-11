
import time,os

def newText(n):

    print(n)

    return None

def newInput(n):

    try:

        return raw_input(n)

    except NameError:

        return input(n)

def convertToNumber(thing):

    return float(thing)

def newLoadingNumber(EverySeconds,times):

    num = 0

    for i in range(times):

        num += 1

        print(f"{num}%")

        time.sleep(EverySeconds)

        os.system("clear")

        if num == times:

            print(f"{num}%")

            return 0

def newTextWithNoLine(n):

    print(n,end="")

    return None

def be(condition):

    if condition:

        print(True)

        return True

    else:

        print(False)

        return False

globals()['newtext'] = newText

globals()['newinput'] = newInput

globals()['intonumber'] = convertToNumber

globals()['newloadingtext'] = newLoadingNumber

globals()['newtextnonl'] = newTextWithNoLine

globals()['If'] = be
