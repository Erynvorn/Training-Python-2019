s45th_a10th = {'ns' : 'green', 'ew':'red' }
s44th_a10th = {'ns' : 'red' , 'ew': ' green' }

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'
    assert 'red' in stoplight.values(), 'Neither light is red ! ' + str(stoplight)


switchLights(s45th_a10th)
