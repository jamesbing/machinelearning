import network
import tool
if __name__ == '__main__':
    network.train()
    '''times = tool.loadList('./times.txt')
    accus = tool.loadList('./accus.txt')
    ttimes = []
    aaccus = []
    for i in xrange(len(times)):
        if i % 3 == 0:
            ttimes.append(times[i] / 3)
            aaccus.append(accus[i])
    tool.showXYData(ttimes, aaccus, './times_accus.png')'''