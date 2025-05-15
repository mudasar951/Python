def make_car(manufacturer, model, **kwargs):
    kwargs['manufacturer'] = manufacturer
    kwargs['model'] = model

    return kwargs