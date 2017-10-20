from calendar import month_abbr
month = "June"
for k, v in enumerate(month_abbr):
    if v == month:
        month = k
        break
print(month)
