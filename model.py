import torch
import random

class Bob(torch.nn.Module):

    def __init__(self):
        super(Bob, self).__init__()
        self.input_size = 317

        self.fc1 = torch.nn.Linear(self.input_size, 180)
        self.fc2 = torch.nn.Linear(180, 180)
        self.fc3 = torch.nn.Linear(180, 180)
        self.fc4 = torch.nn.Linear(180, 180)
        self.fc5 = torch.nn.Linear(180, 52)
        self.relu = torch.nn.ReLU()
        self.softmax = torch.nn.Softmax(dim=0)
    def forward(self, x):
        output = self.relu(self.fc1(x))
        output = self.relu(self.fc2(output))
        output = self.relu(self.fc3(output))
        output = self.relu(self.fc4(output))
        output = self.relu(self.fc5(output))

        output = self.softmax(output)

        output = output * x[52:104]

        return output

def saveBob(model, PATH):
  torch.save(model, PATH)

def loadBob(PATH):
  model = torch.load(PATH)
  model.eval()
  return model