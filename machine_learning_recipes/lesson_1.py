from sklearn import tree

TEXTURES = {
    'bumpy': 0,
    'smooth': 1
}

LABELS = {
    'apple': 0,
    'orange': 1
}

REVERSE_LABELS = {
    '0': 'apple',
    '1': 'orange'
}


FEATURES = [
    [140, TEXTURES['smooth']],
    [130, TEXTURES['smooth']],
    [150, TEXTURES['bumpy']],
    [170, TEXTURES['bumpy']]
]

MY_LABELS = [
    LABELS['apple'],
    LABELS['apple'],
    LABELS['orange'],
    LABELS['orange']
]

CLF = tree.DecisionTreeClassifier()
FIT_MODEL = CLF.fit(FEATURES, MY_LABELS)
print(
    f'\n\nThis fruit must be an {REVERSE_LABELS[str(FIT_MODEL.predict([[160, 0]])[0])]}\n\n')
