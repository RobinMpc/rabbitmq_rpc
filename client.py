import oslo_messaging as messaging  
from oslo_config import cfg  
  
CONF = cfg.CONF  
CONF(default_config_files=['app.conf'])  
 
ctxt = {'c':'d'}  
arg = {'a':'b'}  
  
transport = messaging.get_transport(cfg.CONF)  
target = messaging.Target(topic='test123')  
client = messaging.RPCClient(transport, target)  
print client.call(ctxt, 'test', arg=arg)
cctxt = client.prepare()
print cctxt.cast({'aa':'bb'}, 'stop')
