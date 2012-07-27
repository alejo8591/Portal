#from django.db.models import get_model
from django import template
from blogman.models import Entry

class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''


def do_latest_entries(parser, token):
    return LatestEntriesNode()

register = template.Library()
register.tag('get_latest_entries', do_latest_entries)