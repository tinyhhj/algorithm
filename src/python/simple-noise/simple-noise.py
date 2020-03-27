import torch
import matplotlib.pyplot as plt
from PIL import Image

# sum noise to func
x = torch.empty(1000, 1).uniform_(-10,10)
noise = torch.empty(1000,1).normal_()
y = x * 3 + 4
y_noise = y + noise

# linear func
model = torch.nn.Linear(1,1)
loss = torch.nn.L1Loss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

#traning
for i in range(1000):
    optimizer.zero_grad()
    pred = model(x)
    l = loss(pred, y_noise)
    l.backward()
    optimizer.step()
for p in model.parameters():
    # 2.990126848220825
    # 3.999316453933716
    print(p.item())
plt.plot(x.numpy(),y_noise.numpy(),'ro')
plt.plot(x.numpy(),model(x).detach().numpy(),'o')
plt.show()

x = torch.empty(1000,1).uniform_(-10,10)
noise = torch.empty(1000,1).normal_(std=2)
y = 3*(x**2)+4
y_noise = y + noise

model = torch.nn.Sequential(
    torch.nn.Linear(1,5), # w*x (1000,1) (1,5)
    torch.nn.ReLU(),
    torch.nn.Linear(5,1),
    torch.nn.ReLU())
loss_func = torch.nn.L1Loss()
optimizer = torch.optim.SGD(model.parameters(), lr = 0.01)

for i in range(10000):
    optimizer.zero_grad()
    pred= model(x)
    loss = loss_func(pred, y_noise)
    loss.backward()
    optimizer.step()

print(model[0])
print(model[2])
plt.figure()
plt.plot(x.numpy(),y_noise.numpy(),'ro')
plt.plot(x.numpy(),model(x).detach().numpy(),'o')
plt.show()

print(torch.ones(1000,5) + torch.randn(5,1))


