from trac.core import *
from trac.util.html import html
from trac.web import IRequestHandler
from trac.web.chrome import INavigationContributor

class TicketGanttPlugin(Component):
    implements(INavigationContributor, IRequestHandler)

    # INavigationContributor methods
    def get_active_navigation_item(self, req):
        return 'ticketgantt'
    def get_navigation_items(self, req):
        yield ('mainnav', 'ticketgantt',
            html.A('Gantt Ticket', href= req.href.ticketgantt()))

    # IRequestHandler methods
    def match_request(self, req):
        return req.path_info == '/ticketgantt'

    def process_request(self, req):
        content = 'Hello World!'
        req.send_response(200)
        req.send_header('Content-Type', 'text/plain')
        req.send_header('Content-Length', len(content))
        req.end_headers()
        req.write(content)
