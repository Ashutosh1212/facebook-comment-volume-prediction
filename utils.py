import numpy as np


# requires an input array of at least size 10
def get_hits_at_ten(actual, predicted):
    order_actual = np.argsort(actual)
    order_predicted = np.argsort(predicted)
    top_ten_actual = order_actual[-10:]
    top_ten_predicted = order_predicted[-10:]
    commonalities = np.intersect1d(top_ten_predicted, top_ten_actual)
    hits_at_ten = len(commonalities)
    return hits_at_ten