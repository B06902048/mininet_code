from ryu.base import app_manager
from ryu.ofproto import ofproto_v1_0
from ryu.controller.handler import set_ev_cls, CONFIG_DISPATCHER, MAIN_DISPATCHER
from ryu.controller import ofp_event


class L2Switch(app_manager.RyuApp):
	OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]


	def __init__(self, *args, **kwargs):
		super(L2Switch, self).__init__(*args, **kwargs)

	@set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
	def switch_feature_handler(self, event):
		datapath = event.msg.datapath
		print(datapath)
