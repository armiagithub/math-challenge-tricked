from itertools import permutations
from fpdf import FPDF
import time
def addition_algorithm(a, b, c, result):
    """Generates a formatted addition problem for display."""
    a_str = str(a)
    b_str = str(b)
    c_str = str(c)
    result_str = str(result)
    
    max_length = max(len(a_str), len(b_str), len(c_str), len(result_str))

    a_str = a_str.rjust(max_length)
    b_str = b_str.rjust(max_length)
    c_str = c_str.rjust(max_length)
    result_str = result_str.rjust(max_length)

    return f"   {a_str}\n+  {b_str}\n+  {c_str}\n{'-' * (max_length + 2)}\n   {result_str}\n{'-' * (max_length + 2)}"

def find_valid_combinations():
    """Finds all valid combinations where a 1-digit, 2-digit, and 3-digit number add up to a 4-digit result using unique digits."""
    digits = '0123456789'
    valid_solutions = []
    
    for perm in permutations(digits):
        if '0' not in perm:  # Ensure '0' is included in the sum
            continue

        one_digit = int(perm[0])
        two_digit = int(''.join(perm[1:3]))
        three_digit = int(''.join(perm[3:6]))
        result = int(''.join(perm[6:10]))

        if one_digit + two_digit + three_digit == result and 1000 <= result <= 9999:
            valid_solutions.append((one_digit, two_digit, three_digit, result))
    
    return valid_solutions

def export_to_pdf(solutions):
    """Exports valid solutions to a neatly formatted PDF, fitting five solutions per row."""
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font("Arial", "B", 16)
    pdf.set_text_color(0, 0, 255)  # Blue color for the title
    pdf.cell(200, 10, txt="Valid Addition Solutions", ln=True, align='C')
    pdf.ln(10)  # Line break

    # Set the font for the solutions
    pdf.set_font("Courier", size=8)  # Reduced size to fit 5 solutions per row
    pdf.set_text_color(0, 0, 0)  # Black color for the text

    line_count = 0
    line_text = [""] * 6  # Store lines of the algorithm

    for sol in solutions:
        # Generate the formatted addition problem
        addition_str = addition_algorithm(sol[0], sol[1], sol[2], sol[3])
        addition_lines = addition_str.split("\n")

        if line_count == 0:
            line_text = [""] * len(addition_lines)

        for i, line in enumerate(addition_lines):
            line_text[i] += line.ljust(20)  # Adjust spacing for alignment

        line_count += 1

        if line_count == 5:  # Print 5 solutions per row
            for formatted_line in line_text:
                pdf.cell(0, 5, formatted_line, ln=True)
            pdf.ln(3)  # Space between groups
            line_count = 0

    # Add any remaining problems
    if line_count > 0:
        for formatted_line in line_text:
            pdf.cell(0, 5, formatted_line, ln=True)

    # Footer
    pdf.set_font("Arial", "I", 10)
    # pdf.set_y(-15)
    pdf.cell(0, 10, f"Generated by Your Algorithm Finder.\nTotal valid combinations found: {len(solutions)}", 0, 0, "C")

    # Save the PDF
    pdf.output("addition_solutions.pdf")
    print("PDF exported as addition_solutions.pdf")

def print_solutions(solutions, show_ascii=True):
    """Prints solutions in either ASCII art format or normal format."""
    if solutions:
        for sol in solutions:
            if show_ascii:
                print(addition_algorithm(sol[0], sol[1], sol[2], sol[3]))
            else:
                print(f"{sol[0]} + {sol[1]} + {sol[2]} = {sol[3]}")
        print(f"\nTotal valid combinations found: {len(solutions)}")
    else:
        print("No valid combinations found.")

def main():
    solutions = find_valid_combinations()

    # Get user input for display method
    choice = input("Enter 'a' for ASCII art, 'n' for normal printing, 'b' for both, 'p' to export to PDF, 'ap' for ASCII and PDF, or 'np' for normal printing and PDF: ").lower()

    if choice == 'a':
        print_solutions(solutions, show_ascii=True)
    elif choice == 'n':
        print_solutions(solutions, show_ascii=False)
    elif choice == 'b':
        print_solutions(solutions, show_ascii=True)
        print_solutions(solutions, show_ascii=False)
    elif choice == 'p':
        export_to_pdf(solutions)
    elif choice == 'ap':
        print_solutions(solutions, show_ascii=True)
        export_to_pdf(solutions)
    elif choice == 'np':
        print_solutions(solutions, show_ascii=False)
        export_to_pdf(solutions)
    else:
        print("Invalid choice. Please enter a valid option.")
        main()  # Recursively call main for retry

if __name__ == "__main__":
    main()
time.sleep(1800)
