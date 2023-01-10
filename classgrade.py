def main():

  Harry = 81
  Ron = 78
  Hermione = 99
  Draco = 74
  Neville = 62

  Harry_average = Harry / 1
  Ron_average = Ron / 1
  Hermione_average = Hermione / 1
  Draco_average = Draco / 1
  Neville_average = Neville / 1

  Harry_grade = get_letter_grade(Harry_average)
  Ron_grade = get_letter_grade(Ron_average)
  Hermione_grade = get_letter_grade(Hermione_average)
  Draco_grade = get_letter_grade(Draco_average)
  Neville_grade = get_letter_grade(Neville_average)

  print("Harry has a letter grade of", Harry_grade)
  print("Ron has a letter grade of", Ron_grade)
  print("Hermione has a letter grade of", Hermione_grade)
  print("Draco has a letter grade of", Draco_grade)
  print("Neville has a letter grade of", Neville_grade)

def get_letter_grade(average):
  if average >= 90:
    return "A, Very good!"
  elif average >= 80:
    return "B, Good."
  elif average >= 70:
    return "C, Average"
  elif average >= 60:
    return "D, Needs improvement"
  else:
    return "F, Fail."

main()
