class Response:
    def __init__(self, Status, Description, Data):
        self.Status = Status
        self.Description = Description
        self.Data = Data
    
    def GetData(self):
        ResponseData = {}

        ResponseData['Status'] = self.Status
        
        if self.Status == 'failed':
            ResponseData['Description'] = self.Description

        ResponseData['Data'] = self.Data

        return ResponseData

