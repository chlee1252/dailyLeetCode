def solution(phone_book: [str]) -> bool:
  phone_book.sort()

  # Approach 1: Nested for loop
  for i in range(len(phone_book)):
    for j in range(i+1, len(phone_book)):
      if phone_book[j].startswith(phone_book[i]):
        return False
  
  return True

  # Approach 2: Use zip()

  # for i, j in zip(phone_book, phone_book[1:]):
  #   if j.startswith(i):
  #     return False
  
  # return True

