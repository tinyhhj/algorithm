import torch

class Net(torch.nn.Module):
    def __init__(self):
        super().__init__()
        layers = []
        layers.append(torch.nn.Conv2d(3,32,3))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(2))
        layers.append(torch.nn.Conv2d(32,64,3))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(2))
        layers.append(torch.nn.Conv2d(64,128,3))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(2))
        layers.append(torch.nn.Conv2d(128,128,3))
        layers.append(torch.nn.ReLU())
        layers.append(torch.nn.MaxPool2d(2))

        self.conv = torch.nn.Sequential(*layers)
        self.input_size = 150
        for i in range(4):
            self.input_size = self.cal_size(self.input_size)
        self.fc1 = torch.nn.Linear(self.input_size*self.input_size*128, 512)
        self.fc2 = torch.nn.Linear(512,1)

        def init_func(m):
            classname = m.__class__.__name__
            if hasattr(m, 'weight') and (classname.find('Conv') != -1 or classname.find('Linear') != -1):
                torch.nn.init.kaiming_uniform_(m.weight.data)

        self.apply(init_func)
    def forward(self,x):
        x = self.conv(x)
        x = torch.relu(self.fc1(x.view(-1,self.input_size**2 * 128)))
        x = torch.sigmoid(self.fc2(x))
        return x

    def cal_size(self,input_size):
        return (input_size-2) //2