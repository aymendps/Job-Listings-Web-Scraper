import mywindow as mw

# main_window parameters
width = 400
height = 550
title = "Job Seeker - Apply Right"
logo_path = "./assets/logo.png"
bg_hex_color = '#eb1087'
text_color = 'white'
websites = ["RealPython JobSite", "LinkedIn", "Tanit Jobs"]
websites_title = "Website to use:"
methods = ["Seek everything", "Seek a category", "Seek a keyword"]
methods_title = "Method to use:"
categories = ["Software & Data", "Science", "Engineering", "Sales & Marketing", "Healthcare", "Business",
              "Education", "Arts & Media", "Technology", "Social Services", "Construction"]
categories_title = "Categories / Fields:"
keyword_title = "Seek Keyword:"
seek_button_text = "Seek now!"

if __name__ == '__main__':
    main_window = mw.myWindow(w=width, h=height, title=title, bg_hex_color=bg_hex_color, text_color=text_color)

    main_window.add_image(logo_path)

    text0 = main_window.add_text(websites_title, 'w')
    mw.add_padding(text0, 20, 5)

    dropdown0 = main_window.add_dropdown(websites, 45)

    text1 = main_window.add_text(methods_title, 'w')
    mw.add_padding(text1, 20, 5)

    dropdown1, d1_variable = main_window.add_dropdown(methods, 45)

    text2 = main_window.add_text(categories_title, 'w')
    mw.add_padding(text2, 20, 5)

    dropdown2 = main_window.add_dropdown(categories, 45)

    text3 = main_window.add_text(keyword_title, 'w')
    mw.add_padding(text3, 20, 5)

    field0 = main_window.add_input_field(width=39)

    button0 = main_window.add_button(seek_button_text)
    mw.add_padding(button0, 10, 10)
    mw.set_position(button0, 150, 480)

    main_window.start_window()
