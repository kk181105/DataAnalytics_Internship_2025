DATA CLEANING STEPS PERFORMED

1. Loaded the raw Netflix dataset.

2. MISSING VALUES
   - Found missing values in the 'director' column
   - Replaced all missing director entries with "Unknown"

3. TEXT CLEANING
   - Trimmed leading/trailing spaces in all text columns.

4. DATE FORMAT STANDARDIZATION
   - Converted 'date_added' into a consistent DD-MM-YYYY format.

5. DUPLICATE REMOVAL
   - Checked and removed duplicate rows (none remained after cleaning).

6. EXTRA COLUMNS FIX
   - Removed unwanted empty columns: Unnamed:12, Unnamed:13, Unnamed:14, Unnamed:15, Unnamed:16.

7. DATA TYPE CHECKS
   - Ensured 'release_year' remained integer.
   - Kept 'duration' as string due to mixed formats (e.g., “148 min” vs “3 Seasons”).

8. FINAL OUTPUT
   - Exported cleaned dataset as: netflix_cleaned_dataset.csv
