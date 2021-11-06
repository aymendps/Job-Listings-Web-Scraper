import mywindow as mw

# main_window parameters
width = 400
height = 500
title = "Job Seeker - Apply Right"
logo_path = "./assets/logo.png"
bg_hex_color = '#eb1087'

if __name__ == '__main__':
    main_window = mw.myWindow(w=width, h=height, title=title, bg_hex_color=bg_hex_color)
    main_window.add_image(logo_path)
    main_window.start_window()
