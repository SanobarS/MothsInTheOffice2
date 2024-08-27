import logging
import azure.functions as func
import RiskAnalytics

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridTrigger1(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')

app.register_functions(RiskAnalytics)
