import wcargs_history.cli as hello_wcargs

def test_hello():
    m = hello_wcargs.hello_wcargs()
    assert m == "hello"
