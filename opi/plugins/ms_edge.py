import opi
from opi.plugins import BasePlugin
import subprocess

class MSEdge(BasePlugin):
	main_query = "msedge"
	description = "Microsoft Edge"
	queries = ('microsoftedge', 'msedge', 'edge')

	@classmethod
	def run(cls, query):
		if not opi.ask_yes_or_no("Do you want to install Edge from Microsoft repository?", 'y'):
			return

		opi.add_repo(
			filename = 'microsoft-edge',
			name = 'MS Edge',
			url = 'https://packages.microsoft.com/yumrepos/edge',
			gpgkey = 'https://packages.microsoft.com/keys/microsoft.asc'
		)

		opi.install_packages(['microsoft-edge-dev'])
		opi.ask_keep_repo('microsoft-edge')