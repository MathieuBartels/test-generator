class FuncState:
    def __init__(self, call_args, name, filename):
        self.name = name
        self.filename = filename
        self.call_args = call_args
        self.return_value = None

    def __str__(self):
        return f"{self.name} {self.call_args} {self.return_value}"

calls = {}

def tracefunc(frame, event, arg):
    if not frame.f_code.co_name in ["plus", "min"]:
        return tracefunc
    if event == "call":
        call_args = {}
        for i in range(frame.f_code.co_argcount):
            name = frame.f_code.co_varnames[i]
            call_args[name] = frame.f_locals[name]
        calls[id(frame)] = FuncState(call_args, frame.f_code.co_name, frame.f_code.co_filename)
    elif event == "return":
        calls[id(frame)].return_value = arg
    return tracefunc

import sys
sys.settrace(tracefunc)

from source import plus

for call in calls:
    print(call, calls[call])