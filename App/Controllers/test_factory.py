class Factory:
    def process(self, input):
        raise NotImplementedError

class Extract(Factory):
    def process(self, input):
        print("Extracting...")
        output = {}
        return output

class Parse(Factory):
    def process(self, input):
        print("Parsing...")
        output = {}
        return output

class Load(Factory):
    def process(self, input):
        print("Loading...")
        output = {}
        return output

pipe = {  
    "extract" : Extract(),
    "parse" : Parse(),
    "load" : Load(),
}

inputs = {}  

for name, instance in pipe.items():  
    inputs = instance.process(inputs)