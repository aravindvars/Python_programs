from hello import hello

def test_argument():
  for name in ['Arun', 'Aravind', 'Junior']:
    assert hello(name) == f'hello {name}'   #assert statements are usually designed to test return values rather than side effects like print

def test_default():
  assert hello() =='hello world'

if __name__ == '__main__':
  main()