import pandas as pd
import matplotlib.pyplot as plt
import os


class data_SIMS(object):
    '''
    A data container contains data from a single file

    '''

    def __init__(self, file_adr):
        '''
        file: string,abs path point to a file, a txt file contains standart SIMS data
        self.no:sample's label number
        self.data: a Pandas DataFrame
        '''
        self.data = pd.read_table(file_adr, sep=r'\s+', skiprows=(0, 1, 3, 4))

        filename = os.path.basename(file_adr)
        if filename.endswith('.txt') or filename.endswith('.TXT'):
            self.no = filename[:-4]     # del '.txt'
        else:
            raise ValueError('This is not a txt file')

    def plot(self, ylist=None, logStat=True):
        '''
        ylist: a list or string to choose data of y to plot
        logStat: 'True' to plot log graph, 'False' to plot linear graph
        '''
        if ylist == None:
            ylist = self.data.columns[1:]
        self.data.plot(x='#', y=ylist, logy=logStat)
        plt.show()

# =============================================================================
# case for test
# =============================================================================


if __name__ == '__main__':
    file_dir = '/Users/yfkong/GitHub/SIMS-data-analyzer/test_data.TXT'
    a = data_SIMS(file_dir)
    # print(a.data.columns[1:].copy())
    # a.plot(['Mo+','Na+'])
    print(a.no)
