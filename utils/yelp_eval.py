from evaluate import Evaluation
from submit import load_submit, combine_sub
from load_yelp_data import load_item, load_user

class Evaluate(Evaluation):
    def __init__(self, logit_ind2item_ind, 
        res_filename='../submissions/yelp_res_T', 
        hist_filename = '../submissions/yelp_historical_train', ta=1, 
        old=False, data_dir=None, test=False):

        self.logit_ind2item_ind = logit_ind2item_ind
        res_filename = res_filename + '_test.csv' if test else res_filename + '.csv'
        self.T = load_submit(res_filename)
        hist_filename = hist_filename + '_test.csv' if test else hist_filename + '.csv'
        self.hist = load_submit(hist_filename)
        self.Iatt, _, self.Iid2ind = load_item()
        self.data_dir = data_dir

        self.Uatt, _, self.Uid2ind = load_user()

        self.Uids = self.get_uids()
        self.Uinds = [self.Uid2ind[v] for v in self.Uids]
        self.old = old
        self.combine_sub = combine_sub
        return
