#from django.db.models import get_model
from django import template
from blogman.models import Entry

class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''

def do_latest_entries(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly for arguments")
    return LatestContentNode(bits[1], bits[2], bits[4])

register = template.Library()
register.tag('get_latest_entries', do_latest_entries)