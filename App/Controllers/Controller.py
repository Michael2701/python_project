from typing import Any


class Controller:

    @staticmethod
    def clear_view(view: Any) -> None:
        """
        clear view from it's child elements
        :param view:
        :return:
        """
        master_children = view.winfo_children()
        if len(master_children) > 0:
            for child in master_children:
                child.destroy()

