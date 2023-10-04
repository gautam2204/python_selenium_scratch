import pytest

random = 101
word = 'registration'

def inc(a:int):
    return a+2

@pytest.mark.skip("Not related to selenium")
def test_validateSum():
    assert inc(3) == 5
    
@pytest.mark.skipif(random>100,reason="Skipped cause random value is more than 100")
def test_validateSum1():
    assert inc(3) == 5
    
    
@pytest.mark.skipif(word.__contains__("registration"),reason="skipped coz contains word registration")
def test_validateSum2():
    assert inc(3) == 5
    
@pytest.mark.skipif(word.__contains__("registration"),reason="skipped coz contains word registration")
def test_validateSum2():
    assert inc(3) == 5
    
@pytest.mark.smoke
def test_validateSum3():
    assert inc(2) == 5
   
def dataGenerator():
    li = [['userName1','password1'],['userName2','password2']]
    return li

@pytest.mark.parametrize("data",dataGenerator())
def test_parametrizedCalidation(data):
    print("####################Test Code#######################")
    print(f"List values {data[0]}")    

