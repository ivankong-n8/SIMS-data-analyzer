import pandas as pd
import matplotlib.pyplot as plt


class data_SIMS(object):
    '''
    A data container contains data from a single file

    '''

    def __init__(self, file):
        '''
        file: string, a txt file contains standart SIMS data
        self.no:sample's label number
        self.data: a Pandas DataFrame
        '''

        self.data = pd.read_table(file, sep=r'\s+', skiprows=(0, 1, 3, 4))

        if file.endswith('.txt') or file.endswith('.TXT'):
            self.no = file[:-4]     # del '.txt'
        else:
            raise ValueError('This is not a txt file')

    def plot(self, ylist=None, logStat=True):
        '''
        '''
        if ylist == None:
            ylist = self.data.columns[1:]
        self.data.plot(x='#', y=ylist, logy=logStat)
        plt.show()

# =============================================================================
# case for test
# =============================================================================


if __name__ == '__main__':
    file = 'test_data.TXT'
    a = data_SIMS(file)
    # print(a.data.columns[1:].copy())
    a.plot(['Mo+','Na+'])
