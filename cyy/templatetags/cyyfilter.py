from django import template
import re
register = template.Library()


@register.filter(name='one_two')
def one_two(value):
	if len(str(value)) == 1:
		return '0' + str(value)
	else:
		return str(value)

@register.filter(name='tag_split')
def tag_split(value):
	if value:
		return re.split(' *',value.strip())
