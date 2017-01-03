import numpy as np

import data_utils
import seq2seq_wrapper


'''
    init

'''
print('>> Initializing data')
# load data from pickle and npy files
idx2w, w2idx, limit = data_utils.get_metadata()

# parameters 
xseq_len = limit['maxq']
yseq_len = limit['maxa']
batch_size = 1
xvocab_size = len(idx2w)  
yvocab_size = xvocab_size
emb_dim = 1024


print('>> Initializing model')
model = seq2seq_wrapper.Seq2Seq(xseq_len=xseq_len,
                               yseq_len=yseq_len,
                               xvocab_size=xvocab_size,
                               yvocab_size=yvocab_size,
                               ckpt_path='ckpt/',
                               emb_dim=emb_dim,
                               num_layers=3
                               )

print('\n>> Loading pretrained model')
sess = model.restore_last_session()
print('>> Initialization complete; call respond(msg)')


'''
    interface

'''
def respond(msg):
    encoded_msg = data_utils.encode(msg, w2idx, limit['maxq'])
    response = model.predict(sess, encoded_msg)[0]
    return data_utils.decode(response, idx2w)
