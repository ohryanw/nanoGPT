out_dir = 'out-code-generation'
eval_interval = 250
eval_iters = 20
log_interval = 10

always_save_checkpoint = True

wandb_log = False

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 12
block_size = 128

n_layer = 6
n_head = 6
n_embd = 192
dropout = 0.2

learning_rate = 1e-3
max_iters = 5000
lr_decay_iters = 5000
min_lr = 1e-4
beta2 = 0.99

warmup_iters = 100

device = 'cpu'
compile = False