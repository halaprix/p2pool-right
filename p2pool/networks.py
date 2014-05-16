from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(

 bankcoin=math.Object(
        PARENT=networks.nets['bankcoin'],
        SHARE_PERIOD=20, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        IDENTIFIER='dddd47d48857ee11'.decode('hex'),
        PREFIX='dddda27366ddee98'.decode('hex'),
        P2P_PORT=6564,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=6565,
        BOOTSTRAP_ADDRS='p2poolcoin.com ca.p2poolcoi.com'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-bank',
        VERSION_CHECK=lambda v: True,
    ),
 rightcoin=math.Object(
        PARENT=networks.nets['rightcoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=24*60*60//10, # shares
        REAL_CHAIN_LENGTH=24*60*60//10, # shares
        TARGET_LOOKBEHIND=50, # shares  //with that the pools share diff is adjusting faster, important if huge hashing power comes to the pool
        SPREAD=30, # blocks
        IDENTIFIER='11dddd47d48857ee'.decode('hex'),
        PREFIX='98dddda27366ddee'.decode('hex'),
        P2P_PORT=6563,
        MIN_TARGET=4,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=6564,
        BOOTSTRAP_ADDRS='freebtc.eu'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-right',
        VERSION_CHECK=lambda v: True,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
