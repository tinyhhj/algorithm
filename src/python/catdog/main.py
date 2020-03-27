import torch
import torchvision
import os
from model import Net

train_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((300, 300)),
    torchvision.transforms.RandomResizedCrop((150, 150)),
    torchvision.transforms.RandomRotation(20),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.5], [0.5])
])

val_transform = torchvision.transforms.Compose([
    torchvision.transforms.Resize((150, 150)),
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize([0.5, ], [0.5])
])
device = torch.device('cuda')

train_ds = torchvision.datasets.ImageFolder('data/train', transform=train_transform)
train_dl = torch.utils.data.DataLoader(train_ds, batch_size=4, shuffle=True)

val_ds = torchvision.datasets.ImageFolder('data/val', transform=val_transform)
val_dl = torch.utils.data.DataLoader(val_ds, batch_size=4, shuffle=False)

test_ds = torchvision.datasets.ImageFolder('data/test', transform=val_transform)
test_dl = torch.utils.data.DataLoader(val_ds, batch_size=4, shuffle=False)

checkpoint = 'checkpoints'
os.makedirs(checkpoint, exist_ok=True)

model = Net()
criterion = torch.nn.BCELoss()
optimizer = torch.optim.RMSprop(model.parameters(), 1e-4)


class AvgMeter(object):
    def __init__(self, name, fmt=':f'):
        self.name = name
        self.fmt = fmt
        self.reset()

    def reset(self):
        self.avg = 0
        self.total = 0
        self.val = 0
        self.count = 0

    def update(self, value, n=1):
        self.count += n
        self.val = value
        self.total += (value * n)
        self.avg = self.total / self.count

    def __str__(self):
        fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
        return fmtstr.format(**self.__dict__)


def train():
    model.train()
    avg_loss = AvgMeter('train_loss')
    avg_acc = AvgMeter('train_acc')
    total = 0
    for i, (images, targets) in enumerate(train_dl):
        images = images.to(device)
        targets = targets.to(device)
        optimizer.zero_grad()
        pred = model(images).view(-1)
        label = (pred.detach() > 0.5).float()
        # print((label == targets).sum())
        loss = criterion(pred, targets.float())
        avg_loss.update(loss.item())
        avg_acc.update((label == targets).sum().item())
        total += images.size()[0]
        loss.backward()
        optimizer.step()
    print(avg_loss)
    print(avg_acc.total / total)


def validate():
    model.eval()
    avg_loss = AvgMeter('val_loss')
    avg_acc = AvgMeter('val_acc')
    total = 0
    with torch.no_grad():
        for i, (images, targets) in enumerate(val_dl):
            images = images.to(device)
            targets = targets.to(device)
            batch_size = images.size()[0]
            pred = model(images).view(-1)
            label = (pred > 0.5).float()
            loss = criterion(pred, targets.float())
            avg_loss.update(loss.item())
            avg_acc.update((label == targets).sum().item())
            total += batch_size
        print(avg_loss)
        print(avg_acc.total / total)
    return avg_acc.total / total


def save(i, pred, best_acc):
    print('saving...')
    torch.save(model.state_dict(), os.path.join(checkpoint, f'{i}_{pred}.pth'))
    if best_acc:
        torch.save(model.state_dict(), os.path.join(checkpoint, 'best_model.pth'))
def test():
    model.eval()
    model.load_state_dict(torch.load('checkpoints/best_model.pth',map_location=lambda storage, location: storage))
    avg_acc = AvgMeter('test_acc')
    total = 0
    with torch.no_grad():
        for i, (images, targets) in enumerate(test_dl):
            pred = model(images).view(-1)
            label = (pred > 0.5)
            avg_acc.update((label == targets).sum().item())
            total += images.size()[0]

        print(avg_acc.total, total)
        print(avg_acc.total / total)
    images = torchvision.utils.make_grid(images * 0.5 + 0.5)
    import matplotlib.pyplot as plt
    plt.imshow(images.numpy().transpose((1,2,0)))
    plt.title(' '.join([test_ds.classes[x] for x in label]))
    plt.show()

if __name__ =='__main__':
    # best_acc = 0
    # for i in range(1,31):
    #     is_best = False
    #     train()
    #     pred = validate()
    #     if best_acc < pred:
    #         is_best = True
    #     save(i,pred,is_best)
    # images, target = next(iter(train_dl))
    # images = torchvision.utils.make_grid(images)
    # images * 0.5 + 0.5
    # print(images.size())
    # import matplotlib.pyplot as plt
    #
    # plt.imshow(images.numpy().transpose((1,2,0)))
    # plt.show()
    test()







