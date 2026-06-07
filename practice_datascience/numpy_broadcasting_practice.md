# NumPy Broadcasting — Practice Questions

A problem set moving from fundamentals to real-world applications. Try to answer before checking the explanation.

---

## Part 1: The Rules

**Q1.** State the two rules NumPy uses to decide whether two arrays can be broadcast together, and what happens to the shapes when they can.

*Explanation:* Compare shapes element-wise from the **trailing** (rightmost) dimension. Two dimensions are compatible when (a) they are equal, or (b) one of them is 1. Missing dimensions on the smaller-shaped array are treated as 1 (effectively prepended). Wherever a dimension is 1, the array is "stretched" (conceptually copied, not actually in memory) to match the other array's size along that axis. If neither condition holds for some dimension, broadcasting fails with a `ValueError`.

---

**Q2.** Which of these shape pairs can broadcast together, and what is the resulting shape?
a) `(3, 4)` and `(4,)`
b) `(8, 1, 6, 1)` and `(7, 1, 5)`
c) `(3, 4)` and `(3,)`
d) `(2, 3)` and `(2, 3, 4)`

*Explanation:*
a) Yes → `(3, 4)`. The `(4,)` is treated as `(1, 4)`, then stretched to `(3, 4)`.
b) Yes → `(8, 7, 6, 5)`. Align from the right: `(8,1,6,1)` vs `(_,7,1,5)` → pad to `(1,7,1,5)`; pairwise: 8&1→8, 1&7→7, 6&1→6, 1&5→5.
c) **No.** Aligning from the right, `(3,)` becomes `(1, 3)`. Compare `4` vs `3` — neither is 1 nor equal → error. (To broadcast a length-3 vector against `(3,4)`'s rows, you'd need shape `(3, 1)`.)
d) **No** as written — but if the smaller array is reshaped/expanded, e.g., `(1, 2, 3)`, it would align with `(2, 3, 4)`... actually check trailing dims: `3` vs `4` mismatch, so still no. Broadcasting only works on shapes whose trailing dimensions line up or are 1.

---

**Q3.** Real-world setup: you have a table of daily sales for 5 stores over 30 days, stored as `sales` with shape `(30, 5)`. You also have a single array `region_tax` with shape `(5,)` giving each store's tax rate. Write the broadcasting expression that computes after-tax sales for every store on every day, and explain why it works without writing a loop.

*Explanation:* `sales * (1 - region_tax)`. NumPy aligns the trailing axis: `(30, 5)` and `(5,)`→`(1, 5)`→stretched to `(30, 5)`. Each store's tax rate is applied to its column across all 30 days simultaneously — this is the classic "per-column scalar" broadcast pattern, and it avoids a Python-level loop over 150 cells, running instead as a single vectorized C-level operation.

---

## Part 2: Making Shapes Line Up

**Q4.** You have `temperatures` with shape `(365,)` (one reading per day of the year) and want to subtract the **annual mean** from every day, then separately subtract the **mean of each month** (assume you've reshaped into `monthly = temperatures.reshape(12, -1)`-like structure, or have a `(12,)` array of monthly means and a `(365,)` array of "which month" labels). Focus on the simpler case: given `monthly_data` of shape `(12, 31)` (padded) and `monthly_means` of shape `(12,)`, what do you need to do before subtracting so broadcasting produces the right result — and what happens if you forget?

*Explanation:* You must reshape `monthly_means` to `(12, 1)` — e.g. `monthly_means[:, np.newaxis]` or `.reshape(-1, 1)` — so the trailing dimensions are `31` vs `1` (compatible, stretches across each row). If you forget and write `monthly_data - monthly_means`, NumPy aligns from the right: `(12, 31)` vs `(12,)`→`(1, 12)`. Since `31 != 12` and neither is 1, you get a `ValueError: operands could not be broadcast together`. This is the single most common broadcasting bug: confusing "a vector of per-row values" with "a vector of per-column values" — the fix is always to make the intended axis explicit with `np.newaxis` / `None` indexing or `.reshape`.

---

**Q5.** Given a 2D array of word-embedding vectors `embeddings` with shape `(10000, 300)` (10,000 words, 300-dim vectors) and a single query vector `query` with shape `(300,)`, write a one-line broadcasting expression to compute the Euclidean distance from `query` to every word, returning a `(10000,)` array of distances. Explain the shape of every intermediate array.

*Explanation:*
```python
distances = np.sqrt(((embeddings - query) ** 2).sum(axis=1))
```
- `embeddings - query`: `(10000, 300)` minus `(300,)` → query broadcasts as `(1, 300)` then stretches to `(10000, 300)`; result shape `(10000, 300)`.
- `** 2`: elementwise, shape unchanged, `(10000, 300)`.
- `.sum(axis=1)`: collapses the 300-dim axis → `(10000,)`.
- `np.sqrt(...)`: elementwise, shape unchanged, `(10000,)`.

This single expression replaces what would otherwise be a 10,000-iteration Python loop — it's the core operation behind nearest-neighbor search in recommendation systems and semantic search over embeddings.

---

**Q6.** You want to build a `(5, 5)` "pairwise difference" matrix from a 1D array `x = np.array([1, 2, 3, 4, 5])`, where entry `[i, j] = x[i] - x[j]`. Using only broadcasting (no loops, no `np.subtract.outer`), write the expression — and explain how the two operands' shapes make this possible.

*Explanation:*
```python
diff = x[:, np.newaxis] - x[np.newaxis, :]
# or equivalently: x.reshape(-1, 1) - x.reshape(1, -1)
```
`x[:, np.newaxis]` has shape `(5, 1)`; `x[np.newaxis, :]` has shape `(1, 5)`. Broadcasting stretches the first along axis 1 (columns) and the second along axis 0 (rows), producing a `(5, 5)` result where row `i`, column `j` is `x[i] - x[j]`. This "outer" broadcasting pattern — a column vector against a row vector — is how you generate distance matrices, attention score matrices in transformers (`Q @ K.T` aside, raw position-difference matrices use exactly this trick), and grids of coordinates (`np.meshgrid` is partly built on it).

---

## Part 3: Where Broadcasting Shows Up in ML

**Q7.** In batch normalization (or simple feature standardization), you have a batch of data `X` with shape `(batch_size, num_features) = (64, 20)`, a `mean` of shape `(20,)`, and a `std` of shape `(20,)`. Write the standardization expression and explain why this generalizes correctly to *any* batch size without changes to `mean` or `std`.

*Explanation:* `X_norm = (X - mean) / std`. Both `mean` and `std` have shape `(20,)`, which broadcasts against `(batch_size, 20)` by aligning on the trailing (feature) axis — the batch axis is stretched to whatever `batch_size` is at runtime. This is exactly why frameworks like PyTorch/TensorFlow store per-feature statistics as 1D tensors: broadcasting lets the *same* statistics array apply uniformly whether your batch has 1, 64, or 10,000 examples, with zero reshaping logic in the training loop.

---

**Q8.** Image processing: an RGB image is stored as `img` with shape `(height, width, 3)`. You want to (a) convert it to grayscale-weighted channels by multiplying each channel by weights `[0.299, 0.587, 0.114]`, and (b) add a per-pixel brightness mask of shape `(height, width)` to all three channels equally. Write both expressions and identify which axes broadcasting aligns in each case.

*Explanation:*
a) `weighted = img * np.array([0.299, 0.587, 0.114])` — the weights array has shape `(3,)`, which aligns with the **trailing** axis of `(height, width, 3)`; it's treated as `(1, 1, 3)` and stretched across height and width. Each channel gets its own scalar weight at every pixel.
b) `brightened = img + mask[:, :, np.newaxis]` — `mask` is `(height, width)`; you must add a trailing axis to get `(height, width, 1)` so it broadcasts against `(height, width, 3)` by stretching across the channel axis. Without `[:, :, np.newaxis]`, `(height, width)` would try to align its trailing `width` against `img`'s trailing `3` — mismatch (unless `width == 3`, a nasty silent bug).

This pair of examples is a good illustration of *why* broadcasting aligns from the right: channel-like data is conventionally the last axis, so per-channel operations broadcast "for free," while per-pixel operations need an explicit new axis.

---

**Q9. (Debugging)** The following code throws `ValueError: operands could not be broadcast together with shapes (100,3) (100,)`:
```python
points = np.random.rand(100, 3)       # 100 points in 3D
norms = np.linalg.norm(points, axis=1) # shape (100,) — length of each point
unit_vectors = points / norms
```
Diagnose the bug and provide the corrected line.

*Explanation:* The intent is "divide each 3D point by its own length" — a per-row operation — but `norms` has shape `(100,)`, which broadcasting aligns against the **trailing** axis (length 3) of `points`, not the row axis. Since `100 != 3`, it errors (and if it happened to not error — e.g., if there were exactly 3 points — it would silently produce wrong results by dividing columns instead of rows). Fix:
```python
unit_vectors = points / norms[:, np.newaxis]   # norms reshaped to (100, 1)
```
Now `(100, 3)` and `(100, 1)` align: trailing dims `3` vs `1` → stretch; leading dims `100` vs `100` → match. Result shape `(100, 3)`, each row divided by its own scalar norm. General lesson: whenever a "length-N vector operating against a 2D array" doesn't do what you expect, ask "am I broadcasting along the row axis or the column axis?" and add `np.newaxis` to make the intended axis explicit.

---

## Part 4: Stretch Questions

**Q10.** Without running code, predict the output shape and describe the result of:
```python
a = np.arange(3)              # shape (3,)
b = np.arange(3).reshape(3,1) # shape (3,1)
result = a + b
```

*Explanation:* Shapes `(3,)` → `(1, 3)` and `(3, 1)`. Broadcasting stretches the first to `(3, 3)` (repeating the row `[0,1,2]` down each row) and the second to `(3, 3)` (repeating the column `[0,1,2]` across each column). The result is a `(3, 3)` addition table:
```
[[0 1 2]
 [1 2 3]
 [2 3 4]]
```
This "row vector + column vector → matrix" pattern is the textbook example of broadcasting creating an entirely new array of larger size from two smaller ones — no memory copy of the inputs occurs, but the *output* is a full `(3,3)` array.

**Q11. (Conceptual)** Why does NumPy implement broadcasting via "virtual stretching" (using strides of 0) rather than physically copying data to match shapes before the operation? What would the practical cost be if it did copy?

*Explanation:* NumPy gives the smaller array a stride of 0 along the broadcast axis, so the same memory is read repeatedly without duplication — broadcasting an `(300,)` array against `(10000, 300)` costs no extra memory for the input. If NumPy physically copied, broadcasting `mean` (shape `(20,)`, ~160 bytes) against a batch of shape `(1000000, 20)` would require materializing a `(1000000, 20)` copy of `mean` — 160 MB instead of 160 bytes — for every single broadcasted operation in a training loop. Virtual stretching is what makes broadcasting both memory-efficient and fast (it's implemented in optimized C loops operating directly on strided views).

---

*Tip for self-study:* for any broadcasting expression that confuses you, run `np.broadcast_shapes(shape1, shape2)` first — it tells you the resulting shape (or raises an error) without computing anything, which is the fastest way to build intuition.
