def caterpillar(n):
    if n < 2:
        return 'Length should at least 2'
    body = 'Q' * (n - 1)
    tail = '6'
    return body + tail


def caterpillar_with_backside(n):
    if n < 3:
        return 'Since it need head, body, and tail, the length should at least 3'
    head = 'c'
    body = 'Q' * (n - 2)
    tail = '6'
    return head + body + tail
