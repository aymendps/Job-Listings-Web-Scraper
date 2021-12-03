import mywindow as mw

# main_window parameters:
width = 400
height = 550
title = "Job Seeker - Apply Right"
logo_path = "./assets/logo.png"
bg_hex_color = '#eb1087'
text_color = 'white'
websites = ["RP Jobsite", "LinkedIn", "Indeed"]
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
    dropdown0, varw = main_window.add_dropdown(websites, 45)
    text1 = main_window.add_text(methods_title, 'w')
    text2 = main_window.add_text(categories_title, 'w')
    dropdown2, varc = main_window.add_dropdown(categories, 45)
    text3 = main_window.add_text(keyword_title, 'w')
    field0 = main_window.add_input_field(width=39)
    dropdown1 = main_window.special_main_window_dropdown(methods, 45, dropdown2, field0)
    button0 = main_window.add_button(seek_button_text)

    text1.pack(fill="both")
    dropdown1.pack()
    text0.pack(fill="both")
    dropdown0.pack()
    text2.pack(fill="both")
    dropdown2.pack()
    text3.pack(fill="both")
    field0.pack()
    mw.set_position(button0, 150, 480)

    mw.add_padding(text0, 20, 5)
    mw.add_padding(text1, 20, 5)
    mw.add_padding(text2, 20, 5)
    mw.add_padding(text3, 20, 5)
    mw.add_padding(button0, 10, 10)

    mw.disable_object(dropdown2)
    mw.disable_object(field0) 
    button0.configure(command=lambda : mw.start_scraping(varw,varc,field0))

    main_window.start_window()
