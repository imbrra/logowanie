import os

@given(u'jestem zalogowany na komputerze')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Given jestem zalogowany na komputerze')
    context.os=os

@when(u'sprawdzam liczbe procesorow')
def step_impl(context):
    #raise NotImplementedError(u'STEP: When sprawdzam liczbe procesorow')
    os=context.os
    com="cat /proc/cpuinfo | grep proces | wc -l"
    context.ilosc_linijek=os.popen(com).read().strip()

@then(u'otrzymuje wynik z liczba procesorow')
def step_impl(context):
    #raise NotImplementedError(u'STEP: Then otrzymuje wynik z liczba procesorow')
    print context.ilosc_linijek
    assert context.ilosc_linijek == "2"

