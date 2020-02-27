from imgaug import augmenters as iaa

augmenter = iaa.Sequential(
    [
        iaa.Fliplr(0.5),#水平翻转50%
    ],
    random_order=True,
)
