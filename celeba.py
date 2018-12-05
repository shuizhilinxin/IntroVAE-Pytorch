from    torchvision import datasets, transforms


def load_celeba(root):

    transform = transforms.Compose([
        # transforms.RandomSizedCrop(224),
        # transforms.RandomHorizontalFlip(),
        transforms.Resize([1024, 1024]),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],
                             std=[0.229, 0.224, 0.225])
    ])

    db = datasets.ImageFolder(root, transform=transform)

    return db