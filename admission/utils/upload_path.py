def upload_path(instance, filename):
    return 'application_{0}/{1}'.format(instance.id, filename)