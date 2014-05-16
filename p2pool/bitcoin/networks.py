import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack, jsonrpc

@defer.inlineCallbacks
def check_genesis_block(bitcoind, genesis_block_hash):
    try:
        yield bitcoind.rpc_getblock(genesis_block_hash)
    except jsonrpc.Error_for_code(-5):
        defer.returnValue(False)
    else:
        defer.returnValue(True)

@defer.inlineCallbacks
def get_subsidy(bitcoind, target):
    res = yield bitcoind.rpc_getblock(target)

    defer.returnValue(res)

nets = dict(

 bankcoin=math.Object(
        P2P_PREFIX='b1b2b3b4'.decode('hex'),
        P2P_PORT=26666,
        ADDRESS_VERSION=25,
        RPC_PORT=27777,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bankcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),                           
        SUBSIDY_FUNC=lambda bitcoind, target: get_subsidy(bitcoind, target),
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        BLOCK_PERIOD=60, # s
        SYMBOL='BANK',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'bankcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/bankcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bankcoin'), 'bankcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
 rightcoin=math.Object(
        P2P_PREFIX='xx'.decode('hex'),
        P2P_PORT=xx,
        ADDRESS_VERSION=xx,
        RPC_PORT=xx,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'rightcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),                           
        SUBSIDY_FUNC=lambda bitcoind, target: get_subsidy(bitcoind, target),
        BLOCKHASH_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('xcoin_hash').getPoWHash(data)),
        BLOCK_PERIOD=30, # s
        SYMBOL='RTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'rightcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/rightcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.rightcoin'), 'rightcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='',
        ADDRESS_EXPLORER_URL_PREFIX='',
        TX_EXPLORER_URL_PREFIX='',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**20 - 1), 
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
