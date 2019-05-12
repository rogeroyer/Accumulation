- dict 反序：
```
reverse_word_index = dict([(value, key) for (key, value) in word_index.items()])
```

- 将tuple转化为dict
```
>>> dict([(1, 2), (3, 4)])
{1: 2, 3: 4}
```
