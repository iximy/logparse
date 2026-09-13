from logparse.cache import cache_parse


def test_cache_reuses_result():
    line = '1.1.1.1 - - [x] "GET / HTTP/1.1" 200 0'
    a = cache_parse(line)
    b = cache_parse(line)
    assert a is b
