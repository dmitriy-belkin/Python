import user_interface as ui
import data_provider as dp

def button_click(mark):
    number_one, number_second, number_action = ui.menu_amount(mark)
    res = dp.calculation(number_one, number_second, number_action)
    ui.rec_result(mark, res)