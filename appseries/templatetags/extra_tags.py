from django import template
import time

register = template.Library()


@register.simple_tag
def seasep(season, episode):
    s = '%02d' % season
    e = '%02d' % episode
    return 'S{}E{}'.format(s, e)


@register.simple_tag
def show_date(air_date, status):
    if status == 'running' or status == 'announced':
        return air_date.strftime('%d/%m')
    elif status == 'terminated':
        return '----'
    elif status == 'seasonend':
        return '????'