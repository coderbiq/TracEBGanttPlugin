from genshi.builder import tag

from trac.core import *
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor, ITemplateProvider, add_script
from pkg_resources import resource_filename

class TicketGanttPlugin(Component):
    implements(INavigationContributor, IRequestHandler, ITemplateProvider)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'ticketgantt'

    def get_navigation_items(self, req):
        yield ('mainnav', 'ticketgantt',
            tag.a('Gantt Ticket', href= req.href.ticketgantt()))

    # IRequestHandler methods
    def match_request(self, req):
        return req.path_info == '/ticketgantt'

    def process_request(self, req):
        action = req.args.get('action')

        if action == None:
            re = self.show_main(req)
        elif action == 'getData':
            re = self.get_data(req)

        return re

    def show_main(self, req):
        add_script(req, 'ebgantt/js/gantt.js')
        return 'gantt.html', {}, None

    def get_data(self, req):
        return 'ganttdata.xml', {}, 'test/xml'

    def get_templates_dirs(self):
        return [resource_filename(__name__, 'templates')]

    def get_htdocs_dirs(self):
        return [('ebgantt', resource_filename(__name__, 'htdocs'))]
