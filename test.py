from sklearn.metrics import classification_report
from PIL import Image
from model import Model

model = Model()
preds = []
truths = []
for name in ["grant", "connor", "max", "emre"]:
    for i in range(25):
        path = f"/home/facebeer/data/data/{name}/{str(i).zfill(5)}.jpg"
        img = Image.open(path)
        pred, _ = model.predict(img)
        preds.append(pred)
        truths.append(name)
print(classification_report(truths, preds))
