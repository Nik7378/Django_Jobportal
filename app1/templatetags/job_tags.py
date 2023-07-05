from django import template
from ..models import job
from django.db.models import Max, Subquery ,Q

register = template.Library()

@register.simple_tag
def trending_job(total=3):
    trending = job.objects.all().order_by('-views').distinct()[:total]
    return { 'trending':trending }


@register.inclusion_tag("job/trending_job.html")
def show_trending_job(total=5):
    trending = job.objects.order_by('-views').distinct()[:total]
    total_trending_jobs = job.objects.order_by('-views').distinct().count()
    # trending = job.objects.filter(Q(job.objects.values('role').distinct()), Q(job.objects.order_by('-views')))[:total]
    # trending = job.objects.filter(
    # role__in=Subquery(
    #    job.objects.all().distinct().values('role')
    # )
    # ).order_by('-views')
    return { 'trending':trending, 'total_trending_jobs': total_trending_jobs}
