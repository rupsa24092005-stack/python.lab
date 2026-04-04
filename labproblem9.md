# Problem Statement

# Create a class Course for an online learning platform.

# Requirements:
    # Each course should have:
    # Course Name (public)
    # Instructor Name (public)
    # Course Price (private)
    # Course Code (protected)
    # Number of Students Enrolled (private)
# Platform should have:
    # Class variable platform_name = "CodeLearn"
    # Class variable total_courses to count how many courses are created.
# Methods:
    # enroll_student() → increases student count
    # get_price() → getter for private price
    # set_price(new_price) → setter for private price
    # apply_discount(percent)
    # display_course_info()
# Rules:
    # Price cannot be negative
    # Discount cannot reduce price below 0
    # Students count cannot be accessed directl