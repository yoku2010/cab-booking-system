from django.contrib.auth.models import User, Group

def get_group_choices():
    groups = [(g.name,' '.join(g.name.split('_')).title()) for g in Group.objects.all()]
    groups.insert(0, ('', '- Select Group -'))
    return groups

def get_user_choices():
    users = [(u.id,('%s %s' % (u.first_name and u.first_name or u.username, u.last_name and u.last_name or '')).title()) for u in User.objects.all()]
    users.insert(0, ('', '- Select User -'))
    return users
