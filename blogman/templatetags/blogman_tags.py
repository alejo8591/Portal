#from django.db.models import get_model
from django import template
from blogman.models import Entry
from django.db.models import get_model

class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.live.all()[:5]
        return ''

def do_latest_content(parser, token):
    bits = token.split_contents()
    if len(bits) != 5:
        raise template.TemplateSyntaxError("'get_latest_content' tag takes exactly for arguments")
    model_args = bits[1].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_contet' must be an 'aplication name'.'model name' string")
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("'get_latest_contet' tag got an invalid model: %s" % bits[1])
    return LatestContentNode(model, bits[2], bits[4])

register = template.Library()
register.tag('get_latest_content', do_latest_content)