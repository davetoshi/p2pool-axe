from p2pool.axe import networks

PARENT = networks.nets['axe']
SHARE_PERIOD = 20 # seconds
CHAIN_LENGTH = 24*60*60//20 # shares
REAL_CHAIN_LENGTH = 24*60*60//20 # shares
TARGET_LOOKBEHIND = 100 # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
SPREAD = 10 # blocks
IDENTIFIER = 'e238d5b0c6932427'.decode('hex')
PREFIX = '9420c1a53ef76493'.decode('hex')
COINBASEEXT = '3a1039186f6f9c2d4d15432f'.decode('hex')
P2P_PORT = 8999
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 7903
BOOTSTRAP_ADDRS = '202.91.32.72'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-axe'
VERSION_CHECK = lambda v: v >= 102010
