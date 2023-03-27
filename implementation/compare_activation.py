import torch
import torch.nn as nn
import torch.optim as optim


x = torch.tensor([1.0])
y = torch.tensor([0.0])

model = nn.Sequential(nn.Linear(1, 1), nn.Sigmoid(), nn.Linear(1,1))
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr = 0.01)

for i in range(30):
    optimizer.zero_grad()
    out = model(x)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()

print(model(x))

model = nn.Sequential(nn.Linear(1, 1), nn.ReLU(), nn.Linear(1,1))

for i in range(30):
    optimizer.zero_grad()
    out = model(x)
    loss = criterion(out, y)
    loss.backward()
    optimizer.step()

print(model(x))