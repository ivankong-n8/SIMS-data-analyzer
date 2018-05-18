from os import getcwd, path
import numpy as np
import matplotlib
# matplotlib.use("TkAgg")
# to fix crashed [NSApplication _setup:]:
# unrecognized selector sent to instance
from matplotlib import pyplot as plt


class data_SIMS(object):
    '''
    A data container contains data from a single file

    '''

    def __init__(self, file_adr):
        '''
        file_adr:   string, abs path point to a txt file including standard
        SIMS data
        self.no: sample's label number
        self.data: a Numpy narray
        self.title: a list of title for each data column
        '''
        self.file_adr = file_adr
        self.data = None
        self.title = []
        self.load_data()

        filename = path.basename(file_adr)
        if filename.endswith('.txt') or filename.endswith('.TXT'):
            self.no = filename[:-4]     # del '.txt' or '.TXT'
        else:
            raise ValueError('This is not a txt file')

    def get_no(self):
        '''
        Return sample's label number
        '''
        return self.no

    def get_title_list(self):
        return self.title

    def load_data(self):
        '''
        A method to load data without Pandas
        '''
        self.data = np.loadtxt(self.file_adr, comments='#').T
        # use comments '#' to skip first 5 lines
        print(self.data[0])
        print(self.data[1])

        inFile = open(self.file_adr, 'r')
        lines = inFile.readlines()
        inFile.close()

        self.title = lines[2].split('\t')[1:-1]
        # print(self.title)

        # print(self.data)
        # print(self.data.shape)

    def plot(self, ylist=None, logStat=True):
        '''
        ylist: a list or string to choose data of y to plot
        logStat: 'True' to plot log graph, 'False' to plot linear graph
        '''
        if ylist is None:
            ylist = self.title
        # self.data.plot(x='#', y=ylist, logy=logStat)
        plt.figure()
        for y_title in ylist:
            index = self.title.index(y_title)+1
            plt.semilogy(self.data[0], self.data[index], label=y_title)
        plt.legend()
        plt.show()


# =============================================================================
# case for test
# =============================================================================

if __name__ == '__main__':
    file_dir = 'test_data.TXT'
    # file_path = getcwd()
    # file_dir = path.join(file_path, file)
    a = data_SIMS(file_dir)
    a.plot()
    # print(a.no)
