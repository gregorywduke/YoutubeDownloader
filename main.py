import dearpygui.dearpygui as dpg
import pytube.exceptions
from pytube import YouTube

dpg.create_context()
dpg.create_viewport(title='Youtube Downloader', width=800, height=600)
dpg.setup_dearpygui()

def progress(stream, chunk, bytes_remaining):
    print(bytes_remaining)

def button_callback(sender, app_data):
    try:
        yt = YouTube(dpg.get_value(link))
    except pytube.exceptions.PytubeError:
        dpg.add_text("Video Unavailable", parent="Video Page")
    else:
        dpg.add_text(yt.title, parent="Video Page")
        with dpg.group(label="dwnlds", horizontal=True, parent="Video Page"):
            dpg.add_button(label="Download Video and Audio (720p)", tag="dl",
                        callback=dwnld_callback)
            dpg.add_button(label="Download Audio", tag="dl1",
                           callback=dwnld2_callback)
        dpg.set_item_user_data("dl", yt)
        dpg.set_item_user_data("dl1", yt)

def dwnld_callback(sender, app_data, user_data):
    user_data.register_on_progress_callback(progress)
    user_data.streams.get_highest_resolution().download()

def dwnld2_callback(sender, app_data, user_data):
    user_data.register_on_progress_callback(progress)
    user_data.streams.filter(type="audio").first().download()

with dpg.window(tag="Download Page", label="Choose Video", pos=(0, 0), min_size=(800, 100)):
    dpg.add_text("Insert Link: ")
    link = dpg.add_input_text()
    btn = dpg.add_button(label="Enter", callback=button_callback)
with dpg.window(tag="Video Page", label="Video Information", pos=(0, 100), min_size=(800, 300)):
    pass # Create Video Window
with dpg.window(tag="Help Page", label="Help Page", pos=(0, 400), min_size=(800, 160)):
    dpg.add_text("** If 'Video Unavailable' appears, it cannot be downloaded by this program.")
    dpg.add_text("** Ensure your link is correct. If it is, the video is restricted.")
    dpg.add_text("")
    dpg.add_text("**Highest resolution available is 720p.")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()