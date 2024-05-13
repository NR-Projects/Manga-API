class Response:
    def __init__(self, Description: str, Data):
        self.Description = Description
        self.Data = Data
    
    def GetData(self):
        ResponseData = {}
        
        ResponseData['Description'] = self.Description
        ResponseData['Data'] = self.Data

        return ResponseData

