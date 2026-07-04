# Pandas Practice: Exploring a School Database

**Dataset:** `student_database.xlsx`
**You will need:** Python, `pandas`, and `openpyxl` installed (`pip install pandas openpyxl` if you don't have them yet).

This workbook has several sheets: `Students`, `AL_Results`, `Clubs_Activities`, `Sports`, `Awards`, and `Data Dictionary`. In this exercise you'll mostly work with `Students` and `AL_Results`, with a couple of bonus tasks using `Sports`.

Make sure `student_database.xlsx` is saved in the same folder as your notebook or script before you start.

---

## Worked Example (read this first)

Here's how to load a sheet into a DataFrame and look at the first few rows. Run this before doing anything else:

```python
import pandas as pd

students_df = pd.read_excel("student_database.xlsx", sheet_name="Students")
print(students_df.head())
```

Every task below follows this same pattern: load data (or reuse `students_df`), then write one or two lines of pandas code to answer the question. Replace `# your code here` with your own code.

---

## Part 1: First Look at the Data

**1.1** You already loaded `students_df` above. How many rows and columns does it have? (Hint: a DataFrame has a `.shape` attribute.)

```python
# your code here
```

**1.2** Print the column names of `students_df`.

```python
# your code here
```

**1.3** Use `.info()` on `students_df`. Looking at the output, which columns are stored as numbers, and which are stored as text? Write your answer as a comment.

```python
# your code here
```

---

## Part 2: Selecting Columns & Counting Categories

**2.1** Select only the `FullName` and `Stream` columns from `students_df` and show the first 10 rows. (Hint: pass a list of column names in double square brackets, e.g. `df[["ColA", "ColB"]]`.)

```python
# your code here
```

**2.2** How many male students and how many female students are there? (Hint: look up the `.value_counts()` method — it works on a single column.)

```python
# your code here
```

**2.3** Which A/L stream (`Stream` column) has the most students enrolled?

```python
# your code here
```

---

## Part 3: Filtering Rows

**3.1** Create a new DataFrame called `bio_df` containing only the students in the `"Biological Science"` stream. How many students is that?

```python
# your code here
```

**3.2** Create a DataFrame of only students whose `Status` is `"Currently Enrolled"`.

```python
# your code here
```

**3.3** Create a DataFrame of **female** students in the **Commerce** stream. (Hint: you'll need to combine two conditions with `&`, and wrap each condition in its own parentheses.)

```python
# your code here
```

---

## Part 4: Sorting

**4.1** Sort `students_df` alphabetically by `FullName`. Show the first 5 rows.

```python
# your code here
```

**4.2** Load the `AL_Results` sheet into a new DataFrame called `al_df`. Sort it by `ZScore` from highest to lowest. Which `StudentID` has the highest Z-score? (Hint: look up the `ascending` parameter of `.sort_values()`.)

```python
# your code here
```

> **Note:** Some students don't have a `ZScore` — these show up as `NaN` (Not a Number). That's expected: only students who passed all three main subjects get a Z-score.

---

## Part 5: Basic Statistics

**5.1** Using `al_df`, how many students fall into each category of `OverallResult` (e.g. `"Eligible for University Entrance"`)?

```python
# your code here
```

**5.2** What is the average `ZScore` across all students who have one? (Hint: `.mean()` automatically ignores `NaN` values, so you don't need to remove them yourself.)

```python
# your code here
```

---

## Part 6: Grouping

`.groupby()` lets you split your data into categories and summarize each category — this is one of the most useful things pandas can do.

**6.1** Group `students_df` by `Stream` and count how many students are in each one. (Hint: `.groupby("ColumnName").size()`.) Compare this to your answer in 2.3 — do they match?

```python
# your code here
```

**6.2** Group `students_df` by `Gender` and `Stream` together (pass a list of two column names to `.groupby()`). What does the result tell you?

```python
# your code here
```

---

## Bonus Challenges

**B1.** Load the `Sports` sheet. Use `.value_counts()` on the `Sport` column to find the most popular sport among students.

```python
# your code here
```

**B2. (Harder)** Combine the `Students` and `AL_Results` sheets so you can see each student's name next to their exam result, using `pd.merge()`:

```python
merged_df = pd.merge(students_df, al_df, on="StudentID")
```

Run this, then print `merged_df[["FullName", "OverallResult", "ZScore"]].head(10)`. What happens to columns that exist in *both* sheets (like `Stream`)? Look at the column names in `merged_df.columns` to find out.

**B3. (Harder)** Save your `female_commerce_df` from Task 3.3 to a brand-new Excel file called `female_commerce_students.xlsx` using `.to_excel("filename.xlsx", index=False)`.

```python
# your code here
```

---

## Reflection Questions (no coding — discuss or write a short answer)

1. This dataset is synthetic (made up) for practice purposes. What problems could arise if we drew real conclusions about a real school from fake data like this?
2. Looking at your answer to 5.2, what does the average Z-score tell you — and what does it *not* tell you — about how well students performed overall?
3. If you were the school's data officer, what's one question about students you'd want to answer that this dataset *can't* currently answer? What additional data would you need?
