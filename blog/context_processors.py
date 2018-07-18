from django.contrib.sites.models import Site


current_site = Site.objects.get_current()


def rblog_global_context(request, domain=current_site.domain):
    return {"site": f"{domain}"}

