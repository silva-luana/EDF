from edf2csv import EDF

subject = 'FA96319X.edf'

edf = EDF(subject)

signal = edf.signal()
info = edf.info()

print signal.shape
print info

edf.ann_to_csv()
edf.signal_to_csv()