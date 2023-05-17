def yield_multiple_statments():
  yield "This is the first statment"
  yield "This is the second statement"  
  yield "This is the third statement"
  yield "This is the last statement. Don't call next again!"
example = yield_multiple_statments()
print(next(example))
print(next(example))
print(next(example))
print(next(example))
print(next(example))