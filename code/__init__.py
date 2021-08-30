#import code.test_me
#from .test_me import inc
#from .test_me import test_answer

#__all__ = ['test_me']

def inc(x):
    return x + 1

def test_answer():
    assert inc(3) == 4
