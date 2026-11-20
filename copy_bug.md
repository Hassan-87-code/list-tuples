# The `[[0] * 3] * 3` trap

This expression looks like it creates three separate rows:

```python
grid = [[0] * 3] * 3
grid[0][0] = 1
print(grid)
```

But the result is:

```text
[[1, 0, 0], [1, 0, 0], [1, 0, 0]]
```

The outer multiplication repeats references to the same inner list; it does not
make new inner lists. Changing one row therefore changes what appears in every
row.

Create each row separately with a comprehension instead:

```python
grid = [[0] * 3 for _ in range(3)]
grid[0][0] = 1
print(grid)
```

Now the result is:

```text
[[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```
