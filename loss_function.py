import torch

class SzczepanikLoss(torch.nn.Module):
    def __init__(self):
        super(SzczepanikLoss, self).__init__()
        self.loss = torch.nn.MSELoss()
    def forward(self, inputs, tricks_taken):
        gt = torch.clone(inputs)
        gt[torch.argmax(gt)] += 13 - tricks_taken
        return self.loss(inputs, gt)