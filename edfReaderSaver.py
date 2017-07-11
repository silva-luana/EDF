import eegtools
import pandas as pd

def edfreader(subject):
    # Load Signal
    d = eegtools.io.load_edf(subject)

    data = d.X.transpose()
    smp_rate = d.sample_rate
    channels = d.chan_lab
    ann = d.annotations

    # Save dataframe
    df = pd.DataFrame(data = data, columns = channels)
    df.to_csv('%s.csv' % subject, index = False, encoding='utf-8')

    # Save annotations
    ann = pd.DataFrame(data = ann, columns = ['time', 'duration', 'label'])

    for i in range(len(ann)):
      ann.loc[i, 'label'] = ann.loc[i, 'label'][0]

    ann.to_csv('%s_ann.csv' % subject, index = False, encoding='utf-8')

