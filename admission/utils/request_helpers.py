def is_put_request(request):
    """
    checks if the request object simulates a PUT request.
    """
    return request.method == 'POST' and request.POST.get('_method') == 'put'


def param_not_found_or_empty(param):
    """
    checks if param does not exist, or does but is empty.
    """
    return not param