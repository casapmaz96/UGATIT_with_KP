import torch.nn as nn
import torch.nn.functional as F


class KeypointPredictor(nn.Module):
    def __init__(self):
        super(KeypointPredictor, self).__init__()
        self.conv1 = nn.Conv2d(3, 5, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(5, 16, 5)
        self.fc1 = nn.Linear(16 * 41 * 41, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        #print("0: ", x.shape)
        x = F.relu(self.conv1(x))
        #print("1 :", x.shape)
        x = self.pool(x)
        #print("2: ",x.shape)
        x = F.relu(self.conv2(x))
        #print("3: ",x.shape)
        x = self.pool(x)
        #print("4: ", x.shape)
        x = x.view(1, -1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


#net = Net()

