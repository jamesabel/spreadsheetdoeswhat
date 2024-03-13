# Spreadsheet Does What?

spreadsheet does what?

# real world

Me: "I need to access the data in your database"

Them (email): "Of course! Please see the attached CSV file! Party on! \m/"

# pitfalls

- big spreadsheets - openpyxl doesn't work
- not all Excel readers work with all Excel file types
- `bool()` of anything other than 0 or False is True (no exception raised). Beware of "truthiness".

# other stuff

DNA had to change its format to avoid being a date in Excel.

# TODO

Add something about:
`csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)` and `csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)`.
If you don't do this, and have a mix of string and numbers, you'll get a `TypeError` when you try to write the file.

Also, if you have an integer but read it in, it'll probably end up as a float.
May use attr's `converters` to fix this.
