import logging
from main import run
from tcpServer import tcpServer, setTCPServer

logger = logging.getLogger('server_logger')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('grpc_server.log')
fh.setLevel(logging.DEBUG)

logger.addHandler(fh)

setTCPServer(tcpServer("0.0.0.0", 7780))
run()