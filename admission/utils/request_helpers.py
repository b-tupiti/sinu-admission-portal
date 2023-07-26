
def is_put_request(request):
    """
    checks if the request object actually simulates a PUT request.
    """
    return request.method == 'POST' and request.POST.get('_method') == 'put'