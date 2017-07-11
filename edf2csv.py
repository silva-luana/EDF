import eegtools
import pandas as pd

class EDF:

    def __init__(self, subject):

        self.subject = subject

        edf_data = eegtools.io.load_edf(self.subject)

        self.data = edf_data.X.transpose()
        self.smp_rate = edf_data.sample_rate
        self.channels = edf_data.chan_lab
        self.ann = edf_data.annotations

    def signal_to_csv(self):
        '''
          To save the dataframe
        '''
        df = pd.DataFrame(data = self.data, columns = self.channels)
        df.to_csv('%s.csv' % self.subject, index = False, encoding='utf-8')

    def ann_to_csv(self):
        '''
          To save the annotations
        '''
        ann = pd.DataFrame(data = self.ann, columns = ['time', 'duration', 'label'])

        for i in range(len(ann)):
          ann.loc[i, 'label'] = ann.loc[i, 'label'][0]

        ann.to_csv('%s_ann.csv' % self.subject, index = False, encoding='utf-8')

    def signal(self):
        return self.data

    def info(self):
        return [self.smp_rate, self.channels, self.ann]

