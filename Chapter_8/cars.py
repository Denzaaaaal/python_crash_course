def car(manufacturer, model_name, **kargs):
    kargs['manufacturer'] = manufacturer
    kargs['model_name'] = model_name
    return kargs

build_car = car('subaru', 'outback', colour='blue', tow_package='True')
print (build_car)